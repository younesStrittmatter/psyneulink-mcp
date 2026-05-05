"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '27e668449a905c544e1990d6fcf06d0a2042803156869fb58733dd60c9b7c7a8'
__pnl_qualname__ = 'psyneulink.ContrastiveHebbianMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_contrastive_hebbian_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a ContrastiveHebbianMechanism — a single-layer recurrent network that learns via the Contrastive Hebbian Learning algorithm using alternating minus (free) and plus (clamped) execution phases. Use it when modeling Hopfield-like attractor networks, error-driven Hebbian learning, or brain-inspired predictive coding circuits. Returns a ContrastiveHebbianMechanism instance with OUTPUT_ACTIVITY, CURRENT_ACTIVITY, and ACTIVITY_DIFFERENCE output ports.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clamp": {\n      "default": "HARD_CLAMP",\n      "description": "How INPUT/TARGET values combine with the RECURRENT input. HARD_CLAMP (default) replaces the recurrent activity; SOFT_CLAMP adds to it.",\n      "enum": [\n        "HARD_CLAMP",\n        "SOFT_CLAMP"\n      ],\n      "type": "string"\n    },\n    "continuous": {\n      "default": true,\n      "description": "If true (default), current_activity carries over between trials (not reset at minus phase start). If false, resets to initial_value at the start of each minus phase.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "description": "Whether to enable ContrastiveHebbian learning on the recurrent projection. Defaults to PNL\'s standard learning-enabled flag.",\n      "type": "boolean"\n    },\n    "hidden_size": {\n      "description": "Number of hidden units between input_field and target_field. Omit or set to 0 for no hidden layer.",\n      "type": "integer"\n    },\n    "input_size": {\n      "description": "Number of units in the INPUT InputPort and input_field of current_activity. Required \\u2014 there is no default.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "description": "Rate of integration for the integrator function when integrator_mode is enabled (0\\u20131).",\n      "type": "number"\n    },\n    "integrator_mode": {\n      "description": "If true, activations are integrated over time using integrator_function rather than computed in a single step.",\n      "type": "boolean"\n    },\n    "learning_rate": {\n      "description": "Learning rate for the ContrastiveHebbian learning rule on the recurrent weights.",\n      "type": "number"\n    },\n    "max_passes": {\n      "default": 1000,\n      "description": "Maximum executions per phase before raising an error. Default is 1000. Set to null to allow indefinite execution (risk of infinite loop).",\n      "type": "integer"\n    },\n    "minus_phase_termination_condition": {\n      "default": "CONVERGENCE",\n      "description": "Condition to end the minus (free) phase. CONVERGENCE (default) ends when phase_convergence_function falls below threshold; COUNT ends after a fixed number of passes.",\n      "enum": [\n        "CONVERGENCE",\n        "COUNT"\n      ],\n      "type": "string"\n    },\n    "minus_phase_termination_threshold": {\n      "default": 0.01,\n      "description": "Threshold value for ending the minus phase. Float when condition is CONVERGENCE (default 0.01); integer when condition is COUNT.",\n      "type": "number"\n    },\n    "mode": {\n      "description": "Set to \'SIMPLE_HEBBIAN\' to emulate a standard RecurrentTransferMechanism with Hebbian learning; forces hidden_size=0, separated=False, clamp=SOFT_CLAMP, continuous=False. Omit for standard contrastive Hebbian operation.",\n      "enum": [\n        "SIMPLE_HEBBIAN"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the mechanism instance.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Noise added to the mechanism\'s input on each execution.",\n      "type": "number"\n    },\n    "plus_phase_termination_condition": {\n      "default": "CONVERGENCE",\n      "description": "Condition to end the plus (clamped) phase. CONVERGENCE (default) or COUNT, same semantics as minus_phase_termination_condition.",\n      "enum": [\n        "CONVERGENCE",\n        "COUNT"\n      ],\n      "type": "string"\n    },\n    "plus_phase_termination_threshold": {\n      "default": 0.01,\n      "description": "Threshold value for ending the plus phase. Float for CONVERGENCE (default 0.01); integer for COUNT.",\n      "type": "number"\n    },\n    "separated": {\n      "default": true,\n      "description": "If true (default), target_field occupies its own distinct region of current_activity separate from input_field. If false, target and input fields overlap.",\n      "type": "boolean"\n    },\n    "target_size": {\n      "description": "Number of units in the TARGET InputPort. When separated=True (default), input_size must equal target_size. Omit if no supervised target is needed.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "input_size"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `input_size` is required; the constructor signature has no default for it.\n- When `separated=True` (default) and `target_size > 0`, `input_size` MUST equal `target_size`, or instantiation raises a ContrastiveHebbianError.\n- Setting `mode=\'SIMPLE_HEBBIAN\'` silently overrides: hidden_size→0, separated→False, clamp→SOFT_CLAMP, continuous→False, learning_function→Hebbian. Any values explicitly passed for those parameters are ignored.\n- `combination_function` and `phase_convergence_function` accept callables; these cannot be serialized as plain JSON and should be omitted unless the caller constructs them programmatically.\n- The internal default for `max_passes` is 1000 (the Parameters class value), not None — the docstring header is misleading.\n- `execution_phase` is read-only (False=minus phase, True=plus phase); do not pass it as a constructor argument.\n- When `minus_phase_termination_condition=\'COUNT\'`, pass an integer for `minus_phase_termination_threshold`; when \'CONVERGENCE\', pass a float. Mismatched types cause silent misbehavior, not an exception.\n- `recurrent_size` is computed automatically as input_size + hidden_size (+ target_size if separated). Do not pass it.\n- The ACTIVITY_DIFFERENCE output port (plus_phase_activity − minus_phase_activity) is the learning signal source; it is only meaningful after a full trial (both phases completed).'
TOOL_PARAMETERS = { 'properties': { 'clamp': { 'default': 'HARD_CLAMP',
                             'description': 'How INPUT/TARGET values combine with the '
                                            'RECURRENT input. HARD_CLAMP (default) '
                                            'replaces the recurrent activity; '
                                            'SOFT_CLAMP adds to it.',
                             'enum': ['HARD_CLAMP', 'SOFT_CLAMP'],
                             'type': 'string'},
                  'continuous': { 'default': True,
                                  'description': 'If true (default), current_activity '
                                                 'carries over between trials (not '
                                                 'reset at minus phase start). If '
                                                 'false, resets to initial_value at '
                                                 'the start of each minus phase.',
                                  'type': 'boolean'},
                  'enable_learning': { 'description': 'Whether to enable '
                                                      'ContrastiveHebbian learning on '
                                                      'the recurrent projection. '
                                                      "Defaults to PNL's standard "
                                                      'learning-enabled flag.',
                                       'type': 'boolean'},
                  'hidden_size': { 'description': 'Number of hidden units between '
                                                  'input_field and target_field. Omit '
                                                  'or set to 0 for no hidden layer.',
                                   'type': 'integer'},
                  'input_size': { 'description': 'Number of units in the INPUT '
                                                 'InputPort and input_field of '
                                                 'current_activity. Required — there '
                                                 'is no default.',
                                  'type': 'integer'},
                  'integration_rate': { 'description': 'Rate of integration for the '
                                                       'integrator function when '
                                                       'integrator_mode is enabled '
                                                       '(0–1).',
                                        'type': 'number'},
                  'integrator_mode': { 'description': 'If true, activations are '
                                                      'integrated over time using '
                                                      'integrator_function rather than '
                                                      'computed in a single step.',
                                       'type': 'boolean'},
                  'learning_rate': { 'description': 'Learning rate for the '
                                                    'ContrastiveHebbian learning rule '
                                                    'on the recurrent weights.',
                                     'type': 'number'},
                  'max_passes': { 'default': 1000,
                                  'description': 'Maximum executions per phase before '
                                                 'raising an error. Default is 1000. '
                                                 'Set to null to allow indefinite '
                                                 'execution (risk of infinite loop).',
                                  'type': 'integer'},
                  'minus_phase_termination_condition': { 'default': 'CONVERGENCE',
                                                         'description': 'Condition to '
                                                                        'end the minus '
                                                                        '(free) phase. '
                                                                        'CONVERGENCE '
                                                                        '(default) '
                                                                        'ends when '
                                                                        'phase_convergence_function '
                                                                        'falls below '
                                                                        'threshold; '
                                                                        'COUNT ends '
                                                                        'after a fixed '
                                                                        'number of '
                                                                        'passes.',
                                                         'enum': [ 'CONVERGENCE',
                                                                   'COUNT'],
                                                         'type': 'string'},
                  'minus_phase_termination_threshold': { 'default': 0.01,
                                                         'description': 'Threshold '
                                                                        'value for '
                                                                        'ending the '
                                                                        'minus phase. '
                                                                        'Float when '
                                                                        'condition is '
                                                                        'CONVERGENCE '
                                                                        '(default '
                                                                        '0.01); '
                                                                        'integer when '
                                                                        'condition is '
                                                                        'COUNT.',
                                                         'type': 'number'},
                  'mode': { 'description': "Set to 'SIMPLE_HEBBIAN' to emulate a "
                                           'standard RecurrentTransferMechanism with '
                                           'Hebbian learning; forces hidden_size=0, '
                                           'separated=False, clamp=SOFT_CLAMP, '
                                           'continuous=False. Omit for standard '
                                           'contrastive Hebbian operation.',
                            'enum': ['SIMPLE_HEBBIAN'],
                            'type': 'string'},
                  'name': { 'description': 'Optional name for the mechanism instance.',
                            'type': 'string'},
                  'noise': { 'description': "Noise added to the mechanism's input on "
                                            'each execution.',
                             'type': 'number'},
                  'plus_phase_termination_condition': { 'default': 'CONVERGENCE',
                                                        'description': 'Condition to '
                                                                       'end the plus '
                                                                       '(clamped) '
                                                                       'phase. '
                                                                       'CONVERGENCE '
                                                                       '(default) or '
                                                                       'COUNT, same '
                                                                       'semantics as '
                                                                       'minus_phase_termination_condition.',
                                                        'enum': [ 'CONVERGENCE',
                                                                  'COUNT'],
                                                        'type': 'string'},
                  'plus_phase_termination_threshold': { 'default': 0.01,
                                                        'description': 'Threshold '
                                                                       'value for '
                                                                       'ending the '
                                                                       'plus phase. '
                                                                       'Float for '
                                                                       'CONVERGENCE '
                                                                       '(default '
                                                                       '0.01); integer '
                                                                       'for COUNT.',
                                                        'type': 'number'},
                  'separated': { 'default': True,
                                 'description': 'If true (default), target_field '
                                                'occupies its own distinct region of '
                                                'current_activity separate from '
                                                'input_field. If false, target and '
                                                'input fields overlap.',
                                 'type': 'boolean'},
                  'target_size': { 'description': 'Number of units in the TARGET '
                                                  'InputPort. When separated=True '
                                                  '(default), input_size must equal '
                                                  'target_size. Omit if no supervised '
                                                  'target is needed.',
                                   'type': 'integer'}},
  'required': ['input_size'],
  'type': 'object'}
