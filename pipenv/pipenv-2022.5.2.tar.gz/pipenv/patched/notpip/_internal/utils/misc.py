# The following comment should be removed at some point in the future.
# mypy: strict-optional=False

import contextlib
import errno
import getpass
import hashlib
import io
import logging
import os
import posixpath
import shutil
import stat
import sys
import urllib.parse
from io import StringIO
from itertools import filterfalse, tee, zip_longest
from types import TracebackType
from typing import (
    Any,
    BinaryIO,
    Callable,
    ContextManager,
    Iterable,
    Iterator,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    cast,
)

from pipenv.patched.notpip._vendor.tenacity import retry, stop_after_delay, wait_fixed

from pipenv.patched.notpip import __version__
from pipenv.patched.notpip._internal.exceptions import CommandError
from pipenv.patched.notpip._internal.locations import get_major_minor_version
from pipenv.patched.notpip._internal.utils.compat import WINDOWS
from pipenv.patched.notpip._internal.utils.virtualenv import running_under_virtualenv

__all__ = [
    "rmtree",
    "display_path",
    "backup_dir",
    "ask",
    "splitext",
    "format_size",
    "is_installable_dir",
    "normalize_path",
    "renames",
    "get_prog",
    "captured_stdout",
    "ensure_dir",
    "remove_auth_from_url",
]


logger = logging.getLogger(__name__)

T = TypeVar("T")
ExcInfo = Tuple[Type[BaseException], BaseException, TracebackType]
VersionInfo = Tuple[int, int, int]
NetlocTuple = Tuple[str, Tuple[Optional[str], Optional[str]]]


def get_pip_version() -> str:
    pip_pkg_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    pip_pkg_dir = os.path.abspath(pip_pkg_dir)

    return "pip {} from {} (python {})".format(
        __version__,
        pip_pkg_dir,
        get_major_minor_version(),
    )


def normalize_version_info(py_version_info: Tuple[int, ...]) -> Tuple[int, int, int]:
    """
    Convert a tuple of ints representing a Python version to one of length
    three.

    :param py_version_info: a tuple of ints representing a Python version,
        or None to specify no version. The tuple can have any length.

    :return: a tuple of length three if `py_version_info` is non-None.
        Otherwise, return `py_version_info` unchanged (i.e. None).
    """
    if len(py_version_info) < 3:
        py_version_info += (3 - len(py_version_info)) * (0,)
    elif len(py_version_info) > 3:
        py_version_info = py_version_info[:3]

    return cast("VersionInfo", py_version_info)


def ensure_dir(path: str) -> None:
    """os.path.makedirs without EEXIST."""
    try:
        os.makedirs(path)
    except OSError as e:
        # Windows can raise spurious ENOTEMPTY errors. See #6426.
        if e.errno != errno.EEXIST and e.errno != errno.ENOTEMPTY:
            raise


def get_prog() -> str:
    try:
        prog = os.path.basename(sys.argv[0])
        if prog in ("__main__.py", "-c"):
            return f"{sys.executable} -m pip"
        else:
            return prog
    except (AttributeError, TypeError, IndexError):
        pass
    return "pip"


# Retry every half second for up to 3 seconds
# Tenacity raises RetryError by default, explicitly raise the original exception
@retry(reraise=True, stop=stop_after_delay(3), wait=wait_fixed(0.5))
def rmtree(dir: str, ignore_errors: bool = False) -> None:
    shutil.rmtree(dir, ignore_errors=ignore_errors, onerror=rmtree_errorhandler)


def rmtree_errorhandler(func: Callable[..., Any], path: str, exc_info: ExcInfo) -> None:
    """On Windows, the files in .svn are read-only, so when rmtree() tries to
    remove them, an exception is thrown.  We catch that here, remove the
    read-only attribute, and hopefully continue without problems."""
    try:
        has_attr_readonly = not (os.stat(path).st_mode & stat.S_IWRITE)
    except OSError:
        # it's equivalent to os.path.exists
        return

    if has_attr_readonly:
        # convert to read/write
        os.chmod(path, stat.S_IWRITE)
        # use the original function to repeat the operation
        func(path)
        return
    else:
        raise


def display_path(path: str) -> str:
    """Gives the display value for a given path, making it relative to cwd
    if possible."""
    path = os.path.normcase(os.path.abspath(path))
    if path.startswith(os.getcwd() + os.path.sep):
        path = "." + path[len(os.getcwd()) :]
    return path


