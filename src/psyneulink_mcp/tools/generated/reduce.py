"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a1798dc9c47d1cb61250bd071131b4bcf55fb4ac5850e0746e33b8722e9f67f1'
__pnl_qualname__ = 'psyneulink.Reduce'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_reduce'
TOOL_DESCRIPTION = 'Call this tool to create a Reduce function that collapses each array in a multi-array input into a single scalar value. Use it when you need to aggregate (sum or multiply) elements within each array of a 2D variable, optionally with per-element weights, exponents, and a final scale/offset. Returns a 1D array of scalars, one per input array.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input value and its default. Must contain only numeric entries. Can be 1D or 2D (list of arrays).",\n      "items": {},\n      "type": "array"\n    },\n    "exponents": {\n      "description": "Values used to exponentiate elements before combining. 1D: one exponent per array in variable; 2D: per-element exponents matching variable\'s shape. Defaults to None (no exponentiation).",\n      "items": {},\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the function instance. Auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "offset": {\n      "description": "Scalar added to each element of the result after scale is applied. Default 0.0.",\n      "type": "number"\n    },\n    "operation": {\n      "description": "Whether to sum or multiply elements within each array. Defaults to \'sum\'.",\n      "enum": [\n        "sum",\n        "product"\n      ],\n      "type": "string"\n    },\n    "params": {\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter names, values override defaults.",\n      "type": "object"\n    },\n    "scale": {\n      "description": "Scalar multiplied into each element of the result after the operation. Applied before offset. Default 1.0.",\n      "type": "number"\n    },\n    "weights": {\n      "description": "Values to multiply element-wise before combining. 1D: one weight per array in variable; 2D: per-element weights matching variable\'s shape. Defaults to None (no weighting).",\n      "items": {},\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- Reduce operates along axis=1 of a 2D array: each row is reduced to a scalar. If you pass a 1D input it is treated as a single-row 2D array (via np.atleast_2d), returning a length-1 array.\n- Exponents are applied first, then weights, then the aggregation operation, then scale, then offset.\n- Both scale and offset must be scalars; vector-valued scale/offset will raise a validation error.\n- weights and exponents length must match the number of arrays in variable at execution time (not at construction time).\n- The \'operation\' argument accepts lowercase strings \'sum\' or \'product\' (the PNL constants SUM/PRODUCT resolve to these strings).'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input value '
                                                       'and its default. Must contain '
                                                       'only numeric entries. Can be '
                                                       '1D or 2D (list of arrays).',
                                        'items': {},
                                        'type': 'array'},
                  'exponents': { 'description': 'Values used to exponentiate elements '
                                                'before combining. 1D: one exponent '
                                                'per array in variable; 2D: '
                                                'per-element exponents matching '
                                                "variable's shape. Defaults to None "
                                                '(no exponentiation).',
                                 'items': {},
                                 'type': 'array'},
                  'name': { 'description': 'Optional name for the function instance. '
                                           'Auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'offset': { 'description': 'Scalar added to each element of the '
                                             'result after scale is applied. Default '
                                             '0.0.',
                              'type': 'number'},
                  'operation': { 'description': 'Whether to sum or multiply elements '
                                                "within each array. Defaults to 'sum'.",
                                 'enum': ['sum', 'product'],
                                 'type': 'string'},
                  'params': { 'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter names, values override '
                                             'defaults.',
                              'type': 'object'},
                  'scale': { 'description': 'Scalar multiplied into each element of '
                                            'the result after the operation. Applied '
                                            'before offset. Default 1.0.',
                             'type': 'number'},
                  'weights': { 'description': 'Values to multiply element-wise before '
                                              'combining. 1D: one weight per array in '
                                              'variable; 2D: per-element weights '
                                              "matching variable's shape. Defaults to "
                                              'None (no weighting).',
                               'items': {},
                               'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- Reduce operates along axis=1 of a 2D array: each row is reduced to a scalar. If you pass a 1D input it is treated as a single-row 2D array (via np.atleast_2d), returning a length-1 array.\n- Exponents are applied first, then weights, then the aggregation operation, then scale, then offset.\n- Both scale and offset must be scalars; vector-valued scale/offset will raise a validation error.\n- weights and exponents length must match the number of arrays in variable at execution time (not at construction time).\n- The 'operation' argument accepts lowercase strings 'sum' or 'product' (the PNL constants SUM/PRODUCT resolve to these strings)."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Reduce
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
    def create_reduce(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Reduce function that collapses each array in a multi-array input into a single scalar value.'
        return _impl(args or {})
