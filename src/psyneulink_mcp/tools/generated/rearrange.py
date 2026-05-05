"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7fa98fe061517a798d6f8f97b482eba8c53dd7d58fba7f8bedd3435888c82491'
__pnl_qualname__ = 'psyneulink.Rearrange'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_rearrange'
TOOL_DESCRIPTION = 'Call this tool to create a `Rearrange` function that reorders and/or concatenates rows of a 2D input array. Use it when you need to selectively pick, reorder, or merge rows from a 2D variable — for example, routing specific input channels into combined or separated outputs. The result is a 2D array where each element corresponds to one entry in `arrangement` (a concatenated 1D slice of the input rows).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "arrangement": {\n      "description": "Specifies which rows (axis 0) of the input to include and how to group them. An integer selects a single row as its own group; an array of integers concatenates those rows into a single 1D output element. Pass a list of integers and/or integer-arrays to build the full output ordering. If omitted, all rows are concatenated into a single 1D array (identical to Concatenate behavior).",\n      "oneOf": [\n        {\n          "description": "Single row index",\n          "type": "integer"\n        },\n        {\n          "description": "List of row indices and/or groups (sub-arrays) to concatenate",\n          "items": {\n            "oneOf": [\n              {\n                "type": "integer"\n              },\n              {\n                "description": "Row indices to concatenate into one element",\n                "items": {\n                  "type": "integer"\n                },\n                "type": "array"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "default_variable": {\n      "description": "Template 2D array defining the shape of inputs this function expects. Must be at least 2D with all numeric elements. Optional \\u2014 if omitted, shape is inferred from the maximum index in arrangement.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for this function instance.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Scalar added element-wise to the entire output after scale is applied.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Scalar multiplied element-wise to the entire output after rearrangement. Applied before offset.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `arrangement` indices are zero-based row indices into axis 0 of the input variable. Only rows explicitly listed are included in the output when arrangement is specified — unlisted rows are dropped.\n- Sub-arrays within `arrangement` (representing tuples in Python) cause those rows to be horizontally concatenated (np.hstack) into a single 1D output element.\n- Without `arrangement`, all rows are concatenated into one flat 1D array (same as Concatenate); the result shape collapses to 1D in that case.\n- `default_variable` must be at least 2D; passing a 1D array will raise a FunctionError.\n- `scale` and `offset` must be scalars; arrays will raise a FunctionError.\n- The output is always converted to a 2D numpy array (FunctionOutputType.NP_2D_ARRAY), even when arrangement produces a single element.\n- When arrangement is a bare integer (not a list), it is treated as a list containing that integer.'
TOOL_PARAMETERS = { 'properties': { 'arrangement': { 'description': 'Specifies which rows (axis 0) of '
                                                  'the input to include and how to '
                                                  'group them. An integer selects a '
                                                  'single row as its own group; an '
                                                  'array of integers concatenates '
                                                  'those rows into a single 1D output '
                                                  'element. Pass a list of integers '
                                                  'and/or integer-arrays to build the '
                                                  'full output ordering. If omitted, '
                                                  'all rows are concatenated into a '
                                                  'single 1D array (identical to '
                                                  'Concatenate behavior).',
                                   'oneOf': [ { 'description': 'Single row index',
                                                'type': 'integer'},
                                              { 'description': 'List of row indices '
                                                               'and/or groups '
                                                               '(sub-arrays) to '
                                                               'concatenate',
                                                'items': { 'oneOf': [ { 'type': 'integer'},
                                                                      { 'description': 'Row '
                                                                                       'indices '
                                                                                       'to '
                                                                                       'concatenate '
                                                                                       'into '
                                                                                       'one '
                                                                                       'element',
                                                                        'items': { 'type': 'integer'},
                                                                        'type': 'array'}]},
                                                'type': 'array'}]},
                  'default_variable': { 'description': 'Template 2D array defining the '
                                                       'shape of inputs this function '
                                                       'expects. Must be at least 2D '
                                                       'with all numeric elements. '
                                                       'Optional — if omitted, shape '
                                                       'is inferred from the maximum '
                                                       'index in arrangement.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'name': { 'description': 'Optional name for this function instance.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Scalar added element-wise to the entire '
                                             'output after scale is applied.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Scalar multiplied element-wise to the '
                                            'entire output after rearrangement. '
                                            'Applied before offset.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `arrangement` indices are zero-based row indices into axis 0 of the input variable. Only rows explicitly listed are included in the output when arrangement is specified — unlisted rows are dropped.\n- Sub-arrays within `arrangement` (representing tuples in Python) cause those rows to be horizontally concatenated (np.hstack) into a single 1D output element.\n- Without `arrangement`, all rows are concatenated into one flat 1D array (same as Concatenate); the result shape collapses to 1D in that case.\n- `default_variable` must be at least 2D; passing a 1D array will raise a FunctionError.\n- `scale` and `offset` must be scalars; arrays will raise a FunctionError.\n- The output is always converted to a 2D numpy array (FunctionOutputType.NP_2D_ARRAY), even when arrangement produces a single element.\n- When arrangement is a bare integer (not a list), it is treated as a list containing that integer.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Rearrange
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
    def create_rearrange(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a `Rearrange` function that reorders and/or concatenates rows of a 2D input array.'
        return _impl(args or {})
