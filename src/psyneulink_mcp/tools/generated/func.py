"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b52f0d043840f5c9526f7cd8a7c02ba15415eb2893c42409cc4925b52e6e19f3'
__pnl_qualname__ = 'psyneulink.func'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'func'
TOOL_DESCRIPTION = 'Call this tool to mark a PsyNeuLink Component as PNL-inherent (i.e., built into PsyNeuLink rather than user-defined) by setting its internal `_is_pnl_inherent` flag. The tool has no return value; it modifies the component in place. Only call this when you need to explicitly tag a Component as a native PsyNeuLink object.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "The name associated with the object being marked. Accepted by the function signature but not used internally \\u2014 provided for bookkeeping or future use.",\n      "type": "string"\n    },\n    "obj": {\n      "description": "Reference to the PsyNeuLink Component to mark as PNL-inherent. Pass the component\'s name or string identifier; the server resolves it to the actual Component instance.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "name",\n    "obj"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `name` argument is accepted by the function signature but is never read inside the function body — it has no effect on the outcome. Only objects that are instances of `psyneulink.core.components.component.Component` are modified; passing a non-Component leaves the call a no-op with no error raised. `_is_pnl_inherent` is a private attribute; this function is low-level and primarily intended for internal PsyNeuLink use during library initialization.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'The name associated with the object being '
                                           'marked. Accepted by the function signature '
                                           'but not used internally — provided for '
                                           'bookkeeping or future use.',
                            'type': 'string'},
                  'obj': { 'description': 'Reference to the PsyNeuLink Component to '
                                          "mark as PNL-inherent. Pass the component's "
                                          'name or string identifier; the server '
                                          'resolves it to the actual Component '
                                          'instance.',
                           'type': 'string'}},
  'required': ['name', 'obj'],
  'type': 'object'}
TOOL_NOTES = 'The `name` argument is accepted by the function signature but is never read inside the function body — it has no effect on the outcome. Only objects that are instances of `psyneulink.core.components.component.Component` are modified; passing a non-Component leaves the call a no-op with no error raised. `_is_pnl_inherent` is a private attribute; this function is low-level and primarily intended for internal PsyNeuLink use during library initialization.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.func
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
    def func(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to mark a PsyNeuLink Component as PNL-inherent (i.e., built into PsyNeuLink rather than user-defined) by setting its internal `_is_pnl_inherent` flag.'
        return _impl(args or {})
