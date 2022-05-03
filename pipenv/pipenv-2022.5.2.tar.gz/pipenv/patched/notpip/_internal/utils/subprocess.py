import logging
import os
import shlex
import subprocess
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Iterable,
    List,
    Mapping,
    Optional,
    Union,
)

from pipenv.patched.notpip._vendor.rich.markup import escape

from pipenv.patched.notpip._internal.cli.spinners import SpinnerInterface, open_spinner
from pipenv.patched.notpip._internal.exceptions import InstallationSubprocessError
from pipenv.patched.notpip._internal.utils.logging import VERBOSE, subprocess_logger
from pipenv.patched.notpip._internal.utils.misc import HiddenText

if TYPE_CHECKING:
    # Literal was introduced in Python 3.8.
    #
    # TODO: Remove `if TYPE_CHECKING` when dropping support for Python 3.7.
    from typing import Literal

CommandArgs = List[Union[str, HiddenText]]


def make_command(*args: Union[str, HiddenText, CommandArgs]) -> CommandArgs:
    """
    Create a CommandArgs object.
    """
    command_args: CommandArgs = []
    for arg in args:
        # Check for list instead of CommandArgs since CommandArgs is
        # only known during type-checking.
        if isinstance(arg, list):
            command_args.extend(arg)
        else:
            # Otherwise, arg is str or HiddenText.
            command_args.append(arg)

    return command_args


def format_command_args(args: Union[List[str], CommandArgs]) -> str:
    """
    Format command arguments for display.
    """
    # For HiddenText arguments, display the redacted form by calling str().
    # Also, we don't apply str() to arguments that aren't HiddenText since
    # this can trigger a UnicodeDecodeError in Python 2 if the argument
    # has type unicode and includes a non-ascii character.  (The type
    # checker doesn't ensure the annotations are correct in all cases.)
    return " ".join(
        shlex.quote(str(arg)) if isinstance(arg, HiddenText) else shlex.quote(arg)
        for arg in args
    )


def reveal_command_args(args: Union[List[str], CommandArgs]) -> List[str]:
    """
    Return the arguments in their raw, unredacted form.
    """
    return [arg.secret if isinstance(arg, HiddenText) else arg for arg in args]


