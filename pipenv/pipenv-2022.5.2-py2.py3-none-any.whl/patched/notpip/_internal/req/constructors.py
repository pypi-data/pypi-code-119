"""Backing implementation for InstallRequirement's various constructors

The idea here is that these formed a major chunk of InstallRequirement's size
so, moving them and support code dedicated to them outside of that class
helps creates for better understandability for the rest of the code.

These are meant to be used elsewhere within pip to create instances of
InstallRequirement.
"""

import logging
import os
import re
from typing import Any, Dict, Optional, Set, Tuple, Union

from pipenv.patched.notpip._vendor.packaging.markers import Marker
from pipenv.patched.notpip._vendor.packaging.requirements import InvalidRequirement, Requirement
from pipenv.patched.notpip._vendor.packaging.specifiers import Specifier

from pipenv.patched.notpip._internal.exceptions import InstallationError
from pipenv.patched.notpip._internal.models.index import PyPI, TestPyPI
from pipenv.patched.notpip._internal.models.link import Link
from pipenv.patched.notpip._internal.models.wheel import Wheel
from pipenv.patched.notpip._internal.req.req_file import ParsedRequirement
from pipenv.patched.notpip._internal.req.req_install import InstallRequirement
from pipenv.patched.notpip._internal.utils.filetypes import is_archive_file
from pipenv.patched.notpip._internal.utils.misc import is_installable_dir
from pipenv.patched.notpip._internal.utils.packaging import get_requirement
from pipenv.patched.notpip._internal.utils.urls import path_to_url
from pipenv.patched.notpip._internal.vcs import is_url, vcs

__all__ = [
    "install_req_from_editable",
    "install_req_from_line",
    "parse_editable",
]

logger = logging.getLogger(__name__)
operators = Specifier._operators.keys()


def _strip_extras(path: str) -> Tuple[str, Optional[str]]:
    m = re.match(r"^(.+)(\[[^\]]+\])$", path)
    extras = None
    if m:
        path_no_extras = m.group(1)
        extras = m.group(2)
    else:
        path_no_extras = path

    return path_no_extras, extras


def convert_extras(extras: Optional[str]) -> Set[str]:
    if not extras:
        return set()
    return get_requirement("placeholder" + extras.lower()).extras


def parse_editable(editable_req: str) -> Tuple[Optional[str], str, Set[str]]:
    """Parses an editable requirement into:
        - a requirement name
        - an URL
        - extras
        - editable options
    Accepted requirements:
        svn+http://blahblah@rev#egg=Foobar[baz]&subdirectory=version_subdir
        .[some_extra]
    """

    url = editable_req

    # If a file path is specified with extras, strip off the extras.
    url_no_extras, extras = _strip_extras(url)

    if os.path.isdir(url_no_extras):
        # Treating it as code that has already been checked out
        url_no_extras = path_to_url(url_no_extras)

    if url_no_extras.lower().startswith("file:"):
        package_name = Link(url_no_extras).egg_fragment
        if extras:
            return (
                package_name,
                url_no_extras,
                get_requirement("placeholder" + extras.lower()).extras,
            )
        else:
            return package_name, url_no_extras, set()

    for version_control in vcs:
        if url.lower().startswith(f"{version_control}:"):
            url = f"{version_control}+{url}"
            break

    link = Link(url)

    if not link.is_vcs:
        backends = ", ".join(vcs.all_schemes)
        raise InstallationError(
            f"{editable_req} is not a valid editable requirement. "
            f"It should either be a path to a local project or a VCS URL "
            f"(beginning with {backends})."
        )

    package_name = link.egg_fragment
    if not package_name:
        raise InstallationError(
            "Could not detect requirement name for '{}', please specify one "
            "with #egg=your_package_name".format(editable_req)
        )
    return package_name, url, set()


def check_first_requirement_in_file(filename: str) -> None:
    """Check if file is parsable as a requirements file.

    This is heavily based on ``pkg_resources.parse_requirements``, but
    simplified to just check the first meaningful line.

    :raises InvalidRequirement: If the first meaningful line cannot be parsed
        as an requirement.
    """
    with open(filename, encoding="utf-8", errors="ignore") as f:
        # Create a steppable iterator, so we can handle \-continuations.
        lines = (
            line
            for line in (line.strip() for line in f)
            if line and not line.startswith("#")  # Skip blank lines/comments.
        )

        for line in lines:
            # Drop comments -- a hash without a space may be in a URL.
            if " #" in line:
                line = line[: line.find(" #")]
            # If there is a line continuation, drop it, and append the next line.
            if line.endswith("\\"):
                line = line[:-2].strip() + next(lines, "")
            Requirement(line)
            return


