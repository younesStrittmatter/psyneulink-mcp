"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a7616f78670f80e2f98d0ff7c781e2c3edb417162c1f59e88ef1751bcfc1a04d'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.lcamechanism.LCAMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_lca_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a Leaky Competitive Accumulator (LCA) mechanism — a recurrent neural network component where units inhibit each other and accumulate evidence over time via a leaky integrator. Use it when modeling competitive selection, decision-making, or any process requiring winner-take-all dynamics with sustained accumulation. Returns a PsyNeuLink LCAMechanism instance that can be added to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "Clipping bounds [min, max] applied to the output after each step.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "competition": {\n      "default": 1,\n      "description": "Magnitude of mutual inhibition (off-diagonal terms in the recurrent matrix). Must be positive; PNL internally negates it. Setting this also sets hetero = -competition.",\n      "type": "number"\n    },\n    "initial_value": {\n      "description": "Initial activation values for all units. Length must match input_shapes.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Number of units (input dimensionality). Each unit competes with the others.",\n      "type": "integer"\n    },\n    "integrator_mode": {\n      "default": true,\n      "description": "When True (default for LCA), activations are accumulated via LeakyCompetingIntegrator. Set False to run in transfer-only mode without integration.",\n      "type": "boolean"\n    },\n    "leak": {\n      "default": 0.5,\n      "description": "Leak rate for the LeakyCompetingIntegrator. Scales how much the previous value persists each step. Higher values = more forgetting.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Name for the mechanism instance.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Noise added at each integration step.",\n      "type": "number"\n    },\n    "output_ports": {\n      "description": "Output ports to expose. LCA adds MAX_VS_NEXT and MAX_VS_AVG to the standard RecurrentTransferMechanism ports.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "self_excitation": {\n      "default": 0,\n      "description": "Magnitude of self-excitation (diagonal terms in the recurrent matrix). Alias for the \'auto\' parameter.",\n      "type": "number"\n    },\n    "threshold": {\n      "description": "Value at which the mechanism\'s is_finished flag is set True, terminating execution. Requires at least 2 units if threshold_criterion is MAX_VS_NEXT or MAX_VS_AVG.",\n      "type": "number"\n    },\n    "threshold_criterion": {\n      "description": "Criterion evaluated against threshold. VALUE: max unit value; MAX_VS_NEXT: gap between top two units; MAX_VS_AVG: top unit minus average of others; CONVERGENCE: change between steps (uses LESS_THAN_OR_EQUAL comparison).",\n      "enum": [\n        "VALUE",\n        "MAX_VS_NEXT",\n        "MAX_VS_AVG",\n        "CONVERGENCE"\n      ],\n      "type": "string"\n    },\n    "time_step_size": {\n      "default": 0.1,\n      "description": "Integration time step for the LeakyCompetingIntegrator. Smaller values give finer temporal resolution but require more steps.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nKNOWN PNL BUG (upstream, unfixed as of v0.18.0): Passing an unrecognized string to threshold_criterion triggers `AttributeError: \'LCAMechanism\' object has no attribute \'__name__\'` (PNL uses self.__name__ instead of self.__class__.__name__ in the error branch). Confirmed via feedback to also affect the string "MAX_VS_NEXT" — this string may not match the PNL constant MAX_VS_NEXT depending on how the constant is imported. Safe workaround: omit threshold_criterion and use the default (equivalent to "VALUE"), or test carefully before passing it. Do NOT pass threshold_criterion unless you have verified the exact string value expected by your installed PNL version.\n\ncompetition and hetero are mutually constrained: hetero = -competition. Pass only competition; do not pass hetero directly.\n\nIf matrix is passed as a kwarg, self_excitation and competition are silently ignored and the supplied matrix is used instead.\n\nintegrator_mode defaults to True for LCAMechanism (unlike base RecurrentTransferMechanism where it defaults to False).\n\ninput_shapes must be >= 2 when threshold_criterion is MAX_VS_NEXT or MAX_VS_AVG.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': 'Clipping bounds [min, max] applied to the '
                                           'output after each step.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'competition': { 'default': 1,
                                   'description': 'Magnitude of mutual inhibition '
                                                  '(off-diagonal terms in the '
                                                  'recurrent matrix). Must be '
                                                  'positive; PNL internally negates '
                                                  'it. Setting this also sets hetero = '
                                                  '-competition.',
                                   'type': 'number'},
                  'initial_value': { 'description': 'Initial activation values for all '
                                                    'units. Length must match '
                                                    'input_shapes.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Number of units (input '
                                                   'dimensionality). Each unit '
                                                   'competes with the others.',
                                    'type': 'integer'},
                  'integrator_mode': { 'default': True,
                                       'description': 'When True (default for LCA), '
                                                      'activations are accumulated via '
                                                      'LeakyCompetingIntegrator. Set '
                                                      'False to run in transfer-only '
                                                      'mode without integration.',
                                       'type': 'boolean'},
                  'leak': { 'default': 0.5,
                            'description': 'Leak rate for the '
                                           'LeakyCompetingIntegrator. Scales how much '
                                           'the previous value persists each step. '
                                           'Higher values = more forgetting.',
                            'type': 'number'},
                  'name': { 'description': 'Name for the mechanism instance.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Noise added at each integration step.',
                             'type': 'number'},
                  'output_ports': { 'description': 'Output ports to expose. LCA adds '
                                                   'MAX_VS_NEXT and MAX_VS_AVG to the '
                                                   'standard '
                                                   'RecurrentTransferMechanism ports.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'self_excitation': { 'default': 0,
                                       'description': 'Magnitude of self-excitation '
                                                      '(diagonal terms in the '
                                                      'recurrent matrix). Alias for '
                                                      "the 'auto' parameter.",
                                       'type': 'number'},
                  'threshold': { 'description': "Value at which the mechanism's "
                                                'is_finished flag is set True, '
                                                'terminating execution. Requires at '
                                                'least 2 units if threshold_criterion '
                                                'is MAX_VS_NEXT or MAX_VS_AVG.',
                                 'type': 'number'},
                  'threshold_criterion': { 'description': 'Criterion evaluated against '
                                                          'threshold. VALUE: max unit '
                                                          'value; MAX_VS_NEXT: gap '
                                                          'between top two units; '
                                                          'MAX_VS_AVG: top unit minus '
                                                          'average of others; '
                                                          'CONVERGENCE: change between '
                                                          'steps (uses '
                                                          'LESS_THAN_OR_EQUAL '
                                                          'comparison).',
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
                                                     'more steps.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'KNOWN PNL BUG (upstream, unfixed as of v0.18.0): Passing an unrecognized string to threshold_criterion triggers `AttributeError: \'LCAMechanism\' object has no attribute \'__name__\'` (PNL uses self.__name__ instead of self.__class__.__name__ in the error branch). Confirmed via feedback to also affect the string "MAX_VS_NEXT" — this string may not match the PNL constant MAX_VS_NEXT depending on how the constant is imported. Safe workaround: omit threshold_criterion and use the default (equivalent to "VALUE"), or test carefully before passing it. Do NOT pass threshold_criterion unless you have verified the exact string value expected by your installed PNL version.\n\ncompetition and hetero are mutually constrained: hetero = -competition. Pass only competition; do not pass hetero directly.\n\nIf matrix is passed as a kwarg, self_excitation and competition are silently ignored and the supplied matrix is used instead.\n\nintegrator_mode defaults to True for LCAMechanism (unlike base RecurrentTransferMechanism where it defaults to False).\n\ninput_shapes must be >= 2 when threshold_criterion is MAX_VS_NEXT or MAX_VS_AVG.'


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
        'Call this tool to create a Leaky Competitive Accumulator (LCA) mechanism — a recurrent neural network component where units inhibit each other and accumulate evidence over time via a leaky integrator.'
        return _impl(args or {})
