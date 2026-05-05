"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'af619f0523c5fd4e5322fae1ca4a3b723fa62a751ea7e0307b0438bb565bfc32'
__pnl_qualname__ = 'psyneulink.get_hetero_matrix'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_hetero_matrix'
TOOL_DESCRIPTION = 'Call this tool to construct a hetero weight matrix for a recurrent (autoassociative) projection, given a raw hetero specification and a network size. Returns a 2D hollow numpy array (diagonal forced to zero) suitable for use as off-diagonal connection weights. Returns null if the inputs are incompatible (e.g., a 1D array with more than one element).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "raw_hetero": {\n      "description": "The hetero weight specification. Can be: a numeric scalar (scales a hollow identity matrix), a single-element list or 1D array (uses its one value as a scalar), or a 2D list/array/matrix (used directly with diagonal zeroed out). Any other shape returns null.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "size": {\n      "description": "The number of units (rows and columns) in the square output matrix. Must match the layer size of the RecurrentTransferMechanism or AutoAssociativeProjection being configured.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "raw_hetero",\n    "size"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns None (not an error) for invalid input combinations: a 1D array/list with more than one element, or any type that is not a scalar, 1D single-element array, or 2D matrix. When raw_hetero is a 2D matrix, the diagonal is zeroed in-place before returning — mutates the input if it is a numpy array or matrix. The output is always a plain numpy ndarray (np.matrix input is converted). Pass size matching the actual layer dimensionality; mismatches between size and a provided 2D raw_hetero shape are not validated and may produce unexpected results.'
TOOL_PARAMETERS = { 'properties': { 'raw_hetero': { 'description': 'The hetero weight specification. Can '
                                                 'be: a numeric scalar (scales a '
                                                 'hollow identity matrix), a '
                                                 'single-element list or 1D array '
                                                 '(uses its one value as a scalar), or '
                                                 'a 2D list/array/matrix (used '
                                                 'directly with diagonal zeroed out). '
                                                 'Any other shape returns null.',
                                  'oneOf': [ {'type': 'number'},
                                             { 'items': {'type': 'number'},
                                               'type': 'array'},
                                             { 'items': { 'items': {'type': 'number'},
                                                          'type': 'array'},
                                               'type': 'array'}]},
                  'size': { 'description': 'The number of units (rows and columns) in '
                                           'the square output matrix. Must match the '
                                           'layer size of the '
                                           'RecurrentTransferMechanism or '
                                           'AutoAssociativeProjection being '
                                           'configured.',
                            'minimum': 1,
                            'type': 'integer'}},
  'required': ['raw_hetero', 'size'],
  'type': 'object'}
TOOL_NOTES = 'Returns None (not an error) for invalid input combinations: a 1D array/list with more than one element, or any type that is not a scalar, 1D single-element array, or 2D matrix. When raw_hetero is a 2D matrix, the diagonal is zeroed in-place before returning — mutates the input if it is a numpy array or matrix. The output is always a plain numpy ndarray (np.matrix input is converted). Pass size matching the actual layer dimensionality; mismatches between size and a provided 2D raw_hetero shape are not validated and may produce unexpected results.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_hetero_matrix
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
    def get_hetero_matrix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to construct a hetero weight matrix for a recurrent (autoassociative) projection, given a raw hetero specification and a network size.'
        return _impl(args or {})
