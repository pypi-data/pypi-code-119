import csv
import email.message
import json
import logging
import pathlib
import re
import zipfile
from typing import (
    IO,
    TYPE_CHECKING,
    Collection,
    Container,
    Iterable,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

from pipenv.patched.notpip._vendor.packaging.requirements import Requirement
from pipenv.patched.notpip._vendor.packaging.specifiers import InvalidSpecifier, SpecifierSet
from pipenv.patched.notpip._vendor.packaging.utils import NormalizedName
from pipenv.patched.notpip._vendor.packaging.version import LegacyVersion, Version

from pipenv.patched.notpip._internal.exceptions import NoneMetadataError
from pipenv.patched.notpip._internal.locations import site_packages, user_site
from pipenv.patched.notpip._internal.models.direct_url import (
    DIRECT_URL_METADATA_NAME,
    DirectUrl,
    DirectUrlValidationError,
)
from pipenv.patched.notpip._internal.utils.compat import stdlib_pkgs  # TODO: Move definition here.
from pipenv.patched.notpip._internal.utils.egg_link import (
    egg_link_path_from_location,
    egg_link_path_from_sys_path,
)
from pipenv.patched.notpip._internal.utils.misc import is_local, normalize_path
from pipenv.patched.notpip._internal.utils.urls import url_to_path

if TYPE_CHECKING:
    from typing import Protocol
else:
    Protocol = object

DistributionVersion = Union[LegacyVersion, Version]

InfoPath = Union[str, pathlib.PurePosixPath]

logger = logging.getLogger(__name__)


class BaseEntryPoint(Protocol):
    @property
    def name(self) -> str:
        raise NotImplementedError()

    @property
    def value(self) -> str:
        raise NotImplementedError()

    @property
    def group(self) -> str:
        raise NotImplementedError()


def _convert_installed_files_path(
    entry: Tuple[str, ...],
    info: Tuple[str, ...],
) -> str:
    """Convert a legacy installed-files.txt path into modern RECORD path.

    The legacy format stores paths relative to the info directory, while the
    modern format stores paths relative to the package root, e.g. the
    site-packages directory.

    :param entry: Path parts of the installed-files.txt entry.
    :param info: Path parts of the egg-info directory relative to package root.
    :returns: The converted entry.

    For best compatibility with symlinks, this does not use ``abspath()`` or
    ``Path.resolve()``, but tries to work with path parts:

    1. While ``entry`` starts with ``..``, remove the equal amounts of parts
       from ``info``; if ``info`` is empty, start appending ``..`` instead.
    2. Join the two directly.
    """
    while entry and entry[0] == "..":
        if not info or info[-1] == "..":
            info += ("..",)
        else:
            info = info[:-1]
        entry = entry[1:]
    return str(pathlib.Path(*info, *entry))


class BaseDistribution(Protocol):
    def __repr__(self) -> str:
        return f"{self.raw_name} {self.version} ({self.location})"

    def __str__(self) -> str:
        return f"{self.raw_name} {self.version}"

    @property
    def location(self) -> Optional[str]:
        """Where the distribution is loaded from.

        A string value is not necessarily a filesystem path, since distributions
        can be loaded from other sources, e.g. arbitrary zip archives. ``None``
        means the distribution is created in-memory.

        Do not canonicalize this value with e.g. ``pathlib.Path.resolve()``. If
        this is a symbolic link, we want to preserve the relative path between
        it and files in the distribution.
        """
        raise NotImplementedError()

    @property
    def editable_project_location(self) -> Optional[str]:
        """The project location for editable distributions.

        This is the directory where pyproject.toml or setup.py is located.
        None if the distribution is not installed in editable mode.
        """
        # TODO: this property is relatively costly to compute, memoize it ?
        direct_url = self.direct_url
        if direct_url:
            if direct_url.is_local_editable():
                return url_to_path(direct_url.url)
        else:
            # Search for an .egg-link file by walking sys.path, as it was
            # done before by dist_is_editable().
            egg_link_path = egg_link_path_from_sys_path(self.raw_name)
            if egg_link_path:
                # TODO: get project location from second line of egg_link file
                #       (https://github.com/pypa/pip/issues/10243)
                return self.location
        return None

    @property
    def installed_location(self) -> Optional[str]:
        """The distribution's "installed" location.

        This should generally be a ``site-packages`` directory. This is
        usually ``dist.location``, except for legacy develop-installed packages,
        where ``dist.location`` is the source code location, and this is where
        the ``.egg-link`` file is.

        The returned location is normalized (in particular, with symlinks removed).
        """
        egg_link = egg_link_path_from_location(self.raw_name)
        if egg_link:
            location = egg_link
        elif self.location:
            location = self.location
        else:
            return None
        return normalize_path(location)

    @property
    def info_location(self) -> Optional[str]:
        """Location of the .[egg|dist]-info directory or file.

        Similarly to ``location``, a string value is not necessarily a
        filesystem path. ``None`` means the distribution is created in-memory.

        For a modern .dist-info installation on disk, this should be something
        like ``{location}/{raw_name}-{version}.dist-info``.

        Do not canonicalize this value with e.g. ``pathlib.Path.resolve()``. If
        this is a symbolic link, we want to preserve the relative path between
        it and other files in the distribution.
        """
        raise NotImplementedError()

    @property
    def installed_by_distutils(self) -> bool:
        """Whether this distribution is installed with legacy distutils format.

        A distribution installed with "raw" distutils not patched by setuptools
        uses one single file at ``info_location`` to store metadata. We need to
        treat this specially on uninstallation.
        """
        info_location = self.info_location
        if not info_location:
            return False
        return pathlib.Path(info_location).is_file()

    @property
    def installed_as_egg(self) -> bool:
        """Whether this distribution is installed as an egg.

        This usually indicates the distribution was installed by (older versions
        of) easy_install.
        """
        location = self.location
        if not location:
            return False
        return location.endswith(".egg")

    @property
    def installed_with_setuptools_egg_info(self) -> bool:
        """Whether this distribution is installed with the ``.egg-info`` format.

        This usually indicates the distribution was installed with setuptools
        with an old pip version or with ``single-version-externally-managed``.

        Note that this ensure the metadata store is a directory. distutils can
        also installs an ``.egg-info``, but as a file, not a directory. This
        property is *False* for that case. Also see ``installed_by_distutils``.
        """
        info_location = self.info_location
        if not info_location:
            return False
        if not info_location.endswith(".egg-info"):
            return False
        return pathlib.Path(info_location).is_dir()

    @property
    def installed_with_dist_info(self) -> bool:
        """Whether this distribution is installed with the "modern format".

        This indicates a "modern" installation, e.g. storing metadata in the
        ``.dist-info`` directory. This applies to installations made by
        setuptools (but through pip, not directly), or anything using the
        standardized build backend interface (PEP 517).
        """
        info_location = self.info_location
        if not info_location:
            return False
        if not info_location.endswith(".dist-info"):
            return False
        return pathlib.Path(info_location).is_dir()

    @property
    def canonical_name(self) -> NormalizedName:
        raise NotImplementedError()

    @property
    def version(self) -> DistributionVersion:
        raise NotImplementedError()

    @property
    def setuptools_filename(self) -> str:
        """Convert a project name to its setuptools-compatible filename.

        This is a copy of ``pkg_resources.to_filename()`` for compatibility.
        """
        return self.raw_name.replace("-", "_")

    @property
    def direct_url(self) -> Optional[DirectUrl]:
        """Obtain a DirectUrl from this distribution.

        Returns None if the distribution has no `direct_url.json` metadata,
        or if `direct_url.json` is invalid.
        """
        try:
            content = self.read_text(DIRECT_URL_METADATA_NAME)
        except FileNotFoundError:
            return None
        try:
            return DirectUrl.from_json(content)
        except (
            UnicodeDecodeError,
            json.JSONDecodeError,
            DirectUrlValidationError,
        ) as e:
            logger.warning(
                "Error parsing %s for %s: %s",
                DIRECT_URL_METADATA_NAME,
                self.canonical_name,
                e,
            )
            return None

    @property
    def installer(self) -> str:
        try:
            installer_text = self.read_text("INSTALLER")
        except (OSError, ValueError, NoneMetadataError):
            return ""  # Fail silently if the installer file cannot be read.
        for line in installer_text.splitlines():
            cleaned_line = line.strip()
            if cleaned_line:
                return cleaned_line
        return ""

    @property
    def editable(self) -> bool:
        return bool(self.editable_project_location)

    @property
    def local(self) -> bool:
        """If distribution is installed in the current virtual environment.

        Always True if we're not in a virtualenv.
        """
        if self.installed_location is None:
            return False
        return is_local(self.installed_location)

    @property
    def in_usersite(self) -> bool:
        if self.installed_location is None or user_site is None:
            return False
        return self.installed_location.startswith(normalize_path(user_site))

    @property
    def in_site_packages(self) -> bool:
        if self.installed_location is None or site_packages is None:
            return False
        return self.installed_location.startswith(normalize_path(site_packages))

    def is_file(self, path: InfoPath) -> bool:
        """Check whether an entry in the info directory is a file."""
        raise NotImplementedError()

    def iterdir(self, path: InfoPath) -> Iterator[pathlib.PurePosixPath]:
        """Iterate through a directory in the info directory.

        Each item yielded would be a path relative to the info directory.

        :raise FileNotFoundError: If ``name`` does not exist in the directory.
        :raise NotADirectoryError: If ``name`` does not point to a directory.
        """
        raise NotImplementedError()

    def read_text(self, path: InfoPath) -> str:
        """Read a file in the info directory.

        :raise FileNotFoundError: If ``name`` does not exist in the directory.
        :raise NoneMetadataError: If ``name`` exists in the info directory, but
            cannot be read.
        """
        raise NotImplementedError()

    def iter_entry_points(self) -> Iterable[BaseEntryPoint]:
        raise NotImplementedError()

    @property
    def metadata(self) -> email.message.Message:
        """Metadata of distribution parsed from e.g. METADATA or PKG-INFO.

        This should return an empty message if the metadata file is unavailable.

        :raises NoneMetadataError: If the metadata file is available, but does
            not contain valid metadata.
        """
        raise NotImplementedError()

    @property
    def metadata_version(self) -> Optional[str]:
        """Value of "Metadata-Version:" in distribution metadata, if available."""
        return self.metadata.get("Metadata-Version")

    @property
    def raw_name(self) -> str:
        """Value of "Name:" in distribution metadata."""
        # The metadata should NEVER be missing the Name: key, but if it somehow
        # does, fall back to the known canonical name.
        return self.metadata.get("Name", self.canonical_name)

    @property
    def requires_python(self) -> SpecifierSet:
        """Value of "Requires-Python:" in distribution metadata.

        If the key does not exist or contains an invalid value, an empty
        SpecifierSet should be returned.
        """
        value = self.metadata.get("Requires-Python")
        if value is None:
            return SpecifierSet()
        try:
            # Convert to str to satisfy the type checker; this can be a Header object.
            spec = SpecifierSet(str(value))
        except InvalidSpecifier as e:
            message = "Package %r has an invalid Requires-Python: %s"
            logger.warning(message, self.raw_name, e)
            return SpecifierSet()
        return spec

    def iter_dependencies(self, extras: Collection[str] = ()) -> Iterable[Requirement]:
        """Dependencies of this distribution.

        For modern .dist-info distributions, this is the collection of
        "Requires-Dist:" entries in distribution metadata.
        """
        raise NotImplementedError()

    def iter_provided_extras(self) -> Iterable[str]:
        """Extras provided by this distribution.

        For modern .dist-info distributions, this is the collection of
        "Provides-Extra:" entries in distribution metadata.
        """
        raise NotImplementedError()

    def _iter_declared_entries_from_record(self) -> Optional[Iterator[str]]:
        try:
            text = self.read_text("RECORD")
        except FileNotFoundError:
            return None
        # This extra Path-str cast normalizes entries.
        return (str(pathlib.Path(row[0])) for row in csv.reader(text.splitlines()))

    def _iter_declared_entries_from_legacy(self) -> Optional[Iterator[str]]:
        try:
            text = self.read_text("installed-files.txt")
        except FileNotFoundError:
            return None
        paths = (p for p in text.splitlines(keepends=False) if p)
        root = self.location
        info = self.info_location
        if root is None or info is None:
            return paths
        try:
            info_rel = pathlib.Path(info).relative_to(root)
        except ValueError:  # info is not relative to root.
            return paths
        if not info_rel.parts:  # info *is* root.
            return paths
        return (
            _convert_installed_files_path(pathlib.Path(p).parts, info_rel.parts)
            for p in paths
        )

    def iter_declared_entries(self) -> Optional[Iterator[str]]:
        """Iterate through file entires declared in this distribution.

        For modern .dist-info distributions, this is the files listed in the
        ``RECORD`` metadata file. For legacy setuptools distributions, this
        comes from ``installed-files.txt``, with entries normalized to be
        compatible with the format used by ``RECORD``.

        :return: An iterator for listed entries, or None if the distribution
            contains neither ``RECORD`` nor ``installed-files.txt``.
        """
        return (
            self._iter_declared_entries_from_record()
            or self._iter_declared_entries_from_legacy()
        )


class BaseEnvironment:
    """An environment containing distributions to introspect."""

    @classmethod
    def default(cls) -> "BaseEnvironment":
        raise NotImplementedError()

    @classmethod
    def from_paths(cls, paths: Optional[List[str]]) -> "BaseEnvironment":
        raise NotImplementedError()

    def get_distribution(self, name: str) -> Optional["BaseDistribution"]:
        """Given a requirement name, return the installed distributions.

        The name may not be normalized. The implementation must canonicalize
        it for lookup.
        """
        raise NotImplementedError()

    def _iter_distributions(self) -> Iterator["BaseDistribution"]:
        """Iterate through installed distributions.

        This function should be implemented by subclass, but never called
        directly. Use the public ``iter_distribution()`` instead, which
        implements additional logic to make sure the distributions are valid.
        """
        raise NotImplementedError()

    def iter_distributions(self) -> Iterator["BaseDistribution"]:
        """Iterate through installed distributions."""
        for dist in self._iter_distributions():
            # Make sure the distribution actually comes from a valid Python
            # packaging distribution. Pip's AdjacentTempDirectory leaves folders
            # e.g. ``~atplotlib.dist-info`` if cleanup was interrupted. The
            # valid project name pattern is taken from PEP 508.
            project_name_valid = re.match(
                r"^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$",
                dist.canonical_name,
                flags=re.IGNORECASE,
            )
            if not project_name_valid:
                logger.warning(
                    "Ignoring invalid distribution %s (%s)",
                    dist.canonical_name,
                    dist.location,
                )
                continue
            yield dist

    def iter_installed_distributions(
        self,
        local_only: bool = True,
        skip: Container[str] = stdlib_pkgs,
        include_editables: bool = True,
        editables_only: bool = False,
        user_only: bool = False,
    ) -> Iterator[BaseDistribution]:
        """Return a list of installed distributions.

        :param local_only: If True (default), only return installations
        local to the current virtualenv, if in a virtualenv.
        :param skip: An iterable of canonicalized project names to ignore;
            defaults to ``stdlib_pkgs``.
        :param include_editables: If False, don't report editables.
        :param editables_only: If True, only report editables.
        :param user_only: If True, only report installations in the user
        site directory.
        """
        it = self.iter_distributions()
        if local_only:
            it = (d for d in it if d.local)
        if not include_editables:
            it = (d for d in it if not d.editable)
        if editables_only:
            it = (d for d in it if d.editable)
        if user_only:
            it = (d for d in it if d.in_usersite)
        return (d for d in it if d.canonical_name not in skip)


class Wheel(Protocol):
    location: str

    def as_zipfile(self) -> zipfile.ZipFile:
        raise NotImplementedError()


class FilesystemWheel(Wheel):
    def __init__(self, location: str) -> None:
        self.location = location

    def as_zipfile(self) -> zipfile.ZipFile:
        return zipfile.ZipFile(self.location, allowZip64=True)


class MemoryWheel(Wheel):
    def __init__(self, location: str, stream: IO[bytes]) -> None:
        self.location = location
        self.stream = stream

    def as_zipfile(self) -> zipfile.ZipFile:
        return zipfile.ZipFile(self.stream, allowZip64=True)
