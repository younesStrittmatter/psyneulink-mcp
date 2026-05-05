"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ffab2feb7ebe41346395f8870c8d2738640392f56745fd3fd9410ba7a740b1b9'
__pnl_qualname__ = 'psyneulink.tensor_power'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'tensor_power'
TOOL_DESCRIPTION = 'Call this tool to compute tensor products for all powerset members of a collection of vectors/arrays. Returns higher-order feature interactions (e.g., pairwise, triple-wise cross-products) useful for polynomial feature expansions or connectionist models requiring cross-product terms. When flat=False the result is a list of 1D arrays (one per selected powerset member); when flat=True the result is a single concatenated 1D array.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "flat": {\n      "default": false,\n      "description": "If false (default), returns a list of 1D arrays, one per powerset member. If true, returns a single 1D array of all values concatenated.",\n      "type": "boolean"\n    },\n    "items": {\n      "description": "List of vectors (each a list of numbers) whose powerset tensor products will be computed.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "levels": {\n      "default": null,\n      "description": "Which order terms to include: 1 = first-order (individual vectors), 2 = second-order (pairwise tensor products), etc. If omitted, all orders from 1 up to (but not including) the maximum are returned.",\n      "items": {\n        "minimum": 1,\n        "type": "integer"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "items"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe default `levels` is `range(1, max_levels)` where `max_levels` is the size of the largest powerset subset — this is Python\'s exclusive-end range, so the full-order (all-items) tensor product is excluded by default. Pass `levels` explicitly (e.g., `[1, 2, 3]`) to include higher orders. The levels list is passed directly; the function uses `in list(levels)` internally so any integer iterable works. Raises `UtilitiesError` if any value in levels exceeds the maximum achievable order for the given items. The empty-set powerset member (order 0) is never returned regardless of levels.'
TOOL_PARAMETERS = { 'properties': { 'flat': { 'default': False,
                            'description': 'If false (default), returns a list of 1D '
                                           'arrays, one per powerset member. If true, '
                                           'returns a single 1D array of all values '
                                           'concatenated.',
                            'type': 'boolean'},
                  'items': { 'description': 'List of vectors (each a list of numbers) '
                                            'whose powerset tensor products will be '
                                            'computed.',
                             'items': {'items': {'type': 'number'}, 'type': 'array'},
                             'type': 'array'},
                  'levels': { 'default': None,
                              'description': 'Which order terms to include: 1 = '
                                             'first-order (individual vectors), 2 = '
                                             'second-order (pairwise tensor products), '
                                             'etc. If omitted, all orders from 1 up to '
                                             '(but not including) the maximum are '
                                             'returned.',
                              'items': {'minimum': 1, 'type': 'integer'},
                              'type': 'array'}},
  'required': ['items'],
  'type': 'object'}
TOOL_NOTES = "The default `levels` is `range(1, max_levels)` where `max_levels` is the size of the largest powerset subset — this is Python's exclusive-end range, so the full-order (all-items) tensor product is excluded by default. Pass `levels` explicitly (e.g., `[1, 2, 3]`) to include higher orders. The levels list is passed directly; the function uses `in list(levels)` internally so any integer iterable works. Raises `UtilitiesError` if any value in levels exceeds the maximum achievable order for the given items. The empty-set powerset member (order 0) is never returned regardless of levels."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.tensor_power
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
    def tensor_power(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to compute tensor products for all powerset members of a collection of vectors/arrays.'
        return _impl(args or {})
