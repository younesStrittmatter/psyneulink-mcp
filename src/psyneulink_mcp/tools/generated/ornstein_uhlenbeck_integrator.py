"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4151c675072bb7366f92cdb5c5865ac25b9b8185e358cfd1efe53cd603f37570'
__pnl_qualname__ = 'psyneulink.OrnsteinUhlenbeckIntegrator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_ornstein_uhlenbeck_integrator'
TOOL_DESCRIPTION = 'Call this tool to create an Ornstein-Uhlenbeck stochastic integrator function, modeling mean-reverting drift with Gaussian noise — useful for simulating noisy neural decision variables, diffusion processes, or any system where state decays toward a mean while being driven by stimulus input. Returns a PsyNeuLink OrnsteinUhlenbeckIntegrator object; each call to its function executes one time step, returning a tuple of (updated_value, current_time).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "decay": {\n      "default": 1,\n      "description": "Multiplicative factor applied to the previous value each step (mean-reversion strength). Values <1 cause decay toward zero; 1.0 = no decay. Scalar or array matching variable length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "default_variable": {\n      "description": "Template for the stimulus input (drift component). Scalar or array; array length determines dimensionality of integration.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initializer": {\n      "default": 0,\n      "description": "Starting value(s) for the integrator state (previous_value). Scalar or array matching variable length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the function instance; auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Scales the standard deviation of the Gaussian noise term: sigma = sqrt(time_step_size * noise). Must be a scalar float; array noise is not yet supported.",\n      "type": "number"\n    },\n    "non_decision_time": {\n      "default": 0,\n      "description": "Starting time offset for the integration clock; sets the initial value of previous_time. Useful for modeling non-decision latency in DDM-style models.",\n      "type": "number"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Constant additive bias applied after each integration step. Scalar or array matching variable length. Serves as ADDITIVE_PARAM for modulation.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplicative scaling of the input variable (stimulus drive). Scalar or array matching variable length. Serves as MULTIPLICATIVE_PARAM for modulation.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "seed": {\n      "description": "Seed for the internal numpy RandomState, enabling reproducible stochastic runs.",\n      "type": "integer"\n    },\n    "time_step_size": {\n      "default": 1,\n      "description": "Duration of each integration step. Scales both the drift term and the noise (sigma = sqrt(time_step_size * noise)). Smaller values yield finer temporal resolution.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe update formula is: new_value = previous_value + (decay * previous_value - rate * variable) * time_step_size + sqrt(time_step_size * noise) * N(0,1). Note the sign convention: the rate term subtracts stimulus drive (rate * variable), so increasing rate increases the pull of the input away from the current state, not toward it — this differs from a simple leaky integrator. decay multiplies previous_value additively on top of it; with decay=1.0 the state does not shrink, so set decay<1.0 for true mean-reversion. noise must be a scalar float; passing a list/array will raise a FunctionError. The function returns a tuple (value_array, time_scalar), not a plain array — unpack accordingly. initializer is aliased as starting_value in the constructor; either name works. previous_time is initialized to non_decision_time, not 0, so the reported time after the first step will be non_decision_time + time_step_size.'
TOOL_PARAMETERS = { 'properties': { 'decay': { 'default': 1,
                             'description': 'Multiplicative factor applied to the '
                                            'previous value each step (mean-reversion '
                                            'strength). Values <1 cause decay toward '
                                            'zero; 1.0 = no decay. Scalar or array '
                                            'matching variable length.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'default_variable': { 'description': 'Template for the stimulus '
                                                       'input (drift component). '
                                                       'Scalar or array; array length '
                                                       'determines dimensionality of '
                                                       'integration.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'initializer': { 'default': 0,
                                   'description': 'Starting value(s) for the '
                                                  'integrator state (previous_value). '
                                                  'Scalar or array matching variable '
                                                  'length.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]},
                  'name': { 'description': 'Optional name for the function instance; '
                                           'auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Scales the standard deviation of the '
                                            'Gaussian noise term: sigma = '
                                            'sqrt(time_step_size * noise). Must be a '
                                            'scalar float; array noise is not yet '
                                            'supported.',
                             'type': 'number'},
                  'non_decision_time': { 'default': 0,
                                         'description': 'Starting time offset for the '
                                                        'integration clock; sets the '
                                                        'initial value of '
                                                        'previous_time. Useful for '
                                                        'modeling non-decision latency '
                                                        'in DDM-style models.',
                                         'type': 'number'},
                  'offset': { 'default': 0,
                              'description': 'Constant additive bias applied after '
                                             'each integration step. Scalar or array '
                                             'matching variable length. Serves as '
                                             'ADDITIVE_PARAM for modulation.',
                              'oneOf': [ {'type': 'number'},
                                         { 'items': {'type': 'number'},
                                           'type': 'array'}]},
                  'rate': { 'default': 1,
                            'description': 'Multiplicative scaling of the input '
                                           'variable (stimulus drive). Scalar or array '
                                           'matching variable length. Serves as '
                                           'MULTIPLICATIVE_PARAM for modulation.',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'seed': { 'description': 'Seed for the internal numpy RandomState, '
                                           'enabling reproducible stochastic runs.',
                            'type': 'integer'},
                  'time_step_size': { 'default': 1,
                                      'description': 'Duration of each integration '
                                                     'step. Scales both the drift term '
                                                     'and the noise (sigma = '
                                                     'sqrt(time_step_size * noise)). '
                                                     'Smaller values yield finer '
                                                     'temporal resolution.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The update formula is: new_value = previous_value + (decay * previous_value - rate * variable) * time_step_size + sqrt(time_step_size * noise) * N(0,1). Note the sign convention: the rate term subtracts stimulus drive (rate * variable), so increasing rate increases the pull of the input away from the current state, not toward it — this differs from a simple leaky integrator. decay multiplies previous_value additively on top of it; with decay=1.0 the state does not shrink, so set decay<1.0 for true mean-reversion. noise must be a scalar float; passing a list/array will raise a FunctionError. The function returns a tuple (value_array, time_scalar), not a plain array — unpack accordingly. initializer is aliased as starting_value in the constructor; either name works. previous_time is initialized to non_decision_time, not 0, so the reported time after the first step will be non_decision_time + time_step_size.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.OrnsteinUhlenbeckIntegrator
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
    def create_ornstein_uhlenbeck_integrator(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an Ornstein-Uhlenbeck stochastic integrator function, modeling mean-reverting drift with Gaussian noise — useful for simulating noisy neural decision variables, diffusion processes, or any system where state decays toward a mean while being driven by stimulus input.'
        return _impl(args or {})
