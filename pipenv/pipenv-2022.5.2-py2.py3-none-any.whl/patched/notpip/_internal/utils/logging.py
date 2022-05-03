import contextlib
import errno
import logging
import logging.handlers
import os
import sys
import threading
from dataclasses import dataclass
from logging import Filter
from typing import IO, Any, ClassVar, Iterator, List, Optional, TextIO, Type

from pipenv.patched.notpip._vendor.rich.console import (
    Console,
    ConsoleOptions,
    ConsoleRenderable,
    RenderResult,
)
from pipenv.patched.notpip._vendor.rich.highlighter import NullHighlighter
from pipenv.patched.notpip._vendor.rich.logging import RichHandler
from pipenv.patched.notpip._vendor.rich.segment import Segment
from pipenv.patched.notpip._vendor.rich.style import Style

from pipenv.patched.notpip._internal.exceptions import DiagnosticPipError
from pipenv.patched.notpip._internal.utils._log import VERBOSE, getLogger
from pipenv.patched.notpip._internal.utils.compat import WINDOWS
from pipenv.patched.notpip._internal.utils.deprecation import DEPRECATION_MSG_PREFIX
from pipenv.patched.notpip._internal.utils.misc import ensure_dir

_log_state = threading.local()
subprocess_logger = getLogger("pip.subprocessor")


class BrokenStdoutLoggingError(Exception):
    """
    Raised if BrokenPipeError occurs for the stdout stream while logging.
    """


def _is_broken_pipe_error(exc_class: Type[BaseException], exc: BaseException) -> bool:
    if exc_class is BrokenPipeError:
        return True

    # On Windows, a broken pipe can show up as EINVAL rather than EPIPE:
    # https://bugs.python.org/issue19612
    # https://bugs.python.org/issue30418
    if not WINDOWS:
        return False

    return isinstance(exc, OSError) and exc.errno in (errno.EINVAL, errno.EPIPE)


@contextlib.contextmanager
def indent_log(num: int = 2) -> Iterator[None]:
    """
    A context manager which will cause the log output to be indented for any
    log messages emitted inside it.
    """
    # For thread-safety
    _log_state.indentation = get_indentation()
    _log_state.indentation += num
    try:
        yield
    finally:
        _log_state.indentation -= num


def get_indentation() -> int:
    return getattr(_log_state, "indentation", 0)


