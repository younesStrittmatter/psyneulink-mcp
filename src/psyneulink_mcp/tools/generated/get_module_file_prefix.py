"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0432fba86700a2f6895b97708a538b02b8d5fe629162e9caa4cf980f25ffda95'
__pnl_qualname__ = 'psyneulink.get_module_file_prefix'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_module_file_prefix'
TOOL_DESCRIPTION = 'Call this tool when you need the filesystem path prefix for a Python module — for example, to pass to `get_stacklevel_skip_file_prefixes` or to the `skip_file_prefixes` argument of `warnings.warn` (Python 3.12+) to suppress warnings originating inside that module. Returns a string directory path (or file path if the module is a single file), with `__init__.py` stripped.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "module": {\n      "description": "The fully qualified module name (e.g. \'psyneulink.core.globals.utilities\') or a reference to an already-imported module object. Pass as a string when possible.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "module"\n  ],\n  "type": "object"\n}\n\nNotes:\nAccepts either a module name string or an actual ModuleType object, but since MCP tool arguments are JSON, always pass a string module name. If the module cannot be imported or has no associated file (e.g. built-in C extensions), this will raise an exception.'
TOOL_PARAMETERS = { 'properties': { 'module': { 'description': 'The fully qualified module name (e.g. '
                                             "'psyneulink.core.globals.utilities') or "
                                             'a reference to an already-imported '
                                             'module object. Pass as a string when '
                                             'possible.',
                              'type': 'string'}},
  'required': ['module'],
  'type': 'object'}
TOOL_NOTES = 'Accepts either a module name string or an actual ModuleType object, but since MCP tool arguments are JSON, always pass a string module name. If the module cannot be imported or has no associated file (e.g. built-in C extensions), this will raise an exception.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_module_file_prefix
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
    def get_module_file_prefix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need the filesystem path prefix for a Python module — for example, to pass to `get_stacklevel_skip_file_prefixes` or to the `skip_file_prefixes` argument of `warnings.warn` (Python 3.12+) to suppress warnings originating inside that module.'
        return _impl(args or {})
