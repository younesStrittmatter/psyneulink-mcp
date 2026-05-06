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
TOOL_DESCRIPTION = 'Call this tool to create a Leaky Competitive Accumulator (LCA) mechanism — use it when modeling competitive selection, winner-take-all dynamics, or evidence accumulation with lateral inhibition between units. Returns an LCAMechanism instance that must be added to a Composition before running. The mechanism integrates inputs over time with configurable mutual inhibition, self-excitation, and leak, and can terminate automatically when a threshold criterion is met.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "[min, max] range to clip activations after each integration step.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "competition": {\n      "default": 1,\n      "description": "Magnitude of mutual inhibition between units (off-diagonal recurrent weights). Must be a positive number \\u2014 PNL internally negates it to inhibit competitors.",\n      "type": "number"\n    },\n    "initial_value": {\n      "description": "Starting activation value for all units at the beginning of integration.",\n      "type": "number"\n    },\n    "input_shapes": {\n      "description": "Number of units (input dimensionality). Must be >= 2 when threshold_criterion is \'max_vs_next\' or \'max_vs_avg\'.",\n      "type": "integer"\n    },\n    "leak": {\n      "default": 0.5,\n      "description": "Decay rate in the LeakyCompetingIntegrator. Higher values cause faster decay of activation.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Name for the mechanism.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Noise added to integration on each time step.",\n      "type": "number"\n    },\n    "self_excitation": {\n      "default": 0,\n      "description": "Magnitude of self-recurrent excitation for each unit (diagonal recurrent weights).",\n      "type": "number"\n    },\n    "threshold": {\n      "description": "Activation level at which is_finished is set to True, stopping integration. Used together with threshold_criterion.",\n      "type": "number"\n    },\n    "threshold_criterion": {\n      "description": "Criterion used to evaluate whether threshold is reached. \'value\': max activation >= threshold. \'max_vs_next\': difference between top two units >= threshold (requires input_shapes >= 2). \'max_vs_avg\': max minus average of others >= threshold (requires input_shapes >= 2). \'convergence\': change between steps <= threshold.",\n      "enum": [\n        "value",\n        "max_vs_next",\n        "max_vs_avg",\n        "convergence"\n      ],\n      "type": "string"\n    },\n    "time_step_size": {\n      "default": 0.1,\n      "description": "Integration time step for the LeakyCompetingIntegrator.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — threshold_criterion bug: passing uppercase strings like "MAX_VS_NEXT" triggers an AttributeError in PNL\'s _parse_threshold_args (\'LCAMechanism\' object has no attribute \'__name__\'). Always use lowercase: "value", "max_vs_next", "max_vs_avg", "convergence". This is a bug in PNL source (uses self.__name__ instead of self.__class__.__name__ in the error branch), triggered when an unrecognized string is passed.\n\ncompetition must be positive; PNL stores it as inhibition magnitude and sets off-diagonal recurrent weights to -competition. Passing a negative competition value is allowed but produces a warning and inverts the expected behavior.\n\nself_excitation is an alias for the internal \'auto\' parameter; do not pass both self_excitation and auto.\n\ncompetition and hetero are inverses (hetero = -competition); specifying both with inconsistent values raises LCAError. Omit hetero and use competition only.\n\nPassing a matrix argument overrides both self_excitation and competition silently (with a warning); do not mix matrix with self_excitation/competition.\n\nthreshold_criterion \'max_vs_next\' and \'max_vs_avg\' require input_shapes >= 2; using them with a single unit raises an error at run time.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': '[min, max] range to clip activations after '
                                           'each integration step.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'competition': { 'default': 1,
                                   'description': 'Magnitude of mutual inhibition '
                                                  'between units (off-diagonal '
                                                  'recurrent weights). Must be a '
                                                  'positive number — PNL internally '
                                                  'negates it to inhibit competitors.',
                                   'type': 'number'},
                  'initial_value': { 'description': 'Starting activation value for all '
                                                    'units at the beginning of '
                                                    'integration.',
                                     'type': 'number'},
                  'input_shapes': { 'description': 'Number of units (input '
                                                   'dimensionality). Must be >= 2 when '
                                                   'threshold_criterion is '
                                                   "'max_vs_next' or 'max_vs_avg'.",
                                    'type': 'integer'},
                  'leak': { 'default': 0.5,
                            'description': 'Decay rate in the '
                                           'LeakyCompetingIntegrator. Higher values '
                                           'cause faster decay of activation.',
                            'type': 'number'},
                  'name': {'description': 'Name for the mechanism.', 'type': 'string'},
                  'noise': { 'description': 'Noise added to integration on each time '
                                            'step.',
                             'type': 'number'},
                  'self_excitation': { 'default': 0,
                                       'description': 'Magnitude of self-recurrent '
                                                      'excitation for each unit '
                                                      '(diagonal recurrent weights).',
                                       'type': 'number'},
                  'threshold': { 'description': 'Activation level at which is_finished '
                                                'is set to True, stopping integration. '
                                                'Used together with '
                                                'threshold_criterion.',
                                 'type': 'number'},
                  'threshold_criterion': { 'description': 'Criterion used to evaluate '
                                                          'whether threshold is '
                                                          "reached. 'value': max "
                                                          'activation >= threshold. '
                                                          "'max_vs_next': difference "
                                                          'between top two units >= '
                                                          'threshold (requires '
                                                          'input_shapes >= 2). '
                                                          "'max_vs_avg': max minus "
                                                          'average of others >= '
                                                          'threshold (requires '
                                                          'input_shapes >= 2). '
                                                          "'convergence': change "
                                                          'between steps <= threshold.',
                                           'enum': [ 'value',
                                                     'max_vs_next',
                                                     'max_vs_avg',
                                                     'convergence'],
                                           'type': 'string'},
                  'time_step_size': { 'default': 0.1,
                                      'description': 'Integration time step for the '
                                                     'LeakyCompetingIntegrator.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL — threshold_criterion bug: passing uppercase strings like "MAX_VS_NEXT" triggers an AttributeError in PNL\'s _parse_threshold_args (\'LCAMechanism\' object has no attribute \'__name__\'). Always use lowercase: "value", "max_vs_next", "max_vs_avg", "convergence". This is a bug in PNL source (uses self.__name__ instead of self.__class__.__name__ in the error branch), triggered when an unrecognized string is passed.\n\ncompetition must be positive; PNL stores it as inhibition magnitude and sets off-diagonal recurrent weights to -competition. Passing a negative competition value is allowed but produces a warning and inverts the expected behavior.\n\nself_excitation is an alias for the internal \'auto\' parameter; do not pass both self_excitation and auto.\n\ncompetition and hetero are inverses (hetero = -competition); specifying both with inconsistent values raises LCAError. Omit hetero and use competition only.\n\nPassing a matrix argument overrides both self_excitation and competition silently (with a warning); do not mix matrix with self_excitation/competition.\n\nthreshold_criterion \'max_vs_next\' and \'max_vs_avg\' require input_shapes >= 2; using them with a single unit raises an error at run time.'


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
        'Call this tool to create a Leaky Competitive Accumulator (LCA) mechanism — use it when modeling competitive selection, winner-take-all dynamics, or evidence accumulation with lateral inhibition between units.'
        return _impl(args or {})
