"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '81c604a8fe7f81b3dda271c0bcef18adb6f78fb10762cabffdc7b839fe9e0481'
__pnl_qualname__ = 'psyneulink.AsymptoticTimer'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_asymptotic_timer'
TOOL_DESCRIPTION = 'Call this tool to instantiate an AsymptoticTimer function when you need an exponential decay (or rise) toward an asymptote — for example, modeling time-based habituation, fatigue, or approach to equilibrium in a PsyNeuLink Component. The function maps an elapsed-time variable to a value that starts at `initial` (at variable=0) and approaches `final` exponentially, reaching within `tolerance` fraction of the gap at variable=`duration`. Returns a numeric value or array.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input value (elapsed time). Can be a number or array. Determines the shape of the output.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "duration": {\n      "default": 1,\n      "description": "The variable value at which the function reaches within `tolerance` fraction of the initial-to-final gap. Must be > 0. Defaults to 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "final": {\n      "default": 0,\n      "description": "Asymptotic target value the function decays (or rises) toward. Defaults to 0.0. Function decays if final < initial, rises if final > initial.",\n      "type": "number"\n    },\n    "initial": {\n      "default": 1,\n      "description": "Value of the function when variable=0. Must be > 0. Defaults to 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the Function instance. If omitted, FunctionRegistry assigns a default.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter names, values override the corresponding constructor arguments.",\n      "type": "object"\n    },\n    "tolerance": {\n      "default": 0.01,\n      "description": "Fraction of (initial - final) that defines \'close enough\' to final at variable=duration. Must be strictly between 0 and 1. Defaults to 0.01 (i.e., 1% of the gap remaining at variable=duration).",\n      "exclusiveMaximum": 1,\n      "exclusiveMinimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `initial` must be strictly greater than 0; passing 0 or a negative value will raise a validation error.\n- `tolerance` must be strictly between 0 and 1 (exclusive on both ends); 0.01 means the function reaches 1% of the initial-to-final gap at variable=duration.\n- The `rate` parameter appears in the Parameters class but is intentionally unused and must remain None; do not pass it.\n- The function rises toward `final` when final > initial, and decays when final < initial — direction is implicit from the parameter relationship, not a separate flag.\n- `duration` is not a hard cutoff; the exponential continues past it. It only calibrates where `tolerance` is achieved.\n- Passing `default_variable` as an array returns an array of the same shape, applying the transform element-wise.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input value '
                                                       '(elapsed time). Can be a '
                                                       'number or array. Determines '
                                                       'the shape of the output.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'duration': { 'default': 1,
                                'description': 'The variable value at which the '
                                               'function reaches within `tolerance` '
                                               'fraction of the initial-to-final gap. '
                                               'Must be > 0. Defaults to 1.0.',
                                'exclusiveMinimum': 0,
                                'type': 'number'},
                  'final': { 'default': 0,
                             'description': 'Asymptotic target value the function '
                                            'decays (or rises) toward. Defaults to '
                                            '0.0. Function decays if final < initial, '
                                            'rises if final > initial.',
                             'type': 'number'},
                  'initial': { 'default': 1,
                               'description': 'Value of the function when variable=0. '
                                              'Must be > 0. Defaults to 1.0.',
                               'exclusiveMinimum': 0,
                               'type': 'number'},
                  'name': { 'description': 'Optional name for the Function instance. '
                                           'If omitted, FunctionRegistry assigns a '
                                           'default.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter names, values override the '
                                             'corresponding constructor arguments.',
                              'type': 'object'},
                  'tolerance': { 'default': 0.01,
                                 'description': 'Fraction of (initial - final) that '
                                                "defines 'close enough' to final at "
                                                'variable=duration. Must be strictly '
                                                'between 0 and 1. Defaults to 0.01 '
                                                '(i.e., 1% of the gap remaining at '
                                                'variable=duration).',
                                 'exclusiveMaximum': 1,
                                 'exclusiveMinimum': 0,
                                 'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `initial` must be strictly greater than 0; passing 0 or a negative value will raise a validation error.\n- `tolerance` must be strictly between 0 and 1 (exclusive on both ends); 0.01 means the function reaches 1% of the initial-to-final gap at variable=duration.\n- The `rate` parameter appears in the Parameters class but is intentionally unused and must remain None; do not pass it.\n- The function rises toward `final` when final > initial, and decays when final < initial — direction is implicit from the parameter relationship, not a separate flag.\n- `duration` is not a hard cutoff; the exponential continues past it. It only calibrates where `tolerance` is achieved.\n- Passing `default_variable` as an array returns an array of the same shape, applying the transform element-wise.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.AsymptoticTimer
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
    def create_asymptotic_timer(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate an AsymptoticTimer function when you need an exponential decay (or rise) toward an asymptote — for example, modeling time-based habituation, fatigue, or approach to equilibrium in a PsyNeuLink Component.'
        return _impl(args or {})