class IndentingFormatter(logging.Formatter):
    default_time_format = "%Y-%m-%dT%H:%M:%S"

    def __init__(
        self,
        *args: Any,
        add_timestamp: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        A logging.Formatter that obeys the indent_log() context manager.

        :param add_timestamp: A bool indicating output lines should be prefixed
            with their record's timestamp.
        """
        self.add_timestamp = add_timestamp
        super().__init__(*args, **kwargs)

    def get_message_start(self, formatted: str, levelno: int) -> str:
        """
        Return the start of the formatted log message (not counting the
        prefix to add to each line).
        """
        if levelno < logging.WARNING:
            return ""
        if formatted.startswith(DEPRECATION_MSG_PREFIX):
            # Then the message already has a prefix.  We don't want it to
            # look like "WARNING: DEPRECATION: ...."
            return ""
        if levelno < logging.ERROR:
            return "WARNING: "

        return "ERROR: "

    def format(self, record: logging.LogRecord) -> str:
        """
        Calls the standard formatter, but will indent all of the log message
        lines by our current indentation level.
        """
        formatted = super().format(record)
        message_start = self.get_message_start(formatted, record.levelno)
        formatted = message_start + formatted

        prefix = ""
        if self.add_timestamp:
            prefix = f"{self.formatTime(record)} "
        prefix += " " * get_indentation()
        formatted = "".join([prefix + line for line in formatted.splitlines(True)])
        return formatted


@dataclass
class IndentedRenderable:
    renderable: ConsoleRenderable
    indent: int

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        segments = console.render(self.renderable, options)
        lines = Segment.split_lines(segments)
        for line in lines:
            yield Segment(" " * self.indent)
            yield from line
            yield Segment("\n")


class RichPipStreamHandler(RichHandler):
    KEYWORDS: ClassVar[Optional[List[str]]] = []

    def __init__(self, stream: Optional[TextIO], no_color: bool) -> None:
        super().__init__(
            console=Console(file=stream, no_color=no_color, soft_wrap=True),
            show_time=False,
            show_level=False,
            show_path=False,
            highlighter=NullHighlighter(),
        )

    # Our custom override on Rich's logger, to make things work as we need them to.
    def emit(self, record: logging.LogRecord) -> None:
        style: Optional[Style] = None

        # If we are given a diagnostic error to present, present it with indentation.
        if record.msg == "[present-diagnostic] %s" and len(record.args) == 1:
            diagnostic_error: DiagnosticPipError = record.args[0]  # type: ignore[index]
            assert isinstance(diagnostic_error, DiagnosticPipError)

            renderable: ConsoleRenderable = IndentedRenderable(
                diagnostic_error, indent=get_indentation()
            )
        else:
            message = self.format(record)
            renderable = self.render_message(record, message)
            if record.levelno is not None:
                if record.levelno >= logging.ERROR:
                    style = Style(color="red")
                elif record.levelno >= logging.WARNING:
                    style = Style(color="yellow")

        try:
            self.console.print(renderable, overflow="ignore", crop=False, style=style)
        except Exception:
            self.handleError(record)

    def handleError(self, record: logging.LogRecord) -> None:
        """Called when logging is unable to log some output."""

        exc_class, exc = sys.exc_info()[:2]
        # If a broken pipe occurred while calling write() or flush() on the
        # stdout stream in logging's Handler.emit(), then raise our special
        # exception so we can handle it in main() instead of logging the
        # broken pipe error and continuing.
        if (
            exc_class
            and exc
            and self.console.file is sys.stdout
            and _is_broken_pipe_error(exc_class, exc)
        ):
            raise BrokenStdoutLoggingError()

        return super().handleError(record)


class BetterRotatingFileHandler(logging.handlers.RotatingFileHandler):
    def _open(self) -> IO[Any]:
        ensure_dir(os.path.dirname(self.baseFilename))
        return super()._open()


class MaxLevelFilter(Filter):
    def __init__(self, level: int) -> None:
        self.level = level

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelno < self.level


class ExcludeLoggerFilter(Filter):

    """
    A logging Filter that excludes records from a logger (or its children).
    """

    def filter(self, record: logging.LogRecord) -> bool:
        # The base Filter class allows only records from a logger (or its
        # children).
        return not super().filter(record)


def setup_logging(verbosity: int, no_color: bool, user_log_file: Optional[str]) -> int:
    """Configures and sets up all of the logging

    Returns the requested logging level, as its integer value.
    """

    # Determine the level to be logging at.
    if verbosity >= 2:
        level_number = logging.DEBUG
    elif verbosity == 1:
        level_number = VERBOSE
    elif verbosity == -1:
        level_number = logging.WARNING
    elif verbosity == -2:
        level_number = logging.ERROR
    elif verbosity <= -3:
        level_number = logging.CRITICAL
    else:
        level_number = logging.INFO

    level = logging.getLevelName(level_number)

    # The "root" logger should match the "console" level *unless* we also need
    # to log to a user log file.
    include_user_log = user_log_file is not None
    if include_user_log:
        additional_log_file = user_log_file
        root_level = "DEBUG"
    else:
        additional_log_file = "/dev/null"
        root_level = level

    # Disable any logging besides WARNING unless we have DEBUG level logging
    # enabled for vendored libraries.
    vendored_log_level = "WARNING" if level in ["INFO", "ERROR"] else "DEBUG"

    # Shorthands for clarity
    log_streams = {
        "stdout": "ext://sys.stdout",
        "stderr": "ext://sys.stderr",
    }
    handler_classes = {
        "stream": "pipenv.patched.notpip._internal.utils.logging.RichPipStreamHandler",
        "file": "pipenv.patched.notpip._internal.utils.logging.BetterRotatingFileHandler",
    }
    handlers = ["console", "console_errors", "console_subprocess"] + (
        ["user_log"] if include_user_log else []
    )

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {
                "exclude_warnings": {
                    "()": "pipenv.patched.notpip._internal.utils.logging.MaxLevelFilter",
                    "level": logging.WARNING,
                },
                "restrict_to_subprocess": {
                    "()": "logging.Filter",
                    "name": subprocess_logger.name,
                },
                "exclude_subprocess": {
                    "()": "pipenv.patched.notpip._internal.utils.logging.ExcludeLoggerFilter",
                    "name": subprocess_logger.name,
                },
            },
            "formatters": {
                "indent": {
                    "()": IndentingFormatter,
                    "format": "%(message)s",
                },
                "indent_with_timestamp": {
                    "()": IndentingFormatter,
                    "format": "%(message)s",
                    "add_timestamp": True,
                },
            },
            "handlers": {
                "console": {
                    "level": level,
                    "class": handler_classes["stream"],
                    "no_color": no_color,
                    "stream": log_streams["stdout"],
                    "filters": ["exclude_subprocess", "exclude_warnings"],
                    "formatter": "indent",
                },
                "console_errors": {
                    "level": "WARNING",
                    "class": handler_classes["stream"],
                    "no_color": no_color,
                    "stream": log_streams["stderr"],
                    "filters": ["exclude_subprocess"],
                    "formatter": "indent",
                },
                # A handler responsible for logging to the console messages
                # from the "subprocessor" logger.
                "console_subprocess": {
                    "level": level,
                    "class": handler_classes["stream"],
                    "stream": log_streams["stderr"],
                    "no_color": no_color,
                    "filters": ["restrict_to_subprocess"],
                    "formatter": "indent",
                },
                "user_log": {
                    "level": "DEBUG",
                    "class": handler_classes["file"],
                    "filename": additional_log_file,
                    "encoding": "utf-8",
                    "delay": True,
                    "formatter": "indent_with_timestamp",
                },
            },
            "root": {
                "level": root_level,
                "handlers": handlers,
            },
            "loggers": {"pipenv.patched.notpip._vendor": {"level": vendored_log_level}},
        }
    )

    return level_number
