"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f6d26f594efd6faca317cafb4b0cd11a826540fe44005227c74869d749286cdb'
__pnl_qualname__ = 'psyneulink.update_array_in_place'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'update_array_in_place'
TOOL_DESCRIPTION = 'Call this tool when you need to overwrite the contents of an existing numpy array in-place with values from another array, especially when the arrays may be ragged (object dtype) where numpy.copyto would fail or produce incorrect results. The tool modifies the target array directly and returns nothing; it does not allocate a new array.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "casting": {\n      "default": "same_kind",\n      "description": "Controls what type-casting is allowed when copying values, following numpy.copyto semantics. \'same_kind\' (default) allows casts within a kind (e.g. float64 to float32). Use \'unsafe\' to allow any cast, \'safe\' to only allow lossless casts.",\n      "enum": [\n        "no",\n        "equiv",\n        "safe",\n        "same_kind",\n        "unsafe"\n      ],\n      "type": "string"\n    },\n    "source": {\n      "description": "The array providing the new values. Represented as a nested JSON array. Must have the same shape as target.",\n      "items": {},\n      "type": "array"\n    },\n    "target": {\n      "description": "The array whose values will be overwritten. Represented as a nested JSON array. Must have the same shape as source.",\n      "items": {},\n      "type": "array"\n    }\n  },\n  "required": [\n    "target",\n    "source"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis function modifies `target` in-place and returns None — the agent should not expect a return value. It is primarily useful for ragged/object-dtype arrays; for uniform-dtype arrays, standard numpy assignment or numpy.copyto works equally well. If `source` and `target` have mismatched shapes or dtypes incompatible with the chosen `casting` rule, numpy will raise a TypeError or ValueError.'
TOOL_PARAMETERS = { 'properties': { 'casting': { 'default': 'same_kind',
                               'description': 'Controls what type-casting is allowed '
                                              'when copying values, following '
                                              "numpy.copyto semantics. 'same_kind' "
                                              '(default) allows casts within a kind '
                                              "(e.g. float64 to float32). Use 'unsafe' "
                                              "to allow any cast, 'safe' to only allow "
                                              'lossless casts.',
                               'enum': ['no', 'equiv', 'safe', 'same_kind', 'unsafe'],
                               'type': 'string'},
                  'source': { 'description': 'The array providing the new values. '
                                             'Represented as a nested JSON array. Must '
                                             'have the same shape as target.',
                              'items': {},
                              'type': 'array'},
                  'target': { 'description': 'The array whose values will be '
                                             'overwritten. Represented as a nested '
                                             'JSON array. Must have the same shape as '
                                             'source.',
                              'items': {},
                              'type': 'array'}},
  'required': ['target', 'source'],
  'type': 'object'}
TOOL_NOTES = 'This function modifies `target` in-place and returns None — the agent should not expect a return value. It is primarily useful for ragged/object-dtype arrays; for uniform-dtype arrays, standard numpy assignment or numpy.copyto works equally well. If `source` and `target` have mismatched shapes or dtypes incompatible with the chosen `casting` rule, numpy will raise a TypeError or ValueError.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.update_array_in_place
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
    def update_array_in_place(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to overwrite the contents of an existing numpy array in-place with values from another array, especially when the arrays may be ragged (object dtype) where numpy.copyto would fail or produce incorrect results.'
        return _impl(args or {})
