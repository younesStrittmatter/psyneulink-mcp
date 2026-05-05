"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9cce2aadaf105c1e1f315033ad41ebc188d67866206e53bba1f5ae5764cdcd06'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.selectionfunctions.max_vs_avg'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'max_vs_avg'
TOOL_DESCRIPTION = 'Call this tool to compute how much the maximum value in an array exceeds the mean of all remaining values. Use it when you need a scalar "winner margin" signal — e.g., to measure the dominance of the top activation in a layer or the separation between the best option and the field. Returns a single float: max(x) − mean(x \\ {max}).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "x": {\n      "description": "1-D numeric array of at least 2 elements. The function finds the maximum value and subtracts the mean of all other elements from it.",\n      "items": {\n        "type": "number"\n      },\n      "minItems": 2,\n      "type": "array"\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe array must contain at least 2 elements; passing a length-1 array will raise an IndexError because np.partition requires a valid kth index (-2). The function uses np.partition internally, so duplicate maximum values are handled correctly — only one copy is treated as the max, the rest stay in the "others" pool. Returns a plain Python float (or numpy scalar), not an array.'
TOOL_PARAMETERS = { 'properties': { 'x': { 'description': '1-D numeric array of at least 2 elements. The '
                                        'function finds the maximum value and '
                                        'subtracts the mean of all other elements from '
                                        'it.',
                         'items': {'type': 'number'},
                         'minItems': 2,
                         'type': 'array'}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = 'The array must contain at least 2 elements; passing a length-1 array will raise an IndexError because np.partition requires a valid kth index (-2). The function uses np.partition internally, so duplicate maximum values are handled correctly — only one copy is treated as the max, the rest stay in the "others" pool. Returns a plain Python float (or numpy scalar), not an array.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.max_vs_avg
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
    def max_vs_avg(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to compute how much the maximum value in an array exceeds the mean of all remaining values.'
        return _impl(args or {})
