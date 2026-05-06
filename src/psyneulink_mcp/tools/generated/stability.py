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
TOOL_DESCRIPTION = 'Call this tool to instantiate a PsyNeuLink `Stability` objective function that measures how stable a state vector is under recurrent weight dynamics. Use it when you need a function object to pass as the `function` argument of a `RecurrentTransferMechanism`, or to compute energy/distance-based stability scores directly. Returns a `Stability` instance whose `.execute([array])` method returns a scalar stability value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1-D array defining the shape and default value for the state vector. Use this OR input_shapes, not both.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Length of the state vector (fills with zeros). Use this OR default_variable, not both.",\n      "type": "integer"\n    },\n    "matrix": {\n      "default": "HOLLOW_MATRIX",\n      "description": "Square recurrent weight matrix. Must match the length of the state vector. If a non-hollow matrix is provided, it is convolved with HOLLOW_MATRIX to eliminate self-connections. Defaults to \'HOLLOW_MATRIX\'.",\n      "oneOf": [\n        {\n          "enum": [\n            "HOLLOW_MATRIX",\n            "IDENTITY_MATRIX",\n            "FULL_CONNECTIVITY_MATRIX",\n            "RANDOM_CONNECTIVITY_MATRIX"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "metric": {\n      "default": "ENERGY",\n      "description": "Distance metric used to compare the original state to its matrix-transformed version. \'ENERGY\' is the standard Hopfield energy metric.",\n      "enum": [\n        "ENERGY",\n        "ENTROPY",\n        "EUCLIDEAN",\n        "COSINE",\n        "CORRELATION",\n        "ANGLE",\n        "CROSS_ENTROPY",\n        "MAX_ABS_DIFF"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "If true, divides the stability result by the length of the state vector.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — do NOT pass a `name` argument: `Stability.__init__` does not accept `name` and will raise TypeError. Always supply either `default_variable` or `input_shapes`; omitting both leaves the matrix unsized and causes a NoneType error at execution time (`matrix * self._hollow_matrix` fails). The `matrix` string keyword must be spelled exactly as shown (e.g. `"HOLLOW_MATRIX"`, not `"hollow_matrix"`). The `metric` string is case-sensitive and must be uppercase (e.g. `"ENERGY"`, not `"energy"`). `transfer_fct` accepts a Python callable and cannot be specified through this MCP tool. Do not pass `params`, `owner`, or `prefs` — they are internal PNL wiring arguments not intended for agent use.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1-D array defining the shape '
                                                       'and default value for the '
                                                       'state vector. Use this OR '
                                                       'input_shapes, not both.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Length of the state vector (fills '
                                                   'with zeros). Use this OR '
                                                   'default_variable, not both.',
                                    'type': 'integer'},
                  'matrix': { 'default': 'HOLLOW_MATRIX',
                              'description': 'Square recurrent weight matrix. Must '
                                             'match the length of the state vector. If '
                                             'a non-hollow matrix is provided, it is '
                                             'convolved with HOLLOW_MATRIX to '
                                             'eliminate self-connections. Defaults to '
                                             "'HOLLOW_MATRIX'.",
                              'oneOf': [ { 'enum': [ 'HOLLOW_MATRIX',
                                                     'IDENTITY_MATRIX',
                                                     'FULL_CONNECTIVITY_MATRIX',
                                                     'RANDOM_CONNECTIVITY_MATRIX'],
                                           'type': 'string'},
                                         { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'}]},
                  'metric': { 'default': 'ENERGY',
                              'description': 'Distance metric used to compare the '
                                             'original state to its matrix-transformed '
                                             "version. 'ENERGY' is the standard "
                                             'Hopfield energy metric.',
                              'enum': [ 'ENERGY',
                                        'ENTROPY',
                                        'EUCLIDEAN',
                                        'COSINE',
                                        'CORRELATION',
                                        'ANGLE',
                                        'CROSS_ENTROPY',
                                        'MAX_ABS_DIFF'],
                              'type': 'string'},
                  'normalize': { 'default': False,
                                 'description': 'If true, divides the stability result '
                                                'by the length of the state vector.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL — do NOT pass a `name` argument: `Stability.__init__` does not accept `name` and will raise TypeError. Always supply either `default_variable` or `input_shapes`; omitting both leaves the matrix unsized and causes a NoneType error at execution time (`matrix * self._hollow_matrix` fails). The `matrix` string keyword must be spelled exactly as shown (e.g. `"HOLLOW_MATRIX"`, not `"hollow_matrix"`). The `metric` string is case-sensitive and must be uppercase (e.g. `"ENERGY"`, not `"energy"`). `transfer_fct` accepts a Python callable and cannot be specified through this MCP tool. Do not pass `params`, `owner`, or `prefs` — they are internal PNL wiring arguments not intended for agent use.'


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
        'Call this tool to instantiate a PsyNeuLink `Stability` objective function that measures how stable a state vector is under recurrent weight dynamics.'
        return _impl(args or {})
