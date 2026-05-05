"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '916cb886244fa17c05f9c7a530637204d9910513e4055d8cb83e33936e1c10af'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.recurrenttransfermechanism.Stability'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_stability'
TOOL_DESCRIPTION = 'Use this tool to create a `Stability` objective function that measures how much a state vector changes under a recurrent weight matrix. Call it when you need an energy/distance-based convergence metric for a RecurrentTransferMechanism or any network where you want to track whether a state has settled. Returns a configured `Stability` function object. HISTORICAL FAILURES: do NOT pass `name` (not accepted by Stability.__init__); do NOT pass `matrix="HOLLOW_MATRIX"` as a string literal (causes NoneType runtime error) — omit `matrix` entirely to get the default hollow matrix.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1D list of numbers defining the shape and default value of the state vector. Provide this OR input_shapes, not both.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Length of the state vector; creates a zero-filled array of this size. Provide this OR default_variable, not both.",\n      "type": "integer"\n    },\n    "matrix": {\n      "description": "Square 2D recurrent weight matrix (list of lists). Must be NxN where N matches the variable length. OMIT this parameter to use the default HOLLOW_MATRIX (zeros on diagonal, ones off-diagonal). WARNING: do NOT pass the string \'HOLLOW_MATRIX\' \\u2014 it causes a NoneType runtime error; omit the parameter instead.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "metric": {\n      "default": "ENERGY",\n      "description": "Distance metric used to compute stability. ENERGY (default) computes -0.5 * v^T W v and is the standard Hopfield energy. Use EUCLIDEAN or COSINE for alternative convergence criteria.",\n      "enum": [\n        "ENERGY",\n        "ENTROPY",\n        "COSINE",\n        "CORRELATION",\n        "CROSS_ENTROPY",\n        "EUCLIDEAN",\n        "MAX_ABS_DIFF",\n        "NORMED_L0_SIMILARITY"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "If true, divide the stability value by the length of the variable vector, producing a per-unit metric.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL: `name` is NOT a valid constructor argument for Stability — passing it raises TypeError. Do not include it.\n\nCRITICAL: Passing `matrix="HOLLOW_MATRIX"` as a string literal causes a runtime TypeError (`NoneType * float`) during internal matrix instantiation. To use the default hollow matrix (self-connections zeroed out), simply omit the `matrix` parameter entirely.\n\nYou must provide at least one of `default_variable` or `input_shapes` to define the vector shape; without it Stability defaults to a scalar variable which is rarely useful.\n\n`input_shapes` and `default_variable` are mutually exclusive; providing both raises a FunctionError unless `input_shapes == len(default_variable)`.\n\n`transfer_fct` (a Python callable applied after the weight matrix transform) cannot be passed through MCP and is omitted from the schema.\n\nThe `matrix` is internally convolved with HOLLOW_MATRIX to zero out the diagonal, so self-connections are always excluded from the stability calculation regardless of what matrix you supply.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1D list of numbers defining '
                                                       'the shape and default value of '
                                                       'the state vector. Provide this '
                                                       'OR input_shapes, not both.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Length of the state vector; '
                                                   'creates a zero-filled array of '
                                                   'this size. Provide this OR '
                                                   'default_variable, not both.',
                                    'type': 'integer'},
                  'matrix': { 'description': 'Square 2D recurrent weight matrix (list '
                                             'of lists). Must be NxN where N matches '
                                             'the variable length. OMIT this parameter '
                                             'to use the default HOLLOW_MATRIX (zeros '
                                             'on diagonal, ones off-diagonal). '
                                             'WARNING: do NOT pass the string '
                                             "'HOLLOW_MATRIX' — it causes a NoneType "
                                             'runtime error; omit the parameter '
                                             'instead.',
                              'items': {'items': {'type': 'number'}, 'type': 'array'},
                              'type': 'array'},
                  'metric': { 'default': 'ENERGY',
                              'description': 'Distance metric used to compute '
                                             'stability. ENERGY (default) computes '
                                             '-0.5 * v^T W v and is the standard '
                                             'Hopfield energy. Use EUCLIDEAN or COSINE '
                                             'for alternative convergence criteria.',
                              'enum': [ 'ENERGY',
                                        'ENTROPY',
                                        'COSINE',
                                        'CORRELATION',
                                        'CROSS_ENTROPY',
                                        'EUCLIDEAN',
                                        'MAX_ABS_DIFF',
                                        'NORMED_L0_SIMILARITY'],
                              'type': 'string'},
                  'normalize': { 'default': False,
                                 'description': 'If true, divide the stability value '
                                                'by the length of the variable vector, '
                                                'producing a per-unit metric.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL: `name` is NOT a valid constructor argument for Stability — passing it raises TypeError. Do not include it.\n\nCRITICAL: Passing `matrix="HOLLOW_MATRIX"` as a string literal causes a runtime TypeError (`NoneType * float`) during internal matrix instantiation. To use the default hollow matrix (self-connections zeroed out), simply omit the `matrix` parameter entirely.\n\nYou must provide at least one of `default_variable` or `input_shapes` to define the vector shape; without it Stability defaults to a scalar variable which is rarely useful.\n\n`input_shapes` and `default_variable` are mutually exclusive; providing both raises a FunctionError unless `input_shapes == len(default_variable)`.\n\n`transfer_fct` (a Python callable applied after the weight matrix transform) cannot be passed through MCP and is omitted from the schema.\n\nThe `matrix` is internally convolved with HOLLOW_MATRIX to zero out the diagonal, so self-connections are always excluded from the stability calculation regardless of what matrix you supply.'


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
        'Use this tool to create a `Stability` objective function that measures how much a state vector changes under a recurrent weight matrix.'
        return _impl(args or {})
