"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c011a5dbb95b041274a20cedd0eba4a7277fd6d3d16ebe71b8c0e80bac492ce3'
__pnl_qualname__ = 'psyneulink.extended_array_equal'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'extended_array_equal'
TOOL_DESCRIPTION = 'Call this tool when you need to compare two arrays for equality and at least one may be an object-dtype NumPy array containing ragged or nested sub-arrays — cases where `numpy.array_equal` would incorrectly return False even for identical structures. Returns a single boolean: True if every element (recursively) is equal, False otherwise.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "a": {\n      "description": "First array or array-like value to compare. Can be a list, NumPy array, or object-dtype array containing nested arrays.",\n      "items": {},\n      "type": "array"\n    },\n    "b": {\n      "description": "Second array or array-like value to compare. Must be structurally compatible with \'a\'.",\n      "items": {},\n      "type": "array"\n    },\n    "equal_nan": {\n      "default": false,\n      "description": "If true, NaN values at the same positions are considered equal. Mirrors the numpy.array_equal equal_nan argument. Defaults to false.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "a",\n    "b"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe key difference from numpy.array_equal: object-dtype arrays whose elements are themselves arrays of different lengths (ragged arrays) will be compared element-wise recursively, so two identical ragged arrays return True rather than False. Both inputs are internally converted via convert_all_elements_to_np_array before comparison, so plain Python lists are accepted. The equal_nan flag is passed directly to numpy.array_equal at each recursive level.'
TOOL_PARAMETERS = { 'properties': { 'a': { 'description': 'First array or array-like value to compare. '
                                        'Can be a list, NumPy array, or object-dtype '
                                        'array containing nested arrays.',
                         'items': {},
                         'type': 'array'},
                  'b': { 'description': 'Second array or array-like value to compare. '
                                        "Must be structurally compatible with 'a'.",
                         'items': {},
                         'type': 'array'},
                  'equal_nan': { 'default': False,
                                 'description': 'If true, NaN values at the same '
                                                'positions are considered equal. '
                                                'Mirrors the numpy.array_equal '
                                                'equal_nan argument. Defaults to '
                                                'false.',
                                 'type': 'boolean'}},
  'required': ['a', 'b'],
  'type': 'object'}
TOOL_NOTES = 'The key difference from numpy.array_equal: object-dtype arrays whose elements are themselves arrays of different lengths (ragged arrays) will be compared element-wise recursively, so two identical ragged arrays return True rather than False. Both inputs are internally converted via convert_all_elements_to_np_array before comparison, so plain Python lists are accepted. The equal_nan flag is passed directly to numpy.array_equal at each recursive level.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.extended_array_equal
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
    def extended_array_equal(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to compare two arrays for equality and at least one may be an object-dtype NumPy array containing ragged or nested sub-arrays — cases where `numpy.array_equal` would incorrectly return False even for identical structures.'
        return _impl(args or {})
