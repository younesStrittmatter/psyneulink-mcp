"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4a6754ae8495d513da9d1ac52fcb46a95e13b96ddef3373e7aabe601a381707d'
__pnl_qualname__ = 'psyneulink.DriftDiffusionIntegrator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_drift_diffusion_integrator'
TOOL_DESCRIPTION = 'Use this tool to create a DriftDiffusionIntegrator function that simulates evidence accumulation toward a decision boundary (DDM/random walk model). Call it when building a DDM-based decision mechanism or when you need a stateful integrator that accumulates noisy evidence step-by-step until a threshold is reached. Each call constructs the integrator object; the returned object computes one time step as: previous_value + rate * variable * time_step_size + noise * sqrt(time_step_size) * N(0,1), clipped to [-threshold, threshold].\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Stimulus component of the drift rate (multiplied by rate to get total drift). Scalar or array; if array, each element is an independently integrated decision variable.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this function instance. Auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Scale of normally distributed random noise added each step. Noise variance is noise * sqrt(time_step_size). Must be a float (array support not yet fully implemented). Default 0.0.",\n      "type": "number"\n    },\n    "non_decision_time": {\n      "default": 0,\n      "description": "Non-decision time offset (e.g., encoding + motor delay) added to the starting time. Sets initial previous_time. Default 0.0.",\n      "type": "number"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Constant additive bias applied each step, only when |accumulated value| < threshold. Scalar or 1D array matching variable length. Default 0.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "params": {\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are PsyNeuLink parameter keywords.",\n      "type": "object"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Attentional/multiplicative component of drift rate. Applied element-wise to variable. Must be scalar or 1D array matching variable length. Default 1.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "seed": {\n      "description": "Seed for the internal random state (numpy.RandomState). Set for reproducible stochastic simulations.",\n      "type": "integer"\n    },\n    "starting_value": {\n      "default": 0,\n      "description": "Initial value of the accumulator (alias for initializer). Scalar or 1D array matching variable length. Default 0.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "threshold": {\n      "default": 100,\n      "description": "Decision boundary: integration is clamped to [-threshold, threshold]. Use a WhenFinished Condition on the owning Mechanism to stop execution when this is reached. Default 100.0 (effectively unbounded).",\n      "type": "number"\n    },\n    "time_step_size": {\n      "default": 1,\n      "description": "Duration of each integration step; scales both the drift (rate * variable * time_step_size) and the noise (noise * sqrt(time_step_size)). Default 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The default threshold in the source Parameters class is 100.0, NOT the 1.0 shown in the docstring signature — use 100.0 as the effective default.\n- The default time_step_size in the source Parameters class is 1.0, NOT 0.01 shown in the docstring signature.\n- `starting_value` and `initializer` are aliases; prefer `starting_value` for clarity.\n- `noise` must be a float only; list/array noise is documented as not yet fully implemented.\n- `rate` must be a scalar or 1D array; passing a 2D array raises ValueError.\n- Threshold acts as a hard clamp (saturation barrier for vector variables), not a termination signal by itself — pair with a `WhenFinished` Condition on the owning Mechanism\'s scheduler to actually stop integration.\n- The function returns a 2-element array: [previous_value, previous_time], not just the accumulated evidence.\n- `non_decision_time` shifts the time axis only (previous_time starts at non_decision_time), not the accumulator value.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Stimulus component of the '
                                                       'drift rate (multiplied by rate '
                                                       'to get total drift). Scalar or '
                                                       'array; if array, each element '
                                                       'is an independently integrated '
                                                       'decision variable.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'name': { 'description': 'Name for this function instance. '
                                           'Auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Scale of normally distributed random '
                                            'noise added each step. Noise variance is '
                                            'noise * sqrt(time_step_size). Must be a '
                                            'float (array support not yet fully '
                                            'implemented). Default 0.0.',
                             'type': 'number'},
                  'non_decision_time': { 'default': 0,
                                         'description': 'Non-decision time offset '
                                                        '(e.g., encoding + motor '
                                                        'delay) added to the starting '
                                                        'time. Sets initial '
                                                        'previous_time. Default 0.0.',
                                         'type': 'number'},
                  'offset': { 'default': 0,
                              'description': 'Constant additive bias applied each '
                                             'step, only when |accumulated value| < '
                                             'threshold. Scalar or 1D array matching '
                                             'variable length. Default 0.0.',
                              'oneOf': [ {'type': 'number'},
                                         { 'items': {'type': 'number'},
                                           'type': 'array'}]},
                  'params': { 'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'PsyNeuLink parameter keywords.',
                              'type': 'object'},
                  'rate': { 'default': 1,
                            'description': 'Attentional/multiplicative component of '
                                           'drift rate. Applied element-wise to '
                                           'variable. Must be scalar or 1D array '
                                           'matching variable length. Default 1.0.',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'seed': { 'description': 'Seed for the internal random state '
                                           '(numpy.RandomState). Set for reproducible '
                                           'stochastic simulations.',
                            'type': 'integer'},
                  'starting_value': { 'default': 0,
                                      'description': 'Initial value of the accumulator '
                                                     '(alias for initializer). Scalar '
                                                     'or 1D array matching variable '
                                                     'length. Default 0.0.',
                                      'oneOf': [ {'type': 'number'},
                                                 { 'items': {'type': 'number'},
                                                   'type': 'array'}]},
                  'threshold': { 'default': 100,
                                 'description': 'Decision boundary: integration is '
                                                'clamped to [-threshold, threshold]. '
                                                'Use a WhenFinished Condition on the '
                                                'owning Mechanism to stop execution '
                                                'when this is reached. Default 100.0 '
                                                '(effectively unbounded).',
                                 'type': 'number'},
                  'time_step_size': { 'default': 1,
                                      'description': 'Duration of each integration '
                                                     'step; scales both the drift '
                                                     '(rate * variable * '
                                                     'time_step_size) and the noise '
                                                     '(noise * sqrt(time_step_size)). '
                                                     'Default 1.0.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- The default threshold in the source Parameters class is 100.0, NOT the 1.0 shown in the docstring signature — use 100.0 as the effective default.\n- The default time_step_size in the source Parameters class is 1.0, NOT 0.01 shown in the docstring signature.\n- `starting_value` and `initializer` are aliases; prefer `starting_value` for clarity.\n- `noise` must be a float only; list/array noise is documented as not yet fully implemented.\n- `rate` must be a scalar or 1D array; passing a 2D array raises ValueError.\n- Threshold acts as a hard clamp (saturation barrier for vector variables), not a termination signal by itself — pair with a `WhenFinished` Condition on the owning Mechanism's scheduler to actually stop integration.\n- The function returns a 2-element array: [previous_value, previous_time], not just the accumulated evidence.\n- `non_decision_time` shifts the time axis only (previous_time starts at non_decision_time), not the accumulator value."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DriftDiffusionIntegrator
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
    def create_drift_diffusion_integrator(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a DriftDiffusionIntegrator function that simulates evidence accumulation toward a decision boundary (DDM/random walk model).'
        return _impl(args or {})