def call_subprocess(
    cmd: Union[List[str], CommandArgs],
    show_stdout: bool = False,
    cwd: Optional[str] = None,
    on_returncode: 'Literal["raise", "warn", "ignore"]' = "raise",
    extra_ok_returncodes: Optional[Iterable[int]] = None,
    extra_environ: Optional[Mapping[str, Any]] = None,
    unset_environ: Optional[Iterable[str]] = None,
    spinner: Optional[SpinnerInterface] = None,
    log_failed_cmd: Optional[bool] = True,
    stdout_only: Optional[bool] = False,
    *,
    command_desc: str,
) -> str:
    """
    Args:
      show_stdout: if true, use INFO to log the subprocess's stderr and
        stdout streams.  Otherwise, use DEBUG.  Defaults to False.
      extra_ok_returncodes: an iterable of integer return codes that are
        acceptable, in addition to 0. Defaults to None, which means [].
      unset_environ: an iterable of environment variable names to unset
        prior to calling subprocess.Popen().
      log_failed_cmd: if false, failed commands are not logged, only raised.
      stdout_only: if true, return only stdout, else return both. When true,
        logging of both stdout and stderr occurs when the subprocess has
        terminated, else logging occurs as subprocess output is produced.
    """
    if extra_ok_returncodes is None:
        extra_ok_returncodes = []
    if unset_environ is None:
        unset_environ = []
    # Most places in pip use show_stdout=False. What this means is--
    #
    # - We connect the child's output (combined stderr and stdout) to a
    #   single pipe, which we read.
    # - We log this output to stderr at DEBUG level as it is received.
    # - If DEBUG logging isn't enabled (e.g. if --verbose logging wasn't
    #   requested), then we show a spinner so the user can still see the
    #   subprocess is in progress.
    # - If the subprocess exits with an error, we log the output to stderr
    #   at ERROR level if it hasn't already been displayed to the console
    #   (e.g. if --verbose logging wasn't enabled).  This way we don't log
    #   the output to the console twice.
    #
    # If show_stdout=True, then the above is still done, but with DEBUG
    # replaced by INFO.
    if show_stdout:
        # Then log the subprocess output at INFO level.
        log_subprocess = subprocess_logger.info
        used_level = logging.INFO
    else:
        # Then log the subprocess output using VERBOSE.  This also ensures
        # it will be logged to the log file (aka user_log), if enabled.
        log_subprocess = subprocess_logger.verbose
        used_level = VERBOSE

    # Whether the subprocess will be visible in the console.
    showing_subprocess = subprocess_logger.getEffectiveLevel() <= used_level

    # Only use the spinner if we're not showing the subprocess output
    # and we have a spinner.
    use_spinner = not showing_subprocess and spinner is not None

    log_subprocess("Running command %s", command_desc)
    env = os.environ.copy()
    if extra_environ:
        env.update(extra_environ)
    for name in unset_environ:
        env.pop(name, None)
    try:
        proc = subprocess.Popen(
            # Convert HiddenText objects to the underlying str.
            reveal_command_args(cmd),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT if not stdout_only else subprocess.PIPE,
            cwd=cwd,
            env=env,
            errors="backslashreplace",
        )
    except Exception as exc:
        if log_failed_cmd:
            subprocess_logger.critical(
                "Error %s while executing command %s",
                exc,
                command_desc,
            )
        raise
    all_output = []
    if not stdout_only:
        assert proc.stdout
        assert proc.stdin
        proc.stdin.close()
        # In this mode, stdout and stderr are in the same pipe.
        while True:
            line: str = proc.stdout.readline()
            if not line:
                break
            line = line.rstrip()
            all_output.append(line + "\n")

            # Show the line immediately.
            log_subprocess(line)
            # Update the spinner.
            if use_spinner:
                assert spinner
                spinner.spin()
        try:
            proc.wait()
        finally:
            if proc.stdout:
                proc.stdout.close()
        output = "".join(all_output)
    else:
        # In this mode, stdout and stderr are in different pipes.
        # We must use communicate() which is the only safe way to read both.
        out, err = proc.communicate()
        # log line by line to preserve pip log indenting
        for out_line in out.splitlines():
            log_subprocess(out_line)
        all_output.append(out)
        for err_line in err.splitlines():
            log_subprocess(err_line)
        all_output.append(err)
        output = out

    proc_had_error = proc.returncode and proc.returncode not in extra_ok_returncodes
    if use_spinner:
        assert spinner
        if proc_had_error:
            spinner.finish("error")
        else:
            spinner.finish("done")
    if proc_had_error:
        if on_returncode == "raise":
            error = InstallationSubprocessError(
                command_description=command_desc,
                exit_code=proc.returncode,
                output_lines=all_output if not showing_subprocess else None,
            )
            if log_failed_cmd:
                subprocess_logger.error("[present-diagnostic] %s", error)
                subprocess_logger.verbose(
                    "[bold magenta]full command[/]: [blue]%s[/]",
                    escape(format_command_args(cmd)),
                    extra={"markup": True},
                )
                subprocess_logger.verbose(
                    "[bold magenta]cwd[/]: %s",
                    escape(cwd or "[inherit]"),
                    extra={"markup": True},
                )

            raise error
        elif on_returncode == "warn":
            subprocess_logger.warning(
                'Command "%s" had error code %s in %s',
                command_desc,
                proc.returncode,
                cwd,
            )
        elif on_returncode == "ignore":
            pass
        else:
            raise ValueError(f"Invalid value: on_returncode={on_returncode!r}")
    return output


def runner_with_spinner_message(message: str) -> Callable[..., None]:
    """Provide a subprocess_runner that shows a spinner message.

    Intended for use with for pep517's Pep517HookCaller. Thus, the runner has
    an API that matches what's expected by Pep517HookCaller.subprocess_runner.
    """

    def runner(
        cmd: List[str],
        cwd: Optional[str] = None,
        extra_environ: Optional[Mapping[str, Any]] = None,
    ) -> None:
        with open_spinner(message) as spinner:
            call_subprocess(
                cmd,
                command_desc=message,
                cwd=cwd,
                extra_environ=extra_environ,
                spinner=spinner,
            )

    return runner
