"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '74c99fe5f877b3bdcc077390f92a67a3c910d5d508b208716b30246bf037bf84'
__pnl_qualname__ = 'psyneulink.InteractiveActivationIntegrator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_interactive_activation_integrator'
TOOL_DESCRIPTION = 'Use this tool to create an InteractiveActivationIntegrator function implementing the McClelland & Rumelhart (1981) interactive activation model. Call it when modeling neural activation that asymptotically approaches a maximum (for positive inputs) or minimum (for negative inputs) and decays toward a resting value. Returns a configured integrator object whose function computes: previous_value + (rate * (variable + noise) * distance_from_asymptote) - (decay * distance_from_rest).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "decay": {\n      "default": 0,\n      "description": "Rate at which activity decays back toward rest. Must be in [0, 1]. Scalar applies to all elements; array must match variable length.",\n      "oneOf": [\n        {\n          "maximum": 1,\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "items": {\n            "maximum": 1,\n            "minimum": 0,\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "default_variable": {\n      "description": "Template for the value to be integrated. If a list or array, each element is integrated independently.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initializer": {\n      "description": "Starting value(s) for integration. Defaults to the value of rest if not specified. Array must match variable length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "max_val": {\n      "default": 1,\n      "description": "Upper asymptote approached when input is positive. Must be greater than min_val for all elements.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "min_val": {\n      "default": -1,\n      "description": "Lower asymptote approached when input is negative. Must be less than max_val for all elements.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this integrator instance. Auto-assigned from FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Random value added to variable each call. Float, array (matching variable length), or a noise Function.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "rate": {\n      "default": 1,\n      "description": "Rate of change in activity toward asymptote. Must be in [0, 1]. Scalar applies to all elements; array must match variable length.",\n      "oneOf": [\n        {\n          "maximum": 1,\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "items": {\n            "maximum": 1,\n            "minimum": 0,\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "rest": {\n      "default": 0,\n      "description": "Resting value: initial value and the asymptote toward which decay pulls the state. Array must match variable length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The source-level default for `decay` in the Parameters class is 0.0, NOT 1.0 as stated in the docstring constructor signature. Use 0.0 as the effective default.\n- `initializer` defaults to the value of `rest` (not 0.0) when omitted; `default_variable` similarly defaults to `initializer`.\n- `rate` and `decay` are validated to be strictly within [0, 1]; passing values outside this range raises FunctionError.\n- `rest` should be between `min_val` and `max_val`, though this is not strictly enforced at validation time.\n- When `variable == 0`, distance_from_asymptote is 0, so the only update is the decay term pulling toward rest.\n- The integrator is stateful: it stores `previous_value` across calls. To reset state, reinitialize the integrator.\n- Array inputs for rate/decay/rest/max_val/min_val must exactly match the length of variable — no broadcasting beyond scalar-to-all.'
TOOL_PARAMETERS = { 'properties': { 'decay': { 'default': 0,
                             'description': 'Rate at which activity decays back toward '
                                            'rest. Must be in [0, 1]. Scalar applies '
                                            'to all elements; array must match '
                                            'variable length.',
                             'oneOf': [ {'maximum': 1, 'minimum': 0, 'type': 'number'},
                                        { 'items': { 'maximum': 1,
                                                     'minimum': 0,
                                                     'type': 'number'},
                                          'type': 'array'}]},
                  'default_variable': { 'description': 'Template for the value to be '
                                                       'integrated. If a list or '
                                                       'array, each element is '
                                                       'integrated independently.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'initializer': { 'description': 'Starting value(s) for integration. '
                                                  'Defaults to the value of rest if '
                                                  'not specified. Array must match '
                                                  'variable length.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]},
                  'max_val': { 'default': 1,
                               'description': 'Upper asymptote approached when input '
                                              'is positive. Must be greater than '
                                              'min_val for all elements.',
                               'oneOf': [ {'type': 'number'},
                                          { 'items': {'type': 'number'},
                                            'type': 'array'}]},
                  'min_val': { 'default': -1,
                               'description': 'Lower asymptote approached when input '
                                              'is negative. Must be less than max_val '
                                              'for all elements.',
                               'oneOf': [ {'type': 'number'},
                                          { 'items': {'type': 'number'},
                                            'type': 'array'}]},
                  'name': { 'description': 'Name for this integrator instance. '
                                           'Auto-assigned from FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Random value added to variable each call. '
                                            'Float, array (matching variable length), '
                                            'or a noise Function.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'rate': { 'default': 1,
                            'description': 'Rate of change in activity toward '
                                           'asymptote. Must be in [0, 1]. Scalar '
                                           'applies to all elements; array must match '
                                           'variable length.',
                            'oneOf': [ {'maximum': 1, 'minimum': 0, 'type': 'number'},
                                       { 'items': { 'maximum': 1,
                                                    'minimum': 0,
                                                    'type': 'number'},
                                         'type': 'array'}]},
                  'rest': { 'default': 0,
                            'description': 'Resting value: initial value and the '
                                           'asymptote toward which decay pulls the '
                                           'state. Array must match variable length.',
                            'oneOf': [ {'type': 'number'},
                                       { 'items': {'type': 'number'},
                                         'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The source-level default for `decay` in the Parameters class is 0.0, NOT 1.0 as stated in the docstring constructor signature. Use 0.0 as the effective default.\n- `initializer` defaults to the value of `rest` (not 0.0) when omitted; `default_variable` similarly defaults to `initializer`.\n- `rate` and `decay` are validated to be strictly within [0, 1]; passing values outside this range raises FunctionError.\n- `rest` should be between `min_val` and `max_val`, though this is not strictly enforced at validation time.\n- When `variable == 0`, distance_from_asymptote is 0, so the only update is the decay term pulling toward rest.\n- The integrator is stateful: it stores `previous_value` across calls. To reset state, reinitialize the integrator.\n- Array inputs for rate/decay/rest/max_val/min_val must exactly match the length of variable — no broadcasting beyond scalar-to-all.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.InteractiveActivationIntegrator
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
    def create_interactive_activation_integrator(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create an InteractiveActivationIntegrator function implementing the McClelland & Rumelhart (1981) interactive activation model.'
        return _impl(args or {})