def backup_dir(dir: str, ext: str = ".bak") -> str:
    """Figure out the name of a directory to back up the given dir to
    (adding .bak, .bak2, etc)"""
    n = 1
    extension = ext
    while os.path.exists(dir + extension):
        n += 1
        extension = ext + str(n)
    return dir + extension


def ask_path_exists(message: str, options: Iterable[str]) -> str:
    for action in os.environ.get("PIP_EXISTS_ACTION", "").split():
        if action in options:
            return action
    return ask(message, options)


def _check_no_input(message: str) -> None:
    """Raise an error if no input is allowed."""
    if os.environ.get("PIP_NO_INPUT"):
        raise Exception(
            f"No input was expected ($PIP_NO_INPUT set); question: {message}"
        )


def ask(message: str, options: Iterable[str]) -> str:
    """Ask the message interactively, with the given possible responses"""
    while 1:
        _check_no_input(message)
        response = input(message)
        response = response.strip().lower()
        if response not in options:
            print(
                "Your response ({!r}) was not one of the expected responses: "
                "{}".format(response, ", ".join(options))
            )
        else:
            return response


def ask_input(message: str) -> str:
    """Ask for input interactively."""
    _check_no_input(message)
    return input(message)


def ask_password(message: str) -> str:
    """Ask for a password interactively."""
    _check_no_input(message)
    return getpass.getpass(message)