def deduce_helpful_msg(req: str) -> str:
    """Returns helpful msg in case requirements file does not exist,
    or cannot be parsed.

    :params req: Requirements file path
    """
    if not os.path.exists(req):
        return f" File '{req}' does not exist."
    msg = " The path does exist. "
    # Try to parse and check if it is a requirements file.
    try:
        check_first_requirement_in_file(req)
    except InvalidRequirement:
        logger.debug("Cannot parse '%s' as requirements file", req)
    else:
        msg += (
            f"The argument you provided "
            f"({req}) appears to be a"
            f" requirements file. If that is the"
            f" case, use the '-r' flag to install"
            f" the packages specified within it."
        )
    return msg


class RequirementParts:
    def __init__(
        self,
        requirement: Optional[Requirement],
        link: Optional[Link],
        markers: Optional[Marker],
        extras: Set[str],
    ):
        self.requirement = requirement
        self.link = link
        self.markers = markers
        self.extras = extras


def parse_req_from_editable(editable_req: str) -> RequirementParts:
    name, url, extras_override = parse_editable(editable_req)

    if name is not None:
        try:
            req: Optional[Requirement] = Requirement(name)
        except InvalidRequirement:
            raise InstallationError(f"Invalid requirement: '{name}'")
    else:
        req = None

    link = Link(url)

    return RequirementParts(req, link, None, extras_override)


# ---- The actual constructors follow ----


def install_req_from_editable(
    editable_req: str,
    comes_from: Optional[Union[InstallRequirement, str]] = None,
    use_pep517: Optional[bool] = None,
    isolated: bool = False,
    options: Optional[Dict[str, Any]] = None,
    constraint: bool = False,
    user_supplied: bool = False,
    permit_editable_wheels: bool = False,
) -> InstallRequirement:

    parts = parse_req_from_editable(editable_req)

    return InstallRequirement(
        parts.requirement,
        comes_from=comes_from,
        user_supplied=user_supplied,
        editable=True,
        permit_editable_wheels=permit_editable_wheels,
        link=parts.link,
        constraint=constraint,
        use_pep517=use_pep517,
        isolated=isolated,
        install_options=options.get("install_options", []) if options else [],
        global_options=options.get("global_options", []) if options else [],
        hash_options=options.get("hashes", {}) if options else {},
        extras=parts.extras,
    )


def _looks_like_path(name: str) -> bool:
    """Checks whether the string "looks like" a path on the filesystem.

    This does not check whether the target actually exists, only judge from the
    appearance.

    Returns true if any of the following conditions is true:
    * a path separator is found (either os.path.sep or os.path.altsep);
    * a dot is found (which represents the current directory).
    """
    if os.path.sep in name:
        return True
    if os.path.altsep is not None and os.path.altsep in name:
        return True
    if name.startswith("."):
        return True
    return False


def _get_url_from_path(path: str, name: str) -> Optional[str]:
    """
    First, it checks whether a provided path is an installable directory. If it
    is, returns the path.

    If false, check if the path is an archive file (such as a .whl).
    The function checks if the path is a file. If false, if the path has
    an @, it will treat it as a PEP 440 URL requirement and return the path.
    """
    if _looks_like_path(name) and os.path.isdir(path):
        if is_installable_dir(path):
            return path_to_url(path)
        # TODO: The is_installable_dir test here might not be necessary
        #       now that it is done in load_pyproject_toml too.
        raise InstallationError(
            f"Directory {name!r} is not installable. Neither 'setup.py' "
            "nor 'pyproject.toml' found."
        )
    if not is_archive_file(path):
        return None
    if os.path.isfile(path):
        return path_to_url(path)
    urlreq_parts = name.split("@", 1)
    if len(urlreq_parts) >= 2 and not _looks_like_path(urlreq_parts[0]):
        # If the path contains '@' and the part before it does not look
        # like a path, try to treat it as a PEP 440 URL req instead.
        return None
    logger.warning(
        "Requirement %r looks like a filename, but the file does not exist",
        name,
    )
    return path_to_url(path)


