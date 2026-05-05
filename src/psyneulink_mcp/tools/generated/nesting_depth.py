"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8e00b4a9defe8e9bf2886fe062ff8385e6a84f6d4186549c486ff147dd1cff11'
__pnl_qualname__ = 'psyneulink.nesting_depth'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'nesting_depth'
TOOL_DESCRIPTION = 'Call this tool to determine how deeply nested a list or array is — useful when you need to validate or normalize the dimensionality of a PsyNeuLink input before passing it to a mechanism or projection. Returns an integer depth (1 for a flat list, 2 for a list-of-lists, etc.) or False if the argument is not a list or array.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "l": {\n      "description": "The list (or list-of-lists) whose nesting depth you want to measure. Numpy arrays are also accepted and will be converted to lists internally.",\n      "items": {},\n      "type": "array"\n    }\n  },\n  "required": [\n    "l"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns False (not 0) when the argument is not a list or array — boolean False compares equal to 0 in Python arithmetic, which can cause silent bugs if you do math on the result without checking. An empty list ([]) will raise ValueError because max() cannot operate on an empty sequence. Only the list/array structure is inspected; element types are ignored.'
TOOL_PARAMETERS = { 'properties': { 'l': { 'description': 'The list (or list-of-lists) whose nesting '
                                        'depth you want to measure. Numpy arrays are '
                                        'also accepted and will be converted to lists '
                                        'internally.',
                         'items': {},
                         'type': 'array'}},
  'required': ['l'],
  'type': 'object'}
TOOL_NOTES = 'Returns False (not 0) when the argument is not a list or array — boolean False compares equal to 0 in Python arithmetic, which can cause silent bugs if you do math on the result without checking. An empty list ([]) will raise ValueError because max() cannot operate on an empty sequence. Only the list/array structure is inspected; element types are ignored.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.nesting_depth
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
    def nesting_depth(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to determine how deeply nested a list or array is — useful when you need to validate or normalize the dimensionality of a PsyNeuLink input before passing it to a mechanism or projection.'
        return _impl(args or {})
