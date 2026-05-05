"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8d8ad06cb405ac60f63ee523994dbfb3fd69145cd4259ac47ae88266e2919953'
__pnl_qualname__ = 'psyneulink.FitzHughNagumoIntegrator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_fitz_hugh_nagumo_integrator'
TOOL_DESCRIPTION = 'Use this tool to instantiate a FitzHugh-Nagumo integrator for simulating excitable neural oscillator dynamics (e.g., LC norepinephrine neurons, action potential spiking). Each call configures one integrator; call it then execute the function to advance the state by one time step, returning arrays [v, w, time] representing the fast excitatory variable, slow recovery variable, and current time. Default parameters implement the standard FitzHugh-Nagumo model; set specific parameter combinations to switch to the Modified FitzHughNagumo or Gilzenrat (2002) variants.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "a_v": {\n      "default": -0.3333333333333333,\n      "description": "Coefficient on v^3 term in dv/dt. Default: -1/3 (~-0.333).",\n      "type": "number"\n    },\n    "a_w": {\n      "default": 1,\n      "description": "Coefficient on v term in dw/dt equation. Default: 1.0.",\n      "type": "number"\n    },\n    "b_v": {\n      "default": 0,\n      "description": "Coefficient on v^2 term in dv/dt. Default: 0.0.",\n      "type": "number"\n    },\n    "b_w": {\n      "default": -0.8,\n      "description": "Coefficient on w term in dw/dt equation. Default: -0.8. Note: in Modified FitzHughNagumo variant, the \'c\' parameter maps to NEGATIVE b_w.",\n      "type": "number"\n    },\n    "c_v": {\n      "default": 1,\n      "description": "Coefficient on v term in dv/dt. Default: 1.0.",\n      "type": "number"\n    },\n    "c_w": {\n      "default": 0.7,\n      "description": "Constant term in dw/dt equation. Default: 0.7.",\n      "type": "number"\n    },\n    "d_v": {\n      "default": 0,\n      "description": "Constant term in dv/dt equation. Default: 0.0.",\n      "type": "number"\n    },\n    "default_variable": {\n      "default": 1,\n      "description": "External stimulus (I_ext) input value. Scalar or array. Default: 1.0.",\n      "type": "number"\n    },\n    "e_v": {\n      "default": -1,\n      "description": "Coefficient on w term in dv/dt equation. Default: -1.0.",\n      "type": "number"\n    },\n    "f_v": {\n      "default": 1,\n      "description": "Coefficient on external stimulus (variable/I_ext) in dv/dt. Default: 1.0.",\n      "type": "number"\n    },\n    "initial_v": {\n      "default": 0,\n      "description": "Starting value for the fast excitatory variable v. Default: 0.0.",\n      "type": "number"\n    },\n    "initial_w": {\n      "default": 0,\n      "description": "Starting value for the slow recovery variable w. Default: 0.0.",\n      "type": "number"\n    },\n    "integration_method": {\n      "default": "RK4",\n      "description": "Numerical integration method: \'RK4\' (4th-order Runge-Kutta, more accurate) or \'EULER\' (forward Euler, faster). Default: \'RK4\'.",\n      "enum": [\n        "RK4",\n        "EULER"\n      ],\n      "type": "string"\n    },\n    "mode": {\n      "default": 1,\n      "description": "Electrotonic coupling coefficient (C in Gilzenrat). Scales contribution of v vs. uncorrelated_activity in dw/dt. 1.0 = fully correlated (standard FHN), 0.0 = fully uncorrelated. Default: 1.0.",\n      "type": "number"\n    },\n    "t_0": {\n      "default": 0,\n      "description": "Initial time value. Default: 0.0.",\n      "type": "number"\n    },\n    "threshold": {\n      "default": -1,\n      "description": "Scales v^2 and v terms in dv/dt; acts as excitation threshold \\u2014 stimulus below threshold leads to stable state or single spike, at/above threshold leads to sustained spiking. Default: -1.0.",\n      "type": "number"\n    },\n    "time_constant_v": {\n      "default": 1,\n      "description": "Time constant (tau_v) scaling the dv/dt equation. Default: 1.0.",\n      "type": "number"\n    },\n    "time_constant_w": {\n      "default": 12.5,\n      "description": "Time constant (tau_w or T) scaling the dw/dt equation. Default: 12.5.",\n      "type": "number"\n    },\n    "time_step_size": {\n      "default": 0.05,\n      "description": "Size of each numerical integration time step. Default: 0.05.",\n      "type": "number"\n    },\n    "uncorrelated_activity": {\n      "default": 0,\n      "description": "Baseline/tonic activity constant in dw/dt (d in Gilzenrat). Weighted by (1-mode). Default: 0.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nReturns a 3-element array [previous_v, previous_w, previous_time] after each execution step — not just the instantiation. The integrator is stateful: previous_v, previous_w, and previous_time accumulate across calls. \n\nThree common model variants require specific parameter combinations:\n- Standard FHN (default): all defaults as listed.\n- Modified FHN: set a_v=-1.0, b_v=1.0, c_v=1.0, d_v=0.0, e_v=-1.0, f_v=1.0, time_constant_v=1.0 for dv/dt; set c_w=0.0, mode=1.0, time_constant_w=1.0, uncorrelated_activity=0.0 for dw/dt. `threshold` maps to \'a\' and `variable` maps to I_ext; a_w maps to \'b\' and NEGATIVE b_w maps to \'c\'.\n- Gilzenrat (2002): set a_v=-1.0, b_v=1.0, c_v=1.0, d_v=0.0, e_v=-1.0 for dv/dt; set a_w=1.0, b_w=-1.0, c_w=0.0 for dw/dt. `mode` maps to C, `uncorrelated_activity` maps to d, `time_constant_w` maps to T_u.\n\nThe `noise`, `initializer`, `rate`, and `offset` arguments from the parent IntegratorFunction are NOT supported and will trigger a warning if passed.\n\n`default_variable` is the docstring name for the constructor\'s `default_variable` parameter, which sets the template shape — the actual stimulus is passed at execution time, not construction time.'
TOOL_PARAMETERS = { 'properties': { 'a_v': { 'default': -0.3333333333333333,
                           'description': 'Coefficient on v^3 term in dv/dt. Default: '
                                          '-1/3 (~-0.333).',
                           'type': 'number'},
                  'a_w': { 'default': 1,
                           'description': 'Coefficient on v term in dw/dt equation. '
                                          'Default: 1.0.',
                           'type': 'number'},
                  'b_v': { 'default': 0,
                           'description': 'Coefficient on v^2 term in dv/dt. Default: '
                                          '0.0.',
                           'type': 'number'},
                  'b_w': { 'default': -0.8,
                           'description': 'Coefficient on w term in dw/dt equation. '
                                          'Default: -0.8. Note: in Modified '
                                          "FitzHughNagumo variant, the 'c' parameter "
                                          'maps to NEGATIVE b_w.',
                           'type': 'number'},
                  'c_v': { 'default': 1,
                           'description': 'Coefficient on v term in dv/dt. Default: '
                                          '1.0.',
                           'type': 'number'},
                  'c_w': { 'default': 0.7,
                           'description': 'Constant term in dw/dt equation. Default: '
                                          '0.7.',
                           'type': 'number'},
                  'd_v': { 'default': 0,
                           'description': 'Constant term in dv/dt equation. Default: '
                                          '0.0.',
                           'type': 'number'},
                  'default_variable': { 'default': 1,
                                        'description': 'External stimulus (I_ext) '
                                                       'input value. Scalar or array. '
                                                       'Default: 1.0.',
                                        'type': 'number'},
                  'e_v': { 'default': -1,
                           'description': 'Coefficient on w term in dv/dt equation. '
                                          'Default: -1.0.',
                           'type': 'number'},
                  'f_v': { 'default': 1,
                           'description': 'Coefficient on external stimulus '
                                          '(variable/I_ext) in dv/dt. Default: 1.0.',
                           'type': 'number'},
                  'initial_v': { 'default': 0,
                                 'description': 'Starting value for the fast '
                                                'excitatory variable v. Default: 0.0.',
                                 'type': 'number'},
                  'initial_w': { 'default': 0,
                                 'description': 'Starting value for the slow recovery '
                                                'variable w. Default: 0.0.',
                                 'type': 'number'},
                  'integration_method': { 'default': 'RK4',
                                          'description': 'Numerical integration '
                                                         "method: 'RK4' (4th-order "
                                                         'Runge-Kutta, more accurate) '
                                                         "or 'EULER' (forward Euler, "
                                                         "faster). Default: 'RK4'.",
                                          'enum': ['RK4', 'EULER'],
                                          'type': 'string'},
                  'mode': { 'default': 1,
                            'description': 'Electrotonic coupling coefficient (C in '
                                           'Gilzenrat). Scales contribution of v vs. '
                                           'uncorrelated_activity in dw/dt. 1.0 = '
                                           'fully correlated (standard FHN), 0.0 = '
                                           'fully uncorrelated. Default: 1.0.',
                            'type': 'number'},
                  't_0': { 'default': 0,
                           'description': 'Initial time value. Default: 0.0.',
                           'type': 'number'},
                  'threshold': { 'default': -1,
                                 'description': 'Scales v^2 and v terms in dv/dt; acts '
                                                'as excitation threshold — stimulus '
                                                'below threshold leads to stable state '
                                                'or single spike, at/above threshold '
                                                'leads to sustained spiking. Default: '
                                                '-1.0.',
                                 'type': 'number'},
                  'time_constant_v': { 'default': 1,
                                       'description': 'Time constant (tau_v) scaling '
                                                      'the dv/dt equation. Default: '
                                                      '1.0.',
                                       'type': 'number'},
                  'time_constant_w': { 'default': 12.5,
                                       'description': 'Time constant (tau_w or T) '
                                                      'scaling the dw/dt equation. '
                                                      'Default: 12.5.',
                                       'type': 'number'},
                  'time_step_size': { 'default': 0.05,
                                      'description': 'Size of each numerical '
                                                     'integration time step. Default: '
                                                     '0.05.',
                                      'type': 'number'},
                  'uncorrelated_activity': { 'default': 0,
                                             'description': 'Baseline/tonic activity '
                                                            'constant in dw/dt (d in '
                                                            'Gilzenrat). Weighted by '
                                                            '(1-mode). Default: 0.0.',
                                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Returns a 3-element array [previous_v, previous_w, previous_time] after each execution step — not just the instantiation. The integrator is stateful: previous_v, previous_w, and previous_time accumulate across calls. \n\nThree common model variants require specific parameter combinations:\n- Standard FHN (default): all defaults as listed.\n- Modified FHN: set a_v=-1.0, b_v=1.0, c_v=1.0, d_v=0.0, e_v=-1.0, f_v=1.0, time_constant_v=1.0 for dv/dt; set c_w=0.0, mode=1.0, time_constant_w=1.0, uncorrelated_activity=0.0 for dw/dt. `threshold` maps to 'a' and `variable` maps to I_ext; a_w maps to 'b' and NEGATIVE b_w maps to 'c'.\n- Gilzenrat (2002): set a_v=-1.0, b_v=1.0, c_v=1.0, d_v=0.0, e_v=-1.0 for dv/dt; set a_w=1.0, b_w=-1.0, c_w=0.0 for dw/dt. `mode` maps to C, `uncorrelated_activity` maps to d, `time_constant_w` maps to T_u.\n\nThe `noise`, `initializer`, `rate`, and `offset` arguments from the parent IntegratorFunction are NOT supported and will trigger a warning if passed.\n\n`default_variable` is the docstring name for the constructor's `default_variable` parameter, which sets the template shape — the actual stimulus is passed at execution time, not construction time."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.FitzHughNagumoIntegrator
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
    def create_fitz_hugh_nagumo_integrator(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to instantiate a FitzHugh-Nagumo integrator for simulating excitable neural oscillator dynamics (e.g., LC norepinephrine neurons, action potential spiking).'
        return _impl(args or {})
