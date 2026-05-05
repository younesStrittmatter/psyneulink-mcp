"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '916cb886244fa17c05f9c7a530637204d9910513e4055d8cb83e33936e1c10af'
__pnl_qualname__ = 'psyneulink.Stability'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_stability'
TOOL_DESCRIPTION = 'Call this tool to instantiate a Stability objective function that measures how stable a neural activation pattern is under recurrent self-connections. Use it when building a RecurrentTransferMechanism or ObjectiveMechanism that needs to quantify how much a state vector changes after passing through a weight matrix — e.g., to monitor convergence or implement energy-based stopping criteria. Returns a Stability Function object whose `.function(variable)` call yields a scalar stability score.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1D array defining the shape and default value of the activation vector for which stability is computed. If omitted, use input_shapes instead.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Length of the activation vector. Alternative to default_variable; zeros are used as values. Raises an error if both are specified and input_shapes != len(default_variable).",\n      "type": "integer"\n    },\n    "matrix": {\n      "description": "Recurrent weight matrix (2D list/array) or a PsyNeuLink matrix keyword string (e.g. \'HOLLOW_MATRIX\', \'IDENTITY_MATRIX\'). Must be square with side length equal to len(variable). Internally convolved with HOLLOW_MATRIX to zero out self-connections. Defaults to \'HOLLOW_MATRIX\'.",\n      "type": [\n        "array",\n        "string"\n      ]\n    },\n    "metric": {\n      "description": "Distance metric used to compare the original variable with its transformed version. Default is \'ENERGY\'. \'ENTROPY\' is internally re-mapped to \'CROSS_ENTROPY\'.",\n      "enum": [\n        "ENERGY",\n        "ENTROPY",\n        "EUCLIDEAN",\n        "ANGLE",\n        "CORRELATION",\n        "COSINE",\n        "CROSS_ENTROPY",\n        "MAX_ABS_DIFF",\n        "DIFFERENCE"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "description": "If true, divides the stability score by the length of variable, giving a per-element average. Default is false.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `transfer_fct` (a callable that transforms the post-matrix output before metric comparison) is intentionally omitted from the schema because callables cannot be serialized to JSON; pass it only via direct Python construction.\n- The ENERGY metric is the default and is NOT a standard distance metric — it computes a Hopfield-style energy, not a geometric distance.\n- ENTROPY as metric is silently converted to CROSS_ENTROPY internally; if you need true entropy behavior verify results carefully.\n- matrix is always convolved with HOLLOW_MATRIX before use, so self-connections are always eliminated regardless of what you pass.\n- Passing a 2D matrix as `matrix` requires it to be square with side == len(variable); mismatches raise FunctionError at instantiation, not at call time.\n- If neither default_variable nor input_shapes is provided, the variable shape is flexible and will be inferred at runtime from the first call.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1D array defining the shape '
                                                       'and default value of the '
                                                       'activation vector for which '
                                                       'stability is computed. If '
                                                       'omitted, use input_shapes '
                                                       'instead.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Length of the activation vector. '
                                                   'Alternative to default_variable; '
                                                   'zeros are used as values. Raises '
                                                   'an error if both are specified and '
                                                   'input_shapes != '
                                                   'len(default_variable).',
                                    'type': 'integer'},
                  'matrix': { 'description': 'Recurrent weight matrix (2D list/array) '
                                             'or a PsyNeuLink matrix keyword string '
                                             "(e.g. 'HOLLOW_MATRIX', "
                                             "'IDENTITY_MATRIX'). Must be square with "
                                             'side length equal to len(variable). '
                                             'Internally convolved with HOLLOW_MATRIX '
                                             'to zero out self-connections. Defaults '
                                             "to 'HOLLOW_MATRIX'.",
                              'type': ['array', 'string']},
                  'metric': { 'description': 'Distance metric used to compare the '
                                             'original variable with its transformed '
                                             "version. Default is 'ENERGY'. 'ENTROPY' "
                                             'is internally re-mapped to '
                                             "'CROSS_ENTROPY'.",
                              'enum': [ 'ENERGY',
                                        'ENTROPY',
                                        'EUCLIDEAN',
                                        'ANGLE',
                                        'CORRELATION',
                                        'COSINE',
                                        'CROSS_ENTROPY',
                                        'MAX_ABS_DIFF',
                                        'DIFFERENCE'],
                              'type': 'string'},
                  'normalize': { 'description': 'If true, divides the stability score '
                                                'by the length of variable, giving a '
                                                'per-element average. Default is '
                                                'false.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `transfer_fct` (a callable that transforms the post-matrix output before metric comparison) is intentionally omitted from the schema because callables cannot be serialized to JSON; pass it only via direct Python construction.\n- The ENERGY metric is the default and is NOT a standard distance metric — it computes a Hopfield-style energy, not a geometric distance.\n- ENTROPY as metric is silently converted to CROSS_ENTROPY internally; if you need true entropy behavior verify results carefully.\n- matrix is always convolved with HOLLOW_MATRIX before use, so self-connections are always eliminated regardless of what you pass.\n- Passing a 2D matrix as `matrix` requires it to be square with side == len(variable); mismatches raise FunctionError at instantiation, not at call time.\n- If neither default_variable nor input_shapes is provided, the variable shape is flexible and will be inferred at runtime from the first call.'


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
        'Call this tool to instantiate a Stability objective function that measures how stable a neural activation pattern is under recurrent self-connections.'
        return _impl(args or {})