def parse_req_from_line(name: str, line_source: Optional[str]) -> RequirementParts:
    if is_url(name):
        marker_sep = "; "
    else:
        marker_sep = ";"
    if marker_sep in name:
        name, markers_as_string = name.split(marker_sep, 1)
        markers_as_string = markers_as_string.strip()
        if not markers_as_string:
            markers = None
        else:
            markers = Marker(markers_as_string)
    else:
        markers = None
    name = name.strip()
    req_as_string = None
    path = os.path.normpath(os.path.abspath(name))
    link = None
    extras_as_string = None

    if is_url(name):
        link = Link(name)
    else:
        p, extras_as_string = _strip_extras(path)
        url = _get_url_from_path(p, name)
        if url is not None:
            link = Link(url)

    # it's a local file, dir, or url
    if link:
        # Handle relative file URLs
        if link.scheme == "file" and re.search(r"\.\./", link.url):
            link = Link(path_to_url(os.path.normpath(os.path.abspath(link.path))))
        # wheel file
        if link.is_wheel:
            wheel = Wheel(link.filename)  # can raise InvalidWheelFilename
            req_as_string = f"{wheel.name}=={wheel.version}"
        else:
            # set the req to the egg fragment.  when it's not there, this
            # will become an 'unnamed' requirement
            req_as_string = link.egg_fragment

    # a requirement specifier
    else:
        req_as_string = name

    extras = convert_extras(extras_as_string)

    def with_source(text: str) -> str:
        if not line_source:
            return text
        return f"{text} (from {line_source})"

    def _parse_req_string(req_as_string: str) -> Requirement:
        try:
            req = get_requirement(req_as_string)
        except InvalidRequirement:
            if os.path.sep in req_as_string:
                add_msg = "It looks like a path."
                add_msg += deduce_helpful_msg(req_as_string)
            elif "=" in req_as_string and not any(
                op in req_as_string for op in operators
            ):
                add_msg = "= is not a valid operator. Did you mean == ?"
            else:
                add_msg = ""
            msg = with_source(f"Invalid requirement: {req_as_string!r}")
            if add_msg:
                msg += f"\nHint: {add_msg}"
            raise InstallationError(msg)
        else:
            # Deprecate extras after specifiers: "name>=1.0[extras]"
            # This currently works by accident because _strip_extras() parses
            # any extras in the end of the string and those are saved in
            # RequirementParts
            for spec in req.specifier:
                spec_str = str(spec)
                if spec_str.endswith("]"):
                    msg = f"Extras after version '{spec_str}'."
                    raise InstallationError(msg)
        return req

    if req_as_string is not None:
        req: Optional[Requirement] = _parse_req_string(req_as_string)
    else:
        req = None

    return RequirementParts(req, link, markers, extras)


def install_req_from_line(
    name: str,
    comes_from: Optional[Union[str, InstallRequirement]] = None,
    use_pep517: Optional[bool] = None,
    isolated: bool = False,
    options: Optional[Dict[str, Any]] = None,
    constraint: bool = False,
    line_source: Optional[str] = None,
    user_supplied: bool = False,
) -> InstallRequirement:
    """Creates an InstallRequirement from a name, which might be a
    requirement, directory containing 'setup.py', filename, or URL.

    :param line_source: An optional string describing where the line is from,
        for logging purposes in case of an error.
    """
    parts = parse_req_from_line(name, line_source)

    return InstallRequirement(
        parts.requirement,
        comes_from,
        link=parts.link,
        markers=parts.markers,
        use_pep517=use_pep517,
        isolated=isolated,
        install_options=options.get("install_options", []) if options else [],
        global_options=options.get("global_options", []) if options else [],
        hash_options=options.get("hashes", {}) if options else {},
        constraint=constraint,
        extras=parts.extras,
        user_supplied=user_supplied,
    )


def install_req_from_req_string(
    req_string: str,
    comes_from: Optional[InstallRequirement] = None,
    isolated: bool = False,
    use_pep517: Optional[bool] = None,
    user_supplied: bool = False,
) -> InstallRequirement:
    try:
        req = get_requirement(req_string)
    except InvalidRequirement:
        raise InstallationError(f"Invalid requirement: '{req_string}'")

    domains_not_allowed = [
        PyPI.file_storage_domain,
        TestPyPI.file_storage_domain,
    ]
    if (
        req.url
        and comes_from
        and comes_from.link
        and comes_from.link.netloc in domains_not_allowed
    ):
        # Explicitly disallow pypi packages that depend on external urls
        raise InstallationError(
            "Packages installed from PyPI cannot depend on packages "
            "which are not also hosted on PyPI.\n"
            "{} depends on {} ".format(comes_from.name, req)
        )

    return InstallRequirement(
        req,
        comes_from,
        isolated=isolated,
        use_pep517=use_pep517,
        user_supplied=user_supplied,
    )


def install_req_from_parsed_requirement(
    parsed_req: ParsedRequirement,
    isolated: bool = False,
    use_pep517: Optional[bool] = None,
    user_supplied: bool = False,
) -> InstallRequirement:
    if parsed_req.is_editable:
        req = install_req_from_editable(
            parsed_req.requirement,
            comes_from=parsed_req.comes_from,
            use_pep517=use_pep517,
            constraint=parsed_req.constraint,
            isolated=isolated,
            user_supplied=user_supplied,
        )

    else:
        req = install_req_from_line(
            parsed_req.requirement,
            comes_from=parsed_req.comes_from,
            use_pep517=use_pep517,
            isolated=isolated,
            options=parsed_req.options,
            constraint=parsed_req.constraint,
            line_source=parsed_req.line_source,
            user_supplied=user_supplied,
        )
    return req


def install_req_from_link_and_ireq(
    link: Link, ireq: InstallRequirement
) -> InstallRequirement:
    return InstallRequirement(
        req=ireq.req,
        comes_from=ireq.comes_from,
        editable=ireq.editable,
        link=link,
        markers=ireq.markers,
        use_pep517=ireq.use_pep517,
        isolated=ireq.isolated,
        install_options=ireq.install_options,
        global_options=ireq.global_options,
        hash_options=ireq.hash_options,
    )
