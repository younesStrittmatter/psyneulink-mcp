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
TOOL_DESCRIPTION = 'Call this tool to instantiate a Leaky Competitive Accumulator (LCA) mechanism — a recurrent transfer mechanism that models lateral inhibition between competing accumulators via LeakyCompetingIntegrator dynamics. Use it when building winner-take-all or soft-competition networks where multiple units accumulate evidence and inhibit each other. Returns a handle to the created LCAMechanism for use in compositions.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "Clipping bounds [min, max] applied to activations after each integration step.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "competition": {\n      "default": 1,\n      "description": "Magnitude of lateral inhibition between units. Sets off-diagonal recurrent weights to -competition. Must be non-negative (negative values invert sign convention and produce excitatory off-diagonal weights with a warning).",\n      "type": "number"\n    },\n    "initial_value": {\n      "description": "Initial activation values for each unit. Length must match input_shapes.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Number of competing units (dimensionality of the input/output vector). Must be >= 2 if using MAX_VS_NEXT or MAX_VS_AVG threshold criteria.",\n      "type": "integer"\n    },\n    "integrator_mode": {\n      "default": true,\n      "description": "Whether to run the LeakyCompetingIntegrator on each execution. Defaults to True for LCAMechanism (unlike base TransferMechanism).",\n      "type": "boolean"\n    },\n    "leak": {\n      "default": 0.5,\n      "description": "Decay rate toward zero on each time step. Scales the contribution of the previous activation value in the LeakyCompetingIntegrator. Higher = faster decay.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Identifier for this mechanism within a composition and in logs.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Noise magnitude added to the integrator on each time step.",\n      "type": "number"\n    },\n    "self_excitation": {\n      "default": 0,\n      "description": "Magnitude of each unit\'s self-recurrent excitation. Sets diagonal recurrent weights. Alias for the \'auto\' parameter \\u2014 do not pass both.",\n      "type": "number"\n    },\n    "threshold": {\n      "description": "Activation (or criterion) value at which is_finished is set True, halting execution. Requires threshold_criterion to specify how to evaluate it. Omit if no stopping criterion is needed.",\n      "type": "number"\n    },\n    "threshold_criterion": {\n      "description": "How to evaluate the threshold. VALUE: stops when any unit exceeds threshold (uses max). MAX_VS_NEXT: stops when the gap between the top two units exceeds threshold. MAX_VS_AVG: stops when the top unit minus mean of the others exceeds threshold. CONVERGENCE: stops when max absolute change between steps falls below threshold. Use the exact PNL constant string \\u2014 see notes for known issue with string values.",\n      "enum": [\n        "VALUE",\n        "MAX_VS_NEXT",\n        "MAX_VS_AVG",\n        "CONVERGENCE"\n      ],\n      "type": "string"\n    },\n    "time_step_size": {\n      "default": 0.1,\n      "description": "Integration time step for the LeakyCompetingIntegrator. Smaller values give more precise integration but require more steps.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nKNOWN BUG (from recent feedback): passing threshold_criterion=\'MAX_VS_NEXT\' raised `AttributeError: \'LCAMechanism\' object has no attribute \'__name__\'`. This is a compound issue: (1) the string \'MAX_VS_NEXT\' did not match the PNL constant MAX_VS_NEXT (the constant\'s actual string value may differ from its Python identifier — do NOT assume they are equal), causing the else branch to execute; (2) that else branch contains a PNL bug using `self.__name__` instead of `self.__class__.__name__`, which crashes with AttributeError rather than a descriptive LCAError. Until the exact string values of the PNL threshold constants are confirmed, prefer threshold_criterion=\'VALUE\' (most likely to work as \'value\' lowercase — test carefully) or omit threshold_criterion entirely. If threshold_criterion fails, the error will be an opaque AttributeError rather than a clear validation message.\n\nAdditional caveats:\n- If \'matrix\' is passed directly, both \'self_excitation\' and \'competition\' are silently ignored (warning only).\n- competition must be positive; negative values are accepted with a warning but invert the sign convention so off-diagonal weights become excitatory.\n- MAX_VS_NEXT and MAX_VS_AVG threshold criteria require input_shapes >= 2.\n- integrator_mode=True is the default (unlike RecurrentTransferMechanism base class).\n- The recurrent weight matrix is auto-constructed: diagonal = self_excitation, off-diagonal = -competition. Do not pass \'matrix\' unless you need a fully custom weight structure.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': 'Clipping bounds [min, max] applied to '
                                           'activations after each integration step.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'competition': { 'default': 1,
                                   'description': 'Magnitude of lateral inhibition '
                                                  'between units. Sets off-diagonal '
                                                  'recurrent weights to -competition. '
                                                  'Must be non-negative (negative '
                                                  'values invert sign convention and '
                                                  'produce excitatory off-diagonal '
                                                  'weights with a warning).',
                                   'type': 'number'},
                  'initial_value': { 'description': 'Initial activation values for '
                                                    'each unit. Length must match '
                                                    'input_shapes.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Number of competing units '
                                                   '(dimensionality of the '
                                                   'input/output vector). Must be >= 2 '
                                                   'if using MAX_VS_NEXT or MAX_VS_AVG '
                                                   'threshold criteria.',
                                    'type': 'integer'},
                  'integrator_mode': { 'default': True,
                                       'description': 'Whether to run the '
                                                      'LeakyCompetingIntegrator on '
                                                      'each execution. Defaults to '
                                                      'True for LCAMechanism (unlike '
                                                      'base TransferMechanism).',
                                       'type': 'boolean'},
                  'leak': { 'default': 0.5,
                            'description': 'Decay rate toward zero on each time step. '
                                           'Scales the contribution of the previous '
                                           'activation value in the '
                                           'LeakyCompetingIntegrator. Higher = faster '
                                           'decay.',
                            'type': 'number'},
                  'name': { 'description': 'Identifier for this mechanism within a '
                                           'composition and in logs.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Noise magnitude added to the integrator '
                                            'on each time step.',
                             'type': 'number'},
                  'self_excitation': { 'default': 0,
                                       'description': "Magnitude of each unit's "
                                                      'self-recurrent excitation. Sets '
                                                      'diagonal recurrent weights. '
                                                      "Alias for the 'auto' parameter "
                                                      '— do not pass both.',
                                       'type': 'number'},
                  'threshold': { 'description': 'Activation (or criterion) value at '
                                                'which is_finished is set True, '
                                                'halting execution. Requires '
                                                'threshold_criterion to specify how to '
                                                'evaluate it. Omit if no stopping '
                                                'criterion is needed.',
                                 'type': 'number'},
                  'threshold_criterion': { 'description': 'How to evaluate the '
                                                          'threshold. VALUE: stops '
                                                          'when any unit exceeds '
                                                          'threshold (uses max). '
                                                          'MAX_VS_NEXT: stops when the '
                                                          'gap between the top two '
                                                          'units exceeds threshold. '
                                                          'MAX_VS_AVG: stops when the '
                                                          'top unit minus mean of the '
                                                          'others exceeds threshold. '
                                                          'CONVERGENCE: stops when max '
                                                          'absolute change between '
                                                          'steps falls below '
                                                          'threshold. Use the exact '
                                                          'PNL constant string — see '
                                                          'notes for known issue with '
                                                          'string values.',
                                           'enum': [ 'VALUE',
                                                     'MAX_VS_NEXT',
                                                     'MAX_VS_AVG',
                                                     'CONVERGENCE'],
                                           'type': 'string'},
                  'time_step_size': { 'default': 0.1,
                                      'description': 'Integration time step for the '
                                                     'LeakyCompetingIntegrator. '
                                                     'Smaller values give more precise '
                                                     'integration but require more '
                                                     'steps.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "KNOWN BUG (from recent feedback): passing threshold_criterion='MAX_VS_NEXT' raised `AttributeError: 'LCAMechanism' object has no attribute '__name__'`. This is a compound issue: (1) the string 'MAX_VS_NEXT' did not match the PNL constant MAX_VS_NEXT (the constant's actual string value may differ from its Python identifier — do NOT assume they are equal), causing the else branch to execute; (2) that else branch contains a PNL bug using `self.__name__` instead of `self.__class__.__name__`, which crashes with AttributeError rather than a descriptive LCAError. Until the exact string values of the PNL threshold constants are confirmed, prefer threshold_criterion='VALUE' (most likely to work as 'value' lowercase — test carefully) or omit threshold_criterion entirely. If threshold_criterion fails, the error will be an opaque AttributeError rather than a clear validation message.\n\nAdditional caveats:\n- If 'matrix' is passed directly, both 'self_excitation' and 'competition' are silently ignored (warning only).\n- competition must be positive; negative values are accepted with a warning but invert the sign convention so off-diagonal weights become excitatory.\n- MAX_VS_NEXT and MAX_VS_AVG threshold criteria require input_shapes >= 2.\n- integrator_mode=True is the default (unlike RecurrentTransferMechanism base class).\n- The recurrent weight matrix is auto-constructed: diagonal = self_excitation, off-diagonal = -competition. Do not pass 'matrix' unless you need a fully custom weight structure."


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
        'Call this tool to instantiate a Leaky Competitive Accumulator (LCA) mechanism — a recurrent transfer mechanism that models lateral inhibition between competing accumulators via LeakyCompetingIntegrator dynamics.'
        return _impl(args or {})
