"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '2870b5b269026894756bbf82a3361ba1b34ffcaf6b6daa201012f8486d6ed7f4'
__pnl_qualname__ = 'psyneulink.get_auto_matrix'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_auto_matrix'
TOOL_DESCRIPTION = 'Call this tool to convert a scalar, 1-D array, or 2-D matrix representation of recurrent self-connection weights into a square diagonal numpy array of a given size. Use it when constructing or validating the `auto` parameter for an AutoAssociativeProjection — the result is a 2-D float64 ndarray (size × size) with the self-connection values on the diagonal, or null if the inputs are incompatible.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "raw_auto": {\n      "description": "The auto weight specification. Accepts: a scalar (fills all diagonal entries), a 1-element list/array (same as scalar), an N-element 1-D list/array (one weight per unit, must match size), or a 2-D list/array/matrix (returned as-is without diagonal validation).",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "size": {\n      "description": "The number of units (dimension of the square output matrix). Must match the length of raw_auto when raw_auto is a 1-D array with more than one element.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "raw_auto",\n    "size"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns None (not an error) when raw_auto is a 1-D array whose length differs from size, or when raw_auto is an unrecognised type — the caller must check for None. When raw_auto is a 2-D input the function does NOT verify that it is actually diagonal; any square 2-D array is accepted and returned unchanged. The returned array always has dtype float64.'
TOOL_PARAMETERS = { 'properties': { 'raw_auto': { 'description': 'The auto weight specification. '
                                               'Accepts: a scalar (fills all diagonal '
                                               'entries), a 1-element list/array (same '
                                               'as scalar), an N-element 1-D '
                                               'list/array (one weight per unit, must '
                                               'match size), or a 2-D '
                                               'list/array/matrix (returned as-is '
                                               'without diagonal validation).',
                                'oneOf': [ {'type': 'number'},
                                           { 'items': {'type': 'number'},
                                             'type': 'array'}]},
                  'size': { 'description': 'The number of units (dimension of the '
                                           'square output matrix). Must match the '
                                           'length of raw_auto when raw_auto is a 1-D '
                                           'array with more than one element.',
                            'minimum': 1,
                            'type': 'integer'}},
  'required': ['raw_auto', 'size'],
  'type': 'object'}
TOOL_NOTES = 'Returns None (not an error) when raw_auto is a 1-D array whose length differs from size, or when raw_auto is an unrecognised type — the caller must check for None. When raw_auto is a 2-D input the function does NOT verify that it is actually diagonal; any square 2-D array is accepted and returned unchanged. The returned array always has dtype float64.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_auto_matrix
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
    def get_auto_matrix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to convert a scalar, 1-D array, or 2-D matrix representation of recurrent self-connection weights into a square diagonal numpy array of a given size.'
        return _impl(args or {})
