"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a7616f78670f80e2f98d0ff7c781e2c3edb417162c1f59e88ef1751bcfc1a04d'
__pnl_qualname__ = 'psyneulink.LCAMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_lca_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a Leaky Competitive Accumulator (LCA) mechanism — a recurrent transfer mechanism suitable for decision-making, winner-take-all dynamics, and accumulator-race models. Returns a PsyNeuLink LCAMechanism instance with lateral inhibition via `competition` and optional self-excitation. Use this when you need units that suppress each other over time until one dominates (e.g., a response selection layer).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "[min, max] bounds applied to output activations after each step.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "competition": {\n      "default": 1,\n      "description": "Magnitude of lateral inhibition (off-diagonal elements in recurrent matrix become -competition). Must be non-negative; a negative value is allowed but reverses the sign convention and triggers a warning.",\n      "type": "number"\n    },\n    "function": {\n      "description": "Transfer function applied after integration. Default is Logistic. Pass the PNL function name as a string (e.g., \'Logistic\', \'ReLU\').",\n      "type": "string"\n    },\n    "initial_value": {\n      "description": "Starting activation values, one per unit. Length must match input_shapes.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Number of units (size of the input/output vector). E.g., 3 for a 3-alternative choice.",\n      "type": "integer"\n    },\n    "integrator_mode": {\n      "default": true,\n      "description": "When true (default for LCA), the mechanism accumulates over time steps. Set false to use it as a single-step transfer mechanism.",\n      "type": "boolean"\n    },\n    "leak": {\n      "default": 0.5,\n      "description": "Leak rate of the LeakyCompetingIntegrator; scales how much prior activation decays each step. Range [0,1]: 0 = no decay, 1 = full reset each step.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Name for the mechanism.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Noise added to the integrator each step.",\n      "type": "number"\n    },\n    "self_excitation": {\n      "default": 0,\n      "description": "Magnitude of self-feedback (diagonal of recurrent matrix). Default 0 means no self-excitation.",\n      "type": "number"\n    },\n    "threshold": {\n      "description": "Value at which is_finished becomes True and the mechanism stops accumulating. Set together with threshold_criterion. Omit or set null for no stopping criterion.",\n      "type": "number"\n    },\n    "threshold_criterion": {\n      "default": "VALUE",\n      "description": "How threshold is evaluated. VALUE: max unit activation >= threshold. MAX_VS_NEXT: gap between top two units >= threshold (requires input_shapes >= 2). MAX_VS_AVG: top unit minus average of others >= threshold (requires input_shapes >= 2). CONVERGENCE: max absolute change between steps <= threshold.",\n      "enum": [\n        "VALUE",\n        "MAX_VS_NEXT",\n        "MAX_VS_AVG",\n        "CONVERGENCE"\n      ],\n      "type": "string"\n    },\n    "time_step_size": {\n      "default": 0.1,\n      "description": "Integration time step for the LeakyCompetingIntegrator. Smaller values increase precision but require more steps to reach threshold.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nKNOWN PNL BUG (tracked in corpus issue #3): If `threshold_criterion` is set to an unrecognized value, PsyNeuLink\'s `_parse_threshold_args` raises `AttributeError: \'LCAMechanism\' object has no attribute \'__name__\'` instead of a clean LCAError — this is a bug in the PNL source (`self.__name__` should be `self.__class__.__name__`). The valid enum values above match the PNL constants exactly; only pass one of those four strings. If the error occurs, it means the string did not match a PNL constant, not that the tool schema is wrong.\n\n`competition` and `hetero` are coupled: PNL internally sets `hetero = -competition`. Do not pass both; use `competition` only.\n\n`self_excitation` is an alias for PNL\'s `auto` parameter. Do not pass both.\n\nIf `matrix` is passed directly (not in this schema), PNL ignores `self_excitation` and `competition` and emits a warning — prefer the high-level parameters.\n\n`MAX_VS_NEXT` and `MAX_VS_AVG` threshold criteria require `input_shapes >= 2`; using them with a single-unit mechanism will raise an error at run time.\n\n`integrator_mode` defaults to `True` for LCAMechanism (unlike base TransferMechanism where it is False) — the mechanism is designed for iterative accumulation.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': '[min, max] bounds applied to output '
                                           'activations after each step.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'competition': { 'default': 1,
                                   'description': 'Magnitude of lateral inhibition '
                                                  '(off-diagonal elements in recurrent '
                                                  'matrix become -competition). Must '
                                                  'be non-negative; a negative value '
                                                  'is allowed but reverses the sign '
                                                  'convention and triggers a warning.',
                                   'type': 'number'},
                  'function': { 'description': 'Transfer function applied after '
                                               'integration. Default is Logistic. Pass '
                                               'the PNL function name as a string '
                                               "(e.g., 'Logistic', 'ReLU').",
                                'type': 'string'},
                  'initial_value': { 'description': 'Starting activation values, one '
                                                    'per unit. Length must match '
                                                    'input_shapes.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Number of units (size of the '
                                                   'input/output vector). E.g., 3 for '
                                                   'a 3-alternative choice.',
                                    'type': 'integer'},
                  'integrator_mode': { 'default': True,
                                       'description': 'When true (default for LCA), '
                                                      'the mechanism accumulates over '
                                                      'time steps. Set false to use it '
                                                      'as a single-step transfer '
                                                      'mechanism.',
                                       'type': 'boolean'},
                  'leak': { 'default': 0.5,
                            'description': 'Leak rate of the LeakyCompetingIntegrator; '
                                           'scales how much prior activation decays '
                                           'each step. Range [0,1]: 0 = no decay, 1 = '
                                           'full reset each step.',
                            'type': 'number'},
                  'name': {'description': 'Name for the mechanism.', 'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Noise added to the integrator each step.',
                             'type': 'number'},
                  'self_excitation': { 'default': 0,
                                       'description': 'Magnitude of self-feedback '
                                                      '(diagonal of recurrent matrix). '
                                                      'Default 0 means no '
                                                      'self-excitation.',
                                       'type': 'number'},
                  'threshold': { 'description': 'Value at which is_finished becomes '
                                                'True and the mechanism stops '
                                                'accumulating. Set together with '
                                                'threshold_criterion. Omit or set null '
                                                'for no stopping criterion.',
                                 'type': 'number'},
                  'threshold_criterion': { 'default': 'VALUE',
                                           'description': 'How threshold is evaluated. '
                                                          'VALUE: max unit activation '
                                                          '>= threshold. MAX_VS_NEXT: '
                                                          'gap between top two units '
                                                          '>= threshold (requires '
                                                          'input_shapes >= 2). '
                                                          'MAX_VS_AVG: top unit minus '
                                                          'average of others >= '
                                                          'threshold (requires '
                                                          'input_shapes >= 2). '
                                                          'CONVERGENCE: max absolute '
                                                          'change between steps <= '
                                                          'threshold.',
                                           'enum': [ 'VALUE',
                                                     'MAX_VS_NEXT',
                                                     'MAX_VS_AVG',
                                                     'CONVERGENCE'],
                                           'type': 'string'},
                  'time_step_size': { 'default': 0.1,
                                      'description': 'Integration time step for the '
                                                     'LeakyCompetingIntegrator. '
                                                     'Smaller values increase '
                                                     'precision but require more steps '
                                                     'to reach threshold.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "KNOWN PNL BUG (tracked in corpus issue #3): If `threshold_criterion` is set to an unrecognized value, PsyNeuLink's `_parse_threshold_args` raises `AttributeError: 'LCAMechanism' object has no attribute '__name__'` instead of a clean LCAError — this is a bug in the PNL source (`self.__name__` should be `self.__class__.__name__`). The valid enum values above match the PNL constants exactly; only pass one of those four strings. If the error occurs, it means the string did not match a PNL constant, not that the tool schema is wrong.\n\n`competition` and `hetero` are coupled: PNL internally sets `hetero = -competition`. Do not pass both; use `competition` only.\n\n`self_excitation` is an alias for PNL's `auto` parameter. Do not pass both.\n\nIf `matrix` is passed directly (not in this schema), PNL ignores `self_excitation` and `competition` and emits a warning — prefer the high-level parameters.\n\n`MAX_VS_NEXT` and `MAX_VS_AVG` threshold criteria require `input_shapes >= 2`; using them with a single-unit mechanism will raise an error at run time.\n\n`integrator_mode` defaults to `True` for LCAMechanism (unlike base TransferMechanism where it is False) — the mechanism is designed for iterative accumulation."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LCAMechanism
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
    def create_lca_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Leaky Competitive Accumulator (LCA) mechanism — a recurrent transfer mechanism suitable for decision-making, winner-take-all dynamics, and accumulator-race models.'
        return _impl(args or {})
