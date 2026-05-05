"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a7616f78670f80e2f98d0ff7c781e2c3edb417162c1f59e88ef1751bcfc1a04d'
__pnl_qualname__ = 'psyneulink.LCAMechanism'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_lca_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a Leaky Competitive Accumulator (LCA) — a recurrent mechanism that models competitive decision-making, winner-take-all dynamics, or evidence accumulation over time. Use it when the agent needs units that inhibit each other (lateral inhibition) and accumulate activation with leak. Returns an LCAMechanism instance ready to be added to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "[min, max] bounds to clip output values after each step.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "competition": {\n      "default": 1,\n      "description": "Magnitude of lateral inhibition between units (off-diagonal weights = -competition). Must be positive; negative values produce a warning and result in excitatory cross-connections.",\n      "type": "number"\n    },\n    "initial_value": {\n      "description": "Starting activation value for all units.",\n      "type": "number"\n    },\n    "input_shapes": {\n      "description": "Number of units (competing alternatives). Must be >= 2 if threshold_criterion is MAX_VS_NEXT or MAX_VS_AVG.",\n      "type": "integer"\n    },\n    "integrator_mode": {\n      "default": true,\n      "description": "Whether to run the LeakyCompetingIntegrator (accumulate over time). Defaults to True for LCAMechanism, unlike base TransferMechanism.",\n      "type": "boolean"\n    },\n    "leak": {\n      "default": 0.5,\n      "description": "Decay rate applied to previous activation each time step. Higher values = more forgetting. Maps to LeakyCompetingIntegrator rate.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Name for this mechanism instance.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Noise added to integration at each time step.",\n      "type": "number"\n    },\n    "self_excitation": {\n      "default": 0,\n      "description": "Self-feedback weight on diagonal of recurrent matrix. Positive values create self-sustaining activation; alias for \'auto\'.",\n      "type": "number"\n    },\n    "threshold": {\n      "description": "Value at which is_finished is set to True, stopping accumulation. Evaluated against threshold_criterion. Omit to run indefinitely.",\n      "type": "number"\n    },\n    "threshold_criterion": {\n      "default": "VALUE",\n      "description": "What to compare against threshold. VALUE: max unit value; MAX_VS_NEXT: gap between top two units; MAX_VS_AVG: top unit minus average of others; CONVERGENCE: max absolute change between steps (uses <= comparison).",\n      "enum": [\n        "VALUE",\n        "MAX_VS_NEXT",\n        "MAX_VS_AVG",\n        "CONVERGENCE"\n      ],\n      "type": "string"\n    },\n    "time_step_size": {\n      "default": 0.1,\n      "description": "Integration time step for the LeakyCompetingIntegrator. Smaller values give finer temporal resolution but require more steps to settle.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `integrator_mode` defaults to True here, unlike the parent RecurrentTransferMechanism where it defaults to False — the LCA is designed to run in integrator mode.\n- `competition` specifies inhibition *magnitude*; the off-diagonal weights are set to *negative* competition. Passing a negative competition value produces a warning and creates excitatory (positive) off-diagonal connections.\n- `self_excitation` is an alias for `auto`; do not pass both. Similarly, `competition` and `hetero` encode the same parameter with opposite sign — do not pass both.\n- If `matrix` is passed as a kwarg, `self_excitation` and `competition` are silently ignored and the explicit matrix is used instead.\n- `threshold_criterion` of MAX_VS_NEXT or MAX_VS_AVG requires `input_shapes` >= 2.\n- `threshold` and `termination_threshold` cannot both be specified; likewise `threshold_criterion` and `termination_measure` cannot both be specified.\n- Default transfer function is Logistic (not Linear), giving outputs in (0, 1).\n- The mechanism runs until `is_finished` (threshold reached) or the Composition\'s trial limit. Without a threshold, set trial count explicitly to avoid infinite accumulation.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': '[min, max] bounds to clip output values '
                                           'after each step.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'competition': { 'default': 1,
                                   'description': 'Magnitude of lateral inhibition '
                                                  'between units (off-diagonal weights '
                                                  '= -competition). Must be positive; '
                                                  'negative values produce a warning '
                                                  'and result in excitatory '
                                                  'cross-connections.',
                                   'type': 'number'},
                  'initial_value': { 'description': 'Starting activation value for all '
                                                    'units.',
                                     'type': 'number'},
                  'input_shapes': { 'description': 'Number of units (competing '
                                                   'alternatives). Must be >= 2 if '
                                                   'threshold_criterion is MAX_VS_NEXT '
                                                   'or MAX_VS_AVG.',
                                    'type': 'integer'},
                  'integrator_mode': { 'default': True,
                                       'description': 'Whether to run the '
                                                      'LeakyCompetingIntegrator '
                                                      '(accumulate over time). '
                                                      'Defaults to True for '
                                                      'LCAMechanism, unlike base '
                                                      'TransferMechanism.',
                                       'type': 'boolean'},
                  'leak': { 'default': 0.5,
                            'description': 'Decay rate applied to previous activation '
                                           'each time step. Higher values = more '
                                           'forgetting. Maps to '
                                           'LeakyCompetingIntegrator rate.',
                            'type': 'number'},
                  'name': { 'description': 'Name for this mechanism instance.',
                            'type': 'string'},
                  'noise': { 'description': 'Noise added to integration at each time '
                                            'step.',
                             'type': 'number'},
                  'self_excitation': { 'default': 0,
                                       'description': 'Self-feedback weight on '
                                                      'diagonal of recurrent matrix. '
                                                      'Positive values create '
                                                      'self-sustaining activation; '
                                                      "alias for 'auto'.",
                                       'type': 'number'},
                  'threshold': { 'description': 'Value at which is_finished is set to '
                                                'True, stopping accumulation. '
                                                'Evaluated against '
                                                'threshold_criterion. Omit to run '
                                                'indefinitely.',
                                 'type': 'number'},
                  'threshold_criterion': { 'default': 'VALUE',
                                           'description': 'What to compare against '
                                                          'threshold. VALUE: max unit '
                                                          'value; MAX_VS_NEXT: gap '
                                                          'between top two units; '
                                                          'MAX_VS_AVG: top unit minus '
                                                          'average of others; '
                                                          'CONVERGENCE: max absolute '
                                                          'change between steps (uses '
                                                          '<= comparison).',
                                           'enum': [ 'VALUE',
                                                     'MAX_VS_NEXT',
                                                     'MAX_VS_AVG',
                                                     'CONVERGENCE'],
                                           'type': 'string'},
                  'time_step_size': { 'default': 0.1,
                                      'description': 'Integration time step for the '
                                                     'LeakyCompetingIntegrator. '
                                                     'Smaller values give finer '
                                                     'temporal resolution but require '
                                                     'more steps to settle.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- `integrator_mode` defaults to True here, unlike the parent RecurrentTransferMechanism where it defaults to False — the LCA is designed to run in integrator mode.\n- `competition` specifies inhibition *magnitude*; the off-diagonal weights are set to *negative* competition. Passing a negative competition value produces a warning and creates excitatory (positive) off-diagonal connections.\n- `self_excitation` is an alias for `auto`; do not pass both. Similarly, `competition` and `hetero` encode the same parameter with opposite sign — do not pass both.\n- If `matrix` is passed as a kwarg, `self_excitation` and `competition` are silently ignored and the explicit matrix is used instead.\n- `threshold_criterion` of MAX_VS_NEXT or MAX_VS_AVG requires `input_shapes` >= 2.\n- `threshold` and `termination_threshold` cannot both be specified; likewise `threshold_criterion` and `termination_measure` cannot both be specified.\n- Default transfer function is Logistic (not Linear), giving outputs in (0, 1).\n- The mechanism runs until `is_finished` (threshold reached) or the Composition's trial limit. Without a threshold, set trial count explicitly to avoid infinite accumulation."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LCAMechanism
    resolved = handles.resolve_in(kwargs)
    result = target(**resolved)
    try:
        json.dumps(result)
    except (TypeError, ValueError):
        return handles.register_handle(result)
    return result


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_lca_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Leaky Competitive Accumulator (LCA) — a recurrent mechanism that models competitive decision-making, winner-take-all dynamics, or evidence accumulation over time.'
        return _impl(args or {})
