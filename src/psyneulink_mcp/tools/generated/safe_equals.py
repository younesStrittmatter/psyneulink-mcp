"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '705fce0d0c9f5d875680083d3b60140eeb0e39bfe2e75d0b86bdc1b842378654'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.processing.transfermechanism.safe_equals'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'safe_equals'
TOOL_DESCRIPTION = 'Call this tool when you need to compare two values for equality and either value may be a numpy array, nested list, or dictionary — standard Python `==` would return an array of booleans rather than a single bool. Returns a single boolean: `True` if `x` and `y` are equal, `False` otherwise.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "x": {\n      "description": "The first value to compare. May be a scalar, numpy array, list, or dictionary.",\n      "type": [\n        "boolean",\n        "number",\n        "string",\n        "array",\n        "object"\n      ]\n    },\n    "y": {\n      "description": "The second value to compare. Must be the same kind of structure as x.",\n      "type": [\n        "boolean",\n        "number",\n        "string",\n        "array",\n        "object"\n      ]\n    }\n  },\n  "required": [\n    "x",\n    "y"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis function always returns a single Python bool, never a numpy array. For nested structures (lists of arrays, dicts of arrays), it recurses element-wise. For dict-like objects, key sets must match exactly or it returns False. If one argument is dict-like and the other is not, it returns False. Do not use for floating-point tolerance comparison — this is strict equality only.'
TOOL_PARAMETERS = { 'properties': { 'x': { 'description': 'The first value to compare. May be a scalar, '
                                        'numpy array, list, or dictionary.',
                         'type': ['boolean', 'number', 'string', 'array', 'object']},
                  'y': { 'description': 'The second value to compare. Must be the same '
                                        'kind of structure as x.',
                         'type': ['boolean', 'number', 'string', 'array', 'object']}},
  'required': ['x', 'y'],
  'type': 'object'}
TOOL_NOTES = 'This function always returns a single Python bool, never a numpy array. For nested structures (lists of arrays, dicts of arrays), it recurses element-wise. For dict-like objects, key sets must match exactly or it returns False. If one argument is dict-like and the other is not, it returns False. Do not use for floating-point tolerance comparison — this is strict equality only.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.safe_equals
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
    def safe_equals(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to compare two values for equality and either value may be a numpy array, nested list, or dictionary — standard Python `==` would return an array of booleans rather than a single bool.'
        return _impl(args or {})
