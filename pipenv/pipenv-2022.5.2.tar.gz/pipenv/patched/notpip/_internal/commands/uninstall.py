import logging
from optparse import Values
from typing import List

from pipenv.patched.notpip._vendor.packaging.utils import canonicalize_name

from pipenv.patched.notpip._internal.cli.base_command import Command
from pipenv.patched.notpip._internal.cli.req_command import SessionCommandMixin, warn_if_run_as_root
from pipenv.patched.notpip._internal.cli.status_codes import SUCCESS
from pipenv.patched.notpip._internal.exceptions import InstallationError
from pipenv.patched.notpip._internal.req import parse_requirements
from pipenv.patched.notpip._internal.req.constructors import (
    install_req_from_line,
    install_req_from_parsed_requirement,
)
from pipenv.patched.notpip._internal.utils.misc import protect_pip_from_modification_on_windows

logger = logging.getLogger(__name__)


class UninstallCommand(Command, SessionCommandMixin):
    """
    Uninstall packages.

    pip is able to uninstall most installed packages. Known exceptions are:

    - Pure distutils packages installed with ``python setup.py install``, which
      leave behind no metadata to determine what files were installed.
    - Script wrappers installed by ``python setup.py develop``.
    """

    usage = """
      %prog [options] <package> ...
      %prog [options] -r <requirements file> ..."""

    def add_options(self) -> None:
        self.cmd_opts.add_option(
            "-r",
            "--requirement",
            dest="requirements",
            action="append",
            default=[],
            metavar="file",
            help=(
                "Uninstall all the packages listed in the given requirements "
                "file.  This option can be used multiple times."
            ),
        )
        self.cmd_opts.add_option(
            "-y",
            "--yes",
            dest="yes",
            action="store_true",
            help="Don't ask for confirmation of uninstall deletions.",
        )

        self.parser.insert_option_group(0, self.cmd_opts)

    def run(self, options: Values, args: List[str]) -> int:
        session = self.get_default_session(options)

        reqs_to_uninstall = {}
        for name in args:
            req = install_req_from_line(
                name,
                isolated=options.isolated_mode,
            )
            if req.name:
                reqs_to_uninstall[canonicalize_name(req.name)] = req
            else:
                logger.warning(
                    "Invalid requirement: %r ignored -"
                    " the uninstall command expects named"
                    " requirements.",
                    name,
                )
        for filename in options.requirements:
            for parsed_req in parse_requirements(
                filename, options=options, session=session
            ):
                req = install_req_from_parsed_requirement(
                    parsed_req, isolated=options.isolated_mode
                )
                if req.name:
                    reqs_to_uninstall[canonicalize_name(req.name)] = req
        if not reqs_to_uninstall:
            raise InstallationError(
                f"You must give at least one requirement to {self.name} (see "
                f'"pip help {self.name}")'
            )

        protect_pip_from_modification_on_windows(
            modifying_pip="pip" in reqs_to_uninstall
        )

        for req in reqs_to_uninstall.values():
            uninstall_pathset = req.uninstall(
                auto_confirm=options.yes,
                verbose=self.verbosity > 0,
            )
            if uninstall_pathset:
                uninstall_pathset.commit()

        warn_if_run_as_root()
        return SUCCESS
