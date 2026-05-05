"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '991f4624acf4e51cb08a9da7bdd7f9734a9d4c26b571640bed32fd3f20fd1388'
__pnl_qualname__ = 'psyneulink.is_modulation_operation'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_modulation_operation'
TOOL_DESCRIPTION = 'Call this tool to check whether a value is a valid PsyNeuLink modulation operation. Use it before passing a value as a modulation parameter to a mechanism or projection to confirm it will be accepted. Returns the string name of the modulation operation if valid, or a falsy value (None or empty string) if not.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "val": {\n      "description": "The candidate modulation operation to test. Pass the name of a PsyNeuLink modulation operation (e.g. \'MULTIPLICATIVE\', \'ADDITIVE\', \'OVERRIDE\', \'DISABLE\') or the operation object itself represented as a string.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "val"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe implementation delegates entirely to `get_modulationOperation_name(val)`. The return value is truthy (the operation\'s name string) if valid, falsy (None or empty string) if not — treat it as a boolean check but note the actual string name is returned on success. The commented-out original implementation attempted to call `val(0, 0)` and caught exceptions; the current approach uses name lookup instead, so only recognized named operations pass. Unknown or custom callables that are not registered modulation operations will return falsy even if they are functionally compatible.'
TOOL_PARAMETERS = { 'properties': { 'val': { 'description': 'The candidate modulation operation to test. '
                                          'Pass the name of a PsyNeuLink modulation '
                                          "operation (e.g. 'MULTIPLICATIVE', "
                                          "'ADDITIVE', 'OVERRIDE', 'DISABLE') or the "
                                          'operation object itself represented as a '
                                          'string.',
                           'type': 'string'}},
  'required': ['val'],
  'type': 'object'}
TOOL_NOTES = "The implementation delegates entirely to `get_modulationOperation_name(val)`. The return value is truthy (the operation's name string) if valid, falsy (None or empty string) if not — treat it as a boolean check but note the actual string name is returned on success. The commented-out original implementation attempted to call `val(0, 0)` and caught exceptions; the current approach uses name lookup instead, so only recognized named operations pass. Unknown or custom callables that are not registered modulation operations will return falsy even if they are functionally compatible."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_modulation_operation
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
    def is_modulation_operation(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a value is a valid PsyNeuLink modulation operation.'
        return _impl(args or {})
