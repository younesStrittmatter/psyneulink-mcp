"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '916cb886244fa17c05f9c7a530637204d9910513e4055d8cb83e33936e1c10af'
__pnl_qualname__ = 'psyneulink.Stability'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_stability'
TOOL_DESCRIPTION = 'Call this tool to create a Stability objective function that measures how stable a neural network state is given a recurrent weight matrix. Use it when you need to quantify network energy or distance-based stability for use as an objective in RecurrentTransferMechanism or other components. Returns a Stability function object that, when called with a 1-d array, outputs a scalar stability value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1-d array defining the shape and default value of the input for which stability is computed. Mutually exclusive with input_shapes.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Length of the input array; zeros are used as default values. Cannot be used together with default_variable if they imply different lengths.",\n      "type": "integer"\n    },\n    "matrix": {\n      "description": "Recurrent weight matrix (square, same width as variable length). Can be a 2-d array or a keyword string such as \'HOLLOW_MATRIX\', \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\'. Defaults to HOLLOW_MATRIX (no self-connections).",\n      "oneOf": [\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "metric": {\n      "description": "Distance metric used to compute stability. Must be a lowercase literal from DistanceMetrics. Default is \'energy\'.",\n      "enum": [\n        "max_abs_diff",\n        "difference",\n        "dot_product",\n        "normed_L0_similarity",\n        "euclidean",\n        "angle",\n        "correlation",\n        "cosine",\n        "entropy",\n        "cross-entropy",\n        "energy"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "description": "If true, divides the stability result by the length of variable. Default is false.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCritical: the `metric` parameter is beartype-enforced and must be lowercase (e.g., \'energy\', not \'ENERGY\'). The uppercase constant names shown in the docstring (ENERGY, HOLLOW_MATRIX, etc.) are Python symbols, not the string values accepted by the constructor. Do NOT pass a `name` argument — Stability.__init__() does not accept it and will raise TypeError. The matrix is convolved with HOLLOW_MATRIX internally to zero out the diagonal, so self-connections are always excluded regardless of the matrix supplied. If both default_variable and input_shapes are provided they must agree (input_shapes == len(default_variable)) or an error is raised.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1-d array defining the shape '
                                                       'and default value of the input '
                                                       'for which stability is '
                                                       'computed. Mutually exclusive '
                                                       'with input_shapes.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Length of the input array; zeros '
                                                   'are used as default values. Cannot '
                                                   'be used together with '
                                                   'default_variable if they imply '
                                                   'different lengths.',
                                    'type': 'integer'},
                  'matrix': { 'description': 'Recurrent weight matrix (square, same '
                                             'width as variable length). Can be a 2-d '
                                             'array or a keyword string such as '
                                             "'HOLLOW_MATRIX', 'IDENTITY_MATRIX', "
                                             "'FULL_CONNECTIVITY_MATRIX'. Defaults to "
                                             'HOLLOW_MATRIX (no self-connections).',
                              'oneOf': [ { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'},
                                         {'type': 'string'}]},
                  'metric': { 'description': 'Distance metric used to compute '
                                             'stability. Must be a lowercase literal '
                                             'from DistanceMetrics. Default is '
                                             "'energy'.",
                              'enum': [ 'max_abs_diff',
                                        'difference',
                                        'dot_product',
                                        'normed_L0_similarity',
                                        'euclidean',
                                        'angle',
                                        'correlation',
                                        'cosine',
                                        'entropy',
                                        'cross-entropy',
                                        'energy'],
                              'type': 'string'},
                  'normalize': { 'description': 'If true, divides the stability result '
                                                'by the length of variable. Default is '
                                                'false.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Critical: the `metric` parameter is beartype-enforced and must be lowercase (e.g., 'energy', not 'ENERGY'). The uppercase constant names shown in the docstring (ENERGY, HOLLOW_MATRIX, etc.) are Python symbols, not the string values accepted by the constructor. Do NOT pass a `name` argument — Stability.__init__() does not accept it and will raise TypeError. The matrix is convolved with HOLLOW_MATRIX internally to zero out the diagonal, so self-connections are always excluded regardless of the matrix supplied. If both default_variable and input_shapes are provided they must agree (input_shapes == len(default_variable)) or an error is raised."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Stability
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
    def create_stability(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Stability objective function that measures how stable a neural network state is given a recurrent weight matrix.'
        return _impl(args or {})
