"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ebe64c85e51b68a589479e72b66c9ae55b7b24730b47a384e3dba712b8eba1d6'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.processing.integratormechanism.IntegratorMechanism'
__pnl_kind__ = 'class'
__pnl_parents__ = ['ProcessingMechanism_Base',
 'Mechanism_Base',
 'Mechanism',
 'ShellClass',
 'Component',
 'MDFSerializable']
__pnl_parent_sha256s__ = {'Component': 'b878afca9fca90ac1a952605ca8d39a37f25ebebf1411a7f545b9c48a3eaeec3',
 'MDFSerializable': 'caad6059e8ef158be1269a23127f13da3733824c3585f9b4d6e3a63de82f65da',
 'Mechanism': 'ed9f10960d87126524669ea7084cb8128621de90ddb7306c8c9bde15f524d28d',
 'Mechanism_Base': '91d72ef88b0cb638b5895df2f04ed7f449ce951198c10e44c22558b699e8bf21',
 'ProcessingMechanism_Base': '471c65452d591ff8e0270afdeb8e535a0f97b3b23673c7bc21e9c32a6524cf80',
 'ShellClass': 'adc23754ebeb0c55bdde1324622b33a509116703503508ee7e7de181a8afeee6'}
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_integrator_mechanism'
TOOL_DESCRIPTION = 'Create a PsyNeuLink IntegratorMechanism — a ProcessingMechanism specialized for accumulating input over time via an IntegratorFunction (default AdaptiveIntegrator(rate=0.5)). Use this when you need a Composition node whose value evolves stepwise (leaky/adaptive accumulation, drift-diffusion, FitzHugh-Nagumo, Ornstein-Uhlenbeck, etc.). Adds, beyond Mechanism/ProcessingMechanism: a `reset_default` knob that triggers `reset()` whenever the runtime `reset` parameter is non-zero, restoring the function\'s initial value. Returns a handle to register as a node in a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input shape. Use a 1d list (e.g. [0, 0, 0]) for a single input port of width N, or a 2d list for multi-port. Must match the function\'s expected input width \\u2014 if the function was created with an explicit dimension, this must agree.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "number"\n              },\n              {\n                "items": {\n                  "type": "number"\n                },\n                "type": "array"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "function": {\n      "description": "Handle of an IntegratorFunction created by a function-creation tool (e.g. AdaptiveIntegrator, DriftDiffusionIntegrator, OrnsteinUhlenbeckIntegrator, FitzHughNagumoIntegrator, DriftOnASphereIntegrator). Must accept a scalar/1d input and return a value of the same form. If omitted, AdaptiveIntegrator(rate=0.5) is used.",\n      "type": "string"\n    },\n    "input_ports": {\n      "description": "Input port spec \\u2014 list of names/specs or a dict. Omit for a single default input port.",\n      "oneOf": [\n        {\n          "items": {},\n          "type": "array"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    },\n    "input_shapes": {\n      "description": "Alternative to default_variable: integer or list of integers giving input width(s). Sets the mechanism\'s variable to zeros of that shape.",\n      "oneOf": [\n        {\n          "minimum": 1,\n          "type": "integer"\n        },\n        {\n          "items": {\n            "minimum": 1,\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Identifier for the mechanism within a Composition.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Output port spec \\u2014 name string, list of names/specs.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {},\n          "type": "array"\n        }\n      ]\n    },\n    "params": {\n      "description": "Optional dict of parameter overrides (rarely needed; prefer named arguments).",\n      "type": "object"\n    },\n    "prefs": {\n      "description": "PreferenceSet overrides; usually omit.",\n      "type": "object"\n    },\n    "reset_default": {\n      "description": "Default for the runtime `reset` parameter. When `reset` is set non-zero during a run, the mechanism resets its value to the function\'s initializer. Leave at 0 unless you intend to drive resets.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "number"\n              },\n              {\n                "items": {\n                  "type": "number"\n                },\n                "type": "array"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "name"\n  ],\n  "type": "object"\n}\n\nNotes:\nShape rules for `function`: the mechanism\'s input width must match the function\'s input variable width. If you pass an instantiated function with a multi-element variable (e.g. width N>1) and either no `default_variable` or a length-1 default, the mechanism reshapes itself to N — but if you pass a length>1 `default_variable` that disagrees with the function\'s variable, you get IntegratorMechanismError "Shape of \'variable\' ... does not match ... \'default_variable\'".\n\nKnown broken case (verified, reported in feedback): `DriftOnASphereIntegrator` is asymmetric — input variable shape is (dimension-1,) while output value shape is (dimension,). Wrapping it in an IntegratorMechanism currently fails at function-instantiation time with `ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0 ... (size 1 is different from N)` regardless of how you spec `default_variable` / `input_shapes` (tried length-1, length-N, length-(N-1), and unspecified). The default input_port is built from the function\'s input variable but downstream projections expect output-shape, and there is no working spec on this tool today. Track upstream PNL fix; do not retry the same shape variants.\n\n`reset` is a *runtime* parameter, not an init kwarg — set `reset_default` here to seed it; toggle the actual reset by sending non-zero on the `reset` parameter port during execution.\n\nThe first positional-style argument in PNL examples is `name`; everything else is keyword. The tool layer passes all kwargs by name, so order doesn\'t matter.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input shape. '
                                                       'Use a 1d list (e.g. [0, 0, 0]) '
                                                       'for a single input port of '
                                                       'width N, or a 2d list for '
                                                       'multi-port. Must match the '
                                                       "function's expected input "
                                                       'width — if the function was '
                                                       'created with an explicit '
                                                       'dimension, this must agree.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': { 'oneOf': [ { 'type': 'number'},
                                                                           { 'items': { 'type': 'number'},
                                                                             'type': 'array'}]},
                                                     'type': 'array'}]},
                  'function': { 'description': 'Handle of an IntegratorFunction '
                                               'created by a function-creation tool '
                                               '(e.g. AdaptiveIntegrator, '
                                               'DriftDiffusionIntegrator, '
                                               'OrnsteinUhlenbeckIntegrator, '
                                               'FitzHughNagumoIntegrator, '
                                               'DriftOnASphereIntegrator). Must accept '
                                               'a scalar/1d input and return a value '
                                               'of the same form. If omitted, '
                                               'AdaptiveIntegrator(rate=0.5) is used.',
                                'type': 'string'},
                  'input_ports': { 'description': 'Input port spec — list of '
                                                  'names/specs or a dict. Omit for a '
                                                  'single default input port.',
                                   'oneOf': [ {'items': {}, 'type': 'array'},
                                              {'type': 'object'}]},
                  'input_shapes': { 'description': 'Alternative to default_variable: '
                                                   'integer or list of integers giving '
                                                   'input width(s). Sets the '
                                                   "mechanism's variable to zeros of "
                                                   'that shape.',
                                    'oneOf': [ {'minimum': 1, 'type': 'integer'},
                                               { 'items': { 'minimum': 1,
                                                            'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Identifier for the mechanism within a '
                                           'Composition.',
                            'type': 'string'},
                  'output_ports': { 'description': 'Output port spec — name string, '
                                                   'list of names/specs.',
                                    'oneOf': [ {'type': 'string'},
                                               {'items': {}, 'type': 'array'}]},
                  'params': { 'description': 'Optional dict of parameter overrides '
                                             '(rarely needed; prefer named arguments).',
                              'type': 'object'},
                  'prefs': { 'description': 'PreferenceSet overrides; usually omit.',
                             'type': 'object'},
                  'reset_default': { 'description': 'Default for the runtime `reset` '
                                                    'parameter. When `reset` is set '
                                                    'non-zero during a run, the '
                                                    'mechanism resets its value to the '
                                                    "function's initializer. Leave at "
                                                    '0 unless you intend to drive '
                                                    'resets.',
                                     'oneOf': [ {'type': 'number'},
                                                { 'items': { 'oneOf': [ { 'type': 'number'},
                                                                        { 'items': { 'type': 'number'},
                                                                          'type': 'array'}]},
                                                  'type': 'array'}]}},
  'required': ['name'],
  'type': 'object'}
TOOL_NOTES = 'Shape rules for `function`: the mechanism\'s input width must match the function\'s input variable width. If you pass an instantiated function with a multi-element variable (e.g. width N>1) and either no `default_variable` or a length-1 default, the mechanism reshapes itself to N — but if you pass a length>1 `default_variable` that disagrees with the function\'s variable, you get IntegratorMechanismError "Shape of \'variable\' ... does not match ... \'default_variable\'".\n\nKnown broken case (verified, reported in feedback): `DriftOnASphereIntegrator` is asymmetric — input variable shape is (dimension-1,) while output value shape is (dimension,). Wrapping it in an IntegratorMechanism currently fails at function-instantiation time with `ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0 ... (size 1 is different from N)` regardless of how you spec `default_variable` / `input_shapes` (tried length-1, length-N, length-(N-1), and unspecified). The default input_port is built from the function\'s input variable but downstream projections expect output-shape, and there is no working spec on this tool today. Track upstream PNL fix; do not retry the same shape variants.\n\n`reset` is a *runtime* parameter, not an init kwarg — set `reset_default` here to seed it; toggle the actual reset by sending non-zero on the `reset` parameter port during execution.\n\nThe first positional-style argument in PNL examples is `name`; everything else is keyword. The tool layer passes all kwargs by name, so order doesn\'t matter.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.IntegratorMechanism
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
    def create_integrator_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Create a PsyNeuLink IntegratorMechanism — a ProcessingMechanism specialized for accumulating input over time via an IntegratorFunction (default AdaptiveIntegrator(rate=0.5)).'
        return _impl(args or {})
