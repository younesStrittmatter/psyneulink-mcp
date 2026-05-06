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
TOOL_DESCRIPTION = 'Call this tool to create a PsyNeuLink `Stability` objective function, which measures how stable a state vector is under recurrent dynamics by comparing it to its transformed version (via a weight matrix and optional transfer function) using a distance metric. Returns a `Stability` function object suitable for assigning to a `RecurrentTransferMechanism` or standalone use. Use when you need to quantify network convergence or energy in a recurrent system.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1D array of numbers defining the shape and default value of the state vector for which stability is calculated. Do not combine with input_shapes.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Length of the state vector; zeros are used as values. Use this instead of default_variable. Do not combine with default_variable.",\n      "type": "integer"\n    },\n    "matrix": {\n      "description": "2D square recurrent weight matrix (list of lists of numbers). Must have dimensions matching the length of the variable. Omit this parameter entirely to use the default HOLLOW_MATRIX \\u2014 do NOT pass the string \'HOLLOW_MATRIX\', as that causes a TypeError.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "metric": {\n      "default": "ENERGY",\n      "description": "Distance metric used to compare the variable to its transformed version. Default is \'ENERGY\'.",\n      "enum": [\n        "ENERGY",\n        "ENTROPY",\n        "EUCLIDEAN",\n        "MAX_ABS_DIFF",\n        "COSINE",\n        "CORRELATION",\n        "CROSS_ENTROPY"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "If true, divides the stability result by the length of the variable array.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — two known runtime errors from feedback:\n1. Do NOT pass `matrix` as the string "HOLLOW_MATRIX". This causes `TypeError: unsupported operand type(s) for *: \'NoneType\' and \'float\'` during initialization. Simply omit the `matrix` parameter to use the default hollow matrix.\n2. Do NOT pass a `name` argument. Despite appearing in the docstring, `Stability.__init__()` does not accept `name` and raises `TypeError: got an unexpected keyword argument \'name\'`.\n\nYou must provide either `default_variable` or `input_shapes` (not both) so PNL can determine the size of the weight matrix. If neither is given, a 1-element default is used.\n\nThe matrix is automatically convolved with HOLLOW_MATRIX internally to remove self-connections from the stability calculation — you do not need to do this manually.\n\n`metric="ENTROPY"` is internally converted to CROSS_ENTROPY for the Distance function computation.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1D array of numbers defining '
                                                       'the shape and default value of '
                                                       'the state vector for which '
                                                       'stability is calculated. Do '
                                                       'not combine with input_shapes.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Length of the state vector; zeros '
                                                   'are used as values. Use this '
                                                   'instead of default_variable. Do '
                                                   'not combine with default_variable.',
                                    'type': 'integer'},
                  'matrix': { 'description': '2D square recurrent weight matrix (list '
                                             'of lists of numbers). Must have '
                                             'dimensions matching the length of the '
                                             'variable. Omit this parameter entirely '
                                             'to use the default HOLLOW_MATRIX — do '
                                             "NOT pass the string 'HOLLOW_MATRIX', as "
                                             'that causes a TypeError.',
                              'items': {'items': {'type': 'number'}, 'type': 'array'},
                              'type': 'array'},
                  'metric': { 'default': 'ENERGY',
                              'description': 'Distance metric used to compare the '
                                             'variable to its transformed version. '
                                             "Default is 'ENERGY'.",
                              'enum': [ 'ENERGY',
                                        'ENTROPY',
                                        'EUCLIDEAN',
                                        'MAX_ABS_DIFF',
                                        'COSINE',
                                        'CORRELATION',
                                        'CROSS_ENTROPY'],
                              'type': 'string'},
                  'normalize': { 'default': False,
                                 'description': 'If true, divides the stability result '
                                                'by the length of the variable array.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL — two known runtime errors from feedback:\n1. Do NOT pass `matrix` as the string "HOLLOW_MATRIX". This causes `TypeError: unsupported operand type(s) for *: \'NoneType\' and \'float\'` during initialization. Simply omit the `matrix` parameter to use the default hollow matrix.\n2. Do NOT pass a `name` argument. Despite appearing in the docstring, `Stability.__init__()` does not accept `name` and raises `TypeError: got an unexpected keyword argument \'name\'`.\n\nYou must provide either `default_variable` or `input_shapes` (not both) so PNL can determine the size of the weight matrix. If neither is given, a 1-element default is used.\n\nThe matrix is automatically convolved with HOLLOW_MATRIX internally to remove self-connections from the stability calculation — you do not need to do this manually.\n\n`metric="ENTROPY"` is internally converted to CROSS_ENTROPY for the Distance function computation.'


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
        'Call this tool to create a PsyNeuLink `Stability` objective function, which measures how stable a state vector is under recurrent dynamics by comparing it to its transformed version (via a weight matrix and optional transfer function) using a distance metric.'
        return _impl(args or {})
