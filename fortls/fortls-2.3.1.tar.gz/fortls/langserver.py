# TODO: enable jsonc C-style comments
from __future__ import annotations

import json
import logging
import os
import re
import subprocess
import sys
import traceback
import urllib.request
from multiprocessing import Pool
from pathlib import Path
from typing import Pattern
from urllib.error import URLError

from packaging import version

# Local modules
from fortls.constants import (
    CLASS_TYPE_ID,
    FORTRAN_LITERAL,
    FUNCTION_TYPE_ID,
    INTERFACE_TYPE_ID,
    METH_TYPE_ID,
    MODULE_TYPE_ID,
    SELECT_TYPE_ID,
    SUBROUTINE_TYPE_ID,
    VAR_TYPE_ID,
    FRegex,
    Severity,
    log,
)
from fortls.helper_functions import (
    expand_name,
    get_line_prefix,
    get_paren_level,
    get_var_stack,
    only_dirs,
    resolve_globs,
    set_keyword_ordering,
)
from fortls.intrinsics import (
    fortran_intrinsic_obj,
    get_intrinsic_keywords,
    load_intrinsics,
    set_lowercase_intrinsics,
)
from fortls.json_templates import change_json, symbol_json, uri_json
from fortls.jsonrpc import JSONRPC2Connection, path_from_uri, path_to_uri
from fortls.objects import (
    climb_type_tree,
    find_in_scope,
    find_in_workspace,
    fortran_ast,
    fortran_var,
    get_use_tree,
)
from fortls.parse_fortran import fortran_file, get_line_context
from fortls.regex_patterns import src_file_exts
from fortls.version import __version__

# Global regexes
# TODO: I think this can be replaced by fortls.regex_patterns type & class
TYPE_DEF_REGEX = re.compile(r"[ ]*(TYPE|CLASS)[ ]*\([a-z0-9_ ]*$", re.I)


