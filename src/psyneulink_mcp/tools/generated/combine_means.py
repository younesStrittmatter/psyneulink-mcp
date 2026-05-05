"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '294c604acbf45df024d628b532c41806fae33f966c2b9497a6b567e2ded9107b'
__pnl_qualname__ = 'psyneulink.CombineMeans'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_combine_means'
TOOL_DESCRIPTION = 'Use CombineMeans when you need to reduce multiple arrays to a single scalar by first averaging each array, then combining those means via sum or product. Call this to attach it as a Function to a Mechanism or use it standalone; the result is always a scalar. Typical use: aggregating population activity across input streams with optional differential weighting before combining.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the arrays to be combined. If 2d, all rows must have the same length. Determines the expected input shape.",\n      "items": {},\n      "type": "array"\n    },\n    "exponents": {\n      "description": "Exponents applied to each array\'s mean before combining. If 1d, length must equal number of arrays in variable. Applied after weights.",\n      "items": {},\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for this Function instance; auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "offset": {\n      "description": "Scalar added to the combined result after scale is applied. Default behavior (None) treats it as 0.0.",\n      "type": "number"\n    },\n    "operation": {\n      "default": "sum",\n      "description": "How to combine the (weighted/exponentiated) means: \'sum\' adds them, \'product\' multiplies them. Default: \'sum\'.",\n      "enum": [\n        "sum",\n        "product"\n      ],\n      "type": "string"\n    },\n    "scale": {\n      "description": "Scalar multiplied into the combined result after the operation. Default behavior (None) treats it as 1.0.",\n      "type": "number"\n    },\n    "weights": {\n      "description": "Multipliers applied to each array\'s mean before combining. If 1d, length must equal number of arrays in variable; each scalar scales the corresponding array\'s mean. If 2d, applied element-wise (Hadamard) before taking the mean. Applied before exponents.",\n      "items": {},\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nAlways returns a scalar regardless of input dimensionality. Internally, weights and exponents are reshaped to 2d column vectors (shape (-1, 1)) — pass them as 1d lists and PNL handles the reshape. scale=None and offset=None are silently treated as 1.0 and 0.0 respectively; pass explicit values if you want to control them. The operation parameter accepts lowercase string literals ("sum"/"product"), not the SUM/PRODUCT enum constants directly from the agent. During initialization with zero-valued inputs and negative exponents, means are replaced with ones to avoid divide-by-zero — this is only a concern at init time. weights/exponents length along axis 0 must exactly match the number of items (rows) in variable, or a FunctionError is raised at execution time.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the arrays to be '
                                                       'combined. If 2d, all rows must '
                                                       'have the same length. '
                                                       'Determines the expected input '
                                                       'shape.',
                                        'items': {},
                                        'type': 'array'},
                  'exponents': { 'description': "Exponents applied to each array's "
                                                'mean before combining. If 1d, length '
                                                'must equal number of arrays in '
                                                'variable. Applied after weights.',
                                 'items': {},
                                 'type': 'array'},
                  'name': { 'description': 'Optional name for this Function instance; '
                                           'auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'offset': { 'description': 'Scalar added to the combined result '
                                             'after scale is applied. Default behavior '
                                             '(None) treats it as 0.0.',
                              'type': 'number'},
                  'operation': { 'default': 'sum',
                                 'description': 'How to combine the '
                                                "(weighted/exponentiated) means: 'sum' "
                                                "adds them, 'product' multiplies them. "
                                                "Default: 'sum'.",
                                 'enum': ['sum', 'product'],
                                 'type': 'string'},
                  'scale': { 'description': 'Scalar multiplied into the combined '
                                            'result after the operation. Default '
                                            'behavior (None) treats it as 1.0.',
                             'type': 'number'},
                  'weights': { 'description': "Multipliers applied to each array's "
                                              'mean before combining. If 1d, length '
                                              'must equal number of arrays in '
                                              'variable; each scalar scales the '
                                              "corresponding array's mean. If 2d, "
                                              'applied element-wise (Hadamard) before '
                                              'taking the mean. Applied before '
                                              'exponents.',
                               'items': {},
                               'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Always returns a scalar regardless of input dimensionality. Internally, weights and exponents are reshaped to 2d column vectors (shape (-1, 1)) — pass them as 1d lists and PNL handles the reshape. scale=None and offset=None are silently treated as 1.0 and 0.0 respectively; pass explicit values if you want to control them. The operation parameter accepts lowercase string literals ("sum"/"product"), not the SUM/PRODUCT enum constants directly from the agent. During initialization with zero-valued inputs and negative exponents, means are replaced with ones to avoid divide-by-zero — this is only a concern at init time. weights/exponents length along axis 0 must exactly match the number of items (rows) in variable, or a FunctionError is raised at execution time.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.CombineMeans
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
    def create_combine_means(args: dict[str, Any] | None = None) -> Any:
        'Use CombineMeans when you need to reduce multiple arrays to a single scalar by first averaging each array, then combining those means via sum or product.'
        return _impl(args or {})
