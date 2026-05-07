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
TOOL_DESCRIPTION = 'Create an IntegratorMechanism — a ProcessingMechanism that, on each execution, applies an IntegratorFunction (e.g. AdaptiveIntegrator, DriftDiffusionIntegrator, DriftOnASphereIntegrator, AccumulatorIntegrator, OrnsteinUhlenbeckIntegrator) to its input and accumulates state across calls. Use it when you need a node that *remembers* across timesteps — leaky integration, evidence accumulation, drift-diffusion, or any path-dependent processing — rather than a stateless transform. Returns a Mechanism handle suitable for placement in a Composition; the integrator\'s running state lives on the mechanism and is reset via the `reset` parameter (non-zero → reset to initial value before computing output).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Default input shape as a 1d list of numbers (or nested list for multi-port input). Its length MUST be compatible with the chosen function\'s expected variable shape \\u2014 see notes for DriftOnASphereIntegrator and other shape-sensitive integrators.",\n      "items": {},\n      "type": "array"\n    },\n    "function": {\n      "description": "An IntegratorFunction handle produced by the corresponding create_* tool (e.g. an AdaptiveIntegrator, DriftDiffusionIntegrator, LeakyCompetingIntegrator, DriftOnASphereIntegrator, AccumulatorIntegrator, OrnsteinUhlenbeckIntegrator handle). MUST be a function handle, not a string name. Defaults to AdaptiveIntegrator(rate=0.5) if omitted.",\n      "type": "string"\n    },\n    "input_ports": {\n      "description": "Optional list/dict specifying input ports (names or full specs). Most uses don\'t need this.",\n      "oneOf": [\n        {\n          "items": {},\n          "type": "array"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    },\n    "input_shapes": {\n      "description": "Alternative to default_variable: an integer (or list of ints for multiple input_ports) giving the size of each input port. Use this when you only know the dimensionality, not concrete default values.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the mechanism (used in logs and Composition graphs).",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Optional output port specification (name or iterable of names/specs).",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {},\n          "type": "array"\n        }\n      ]\n    },\n    "params": {\n      "description": "Optional dict of additional parameter overrides forwarded to the underlying constructor.",\n      "type": "object"\n    },\n    "reset_default": {\n      "default": 0,\n      "description": "Default value of the `reset` parameter. If non-zero at execution time, the mechanism resets its `value` to the function\'s initializer before computing output. Number, list, or 1d array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDIMENSIONAL CONTRACT (this is the single most common failure mode, and is what recent feedback flagged): the IntegratorMechanism\'s `default_variable` length must match the variable shape that its `function` expects, otherwise PNL raises a numpy matmul / shape error during construction (not at runtime). Specific gotchas:\n\n- DriftOnASphereIntegrator embeds an N-sphere in N+1-D space: if the function has `dimension=D`, it expects a variable of length D-1. So a 24-dim drift on a sphere requires `dimension=25` on the function AND `default_variable` of length 24, OR omit `default_variable` and let the function\'s variable propagate. Passing `default_variable=[0]*24` with a DriftOnASphereIntegrator whose `dimension` was not set to 25 produces "matmul: size 1 is different from 24" because B is (25,24) and noise is scalar/length-1.\n- AdaptiveIntegrator, DriftDiffusionIntegrator, LeakyCompetingIntegrator, OrnsteinUhlenbeckIntegrator, AccumulatorIntegrator: variable length = output length; just keep `default_variable` and the function\'s `initializer`/`default_variable` consistent.\n\nOTHER:\n- `function` must be a function HANDLE returned by the matching create_* IntegratorFunction tool, not a class name string. Passing a stale handle string (e.g. from an older session) will fail to resolve.\n- `reset` is a Parameter with `constructor_argument=\'reset_default\'` — agents must use the kwarg name `reset_default` here; `reset` itself is read at execution time, not at construction.\n- The `reset` mechanic only triggers when `reset` evaluates non-zero AND the mechanism is not in initialization; it then resets `value` to the function\'s initializer and reshapes back to the prior output shape.\n- Inherits all standard Mechanism kwargs (input_ports, output_ports, params, name, prefs) — see the Mechanism / ProcessingMechanism tools for those semantics.\n- This is a stateful node: placing the same handle in two Compositions shares state across them; create separate mechanisms for independent runs.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Default input shape as a 1d '
                                                       'list of numbers (or nested '
                                                       'list for multi-port input). '
                                                       'Its length MUST be compatible '
                                                       "with the chosen function's "
                                                       'expected variable shape — see '
                                                       'notes for '
                                                       'DriftOnASphereIntegrator and '
                                                       'other shape-sensitive '
                                                       'integrators.',
                                        'items': {},
                                        'type': 'array'},
                  'function': { 'description': 'An IntegratorFunction handle produced '
                                               'by the corresponding create_* tool '
                                               '(e.g. an AdaptiveIntegrator, '
                                               'DriftDiffusionIntegrator, '
                                               'LeakyCompetingIntegrator, '
                                               'DriftOnASphereIntegrator, '
                                               'AccumulatorIntegrator, '
                                               'OrnsteinUhlenbeckIntegrator handle). '
                                               'MUST be a function handle, not a '
                                               'string name. Defaults to '
                                               'AdaptiveIntegrator(rate=0.5) if '
                                               'omitted.',
                                'type': 'string'},
                  'input_ports': { 'description': 'Optional list/dict specifying input '
                                                  'ports (names or full specs). Most '
                                                  "uses don't need this.",
                                   'oneOf': [ {'items': {}, 'type': 'array'},
                                              {'type': 'object'}]},
                  'input_shapes': { 'description': 'Alternative to default_variable: '
                                                   'an integer (or list of ints for '
                                                   'multiple input_ports) giving the '
                                                   'size of each input port. Use this '
                                                   'when you only know the '
                                                   'dimensionality, not concrete '
                                                   'default values.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Optional name for the mechanism (used in '
                                           'logs and Composition graphs).',
                            'type': 'string'},
                  'output_ports': { 'description': 'Optional output port specification '
                                                   '(name or iterable of names/specs).',
                                    'oneOf': [ {'type': 'string'},
                                               {'items': {}, 'type': 'array'}]},
                  'params': { 'description': 'Optional dict of additional parameter '
                                             'overrides forwarded to the underlying '
                                             'constructor.',
                              'type': 'object'},
                  'reset_default': { 'default': 0,
                                     'description': 'Default value of the `reset` '
                                                    'parameter. If non-zero at '
                                                    'execution time, the mechanism '
                                                    'resets its `value` to the '
                                                    "function's initializer before "
                                                    'computing output. Number, list, '
                                                    'or 1d array.',
                                     'oneOf': [ {'type': 'number'},
                                                { 'items': {'type': 'number'},
                                                  'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'DIMENSIONAL CONTRACT (this is the single most common failure mode, and is what recent feedback flagged): the IntegratorMechanism\'s `default_variable` length must match the variable shape that its `function` expects, otherwise PNL raises a numpy matmul / shape error during construction (not at runtime). Specific gotchas:\n\n- DriftOnASphereIntegrator embeds an N-sphere in N+1-D space: if the function has `dimension=D`, it expects a variable of length D-1. So a 24-dim drift on a sphere requires `dimension=25` on the function AND `default_variable` of length 24, OR omit `default_variable` and let the function\'s variable propagate. Passing `default_variable=[0]*24` with a DriftOnASphereIntegrator whose `dimension` was not set to 25 produces "matmul: size 1 is different from 24" because B is (25,24) and noise is scalar/length-1.\n- AdaptiveIntegrator, DriftDiffusionIntegrator, LeakyCompetingIntegrator, OrnsteinUhlenbeckIntegrator, AccumulatorIntegrator: variable length = output length; just keep `default_variable` and the function\'s `initializer`/`default_variable` consistent.\n\nOTHER:\n- `function` must be a function HANDLE returned by the matching create_* IntegratorFunction tool, not a class name string. Passing a stale handle string (e.g. from an older session) will fail to resolve.\n- `reset` is a Parameter with `constructor_argument=\'reset_default\'` — agents must use the kwarg name `reset_default` here; `reset` itself is read at execution time, not at construction.\n- The `reset` mechanic only triggers when `reset` evaluates non-zero AND the mechanism is not in initialization; it then resets `value` to the function\'s initializer and reshapes back to the prior output shape.\n- Inherits all standard Mechanism kwargs (input_ports, output_ports, params, name, prefs) — see the Mechanism / ProcessingMechanism tools for those semantics.\n- This is a stateful node: placing the same handle in two Compositions shares state across them; create separate mechanisms for independent runs.'


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
        'Create an IntegratorMechanism — a ProcessingMechanism that, on each execution, applies an IntegratorFunction (e.g.'
        return _impl(args or {})