class LangServer:
    def __init__(self, conn, settings: dict):
        self.conn: JSONRPC2Connection = conn
        self.running: bool = True
        self.root_path: str = None
        self.workspace: dict[str, fortran_file] = {}
        self.obj_tree: dict = {}
        self.link_version = 0
        self._version = version.parse(__version__)
        # Parse a dictionary of the command line interface and make them into
        # class variable. This way the command line and the file interfaces
        # are always on sync, with the same default arguments
        for k, v in settings.items():
            # Do not parse command line debug arguments
            if k.startswith("debug_") and k != "debug_log":
                continue
            setattr(self, k, v)

        self.sync_type: int = 2 if self.incremental_sync else 1
        self.post_messages = []
        self.FORTRAN_SRC_EXT_REGEX: Pattern[str] = src_file_exts()
        # Intrinsic (re-loaded during initialize)
        (
            self.statements,
            self.keywords,
            self.intrinsic_funs,
            self.intrinsic_mods,
        ) = load_intrinsics()
        # Set object settings
        set_keyword_ordering(self.sort_keywords)

    def post_message(self, msg: str, severity: int = Severity.error, exc_info=False):
        self.conn.send_notification(
            "window/showMessage", {"type": severity, "message": msg}
        )
        if severity == 1:
            log.error(msg, exc_info=exc_info)
        elif severity == 2:
            log.warning(msg, exc_info=exc_info)
        elif severity == 3:
            log.info(msg, exc_info=exc_info)

    def run(self):
        # Run server
        while self.running:
            try:
                request = self.conn.read_message()
                self.handle(request)
            except EOFError:
                break
            except Exception as e:
                self.post_message(f"Unexpected error: {e}", exc_info=True)
                break
            else:
                for message in self.post_messages:
                    self.post_message(message[1], message[0])
                self.post_messages = []

    def handle(self, request: dict):
        def noop(request: dict):
            return None

        # Request handler
        log.debug("REQUEST %s %s", request.get("id"), request.get("method"))
        handler = {
            "initialize": self.serve_initialize,
            "textDocument/documentSymbol": self.serve_document_symbols,
            "textDocument/completion": self.serve_autocomplete,
            "textDocument/signatureHelp": self.serve_signature,
            "textDocument/definition": self.serve_definition,
            "textDocument/references": self.serve_references,
            "textDocument/hover": self.serve_hover,
            "textDocument/implementation": self.serve_implementation,
            "textDocument/rename": self.serve_rename,
            "textDocument/didOpen": self.serve_onOpen,
            "textDocument/didSave": self.serve_onSave,
            "textDocument/didClose": self.serve_onClose,
            "textDocument/didChange": self.serve_onChange,
            "textDocument/codeAction": self.serve_codeActions,
            "initialized": noop,
            "workspace/didChangeWatchedFiles": noop,
            "workspace/symbol": self.serve_workspace_symbol,
            "$/cancelRequest": noop,
            "$/setTrace": noop,
            "shutdown": noop,
            "exit": self.serve_exit,
        }.get(request["method"], self.serve_default)

        # We handle notifications differently since we can't respond
        if "id" not in request:
            try:
                handler(request)
            except:
                log.exception("error handling request: %s", request, exc_info=True)
            return
        #
        try:
            resp = handler(request)
        except JSONRPC2Error as e:
            self.conn.write_error(
                request["id"], code=e.code, message=e.message, data=e.data
            )
            log.warning("RPC error handling request %s", request, exc_info=True)
        except Exception as e:
            self.conn.write_error(
                request["id"],
                code=-32603,
                message=str(e),
                data={
                    "traceback": traceback.format_exc(),
                },
            )
            log.warning("error handling request %s", request, exc_info=True)
        else:
            self.conn.write_response(request["id"], resp)

    def serve_initialize(self, request: dict):
        # Setup language server
        params: dict = request["params"]
        self.root_path = path_from_uri(
            params.get("rootUri") or params.get("rootPath") or ""
        )
        self.source_dirs.add(self.root_path)

        self._load_config_file()
        self._config_logger(request)
        self._load_intrinsics()
        self._add_source_dirs()
        if self._update_version_pypi():
            self.post_message(
                "Please restart the server for the new version to activate",
                Severity.info,
            )

        # Initialize workspace
        self.workspace_init()
        log.info(f"fortls - Fortran Language Server {__version__} Initialized")
        #
        server_capabilities = {
            "completionProvider": {
                "resolveProvider": False,
                "triggerCharacters": ["%"],
            },
            "definitionProvider": True,
            "documentSymbolProvider": True,
            "referencesProvider": True,
            "hoverProvider": True,
            "implementationProvider": True,
            "renameProvider": True,
            "workspaceSymbolProvider": True,
            "textDocumentSync": self.sync_type,
        }
        if self.use_signature_help:
            server_capabilities["signatureHelpProvider"] = {
                "triggerCharacters": ["(", ","]
            }
        if self.enable_code_actions:
            server_capabilities["codeActionProvider"] = True
        if self.notify_init:
            self.post_message("fortls initialization complete", Severity.info)
        return {"capabilities": server_capabilities}

    def serve_workspace_symbol(self, request):
        def map_types(type):
            if type == 1:
                return 2
            elif type == 2:
                return 6
            elif type == 3:
                return 12
            elif type == 4:
                return 5
            elif type == 5:
                return 11
            elif type == 6:
                return 13
            elif type == 7:
                return 6
            else:
                return 1

        matching_symbols = []
        query = request["params"]["query"].lower()
        for candidate in find_in_workspace(self.obj_tree, query):
            tmp_out = {
                "name": candidate.name,
                "kind": map_types(candidate.get_type()),
                "location": {
                    "uri": path_to_uri(candidate.file_ast.path),
                    "range": {
                        "start": {"line": candidate.sline - 1, "character": 0},
                        "end": {"line": candidate.eline - 1, "character": 0},
                    },
                },
            }
            # Set containing scope
            if candidate.FQSN.find("::") > 0:
                tmp_list = candidate.FQSN.split("::")
                tmp_out["containerName"] = tmp_list[0]
            matching_symbols.append(tmp_out)
        return sorted(matching_symbols, key=lambda k: k["name"])

    def serve_document_symbols(self, request: dict):
        def map_types(type, in_class: bool = False):
            if type == 1:
                return 2
            elif type in (2, 3):
                if in_class:
                    return 6
                else:
                    return 12
            elif type == 4:
                return 5
            elif type == 5:
                return 11
            elif type == 6:
                return 13
            elif type == 7:
                return 6
            else:
                return 1

        # Get parameters from request
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        path: str = path_from_uri(uri)
        file_obj = self.workspace.get(path)
        if file_obj is None:
            return []
        # Add scopes to outline view
        test_output = []
        for scope in file_obj.ast.get_scopes():
            if (scope.name[0] == "#") or (scope.get_type() == SELECT_TYPE_ID):
                continue
            scope_tree = scope.FQSN.split("::")
            if len(scope_tree) > 2:
                if scope_tree[1].startswith("#gen_int"):
                    scope_type = 11
                else:
                    continue
            else:
                scope_type = map_types(scope.get_type())

            # Set containing scope
            if scope.FQSN.find("::") > 0:
                tmp_list = scope.FQSN.split("::")
                test_output.append(
                    symbol_json(
                        scope.name,
                        scope_type,
                        uri,
                        scope.sline - 1,
                        0,
                        scope.eline - 1,
                        0,
                        tmp_list[0],
                    )
                )
            else:
                test_output.append(
                    symbol_json(
                        scope.name,
                        scope_type,
                        uri,
                        scope.sline - 1,
                        0,
                        scope.eline - 1,
                        0,
                    )
                )
            # If class add members
            if scope.get_type() == CLASS_TYPE_ID and not self.symbol_skip_mem:
                for child in scope.children:
                    test_output.append(
                        symbol_json(
                            child.name,
                            map_types(child.get_type(), True),
                            uri,
                            child.sline - 1,
                            0,
                            container_name=scope.name,
                        )
                    )
        return test_output

    def serve_autocomplete(self, request: dict):
        #
        def map_types(type: int):
            if type == 1:
                return 9
            elif type == 2:
                return 3
            elif type == 4:
                return 7
            elif type == 6:
                return 6
            else:
                return type

        def set_type_mask(def_value):
            return [def_value if i < 8 else True for i in range(16)]

        def get_candidates(
            scope_list: list,
            var_prefix: str,
            inc_globals: bool = True,
            public_only: bool = False,
            abstract_only: bool = False,
            no_use: bool = False,
        ):
            #
            def child_candidates(
                scope, only_list: list = None, filter_public=True, req_abstract=False
            ):
                if only_list is None:
                    only_list = []
                tmp_list = []
                # Filter children
                nonly = len(only_list)
                for child in scope.get_children(filter_public):
                    if req_abstract:
                        if child.is_abstract():
                            tmp_list += child_candidates(
                                child, only_list, filter_public
                            )
                    else:
                        if child.is_external_int():
                            tmp_list += child_candidates(
                                child, only_list, filter_public
                            )
                        else:
                            if (nonly > 0) and (child.name.lower() not in only_list):
                                continue
                            tmp_list.append(child)
                return tmp_list

            var_list = []
            use_dict = {}
            for scope in scope_list:
                var_list += child_candidates(
                    scope, filter_public=public_only, req_abstract=abstract_only
                )
                # Traverse USE tree and add to list
                if not no_use:
                    use_dict = get_use_tree(scope, use_dict, self.obj_tree)
            # Look in found use modules
            rename_list = [None for _ in var_list]
            for use_mod, use_info in use_dict.items():
                scope = self.obj_tree[use_mod][0]
                only_list = use_info.only_list
                if len(use_info.rename_map) > 0:
                    only_list = [
                        use_info.rename_map.get(only_name, only_name)
                        for only_name in only_list
                    ]
                tmp_list = child_candidates(
                    scope, only_list, req_abstract=abstract_only
                )
                # Setup renaming
                if len(use_info.rename_map) > 0:
                    rename_reversed = {
                        value: key for (key, value) in use_info.rename_map.items()
                    }
                    for tmp_obj in tmp_list:
                        var_list.append(tmp_obj)
                        rename_list.append(
                            rename_reversed.get(tmp_obj.name.lower(), None)
                        )
                else:
                    var_list += tmp_list
                    rename_list += [None for _ in tmp_list]
            # Add globals
            if inc_globals:
                tmp_list = [obj[0] for (_, obj) in self.obj_tree.items()]
                var_list += tmp_list + self.intrinsic_funs
                rename_list += [None for _ in tmp_list + self.intrinsic_funs]
            # Filter by prefix if necessary
            if var_prefix == "":
                return var_list, rename_list
            else:
                tmp_list = []
                tmp_rename = []
                for (i, var) in enumerate(var_list):
                    var_name = rename_list[i]
                    if var_name is None:
                        var_name = var.name
                    if var_name.lower().startswith(var_prefix):
                        tmp_list.append(var)
                        tmp_rename.append(rename_list[i])
                return tmp_list, tmp_rename

        def build_comp(
            candidate,
            name_only: bool = self.autocomplete_name_only,
            name_replace: str = None,
            is_interface: bool = False,
            is_member: bool = False,
        ):
            comp_obj = {}
            call_sig = None
            if name_only:
                comp_obj["label"] = candidate.name
            else:
                comp_obj["label"] = candidate.name
                if name_replace is not None:
                    comp_obj["label"] = name_replace
                call_sig, snippet = candidate.get_snippet(name_replace)
                if self.autocomplete_no_snippets:
                    snippet = call_sig
                if snippet is not None:
                    if self.use_signature_help and (not is_interface):
                        arg_open = snippet.find("(")
                        if arg_open > 0:
                            snippet = snippet[:arg_open]
                    comp_obj["insertText"] = snippet
                    comp_obj["insertTextFormat"] = 2
            comp_obj["kind"] = map_types(candidate.get_type())
            if is_member and (comp_obj["kind"] == 3):
                comp_obj["kind"] = 2
            comp_obj["detail"] = candidate.get_desc()
            if call_sig is not None:
                comp_obj["detail"] += " " + call_sig
            doc_str, _ = candidate.get_hover()
            if doc_str is not None:
                comp_obj["documentation"] = doc_str
            return comp_obj

        # Get parameters from request
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        path: str = path_from_uri(uri)
        file_obj: fortran_file = self.workspace.get(path)
        if file_obj is None:
            return None
        # Check line
        ac_line: int = params["position"]["line"]
        ac_char: int = params["position"]["character"]
        # Get full line (and possible continuations) from file
        pre_lines, curr_line, _ = file_obj.get_code_line(
            ac_line, forward=False, strip_comment=True
        )
        line_prefix = get_line_prefix(pre_lines, curr_line, ac_char)
        if line_prefix is None:
            return None
        is_member = False
        try:
            var_stack = get_var_stack(line_prefix)
            is_member = len(var_stack) > 1
            var_prefix = var_stack[-1].strip()
        except (TypeError, AttributeError):
            return None
        # print(var_stack)
        item_list = []
        # Get context
        name_only = self.autocomplete_name_only
        public_only = False
        include_globals = True
        line_context, context_info = get_line_context(line_prefix)
        if (line_context == "skip") or (var_prefix == "" and (not is_member)):
            return None
        if self.autocomplete_no_prefix:
            var_prefix = ""
        # Suggestions for user-defined type members
        scope_list = []
        if is_member:
            curr_scope = file_obj.ast.get_inner_scope(ac_line + 1)
            type_scope = climb_type_tree(var_stack, curr_scope, self.obj_tree)
            # Set enclosing type as scope
            if type_scope is None:
                return None
            else:
                include_globals = False
                scope_list = [type_scope]
        else:
            scope_list = file_obj.ast.get_scopes(ac_line + 1)
        # Setup based on context
        req_callable = False
        abstract_only = False
        no_use = False
        type_mask = set_type_mask(False)
        type_mask[MODULE_TYPE_ID] = True
        type_mask[CLASS_TYPE_ID] = True
        if line_context == "mod_only":
            # Module names only (USE statement)
            for key in self.obj_tree:
                candidate = self.obj_tree[key][0]
                if (
                    candidate.get_type() == MODULE_TYPE_ID
                ) and candidate.name.lower().startswith(var_prefix):
                    item_list.append(build_comp(candidate, name_only=True))
            return item_list
        elif line_context == "mod_mems":
            # Public module members only (USE ONLY statement)
            name_only = True
            mod_name = context_info.lower()
            if mod_name in self.obj_tree:
                scope_list = [self.obj_tree[mod_name][0]]
                public_only = True
                include_globals = False
                type_mask[CLASS_TYPE_ID] = False
            else:
                return None
        elif line_context == "pro_link":
            # Link to local subroutine/functions
            type_mask = set_type_mask(True)
            type_mask[SUBROUTINE_TYPE_ID] = False
            type_mask[FUNCTION_TYPE_ID] = False
            name_only = True
            include_globals = False
            no_use = True
        elif line_context == "call":
            # Callable objects only ("CALL" statements)
            req_callable = True
        elif line_context == "type_only":
            # User-defined types only (variable definitions, select clauses)
            type_mask = set_type_mask(True)
            type_mask[CLASS_TYPE_ID] = False
        elif line_context == "import":
            # Import statement (variables and user-defined types only)
            name_only = True
            type_mask = set_type_mask(True)
            type_mask[CLASS_TYPE_ID] = False
            type_mask[VAR_TYPE_ID] = False
        elif line_context == "vis":
            # Visibility statement (local objects only)
            include_globals = False
            name_only = True
            type_mask = set_type_mask(True)
            type_mask[CLASS_TYPE_ID] = False
            type_mask[VAR_TYPE_ID] = False
            type_mask[SUBROUTINE_TYPE_ID] = False
            type_mask[FUNCTION_TYPE_ID] = False
            curr_scope = [file_obj.ast.get_inner_scope(ac_line + 1)]
        elif line_context == "int_only":
            # Interfaces only (procedure definitions)
            abstract_only = True
            include_globals = False
            name_only = True
            type_mask = set_type_mask(True)
            type_mask[SUBROUTINE_TYPE_ID] = False
            type_mask[FUNCTION_TYPE_ID] = False
        elif line_context == "var_only":
            # Variables only (variable definitions)
            name_only = True
            type_mask[SUBROUTINE_TYPE_ID] = True
            type_mask[FUNCTION_TYPE_ID] = True
        elif line_context == "var_key":
            # Variable definition keywords only (variable definition)
            key_context = 0
            enc_scope_type = scope_list[-1].get_type()
            if enc_scope_type == MODULE_TYPE_ID:
                key_context = 1
            elif (enc_scope_type == SUBROUTINE_TYPE_ID) or (
                enc_scope_type == FUNCTION_TYPE_ID
            ):
                key_context = 2
            elif enc_scope_type == CLASS_TYPE_ID:
                key_context = 3
            for candidate in get_intrinsic_keywords(
                self.statements, self.keywords, key_context
            ):
                if candidate.name.lower().startswith(var_prefix):
                    item_list.append(build_comp(candidate))
            return item_list
        elif line_context == "first":
            # First word -> default context plus Fortran statements
            for candidate in get_intrinsic_keywords(self.statements, self.keywords, 0):
                if candidate.name.lower().startswith(var_prefix):
                    item_list.append(build_comp(candidate))
        # Build completion list
        candidate_list, rename_list = get_candidates(
            scope_list, var_prefix, include_globals, public_only, abstract_only, no_use
        )
        for (i, candidate) in enumerate(candidate_list):
            # Skip module names (only valid in USE)
            candidate_type = candidate.get_type()
            if type_mask[candidate_type]:
                continue
            if req_callable and (not candidate.is_callable()):
                continue
            #
            name_replace = rename_list[i]
            if candidate_type == INTERFACE_TYPE_ID:
                tmp_list = []
                if name_replace is None:
                    name_replace = candidate.name
                for member in candidate.mems:
                    tmp_text, _ = member.get_snippet(name_replace)
                    if tmp_list.count(tmp_text) > 0:
                        continue
                    tmp_list.append(tmp_text)
                    item_list.append(
                        build_comp(
                            member,
                            name_replace=name_replace,
                            is_interface=True,
                            is_member=is_member,
                        )
                    )
                continue
            #
            item_list.append(
                build_comp(candidate, name_only=name_only, name_replace=name_replace)
            )
        return item_list

    def get_definition(
        self,
        def_file: fortran_file,
        def_line: int,
        def_char: int,
        hover_req: bool = False,
    ):
        """Return the Fortran object for the definition that matches the
        Fortran file, line number, column number

        Parameters
        ----------
        def_file : fortran_file
            File to query
        def_line : int
            Line position in the file
        def_char : int
            Column position in the file
        hover_req : bool, optional
            Flag to enable if calling from a hover request, by default False

        Returns
        -------
        fortran_var | fortran_include | None
            Fortran object
        """
        # Get full line (and possible continuations) from file
        pre_lines, curr_line, _ = def_file.get_code_line(
            def_line, forward=False, strip_comment=True
        )
        # Returns none for string literals, when the query is in the middle
        line_prefix = get_line_prefix(pre_lines, curr_line, def_char, qs=False)
        if line_prefix is None:
            return None
        is_member = False
        try:
            var_stack = get_var_stack(line_prefix)
            is_member = len(var_stack) > 1
            def_name = expand_name(curr_line, def_char)
        except (TypeError, AttributeError):
            return None
        if def_name == "":
            return None
        # Search in Preprocessor defined variables
        if def_name in def_file.pp_defs:
            var = fortran_var(
                def_file.ast,
                def_line + 1,
                def_name,
                f"#define {def_name} {def_file.pp_defs.get(def_name)}",
                [],
            )
            return var
        curr_scope = def_file.ast.get_inner_scope(def_line + 1)
        # Traverse type tree if necessary
        if is_member:
            type_scope = climb_type_tree(var_stack, curr_scope, self.obj_tree)
            # Set enclosing type as scope
            if type_scope is None:
                return None
            else:
                curr_scope = type_scope
        # Find in available scopes
        var_obj = None
        if curr_scope is not None:
            if (
                (curr_scope.get_type() == CLASS_TYPE_ID)
                and (not is_member)
                and (
                    (
                        line_prefix.lstrip().lower().startswith("procedure")
                        and (line_prefix.count("=>") > 0)
                    )
                    or TYPE_DEF_REGEX.match(line_prefix)
                )
            ):
                curr_scope = curr_scope.parent
            var_obj = find_in_scope(
                curr_scope, def_name, self.obj_tree, var_line_number=def_line + 1
            )
        # Search in global scope
        if var_obj is None:
            if is_member:
                return None
            key = def_name.lower()
            if key in self.obj_tree:
                return self.obj_tree[key][0]
            for obj in self.intrinsic_funs:
                if obj.name.lower() == key:
                    return obj

            # If we have a Fortran literal constant e.g. 100, .false., etc.
            # Return a dummy object with the correct type & position in the doc
            if hover_req and curr_scope:
                var_type = None
                if FRegex.NUMBER.match(def_name):
                    if any(s in def_name for s in [".", "e", "d"]):
                        var_type = f"{FORTRAN_LITERAL}REAL"
                    else:
                        var_type = f"{FORTRAN_LITERAL}INTEGER"
                elif FRegex.LOGICAL.match(def_name):
                    var_type = f"{FORTRAN_LITERAL}LOGICAL"
                elif FRegex.SQ_STRING.match(def_name) or FRegex.DQ_STRING.match(
                    def_name
                ):
                    var_type = f"{FORTRAN_LITERAL}STRING"
                if var_type:
                    return fortran_var(
                        curr_scope.file_ast,
                        def_line + 1,
                        def_name,
                        var_type,
                        curr_scope.keywords,
                    )

        else:
            return var_obj
        return None

    def serve_signature(self, request: dict):
        def get_sub_name(line: str):
            _, sections = get_paren_level(line)
            if sections[0].start <= 1:
                return None, None, None
            arg_string = line[sections[0].start : sections[-1].end]
            sub_string, sections = get_paren_level(line[: sections[0].start - 1])
            return sub_string.strip(), arg_string.split(","), sections[-1].start

        def check_optional(arg, params: dict):
            opt_split = arg.split("=")
            if len(opt_split) > 1:
                opt_arg = opt_split[0].strip().lower()
                for i, param in enumerate(params):
                    param_split = param["label"].split("=")[0]
                    if param_split.lower() == opt_arg:
                        return i
            return None

        # Get parameters from request
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        path: str = path_from_uri(uri)
        file_obj = self.workspace.get(path)
        if file_obj is None:
            return None
        # Check line
        sig_line: int = params["position"]["line"]
        sig_char: int = params["position"]["character"]
        # Get full line (and possible continuations) from file
        pre_lines, curr_line, _ = file_obj.get_code_line(
            sig_line, forward=False, strip_comment=True
        )
        line_prefix = get_line_prefix(pre_lines, curr_line, sig_char)
        if line_prefix is None:
            return None
        # Test if scope declaration or end statement
        if FRegex.SCOPE_DEF.match(curr_line) or FRegex.END.match(curr_line):
            return None
        is_member = False
        try:
            sub_name, arg_strings, sub_end = get_sub_name(line_prefix)
            var_stack = get_var_stack(sub_name)
            is_member = len(var_stack) > 1
        except (TypeError, AttributeError):
            return None
        #
        curr_scope = file_obj.ast.get_inner_scope(sig_line + 1)
        # Traverse type tree if necessary
        if is_member:
            type_scope = climb_type_tree(var_stack, curr_scope, self.obj_tree)
            # Set enclosing type as scope
            if type_scope is None:
                curr_scope = None
            else:
                curr_scope = type_scope
        sub_name = var_stack[-1]
        # Find in available scopes
        var_obj = None
        if curr_scope is not None:
            var_obj = find_in_scope(curr_scope, sub_name, self.obj_tree)
        # Search in global scope
        if var_obj is None:
            key = sub_name.lower()
            if key in self.obj_tree:
                var_obj = self.obj_tree[key][0]
            else:
                for obj in self.intrinsic_funs:
                    if obj.name.lower() == key:
                        var_obj = obj
                        break
        # Check keywords
        if (var_obj is None) and (
            FRegex.INT_STMNT.match(line_prefix[:sub_end]) is not None
        ):
            key = sub_name.lower()
            for candidate in get_intrinsic_keywords(self.statements, self.keywords, 0):
                if candidate.name.lower() == key:
                    var_obj = candidate
                    break
        if var_obj is None:
            return None
        # Build signature
        label, doc_str, params = var_obj.get_signature()
        if label is None:
            return None
        # Find current parameter by index or by
        # looking at last arg with optional name
        param_num = len(arg_strings) - 1
        opt_num = check_optional(arg_strings[-1], params)
        if opt_num is None:
            if len(arg_strings) > 1:
                opt_num = check_optional(arg_strings[-2], params)
                if opt_num is not None:
                    param_num = opt_num + 1
        else:
            param_num = opt_num
        signature = {"label": label, "parameters": params}
        if doc_str is not None:
            signature["documentation"] = doc_str
        req_dict = {"signatures": [signature], "activeParameter": param_num}
        return req_dict

    def get_all_references(
        self,
        def_obj,
        type_mem: bool,
        file_obj: fortran_file = None,
    ):
        # Search through all files
        def_name: str = def_obj.name.lower()
        def_fqsn: str = def_obj.FQSN
        NAME_REGEX = re.compile(rf"(?:\W|^)({def_name})(?:\W|$)", re.I)
        if file_obj is None:
            file_set = self.workspace.items()
        else:
            file_set = ((file_obj.path, file_obj),)
        # A container that includes all the FQSN signatures for objects that
        # are linked to the rename request and that should also be replaced
        override_cache: list[str] = []
        refs = {}
        ref_objs = []
        for filename, file_obj in file_set:
            file_refs = []
            # Search through file line by line
            for (i, line) in enumerate(file_obj.contents_split):
                if len(line) == 0:
                    continue
                # Skip comment lines
                line = file_obj.strip_comment(line)
                if (line == "") or (line[0] == "#"):
                    continue
                for match in NAME_REGEX.finditer(line):
                    var_def = self.get_definition(file_obj, i, match.start(1) + 1)
                    if var_def is None:
                        continue
                    ref_match = False
                    try:
                        # NOTE: throws AttributeError if object is intrinsic since
                        # it will not have a FQSN
                        # BUG: intrinsic objects should be excluded, but get_definition
                        # does not recognise the arguments
                        if def_fqsn == var_def.FQSN or var_def.FQSN in override_cache:
                            ref_match = True
                        # NOTE: throws AttributeError if object is None
                        elif var_def.parent.get_type() == CLASS_TYPE_ID:
                            if type_mem:
                                for inherit_def in var_def.parent.get_overridden(
                                    def_name
                                ):
                                    if def_fqsn == inherit_def.FQSN:
                                        ref_match = True
                                        override_cache.append(var_def.FQSN)
                                        break

                            # Standalone definition of a type-bound procedure,
                            # no pointer replace all its instances in the current scope
                            # NOTE: throws AttributeError if object has no link_obj
                            if (
                                var_def.sline - 1 == i
                                and var_def.file_ast.path == filename
                                and line.count("=>") == 0
                                and var_def.link_obj is def_obj
                            ):
                                ref_objs.append(var_def)
                                override_cache.append(var_def.FQSN)
                                ref_match = True

                        # Object is a Method and the linked object i.e. the
                        # implementation
                        # shares the same parent signature as the current variable
                        # NOTE:: throws and AttributeError if the link_object or
                        # parent are not present OR they are set to None
                        # hence not having a FQSN
                        elif (
                            def_obj.get_type(True) == METH_TYPE_ID
                            and def_obj.link_obj.parent.FQSN == var_def.parent.FQSN
                        ):
                            ref_match = True
                            override_cache.append(var_def.FQSN)
                    except AttributeError:
                        ref_match = False

                    if ref_match:
                        file_refs.append([i, match.start(1), match.end(1)])
            if len(file_refs) > 0:
                refs[filename] = file_refs
        return refs, ref_objs

    def serve_references(self, request):
        # Get parameters from request
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        def_line: int = params["position"]["line"]
        def_char: int = params["position"]["character"]
        path = path_from_uri(uri)
        # Find object
        file_obj = self.workspace.get(path)
        if file_obj is None:
            return None
        def_obj = self.get_definition(file_obj, def_line, def_char)
        if def_obj is None:
            return None
        # Determine global accessibility and type membership
        restrict_file = None
        type_mem = False
        if def_obj.FQSN.count(":") > 2:
            if def_obj.parent.get_type() == CLASS_TYPE_ID:
                type_mem = True
            else:
                restrict_file = def_obj.file_ast.file
                if restrict_file is None:
                    return None
        all_refs, _ = self.get_all_references(def_obj, type_mem, file_obj=restrict_file)
        refs = []
        for (filename, file_refs) in all_refs.items():
            for ref in file_refs:
                refs.append(
                    uri_json(path_to_uri(filename), ref[0], ref[1], ref[0], ref[2])
                )
        return refs

    def serve_definition(self, request: dict):
        # Get parameters from request
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        def_line: int = params["position"]["line"]
        def_char: int = params["position"]["character"]
        path = path_from_uri(uri)
        # Find object
        file_obj = self.workspace.get(path)
        if file_obj is None:
            return None
        var_obj = self.get_definition(file_obj, def_line, def_char)
        if var_obj is None:
            return None
        # Construct link reference
        if var_obj.file_ast.file is not None:
            return self._create_ref_link(var_obj)
        return None

    def serve_hover(self, request: dict):
        def create_hover(string: str, highlight: bool):
            if highlight:
                return {"language": self.hover_language, "value": string}
            else:
                return string

        def create_signature_hover():
            sig_request = request.copy()
            sig_result = self.serve_signature(sig_request)
            try:
                arg_id = sig_result.get("activeParameter")
                if arg_id is not None:
                    arg_info = sig_result["signatures"][0]["parameters"][arg_id]
                    arg_doc = arg_info["documentation"]
                    doc_split = arg_doc.find("\n !!")
                    if doc_split < 0:
                        arg_string = f"{arg_doc} :: {arg_info['label']}"
                    else:
                        arg_string = (
                            f"{arg_doc[:doc_split]} :: "
                            f"{arg_info['label']}{arg_doc[doc_split:]}"
                        )
                    return create_hover(arg_string, True)
            except:
                pass

        # Get parameters from request
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        def_line: int = params["position"]["line"]
        def_char: int = params["position"]["character"]
        path = path_from_uri(uri)
        file_obj = self.workspace.get(path)
        if file_obj is None:
            return None
        # Find object
        var_obj = self.get_definition(file_obj, def_line, def_char, hover_req=True)
        if var_obj is None:
            return None
        # Construct hover information
        var_type = var_obj.get_type()
        hover_array = []
        if var_type in (SUBROUTINE_TYPE_ID, FUNCTION_TYPE_ID):
            hover_str, highlight = var_obj.get_hover(long=True)
            hover_array.append(create_hover(hover_str, highlight))
        elif var_type == INTERFACE_TYPE_ID:
            for member in var_obj.mems:
                hover_str, highlight = member.get_hover(long=True)
                if hover_str is not None:
                    hover_array.append(create_hover(hover_str, highlight))
        elif var_type == VAR_TYPE_ID:
            # Unless we have a Fortran literal include the desc in the hover msg
            # See get_definition for an explanation about this default name
            if not var_obj.desc.startswith(FORTRAN_LITERAL):
                hover_str, highlight = var_obj.get_hover()
                hover_array.append(create_hover(hover_str, highlight))
            # Hover for Literal variables
            elif var_obj.desc.endswith("REAL"):
                hover_array.append(create_hover("REAL", True))
            elif var_obj.desc.endswith("INTEGER"):
                hover_array.append(create_hover("INTEGER", True))
            elif var_obj.desc.endswith("LOGICAL"):
                hover_array.append(create_hover("LOGICAL", True))
            elif var_obj.desc.endswith("STRING"):
                hover_str = f"CHARACTER(LEN={len(var_obj.name)-2})"
                hover_array.append(create_hover(hover_str, True))

            # Include the signature if one is present e.g. if in an argument list
            if self.hover_signature:
                hover_str = create_signature_hover()
                if hover_str is not None:
                    hover_array.append(hover_str)
        #
        if len(hover_array) > 0:
            return {"contents": hover_array}
        return None

    def serve_implementation(self, request: dict):
        # Get parameters from request
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        def_line: int = params["position"]["line"]
        def_char: int = params["position"]["character"]
        path = path_from_uri(uri)
        file_obj = self.workspace.get(path)
        if file_obj is None:
            return None
        # Find object
        var_obj = self.get_definition(file_obj, def_line, def_char)
        if var_obj is None:
            return None
        # Intrinsics do not have implementations we can access
        if isinstance(var_obj, fortran_intrinsic_obj):
            return None
        # Construct implementation reference
        if var_obj.parent.get_type() == CLASS_TYPE_ID:
            impl_obj = var_obj.link_obj
            if (impl_obj is not None) and (impl_obj.file_ast.file is not None):
                return self._create_ref_link(impl_obj)
        return None

    def serve_rename(self, request: dict):
        # Get parameters from request
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        def_line: int = params["position"]["line"]
        def_char: int = params["position"]["character"]
        path = path_from_uri(uri)
        # Find object
        file_obj = self.workspace.get(path)
        if file_obj is None:
            return None
        def_obj = self.get_definition(file_obj, def_line, def_char)
        if def_obj is None:
            return None
        if isinstance(def_obj, fortran_intrinsic_obj):
            self.post_message("Rename failed: Cannot rename intrinsics", Severity.warn)
            return None
        # Determine global accesibility and type membership
        restrict_file = None
        type_mem = False
        if def_obj.FQSN.count(":") > 2:
            if def_obj.parent.get_type() == CLASS_TYPE_ID:
                type_mem = True
            else:
                restrict_file = def_obj.file_ast.file
                if restrict_file is None:
                    return None
        all_refs, ref_objs = self.get_all_references(
            def_obj, type_mem, file_obj=restrict_file
        )
        if len(all_refs) == 0:
            self.post_message("Rename failed: No usages found to rename", Severity.warn)
            return None
        # Create rename changes
        new_name = params["newName"]
        changes: dict[str, list[dict]] = {}
        for filename, file_refs in all_refs.items():
            file_uri = path_to_uri(filename)
            changes[file_uri] = []
            for ref in file_refs:
                changes[file_uri].append(
                    change_json(new_name, ref[0], ref[1], ref[0], ref[2])
                )
        return {"changes": changes}

    def serve_codeActions(self, request: dict):
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        sline: int = params["range"]["start"]["line"]
        eline: int = params["range"]["end"]["line"]
        path = path_from_uri(uri)
        file_obj = self.workspace.get(path)
        # Find object
        if file_obj is None:
            return None
        curr_scope = file_obj.ast.get_inner_scope(sline)
        if curr_scope is None:
            return None
        action_list = curr_scope.get_actions(sline, eline)
        if action_list is None:
            return None
        # Convert diagnostics
        for action in action_list:
            diagnostics = action.get("diagnostics")
            if diagnostics is not None:
                new_diags = []
                for diagnostic in diagnostics:
                    new_diags.append(diagnostic.build(file_obj))
                action["diagnostics"] = new_diags
        return action_list

    def send_diagnostics(self, uri: str):
        diag_results, diag_exp = self.get_diagnostics(uri)
        if diag_results is not None:
            self.conn.send_notification(
                "textDocument/publishDiagnostics",
                {"uri": uri, "diagnostics": diag_results},
            )
        elif diag_exp is not None:
            self.conn.write_error(
                -1,
                code=-32603,
                message=str(diag_exp),
                data={
                    "traceback": traceback.format_exc(),
                },
            )

    def get_diagnostics(self, uri: str):
        filepath = path_from_uri(uri)
        file_obj = self.workspace.get(filepath)
        if file_obj is not None:
            try:
                diags = file_obj.check_file(
                    self.obj_tree,
                    max_line_length=self.max_line_length,
                    max_comment_line_length=self.max_comment_line_length,
                )
            except Exception as e:
                return None, e
            else:
                return diags, None
        return None, None

    def serve_onChange(self, request: dict):
        # Update workspace from file sent by editor
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        path = path_from_uri(uri)
        file_obj = self.workspace.get(path)
        if file_obj is None:
            self.post_message(f"Change request failed for unknown file '{path}'")
            return
        else:
            # Update file contents with changes
            reparse_req = True
            if self.sync_type == 1:
                file_obj.apply_change(params["contentChanges"][0])
            else:
                try:
                    reparse_req = False
                    for change in params["contentChanges"]:
                        reparse_flag = file_obj.apply_change(change)
                        reparse_req = reparse_req or reparse_flag
                except:
                    self.post_message(
                        f"Change request failed for file '{path}': Could not apply"
                        " change",
                        Severity.error,
                        exc_info=True,
                    )
                    return
        # Parse newly updated file
        if reparse_req:
            _, err_str = self.update_workspace_file(path, update_links=True)
            if err_str is not None:
                self.post_message(f"Change request failed for file '{path}': {err_str}")
                return
            # Update include statements linking to this file
            for _, tmp_file in self.workspace.items():
                tmp_file.ast.resolve_includes(self.workspace, path=path)
            file_obj.ast.resolve_includes(self.workspace)
            # Update inheritance (currently file only)
            # tmp_file.ast.resolve_links(self.obj_tree, self.link_version)
        elif file_obj.preproc:
            file_obj.preprocess(pp_defs=self.pp_defs)
            self.pp_defs = {**self.pp_defs, **file_obj.pp_defs}

    def serve_onOpen(self, request: dict):
        self.serve_onSave(request, did_open=True)

    def serve_onClose(self, request: dict):
        self.serve_onSave(request, did_close=True)

    def serve_onSave(
        self, request: dict, did_open: bool = False, did_close: bool = False
    ):
        # Update workspace from file on disk
        params: dict = request["params"]
        uri: str = params["textDocument"]["uri"]
        filepath = path_from_uri(uri)
        # Skip update and remove objects if file is deleted
        if did_close and (not os.path.isfile(filepath)):
            # Remove old objects from tree
            file_obj = self.workspace.get(filepath)
            if file_obj is not None:
                ast_old = file_obj.ast
                if ast_old is not None:
                    for key in ast_old.global_dict:
                        self.obj_tree.pop(key, None)
            return
        did_change, err_str = self.update_workspace_file(
            filepath, read_file=True, allow_empty=did_open
        )
        if err_str is not None:
            self.post_message(f"Save request failed for file '{filepath}': {err_str}")
            return
        if did_change:
            # Update include statements linking to this file
            for _, file_obj in self.workspace.items():
                file_obj.ast.resolve_includes(self.workspace, path=filepath)
            file_obj = self.workspace.get(filepath)
            file_obj.ast.resolve_includes(self.workspace)
            # Update inheritance/links
            self.link_version = (self.link_version + 1) % 1000
            for _, file_obj in self.workspace.items():
                file_obj.ast.resolve_links(self.obj_tree, self.link_version)
        if not self.disable_diagnostics:
            self.send_diagnostics(uri)

    def update_workspace_file(
        self,
        filepath: str,
        read_file: bool = False,
        allow_empty: bool = False,
        update_links: bool = False,
    ):
        # Update workspace from file contents and path
        try:
            file_obj = self.workspace.get(filepath)
            if read_file:
                if file_obj is None:
                    file_obj = fortran_file(filepath, self.pp_suffixes)
                    # Create empty file if not yet saved to disk
                    if not os.path.isfile(filepath):
                        if allow_empty:
                            file_obj.ast = fortran_ast(file_obj)
                            self.workspace[filepath] = file_obj
                            return False, None
                        else:
                            return False, "File does not exist"  # Error during load
                err_string, file_changed = file_obj.load_from_disk()
                if err_string:
                    log.error(f"{err_string} : {filepath}")
                    return False, err_string  # Error during file read
                if not file_changed:
                    return False, None
            ast_new = file_obj.parse(
                pp_defs=self.pp_defs, include_dirs=self.include_dirs
            )
            # Add the included read in pp_defs from to the ones specified in the
            # configuration file
            self.pp_defs = {**self.pp_defs, **file_obj.pp_defs}
        except:
            log.error("Error while parsing file %s", filepath, exc_info=True)
            return False, "Error during parsing"  # Error during parsing
        # Remove old objects from tree
        ast_old = file_obj.ast
        if ast_old is not None:
            for key in ast_old.global_dict:
                self.obj_tree.pop(key, None)
        # Add new file to workspace
        file_obj.ast = ast_new
        if filepath not in self.workspace:
            self.workspace[filepath] = file_obj
        # Add top-level objects to object tree
        for key, obj in ast_new.global_dict.items():
            self.obj_tree[key] = [obj, filepath]
        # Update local links/inheritance if necessary
        if update_links:
            self.link_version = (self.link_version + 1) % 1000
            ast_new.resolve_links(self.obj_tree, self.link_version)
        return True, None

    @staticmethod
    def file_init(
        filepath: str,
        pp_defs: dict,
        pp_suffixes: list[str],
        include_dirs: set[str],
        sort: bool,
    ):
        """Initialise a Fortran file

        Parameters
        ----------
        filepath : str
            Path to file
        pp_defs : dict
            Preprocessor definitions
        pp_suffixes : list[str]
            Preprocessor file extension, additional to default
        include_dirs : set[str]
            Preprocessor only include directories, not used by normal parser
        sort : bool
            Whether or not keywords should be sorted

        Returns
        -------
        fortran_file | str
            A Fortran file object or a string containing the error message
        """
        file_obj = fortran_file(filepath, pp_suffixes)
        err_str, _ = file_obj.load_from_disk()
        if err_str:
            return err_str
        try:
            # On Windows multiprocess does not propagate global variables in a shell.
            # Windows uses 'spawn' while Unix uses 'fork' which propagates globals.
            # This is a bypass.
            # For more see on SO: shorturl.at/hwAG1
            set_keyword_ordering(sort)
            file_ast = file_obj.parse(pp_defs=pp_defs, include_dirs=include_dirs)
        except:
            log.error("Error while parsing file %s", filepath, exc_info=True)
            return "Error during parsing"
        file_obj.ast = file_ast
        return file_obj

    def workspace_init(self):
        """Initialise the workspace root across multiple threads"""

        file_list = self._get_source_files()
        # Process files
        pool = Pool(processes=self.nthreads)
        results = {}
        for filepath in file_list:
            results[filepath] = pool.apply_async(
                self.file_init,
                args=(
                    filepath,
                    self.pp_defs,
                    self.pp_suffixes,
                    self.include_dirs,
                    self.sort_keywords,
                ),
            )
        pool.close()
        pool.join()
        for path, result in results.items():
            result_obj = result.get()
            if isinstance(result_obj, str):
                self.post_message(
                    f"Initialization failed for file '{path}': {result_obj}"
                )
                continue
            self.workspace[path] = result_obj
            # Add top-level objects to object tree
            ast_new = self.workspace[path].ast
            for key in ast_new.global_dict:
                self.obj_tree[key] = [ast_new.global_dict[key], path]
        # Update include statements
        for _, file_obj in self.workspace.items():
            file_obj.ast.resolve_includes(self.workspace)
        # Update inheritance/links
        self.link_version = (self.link_version + 1) % 1000
        for _, file_obj in self.workspace.items():
            file_obj.ast.resolve_links(self.obj_tree, self.link_version)

    def serve_exit(self, request: dict) -> None:
        # Exit server
        self.workspace = {}
        self.obj_tree = {}
        self.running = False

    def serve_default(self, request: dict):
        """Raise an error in the Language Server

        Parameters
        ----------
        request : dict
            client dictionary with requests

        Raises
        ------
        JSONRPC2Error
            error with code -32601
        """
        # Default handler (errors!)
        raise JSONRPC2Error(
            code=-32601, message=f"method {request['method']} not found"
        )

    def _load_config_file(self) -> None:
        """Loads the configuration file for the Language Server"""

        # Check for config file
        config_path = os.path.join(self.root_path, self.config)
        if not os.path.isfile(config_path):
            return None

        try:
            with open(config_path, "r") as jsonfile:
                # Allow for jsonc C-style commnets
                # jsondata = "".join(
                #     line for line in jsonfile if not line.startswith("//")
                # )
                # config_dict = json.loads(jsondata)
                config_dict = json.load(jsonfile)

                # Include and Exclude directories
                self._load_config_file_dirs(config_dict)

                # General options
                self._load_config_file_general(config_dict)

                # Preprocessor options
                self._load_config_file_preproc(config_dict)

                # Debug options
                debugging: bool = config_dict.get("debug_log", self.debug_log)
                # If conf option is different than the debug option passed as a
                # command line argument return True so that debug log is setup
                if debugging != self.debug_log and not self.debug_log:
                    self.debug_log = True

        except FileNotFoundError:
            self.post_messages(
                [Severity.error, f"Error settings file '{self.config}' not found"]
            )

        except ValueError:
            self.post_messages(
                [Severity.error, f"Error while parsing '{self.config}' settings file"]
            )

    def _load_config_file_dirs(self, config_dict: dict) -> None:
        # Exclude paths (directories & files)
        # with glob resolution
        for path in config_dict.get("excl_paths", []):
            self.excl_paths.update(set(resolve_globs(path, self.root_path)))

        # Source directory paths (directories)
        # with glob resolution
        source_dirs = config_dict.get("source_dirs", [])
        for path in source_dirs:
            self.source_dirs.update(
                set(
                    only_dirs(
                        resolve_globs(path, self.root_path),
                        self.post_messages,
                    )
                )
            )
        # Keep all directories present in source_dirs but not excl_paths
        self.source_dirs = {i for i in self.source_dirs if i not in self.excl_paths}
        self.incl_suffixes = config_dict.get("incl_suffixes", [])
        # Update the source file REGEX
        self.FORTRAN_SRC_EXT_REGEX = src_file_exts(self.incl_suffixes)
        self.excl_suffixes = set(config_dict.get("excl_suffixes", []))

    def _load_config_file_general(self, config_dict: dict) -> None:
        # General options ------------------------------------------------------
        self.nthreads = config_dict.get("nthreads", self.nthreads)
        self.notify_init = config_dict.get("notify_init", self.notify_init)
        self.incremental_sync = config_dict.get(
            "incremental_sync", self.incremental_sync
        )
        self.sync_type: int = 2 if self.incremental_sync else 1
        self.sort_keywords = config_dict.get("sort_keywords", self.sort_keywords)
        self.disable_autoupdate = config_dict.get(
            "disable_autoupdate", self.disable_autoupdate
        )

        # Autocomplete options -------------------------------------------------
        self.autocomplete_no_prefix = config_dict.get(
            "autocomplete_no_prefix", self.autocomplete_no_prefix
        )
        self.autocomplete_no_snippets = config_dict.get(
            "autocomplete_no_snippets", self.autocomplete_no_snippets
        )
        self.autocomplete_name_only = config_dict.get(
            "autocomplete_name_only", self.autocomplete_name_only
        )
        self.lowercase_intrinsics = config_dict.get(
            "lowercase_intrinsics", self.lowercase_intrinsics
        )
        self.use_signature_help = config_dict.get(
            "use_signature_help", self.use_signature_help
        )

        # Hover options --------------------------------------------------------
        self.hover_signature = config_dict.get("hover_signature", self.hover_signature)
        self.hover_language = config_dict.get("hover_language", self.hover_language)

        # Diagnostic options ---------------------------------------------------
        self.max_line_length = config_dict.get("max_line_length", self.max_line_length)
        self.max_comment_line_length = config_dict.get(
            "max_comment_line_length", self.max_comment_line_length
        )
        self.disable_diagnostics = config_dict.get(
            "disable_diagnostics", self.disable_diagnostics
        )

        # Symbols options ------------------------------------------------------
        self.symbol_skip_mem = config_dict.get("symbol_skip_mem", self.symbol_skip_mem)

        # Code Actions options -------------------------------------------------
        self.enable_code_actions = config_dict.get(
            "enable_code_actions", self.enable_code_actions
        )

    def _load_config_file_preproc(self, config_dict: dict) -> None:
        self.pp_suffixes = config_dict.get("pp_suffixes", None)  # TODO: set def
        self.pp_defs = config_dict.get("pp_defs", {})  # TODO: set other dif?
        if isinstance(self.pp_defs, list):
            self.pp_defs = {key: "" for key in self.pp_defs}

        for path in config_dict.get("include_dirs", set()):
            self.include_dirs.update(
                only_dirs(resolve_globs(path, self.root_path), self.post_messages)
            )

    def _add_source_dirs(self) -> None:
        """Will recursively add all subdirectories that contain Fortran
        source files only if the option `source_dirs` has not been specified
        in the configuration file or no configuration file is present
        """
        # Recursively add sub-directories that only match Fortran extensions
        if len(self.source_dirs) != 1:
            return None
        if self.root_path not in self.source_dirs:
            return None
        self.source_dirs = set()
        for root, dirs, files in os.walk(self.root_path):
            # Match not found
            if not list(filter(self.FORTRAN_SRC_EXT_REGEX.search, files)):
                continue
            if root not in self.source_dirs and root not in self.excl_paths:
                self.source_dirs.add(str(Path(root).resolve()))

    def _get_source_files(self) -> list[str]:
        """Get all the source files present in `self.source_dirs`,
        exclude any files found in `self.excl_paths`^ and ignore
        any files ending with `self.excl_suffixes`.

        ^: the only case where this has not allready happened is when
           `source_dirs` is not specified or a configuration file is not present

        Returns
        -------
        list[str]
            List of source Fortran source files
        """
        # Get filenames
        file_list = []
        for src_dir in self.source_dirs:
            for f in os.listdir(src_dir):
                p = os.path.join(src_dir, f)
                # Process only files
                if not os.path.isfile(p):
                    continue
                # File extension must match supported extensions
                if not self.FORTRAN_SRC_EXT_REGEX.search(f):
                    continue
                # File cannot be in excluded paths/files
                if p in self.excl_paths:
                    continue
                # File cannot have an excluded extension
                if any(f.endswith(ext) for ext in self.excl_suffixes):
                    continue
                file_list.append(p)
        return file_list

    def _config_logger(self, request) -> None:
        """Configures the logger to save Language Server requests/responses to a file
        the logger will by default output to the main (stderr, stdout) channels.
        """

        file_log = True if self.debug_log and self.root_path else False
        fmt = "[%(levelname)-.4s - %(asctime)s] %(message)s"
        if file_log:
            fname = "fortls_debug.log"
            fname = os.path.join(self.root_path, fname)
            logging.basicConfig(filename=fname, level=logging.DEBUG, filemode="w")
            # Also forward logs to the console
            consoleHandler = logging.StreamHandler()
            log.addHandler(consoleHandler)
            log.debug("REQUEST %s %s", request.get("id"), request.get("method"))
            self.post_messages.append([Severity.info, "fortls debugging enabled"])
        else:
            logging.basicConfig(format=fmt, datefmt="%H:%M:%S", level=logging.INFO)

    def _load_intrinsics(self) -> None:
        # Load intrinsics
        set_keyword_ordering(True)  # Always sort intrinsics
        if self.lowercase_intrinsics:
            set_lowercase_intrinsics()
        (
            self.statements,
            self.keywords,
            self.intrinsic_funs,
            self.intrinsic_mods,
        ) = load_intrinsics()
        for module in self.intrinsic_mods:
            self.obj_tree[module.FQSN] = [module, None]
        # Set object settings
        set_keyword_ordering(self.sort_keywords)

    def _create_ref_link(self, obj) -> dict:
        """Create a link reference to an object"""
        obj_file: fortran_file = obj.file_ast.file
        sline, (schar, echar) = obj_file.find_word_in_code_line(obj.sline - 1, obj.name)
        if schar < 0:
            schar = echar = 0
        return uri_json(path_to_uri(obj_file.path), sline, schar, sline, echar)

    def _update_version_pypi(self, test: bool = False):
        """Fetch updates from PyPi for fortls

        Parameters
        ----------
        test : bool, optional
            flag used to override exit checks, only for unittesting, by default False
        """
        if self.disable_autoupdate:
            return False
        # Do not run for prerelease and dev release
        if self._version.is_prerelease and not test:
            return False
        try:
            # For security reasons register as Request before opening
            request = urllib.request.Request("https://pypi.org/pypi/fortls/json")
            with urllib.request.urlopen(request) as resp:
                info = json.loads(resp.read().decode("utf-8"))
                remote_v = version.parse(info["info"]["version"])
                # Do not update from remote if it is a prerelease
                if remote_v.is_prerelease:
                    return False
                # This is the only reliable way to compare version semantics
                if remote_v > self._version or test:
                    self.post_message(
                        "A newer version of fortls is available for download",
                        Severity.info,
                    )
                    # Anaconda environments should handle their updates through conda
                    if os.path.exists(os.path.join(sys.prefix, "conda-meta")):
                        return False
                    self.post_message(
                        f"Downloading from PyPi fortls {info['info']['version']}",
                        Severity.info,
                    )
                    # Run pip
                    result = subprocess.run(
                        [
                            sys.executable,
                            "-m",
                            "pip",
                            "install",
                            "fortls",
                            "--upgrade",
                        ],
                        capture_output=True,
                    )
                    if result.stdout:
                        log.info(result.stdout.decode("utf-8"))
                    if result.stderr:
                        log.error(result.stderr.decode("utf-8"))
                    return True
        # No internet connection exceptions
        except (URLError, KeyError):
            self.post_message("Failed to update the fortls", Severity.warn)
        return False


class JSONRPC2Error(Exception):
    def __init__(self, code, message, data=None):
        self.code = code
        self.message = message
        self.data = data
