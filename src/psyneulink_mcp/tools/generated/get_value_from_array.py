"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '21a085613cec07e9dea5c883a5f764fda4bdde8a53cd21a8962a889d4fb24662'
__pnl_qualname__ = 'psyneulink.get_value_from_array'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_value_from_array'
TOOL_DESCRIPTION = 'Call this tool when you have a PsyNeuLink value that may be wrapped in a nested array (e.g., `[[0.5]]` or `[1.0]`) and you need a bare scalar number. It unwraps the outermost array structure and returns a single numeric value, preserving the original int or float type.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "array": {\n      "description": "The array (or nested array) from which to extract a numeric scalar. Typically a list, nested list, or numpy array returned by a PsyNeuLink mechanism or function.",\n      "items": {},\n      "type": "array"\n    }\n  },\n  "required": [\n    "array"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function signature accepts any array-like but only makes sense when the array ultimately contains a single numeric element. Passing a multi-element array whose meaning is ambiguous may yield an unexpected extraction. The return value preserves numeric type (int vs float), so downstream type checks should not assume float.'
TOOL_PARAMETERS = { 'properties': { 'array': { 'description': 'The array (or nested array) from which to '
                                            'extract a numeric scalar. Typically a '
                                            'list, nested list, or numpy array '
                                            'returned by a PsyNeuLink mechanism or '
                                            'function.',
                             'items': {},
                             'type': 'array'}},
  'required': ['array'],
  'type': 'object'}
TOOL_NOTES = 'The function signature accepts any array-like but only makes sense when the array ultimately contains a single numeric element. Passing a multi-element array whose meaning is ambiguous may yield an unexpected extraction. The return value preserves numeric type (int vs float), so downstream type checks should not assume float.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_value_from_array
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
    def get_value_from_array(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you have a PsyNeuLink value that may be wrapped in a nested array (e.g., `[[0.5]]` or `[1.0]`) and you need a bare scalar number.'
        return _impl(args or {})
