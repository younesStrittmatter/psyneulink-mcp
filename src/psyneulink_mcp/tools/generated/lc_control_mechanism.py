"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '40d0473c215d0f7fc1340eceefe6bc90ff3c12669bec3a84c7da20bc00432649'
__pnl_qualname__ = 'psyneulink.LCControlMechanism'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_lc_control_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a Locus Coeruleus / Norepinephrine (LC-NE) control mechanism that dynamically modulates the gain (multiplicative parameter) of one or more processing mechanisms over time. Use it when modeling arousal, attention, or task-engagement effects where a single neuromodulatory signal — governed by FitzHugh-Nagumo dynamics — should simultaneously scale the responsiveness of multiple processing units. Returns a configured LCControlMechanism object whose output (gain signal g(t) = base_level_gain + scaling_factor_gain * w(t)) is broadcast via ControlProjections to all specified target mechanisms.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "a_v_FitzHughNagumo": {\n      "default": -0.3333333333333333,\n      "description": "Coefficient a_v in the v-nullcline of the FitzHugh-Nagumo equations (default -1/3).",\n      "type": "number"\n    },\n    "a_w_FitzHughNagumo": {\n      "default": 1,\n      "description": "Coefficient a_w in the w-nullcline of the FitzHugh-Nagumo equations.",\n      "type": "number"\n    },\n    "b_v_FitzHughNagumo": {\n      "default": 0,\n      "description": "Coefficient b_v in the FitzHugh-Nagumo v equation.",\n      "type": "number"\n    },\n    "b_w_FitzHughNagumo": {\n      "default": -0.8,\n      "description": "Coefficient b_w in the FitzHugh-Nagumo w equation.",\n      "type": "number"\n    },\n    "base_level_gain": {\n      "default": 0.5,\n      "description": "Baseline gain G in g(t) = G + k*w(t). Applied even when the LC is in tonic (low arousal) mode.",\n      "type": "number"\n    },\n    "c_v_FitzHughNagumo": {\n      "default": 1,\n      "description": "Coefficient c_v in the FitzHugh-Nagumo v equation.",\n      "type": "number"\n    },\n    "c_w_FitzHughNagumo": {\n      "default": 0.7,\n      "description": "Constant c_w in the FitzHugh-Nagumo w equation.",\n      "type": "number"\n    },\n    "d_v_FitzHughNagumo": {\n      "default": 0,\n      "description": "Coefficient d_v in the FitzHugh-Nagumo v equation.",\n      "type": "number"\n    },\n    "e_v_FitzHughNagumo": {\n      "default": -1,\n      "description": "Coefficient e_v in the FitzHugh-Nagumo v equation.",\n      "type": "number"\n    },\n    "f_v_FitzHughNagumo": {\n      "default": 1,\n      "description": "Coefficient f_v in the FitzHugh-Nagumo v equation.",\n      "type": "number"\n    },\n    "initial_v_FitzHughNagumo": {\n      "default": 0,\n      "description": "Initial value of the v (membrane potential) variable in the FitzHugh-Nagumo integrator.",\n      "type": "number"\n    },\n    "initial_w_FitzHughNagumo": {\n      "default": 0,\n      "description": "Initial value of the w (recovery/adaptation) variable in the FitzHugh-Nagumo integrator.",\n      "type": "number"\n    },\n    "integration_method": {\n      "default": "RK4",\n      "description": "Numerical integration method for the FitzHugh-Nagumo equations. RK4 (Runge-Kutta 4th order) is more accurate; EULER is faster.",\n      "enum": [\n        "RK4",\n        "EULER"\n      ],\n      "type": "string"\n    },\n    "mode_FitzHughNagumo": {\n      "default": 1,\n      "description": "Blend parameter between tonic (0.0) and phasic (1.0) LC operation modes.",\n      "type": "number"\n    },\n    "modulated_mechanisms": {\n      "description": "Mechanisms whose multiplicative_param will be modulated. Pass a list of Mechanism objects, a Composition (modulates all eligible ProcessingMechanisms added so far), or the string \'ALL\'. Each Mechanism must have a function with a multiplicative_param.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "object"\n          },\n          "type": "array"\n        },\n        {\n          "type": "object"\n        },\n        {\n          "enum": [\n            "ALL"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the LCControlMechanism instance.",\n      "type": "string"\n    },\n    "scaling_factor_gain": {\n      "default": 3,\n      "description": "Scaling factor k in g(t) = G + k*w(t). Controls how strongly the w-variable of the FitzHugh-Nagumo integrator drives the gain signal.",\n      "type": "number"\n    },\n    "t_0_FitzHughNagumo": {\n      "default": 0,\n      "description": "Starting time for the FitzHugh-Nagumo integrator.",\n      "type": "number"\n    },\n    "threshold_FitzHughNagumo": {\n      "default": -1,\n      "description": "Threshold parameter for the FitzHugh-Nagumo integrator, influencing the excitability boundary.",\n      "type": "number"\n    },\n    "time_constant_v_FitzHughNagumo": {\n      "default": 1,\n      "description": "Time constant controlling the rate of change of the v variable.",\n      "type": "number"\n    },\n    "time_constant_w_FitzHughNagumo": {\n      "default": 12.5,\n      "description": "Time constant controlling the rate of change of the w (recovery) variable. Larger values make adaptation slower.",\n      "type": "number"\n    },\n    "time_step_size_FitzHughNagumo": {\n      "default": 0.05,\n      "description": "Integration time step size for the FitzHugh-Nagumo equations.",\n      "type": "number"\n    },\n    "uncorrelated_activity_FitzHughNagumo": {\n      "default": 0,\n      "description": "Baseline uncorrelated activity added to the w equation; shifts the resting gain level.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- modulated_mechanisms items must each have a function with a multiplicative_param (e.g., Logistic gain, Linear slope); mechanisms without one will raise an error.\n- When passing a Composition to modulated_mechanisms, only ProcessingMechanisms already added to the Composition at construction time are captured — mechanisms added later are not automatically included.\n- The output gain signal is g(t) = base_level_gain + scaling_factor_gain * w(t), where w is the second element returned by the FitzHugh-Nagumo integrator, NOT v; confusing w and v is a common error.\n- value (4-element array: [gain, w, v, x]) differs from output_values (1-element: [gain] only); use output_values when reading the control allocation downstream.\n- The docstring labels time_step_size default as 0.0, but the constructor signature shows 0.05 — trust the constructor.\n- mode_FitzHughNagumo=1.0 is full phasic mode; set toward 0.0 for tonic-dominant behavior.\n- An ObjectiveMechanism using CombineMeans(SUM) is automatically created unless objective_mechanism is explicitly provided; pass objective_mechanism=False to suppress it (e.g., when driving LC with a direct input port instead).\n- base_level_gain and scaling_factor_gain are modulable parameters, meaning they can themselves be controlled by an outer ControlMechanism.'
TOOL_PARAMETERS = { 'properties': { 'a_v_FitzHughNagumo': { 'default': -0.3333333333333333,
                                          'description': 'Coefficient a_v in the '
                                                         'v-nullcline of the '
                                                         'FitzHugh-Nagumo equations '
                                                         '(default -1/3).',
                                          'type': 'number'},
                  'a_w_FitzHughNagumo': { 'default': 1,
                                          'description': 'Coefficient a_w in the '
                                                         'w-nullcline of the '
                                                         'FitzHugh-Nagumo equations.',
                                          'type': 'number'},
                  'b_v_FitzHughNagumo': { 'default': 0,
                                          'description': 'Coefficient b_v in the '
                                                         'FitzHugh-Nagumo v equation.',
                                          'type': 'number'},
                  'b_w_FitzHughNagumo': { 'default': -0.8,
                                          'description': 'Coefficient b_w in the '
                                                         'FitzHugh-Nagumo w equation.',
                                          'type': 'number'},
                  'base_level_gain': { 'default': 0.5,
                                       'description': 'Baseline gain G in g(t) = G + '
                                                      'k*w(t). Applied even when the '
                                                      'LC is in tonic (low arousal) '
                                                      'mode.',
                                       'type': 'number'},
                  'c_v_FitzHughNagumo': { 'default': 1,
                                          'description': 'Coefficient c_v in the '
                                                         'FitzHugh-Nagumo v equation.',
                                          'type': 'number'},
                  'c_w_FitzHughNagumo': { 'default': 0.7,
                                          'description': 'Constant c_w in the '
                                                         'FitzHugh-Nagumo w equation.',
                                          'type': 'number'},
                  'd_v_FitzHughNagumo': { 'default': 0,
                                          'description': 'Coefficient d_v in the '
                                                         'FitzHugh-Nagumo v equation.',
                                          'type': 'number'},
                  'e_v_FitzHughNagumo': { 'default': -1,
                                          'description': 'Coefficient e_v in the '
                                                         'FitzHugh-Nagumo v equation.',
                                          'type': 'number'},
                  'f_v_FitzHughNagumo': { 'default': 1,
                                          'description': 'Coefficient f_v in the '
                                                         'FitzHugh-Nagumo v equation.',
                                          'type': 'number'},
                  'initial_v_FitzHughNagumo': { 'default': 0,
                                                'description': 'Initial value of the v '
                                                               '(membrane potential) '
                                                               'variable in the '
                                                               'FitzHugh-Nagumo '
                                                               'integrator.',
                                                'type': 'number'},
                  'initial_w_FitzHughNagumo': { 'default': 0,
                                                'description': 'Initial value of the w '
                                                               '(recovery/adaptation) '
                                                               'variable in the '
                                                               'FitzHugh-Nagumo '
                                                               'integrator.',
                                                'type': 'number'},
                  'integration_method': { 'default': 'RK4',
                                          'description': 'Numerical integration method '
                                                         'for the FitzHugh-Nagumo '
                                                         'equations. RK4 (Runge-Kutta '
                                                         '4th order) is more accurate; '
                                                         'EULER is faster.',
                                          'enum': ['RK4', 'EULER'],
                                          'type': 'string'},
                  'mode_FitzHughNagumo': { 'default': 1,
                                           'description': 'Blend parameter between '
                                                          'tonic (0.0) and phasic '
                                                          '(1.0) LC operation modes.',
                                           'type': 'number'},
                  'modulated_mechanisms': { 'description': 'Mechanisms whose '
                                                           'multiplicative_param will '
                                                           'be modulated. Pass a list '
                                                           'of Mechanism objects, a '
                                                           'Composition (modulates all '
                                                           'eligible '
                                                           'ProcessingMechanisms added '
                                                           'so far), or the string '
                                                           "'ALL'. Each Mechanism must "
                                                           'have a function with a '
                                                           'multiplicative_param.',
                                            'oneOf': [ { 'items': {'type': 'object'},
                                                         'type': 'array'},
                                                       {'type': 'object'},
                                                       { 'enum': ['ALL'],
                                                         'type': 'string'}]},
                  'name': { 'description': 'Optional name for the LCControlMechanism '
                                           'instance.',
                            'type': 'string'},
                  'scaling_factor_gain': { 'default': 3,
                                           'description': 'Scaling factor k in g(t) = '
                                                          'G + k*w(t). Controls how '
                                                          'strongly the w-variable of '
                                                          'the FitzHugh-Nagumo '
                                                          'integrator drives the gain '
                                                          'signal.',
                                           'type': 'number'},
                  't_0_FitzHughNagumo': { 'default': 0,
                                          'description': 'Starting time for the '
                                                         'FitzHugh-Nagumo integrator.',
                                          'type': 'number'},
                  'threshold_FitzHughNagumo': { 'default': -1,
                                                'description': 'Threshold parameter '
                                                               'for the '
                                                               'FitzHugh-Nagumo '
                                                               'integrator, '
                                                               'influencing the '
                                                               'excitability boundary.',
                                                'type': 'number'},
                  'time_constant_v_FitzHughNagumo': { 'default': 1,
                                                      'description': 'Time constant '
                                                                     'controlling the '
                                                                     'rate of change '
                                                                     'of the v '
                                                                     'variable.',
                                                      'type': 'number'},
                  'time_constant_w_FitzHughNagumo': { 'default': 12.5,
                                                      'description': 'Time constant '
                                                                     'controlling the '
                                                                     'rate of change '
                                                                     'of the w '
                                                                     '(recovery) '
                                                                     'variable. Larger '
                                                                     'values make '
                                                                     'adaptation '
                                                                     'slower.',
                                                      'type': 'number'},
                  'time_step_size_FitzHughNagumo': { 'default': 0.05,
                                                     'description': 'Integration time '
                                                                    'step size for the '
                                                                    'FitzHugh-Nagumo '
                                                                    'equations.',
                                                     'type': 'number'},
                  'uncorrelated_activity_FitzHughNagumo': { 'default': 0,
                                                            'description': 'Baseline '
                                                                           'uncorrelated '
                                                                           'activity '
                                                                           'added to '
                                                                           'the w '
                                                                           'equation; '
                                                                           'shifts the '
                                                                           'resting '
                                                                           'gain '
                                                                           'level.',
                                                            'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- modulated_mechanisms items must each have a function with a multiplicative_param (e.g., Logistic gain, Linear slope); mechanisms without one will raise an error.\n- When passing a Composition to modulated_mechanisms, only ProcessingMechanisms already added to the Composition at construction time are captured — mechanisms added later are not automatically included.\n- The output gain signal is g(t) = base_level_gain + scaling_factor_gain * w(t), where w is the second element returned by the FitzHugh-Nagumo integrator, NOT v; confusing w and v is a common error.\n- value (4-element array: [gain, w, v, x]) differs from output_values (1-element: [gain] only); use output_values when reading the control allocation downstream.\n- The docstring labels time_step_size default as 0.0, but the constructor signature shows 0.05 — trust the constructor.\n- mode_FitzHughNagumo=1.0 is full phasic mode; set toward 0.0 for tonic-dominant behavior.\n- An ObjectiveMechanism using CombineMeans(SUM) is automatically created unless objective_mechanism is explicitly provided; pass objective_mechanism=False to suppress it (e.g., when driving LC with a direct input port instead).\n- base_level_gain and scaling_factor_gain are modulable parameters, meaning they can themselves be controlled by an outer ControlMechanism.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LCControlMechanism
    instance = target(**kwargs)
    return repr(instance)


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_lc_control_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Locus Coeruleus / Norepinephrine (LC-NE) control mechanism that dynamically modulates the gain (multiplicative parameter) of one or more processing mechanisms over time.'
        return _impl(args or {})