TOOL_NOTES = "- `input_size` is required; the constructor signature has no default for it.\n- When `separated=True` (default) and `target_size > 0`, `input_size` MUST equal `target_size`, or instantiation raises a ContrastiveHebbianError.\n- Setting `mode='SIMPLE_HEBBIAN'` silently overrides: hidden_size→0, separated→False, clamp→SOFT_CLAMP, continuous→False, learning_function→Hebbian. Any values explicitly passed for those parameters are ignored.\n- `combination_function` and `phase_convergence_function` accept callables; these cannot be serialized as plain JSON and should be omitted unless the caller constructs them programmatically.\n- The internal default for `max_passes` is 1000 (the Parameters class value), not None — the docstring header is misleading.\n- `execution_phase` is read-only (False=minus phase, True=plus phase); do not pass it as a constructor argument.\n- When `minus_phase_termination_condition='COUNT'`, pass an integer for `minus_phase_termination_threshold`; when 'CONVERGENCE', pass a float. Mismatched types cause silent misbehavior, not an exception.\n- `recurrent_size` is computed automatically as input_size + hidden_size (+ target_size if separated). Do not pass it.\n- The ACTIVITY_DIFFERENCE output port (plus_phase_activity − minus_phase_activity) is the learning signal source; it is only meaningful after a full trial (both phases completed)."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ContrastiveHebbianMechanism
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
    def create_contrastive_hebbian_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a ContrastiveHebbianMechanism — a single-layer recurrent network that learns via the Contrastive Hebbian Learning algorithm using alternating minus (free) and plus (clamped) execution phases.'
        return _impl(args or {})
