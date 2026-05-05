"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '33ec626dccfc2f814da883fd40135ea6d55aa8d10ec171e721ef3ade54da55b0'
__pnl_qualname__ = 'psyneulink.np_array_less_than_2d'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'np_array_less_than_2d'
TOOL_DESCRIPTION = 'Call this tool to check whether a numpy array has fewer than 2 dimensions (i.e., is 0D or 1D). Returns True if the array\'s ndim is 0 or 1, False if it is 2 or more. Use this as a guard before operations that require flat/scalar arrays or to branch logic based on array dimensionality.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "array": {\n      "description": "The array to test. Must be convertible to a numpy ndarray. Pass a flat list for a 1D array, a nested list for 2D+. The function requires an actual np.ndarray \\u2014 the host will convert this JSON array before calling.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "array"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function raises UtilitiesError (not TypeError or ValueError) if the argument is not an np.ndarray — the host must convert the JSON array to np.ndarray before calling. A 0D array (scalar) returns True because its ndim is 0, which satisfies ndim <= 1. A 2D array [[1,2],[3,4]] returns False. There is no support for complex or non-numeric dtypes based on the source.'
TOOL_PARAMETERS = { 'properties': { 'array': { 'description': 'The array to test. Must be convertible to '
                                            'a numpy ndarray. Pass a flat list for a '
                                            '1D array, a nested list for 2D+. The '
                                            'function requires an actual np.ndarray — '
                                            'the host will convert this JSON array '
                                            'before calling.',
                             'items': {'type': 'number'},
                             'type': 'array'}},
  'required': ['array'],
  'type': 'object'}
TOOL_NOTES = 'The function raises UtilitiesError (not TypeError or ValueError) if the argument is not an np.ndarray — the host must convert the JSON array to np.ndarray before calling. A 0D array (scalar) returns True because its ndim is 0, which satisfies ndim <= 1. A 2D array [[1,2],[3,4]] returns False. There is no support for complex or non-numeric dtypes based on the source.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.np_array_less_than_2d
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
    def np_array_less_than_2d(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a numpy array has fewer than 2 dimensions (i.e., is 0D or 1D).'
        return _impl(args or {})
