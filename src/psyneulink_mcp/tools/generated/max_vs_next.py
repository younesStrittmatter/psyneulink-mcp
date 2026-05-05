"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e8d24b32778a02b9c94c7ae0b69154c8d38f7f5409f7429cd8ccfe41cfb84906'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.selectionfunctions.max_vs_next'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'max_vs_next'
TOOL_DESCRIPTION = 'Call this tool when you need to quantify how dominant the maximum value is over the runner-up in a numeric array — for example, to measure selection confidence or winner-take-all strength after a competition. Returns a single scalar: the difference between the largest and second-largest element of the input.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "x": {\n      "description": "Numeric array of at least two elements. The function finds the maximum and second-maximum values and returns their difference.",\n      "items": {\n        "type": "number"\n      },\n      "minItems": 2,\n      "type": "array"\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nInput array must contain at least 2 elements; passing a length-1 array will raise an IndexError because np.partition(x, -2) requires at least 2 entries. The function uses numpy partition internally, so x must be array-like with numeric dtype. Returns a scalar (not an array). A return value of 0 means two or more elements share the maximum value.'
TOOL_PARAMETERS = { 'properties': { 'x': { 'description': 'Numeric array of at least two elements. The '
                                        'function finds the maximum and second-maximum '
                                        'values and returns their difference.',
                         'items': {'type': 'number'},
                         'minItems': 2,
                         'type': 'array'}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = 'Input array must contain at least 2 elements; passing a length-1 array will raise an IndexError because np.partition(x, -2) requires at least 2 entries. The function uses numpy partition internally, so x must be array-like with numeric dtype. Returns a scalar (not an array). A return value of 0 means two or more elements share the maximum value.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.max_vs_next
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
    def max_vs_next(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to quantify how dominant the maximum value is over the runner-up in a numeric array — for example, to measure selection confidence or winner-take-all strength after a competition.'
        return _impl(args or {})
