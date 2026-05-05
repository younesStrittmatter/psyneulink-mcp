"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4c42ba84e1d801b6e5c0b7c6ecc59bdc3188aa9f63960fc3a627b1e8c751861c'
__pnl_qualname__ = 'psyneulink.get_stacklevel_skip_file_prefixes'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_stacklevel_skip_file_prefixes'
TOOL_DESCRIPTION = 'Call this tool when you need to compute the correct `stacklevel` integer for `warnings.warn()` or `logging.log()` so that warnings and log messages are attributed to the outermost caller frame that lies outside a given set of PsyNeuLink (or other) modules. Returns a single integer ready to pass as the `stacklevel` argument.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "modules": {\n      "description": "Names of Python modules whose stack frames should be skipped (e.g. [\'psyneulink\', \'psyneulink.core.globals.utilities\']). Only string module names are supported via MCP \\u2014 module objects cannot be serialised.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "modules"\n  ],\n  "type": "object"\n}\n\nNotes:\nBecause this function inspects the live Python call stack at the moment it executes, the returned stacklevel reflects the MCP server\'s internal call stack, not any user application stack. The result is therefore only meaningful if the caller intends to emit a warning or log message from within the same MCP server process. Passing a module name that is not importable or has no associated file (e.g. built-in modules) silently produces a prefix of \'\' which may match everything; verify module names resolve correctly. If no frame outside the specified modules is found, the function falls back to returning 1.'
TOOL_PARAMETERS = { 'properties': { 'modules': { 'description': 'Names of Python modules whose stack '
                                              'frames should be skipped (e.g. '
                                              "['psyneulink', "
                                              "'psyneulink.core.globals.utilities']). "
                                              'Only string module names are supported '
                                              'via MCP — module objects cannot be '
                                              'serialised.',
                               'items': {'type': 'string'},
                               'type': 'array'}},
  'required': ['modules'],
  'type': 'object'}
TOOL_NOTES = "Because this function inspects the live Python call stack at the moment it executes, the returned stacklevel reflects the MCP server's internal call stack, not any user application stack. The result is therefore only meaningful if the caller intends to emit a warning or log message from within the same MCP server process. Passing a module name that is not importable or has no associated file (e.g. built-in modules) silently produces a prefix of '' which may match everything; verify module names resolve correctly. If no frame outside the specified modules is found, the function falls back to returning 1."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_stacklevel_skip_file_prefixes
    resolved = handles.resolve_in(kwargs)
    result = target(**resolved)
    try:
        json.dumps(result)
    except (TypeError, ValueError):
        payload = handles.register_handle(result)
        handles.record_call(
            TOOL_NAME,
            kwargs,
            result_handle=payload.get('handle') if isinstance(payload, dict) else None,
            tool_layer="generated",
        )
        return payload
    handles.record_call(TOOL_NAME, kwargs, result_handle=None, tool_layer="generated")
    return result


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def get_stacklevel_skip_file_prefixes(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to compute the correct `stacklevel` integer for `warnings.warn()` or `logging.log()` so that warnings and log messages are attributed to the outermost caller frame that lies outside a given set of PsyNeuLink (or other) modules.'
        return _impl(args or {})