def strtobool(val: str) -> int:
    """Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return 1
    elif val in ("n", "no", "f", "false", "off", "0"):
        return 0
    else:
        raise ValueError(f"invalid truth value {val!r}")


def format_size(bytes: float) -> str:
    if bytes > 1000 * 1000:
        return "{:.1f} MB".format(bytes / 1000.0 / 1000)
    elif bytes > 10 * 1000:
        return "{} kB".format(int(bytes / 1000))
    elif bytes > 1000:
        return "{:.1f} kB".format(bytes / 1000.0)
    else:
        return "{} bytes".format(int(bytes))


def tabulate(rows: Iterable[Iterable[Any]]) -> Tuple[List[str], List[int]]:
    """Return a list of formatted rows and a list of column sizes.

    For example::

    >>> tabulate([['foobar', 2000], [0xdeadbeef]])
    (['foobar     2000', '3735928559'], [10, 4])
    """
    rows = [tuple(map(str, row)) for row in rows]
    sizes = [max(map(len, col)) for col in zip_longest(*rows, fillvalue="")]
    table = [" ".join(map(str.ljust, row, sizes)).rstrip() for row in rows]
    return table, sizes


def is_installable_dir(path: str) -> bool:
    """Is path is a directory containing pyproject.toml or setup.py?

    If pyproject.toml exists, this is a PEP 517 project. Otherwise we look for
    a legacy setuptools layout by identifying setup.py. We don't check for the
    setup.cfg because using it without setup.py is only available for PEP 517
    projects, which are already covered by the pyproject.toml check.
    """
    if not os.path.isdir(path):
        return False
    if os.path.isfile(os.path.join(path, "pyproject.toml")):
        return True
    if os.path.isfile(os.path.join(path, "setup.py")):
        return True
    return False


def read_chunks(file: BinaryIO, size: int = io.DEFAULT_BUFFER_SIZE) -> Iterator[bytes]:
    """Yield pieces of data from a file-like object until EOF."""
    while True:
        chunk = file.read(size)
        if not chunk:
            break
        yield chunk


def normalize_path(path: str, resolve_symlinks: bool = True) -> str:
    """
    Convert a path to its canonical, case-normalized, absolute version.

    """
    path = os.path.expanduser(path)
    if resolve_symlinks:
        path = os.path.realpath(path)
    else:
        path = os.path.abspath(path)
    return os.path.normcase(path)


def splitext(path: str) -> Tuple[str, str]:
    """Like os.path.splitext, but take off .tar too"""
    base, ext = posixpath.splitext(path)
    if base.lower().endswith(".tar"):
        ext = base[-4:] + ext
        base = base[:-4]
    return base, ext


def renames(old: str, new: str) -> None:
    """Like os.renames(), but handles renaming across devices."""
    # Implementation borrowed from os.renames().
    head, tail = os.path.split(new)
    if head and tail and not os.path.exists(head):
        os.makedirs(head)

    shutil.move(old, new)

    head, tail = os.path.split(old)
    if head and tail:
        try:
            os.removedirs(head)
        except OSError:
            pass


def is_local(path: str) -> bool:
    """
    Return True if path is within sys.prefix, if we're running in a virtualenv.

    If we're not in a virtualenv, all paths are considered "local."

    Caution: this function assumes the head of path has been normalized
    with normalize_path.
    """
    if not running_under_virtualenv():
        return True
    return path.startswith(normalize_path(sys.prefix))


def write_output(msg: Any, *args: Any) -> None:
    logger.info(msg, *args)


class StreamWrapper(StringIO):
    orig_stream: TextIO = None

    @classmethod
    def from_stream(cls, orig_stream: TextIO) -> "StreamWrapper":
        cls.orig_stream = orig_stream
        return cls()

    # compileall.compile_dir() needs stdout.encoding to print to stdout
    # https://github.com/python/mypy/issues/4125
    @property
    def encoding(self):  # type: ignore
        return self.orig_stream.encoding


@contextlib.contextmanager
def captured_output(stream_name: str) -> Iterator[StreamWrapper]:
    """Return a context manager used by captured_stdout/stdin/stderr
    that temporarily replaces the sys stream *stream_name* with a StringIO.

    Taken from Lib/support/__init__.py in the CPython repo.
    """
    orig_stdout = getattr(sys, stream_name)
    setattr(sys, stream_name, StreamWrapper.from_stream(orig_stdout))
    try:
        yield getattr(sys, stream_name)
    finally:
        setattr(sys, stream_name, orig_stdout)


def captured_stdout() -> ContextManager[StreamWrapper]:
    """Capture the output of sys.stdout:

       with captured_stdout() as stdout:
           print('hello')
       self.assertEqual(stdout.getvalue(), 'hello\n')

    Taken from Lib/support/__init__.py in the CPython repo.
    """
    return captured_output("stdout")


def captured_stderr() -> ContextManager[StreamWrapper]:
    """
    See captured_stdout().
    """
    return captured_output("stderr")


# Simulates an enum
def enum(*sequential: Any, **named: Any) -> Type[Any]:
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = {value: key for key, value in enums.items()}
    enums["reverse_mapping"] = reverse
    return type("Enum", (), enums)


def build_netloc(host: str, port: Optional[int]) -> str:
    """
    Build a netloc from a host-port pair
    """
    if port is None:
        return host
    if ":" in host:
        # Only wrap host with square brackets when it is IPv6
        host = f"[{host}]"
    return f"{host}:{port}"


def build_url_from_netloc(netloc: str, scheme: str = "https") -> str:
    """
    Build a full URL from a netloc.
    """
    if netloc.count(":") >= 2 and "@" not in netloc and "[" not in netloc:
        # It must be a bare IPv6 address, so wrap it with brackets.
        netloc = f"[{netloc}]"
    return f"{scheme}://{netloc}"


def parse_netloc(netloc: str) -> Tuple[str, Optional[int]]:
    """
    Return the host-port pair from a netloc.
    """
    url = build_url_from_netloc(netloc)
    parsed = urllib.parse.urlparse(url)
    return parsed.hostname, parsed.port


def split_auth_from_netloc(netloc: str) -> NetlocTuple:
    """
    Parse out and remove the auth information from a netloc.

    Returns: (netloc, (username, password)).
    """
    if "@" not in netloc:
        return netloc, (None, None)

    # Split from the right because that's how urllib.parse.urlsplit()
    # behaves if more than one @ is present (which can be checked using
    # the password attribute of urlsplit()'s return value).
    auth, netloc = netloc.rsplit("@", 1)
    pw: Optional[str] = None
    if ":" in auth:
        # Split from the left because that's how urllib.parse.urlsplit()
        # behaves if more than one : is present (which again can be checked
        # using the password attribute of the return value)
        user, pw = auth.split(":", 1)
    else:
        user, pw = auth, None

    user = urllib.parse.unquote(user)
    if pw is not None:
        pw = urllib.parse.unquote(pw)

    return netloc, (user, pw)


def redact_netloc(netloc: str) -> str:
    """
    Replace the sensitive data in a netloc with "****", if it exists.

    For example:
        - "user:pass@example.com" returns "user:****@example.com"
        - "accesstoken@example.com" returns "****@example.com"
    """
    netloc, (user, password) = split_auth_from_netloc(netloc)
    if user is None:
        return netloc
    if password is None:
        user = "****"
        password = ""
    else:
        user = urllib.parse.quote(user)
        password = ":****"
    return "{user}{password}@{netloc}".format(
        user=user, password=password, netloc=netloc
    )


def _transform_url(
    url: str, transform_netloc: Callable[[str], Tuple[Any, ...]]
) -> Tuple[str, NetlocTuple]:
    """Transform and replace netloc in a url.

    transform_netloc is a function taking the netloc and returning a
    tuple. The first element of this tuple is the new netloc. The
    entire tuple is returned.

    Returns a tuple containing the transformed url as item 0 and the
    original tuple returned by transform_netloc as item 1.
    """
    purl = urllib.parse.urlsplit(url)
    netloc_tuple = transform_netloc(purl.netloc)
    # stripped url
    url_pieces = (purl.scheme, netloc_tuple[0], purl.path, purl.query, purl.fragment)
    surl = urllib.parse.urlunsplit(url_pieces)
    return surl, cast("NetlocTuple", netloc_tuple)


def _get_netloc(netloc: str) -> NetlocTuple:
    return split_auth_from_netloc(netloc)


def _redact_netloc(netloc: str) -> Tuple[str]:
    return (redact_netloc(netloc),)


def split_auth_netloc_from_url(url: str) -> Tuple[str, str, Tuple[str, str]]:
    """
    Parse a url into separate netloc, auth, and url with no auth.

    Returns: (url_without_auth, netloc, (username, password))
    """
    url_without_auth, (netloc, auth) = _transform_url(url, _get_netloc)
    return url_without_auth, netloc, auth


def remove_auth_from_url(url: str) -> str:
    """Return a copy of url with 'username:password@' removed."""
    # username/pass params are passed to subversion through flags
    # and are not recognized in the url.
    return _transform_url(url, _get_netloc)[0]


def redact_auth_from_url(url: str) -> str:
    """Replace the password in a given url with ****."""
    return _transform_url(url, _redact_netloc)[0]


class HiddenText:
    def __init__(self, secret: str, redacted: str) -> None:
        self.secret = secret
        self.redacted = redacted

    def __repr__(self) -> str:
        return "<HiddenText {!r}>".format(str(self))

    def __str__(self) -> str:
        return self.redacted

    # This is useful for testing.
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other):
            return False

        # The string being used for redaction doesn't also have to match,
        # just the raw, original string.
        return self.secret == other.secret


def hide_value(value: str) -> HiddenText:
    return HiddenText(value, redacted="****")


def hide_url(url: str) -> HiddenText:
    redacted = redact_auth_from_url(url)
    return HiddenText(url, redacted=redacted)


def protect_pip_from_modification_on_windows(modifying_pip: bool) -> None:
    """Protection of pip.exe from modification on Windows

    On Windows, any operation modifying pip should be run as:
        python -m pip ...
    """
    pip_names = [
        "pip.exe",
        "pip{}.exe".format(sys.version_info[0]),
        "pip{}.{}.exe".format(*sys.version_info[:2]),
    ]

    # See https://github.com/pypa/pip/issues/1299 for more discussion
    should_show_use_python_msg = (
        modifying_pip and WINDOWS and os.path.basename(sys.argv[0]) in pip_names
    )

    if should_show_use_python_msg:
        new_command = [sys.executable, "-m", "pip"] + sys.argv[1:]
        raise CommandError(
            "To modify pip, please run the following command:\n{}".format(
                " ".join(new_command)
            )
        )


def is_console_interactive() -> bool:
    """Is this console interactive?"""
    return sys.stdin is not None and sys.stdin.isatty()


def hash_file(path: str, blocksize: int = 1 << 20) -> Tuple[Any, int]:
    """Return (hash, length) for path using hashlib.sha256()"""

    h = hashlib.sha256()
    length = 0
    with open(path, "rb") as f:
        for block in read_chunks(f, size=blocksize):
            length += len(block)
            h.update(block)
    return h, length


def is_wheel_installed() -> bool:
    """
    Return whether the wheel package is installed.
    """
    try:
        import pipenv.vendor.wheel as wheel  # noqa: F401
    except ImportError:
        return False

    return True


def pairwise(iterable: Iterable[Any]) -> Iterator[Tuple[Any, Any]]:
    """
    Return paired elements.

    For example:
        s -> (s0, s1), (s2, s3), (s4, s5), ...
    """
    iterable = iter(iterable)
    return zip_longest(iterable, iterable)


def partition(
    pred: Callable[[T], bool],
    iterable: Iterable[T],
) -> Tuple[Iterable[T], Iterable[T]]:
    """
    Use a predicate to partition entries into false entries and true entries,
    like

        partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    """
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)
