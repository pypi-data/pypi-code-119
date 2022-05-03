import logging
import os
from optparse import Values
from typing import List

from pipenv.patched.notpip._internal.cli import cmdoptions
from pipenv.patched.notpip._internal.cli.cmdoptions import make_target_python
from pipenv.patched.notpip._internal.cli.req_command import RequirementCommand, with_cleanup
from pipenv.patched.notpip._internal.cli.status_codes import SUCCESS
from pipenv.patched.notpip._internal.req.req_tracker import get_requirement_tracker
from pipenv.patched.notpip._internal.utils.misc import ensure_dir, normalize_path, write_output
from pipenv.patched.notpip._internal.utils.temp_dir import TempDirectory

logger = logging.getLogger(__name__)


class DownloadCommand(RequirementCommand):
    """
    Download packages from:

    - PyPI (and other indexes) using requirement specifiers.
    - VCS project urls.
    - Local project directories.
    - Local or remote source archives.

    pip also supports downloading from "requirements files", which provide
    an easy way to specify a whole environment to be downloaded.
    """

    usage = """
      %prog [options] <requirement specifier> [package-index-options] ...
      %prog [options] -r <requirements file> [package-index-options] ...
      %prog [options] <vcs project url> ...
      %prog [options] <local project path> ...
      %prog [options] <archive url/path> ..."""

    def add_options(self) -> None:
        self.cmd_opts.add_option(cmdoptions.constraints())
        self.cmd_opts.add_option(cmdoptions.requirements())
        self.cmd_opts.add_option(cmdoptions.no_deps())
        self.cmd_opts.add_option(cmdoptions.global_options())
        self.cmd_opts.add_option(cmdoptions.no_binary())
        self.cmd_opts.add_option(cmdoptions.only_binary())
        self.cmd_opts.add_option(cmdoptions.prefer_binary())
        self.cmd_opts.add_option(cmdoptions.src())
        self.cmd_opts.add_option(cmdoptions.pre())
        self.cmd_opts.add_option(cmdoptions.require_hashes())
        self.cmd_opts.add_option(cmdoptions.progress_bar())
        self.cmd_opts.add_option(cmdoptions.no_build_isolation())
        self.cmd_opts.add_option(cmdoptions.use_pep517())
        self.cmd_opts.add_option(cmdoptions.no_use_pep517())
        self.cmd_opts.add_option(cmdoptions.ignore_requires_python())

        self.cmd_opts.add_option(
            "-d",
            "--dest",
            "--destination-dir",
            "--destination-directory",
            dest="download_dir",
            metavar="dir",
            default=os.curdir,
            help="Download packages into <dir>.",
        )

        cmdoptions.add_target_python_options(self.cmd_opts)

        index_opts = cmdoptions.make_option_group(
            cmdoptions.index_group,
            self.parser,
        )

        self.parser.insert_option_group(0, index_opts)
        self.parser.insert_option_group(0, self.cmd_opts)

    @with_cleanup
    def run(self, options: Values, args: List[str]) -> int:

        options.ignore_installed = True
        # editable doesn't really make sense for `pip download`, but the bowels
        # of the RequirementSet code require that property.
        options.editables = []

        cmdoptions.check_dist_restriction(options)

        options.download_dir = normalize_path(options.download_dir)
        ensure_dir(options.download_dir)

        session = self.get_default_session(options)

        target_python = make_target_python(options)
        finder = self._build_package_finder(
            options=options,
            session=session,
            target_python=target_python,
            ignore_requires_python=options.ignore_requires_python,
        )

        req_tracker = self.enter_context(get_requirement_tracker())

        directory = TempDirectory(
            delete=not options.no_clean,
            kind="download",
            globally_managed=True,
        )

        reqs = self.get_requirements(args, options, finder, session)

        preparer = self.make_requirement_preparer(
            temp_build_dir=directory,
            options=options,
            req_tracker=req_tracker,
            session=session,
            finder=finder,
            download_dir=options.download_dir,
            use_user_site=False,
            verbosity=self.verbosity,
        )

        resolver = self.make_resolver(
            preparer=preparer,
            finder=finder,
            options=options,
            ignore_requires_python=options.ignore_requires_python,
            py_version_info=options.python_version,
        )

        self.trace_basic_info(finder)

        requirement_set = resolver.resolve(reqs, check_supported_wheels=True)

        downloaded: List[str] = []
        for req in requirement_set.requirements.values():
            if req.satisfied_by is None:
                assert req.name is not None
                preparer.save_linked_requirement(req)
                downloaded.append(req.name)
        if downloaded:
            write_output("Successfully downloaded %s", " ".join(downloaded))

        return SUCCESS
