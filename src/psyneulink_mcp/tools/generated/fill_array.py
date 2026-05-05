"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f0f087a620e96923032c2ffece450635e86a3e73457b7dc46b5ca9c9f34e29f6'
__pnl_qualname__ = 'psyneulink.fill_array'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'fill_array'
TOOL_DESCRIPTION = 'Call this tool to fill every element of a NumPy array in-place with a single scalar or value, including object-dtype arrays that contain nested arrays of varying shapes. The tool returns nothing — it mutates `arr` directly. Use it when you need to reset or initialize an array (including ragged/object arrays) to a uniform value without allocating a new array.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "arr": {\n      "description": "The NumPy array to fill in-place, represented as a nested list. Object-dtype arrays with embedded sub-arrays are supported and will be filled recursively.",\n      "type": "array"\n    },\n    "value": {\n      "description": "The scalar value to fill every element with (e.g. 0, 1, or any numeric constant).",\n      "type": "number"\n    }\n  },\n  "required": [\n    "arr",\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function mutates `arr` in-place and returns None — do not use the return value. For object-dtype arrays (ragged or nested), it recurses into each element, so each sub-array is filled individually while preserving its shape. The `value` parameter accepts Any in the Python signature, but JSON Schema cannot represent arbitrary Python objects; pass a number for typical numeric fill use cases. If you need to fill with a non-numeric value (e.g. None or a string), this tool may not handle the serialization correctly — use a curated tool or direct Python instead.'
TOOL_PARAMETERS = { 'properties': { 'arr': { 'description': 'The NumPy array to fill in-place, '
                                          'represented as a nested list. Object-dtype '
                                          'arrays with embedded sub-arrays are '
                                          'supported and will be filled recursively.',
                           'type': 'array'},
                  'value': { 'description': 'The scalar value to fill every element '
                                            'with (e.g. 0, 1, or any numeric '
                                            'constant).',
                             'type': 'number'}},
  'required': ['arr', 'value'],
  'type': 'object'}
TOOL_NOTES = 'The function mutates `arr` in-place and returns None — do not use the return value. For object-dtype arrays (ragged or nested), it recurses into each element, so each sub-array is filled individually while preserving its shape. The `value` parameter accepts Any in the Python signature, but JSON Schema cannot represent arbitrary Python objects; pass a number for typical numeric fill use cases. If you need to fill with a non-numeric value (e.g. None or a string), this tool may not handle the serialization correctly — use a curated tool or direct Python instead.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.fill_array
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
    def fill_array(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to fill every element of a NumPy array in-place with a single scalar or value, including object-dtype arrays that contain nested arrays of varying shapes.'
        return _impl(args or {})
