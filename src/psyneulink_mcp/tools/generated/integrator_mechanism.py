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
TOOL_DESCRIPTION = 'Creates a PsyNeuLink IntegratorMechanism — a ProcessingMechanism whose `function` is an IntegratorFunction (default `AdaptiveIntegrator(rate=0.5)`), so its output accumulates / decays across executions instead of being a pure function of the current input. Beyond ProcessingMechanism it adds (1) a `reset_default` / `reset` parameter that, when truthy at execute time, resets the function\'s stateful value to its initializer, and (2) auto-reshaping of the Mechanism\'s variable to match the inner dimensionality of an instantiated function (so a function with a length-N initializer drives an N-wide port even if `default_variable` is left at default). Returns a handle id usable as a node in a Composition; for argument and port semantics inherited from ProcessingMechanism / Mechanism / Component, drill into those parent tools.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Default input template. Sets the input shape; usually a 1-D list/array. If you also pass an instantiated `function`, you can leave this unset and the Mechanism will adopt the function\'s variable shape \\u2014 but if you set both and the inner lengths conflict (and neither is 1), construction raises IntegratorMechanismError.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "array"\n        }\n      ]\n    },\n    "function": {\n      "description": "Handle id of a previously created IntegratorFunction (e.g. AdaptiveIntegrator, SimpleIntegrator, LeakyCompetingIntegrator, FitzHughNagumoIntegrator, AccumulatorIntegrator, OrnsteinUhlenbeckIntegrator). Must take a single numeric value (or list/array) and return the same form. Defaults to `AdaptiveIntegrator(rate=0.5)` if omitted. NOTE: do not pass DriftOnASphereIntegrator here \\u2014 its variable shape is (dimension-1,) but its output shape is (dimension,), and the IntegratorMechanism\'s port wiring assumes input and output share a shape, which causes a `matmul: size 1 is different from N` ValueError at construction regardless of `default_variable`. Use a Cartesian-shaped IntegratorFunction instead.",\n      "type": "string"\n    },\n    "input_ports": {\n      "description": "Optional InputPort spec \\u2014 list of names/specs or a dict. Use the default unless you need to rename or shape ports explicitly.",\n      "oneOf": [\n        {\n          "type": "array"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    },\n    "input_shapes": {\n      "description": "Alternative to `default_variable`: integer or list of integers giving the size of each InputPort. Pass either this or `default_variable`, not both.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Identifier for this Mechanism instance (used by Composition wiring and logs).",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Optional OutputPort spec \\u2014 string name or iterable of port specs.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "type": "array"\n        }\n      ]\n    },\n    "params": {\n      "description": "Optional dict of parameter overrides; rarely needed \\u2014 prefer named arguments.",\n      "type": "object"\n    },\n    "prefs": {\n      "description": "Optional PreferenceSet override; rarely needed.",\n      "type": "object"\n    },\n    "reset_default": {\n      "description": "Default value of the `reset` Parameter (number, list, or 1-D array; default 0). At execute time, if the current `reset` value is non-zero/non-empty the function\'s stateful value is reset to its initializer before returning. Leave at 0 unless you intend control-driven resets.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nStateful: same instance produces different outputs across executions because the wrapped IntegratorFunction carries hidden state — never share one handle between Compositions you intend to run independently. The Mechanism reshapes its variable to match an instantiated `function`\'s inner dimension when its own `default_variable` was not user-specified, but if both are user-specified and inner lengths differ (and neither is 1) construction raises IntegratorMechanismError — set `default_variable` to match the function\'s variable shape, not 1-wider/narrower. The `reset` Parameter is checked every execute; setting `reset_default` to non-zero will fire a reset on the first non-initialization execute. DriftOnASphereIntegrator is currently incompatible as the `function` argument because of an input/output shape asymmetry (variable is (dimension-1,), value is (dimension,)) that the Mechanism\'s default port wiring does not handle — this fails at construction with a numpy matmul dimension-mismatch error and cannot be worked around via `default_variable` (1-D, 2-D, or omitted all fail the same way). For `Composition`-level usage and how this handle is wired into pathways, see the Composition tool.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Default input template. Sets '
                                                       'the input shape; usually a 1-D '
                                                       'list/array. If you also pass '
                                                       'an instantiated `function`, '
                                                       'you can leave this unset and '
                                                       'the Mechanism will adopt the '
                                                       "function's variable shape — "
                                                       'but if you set both and the '
                                                       'inner lengths conflict (and '
                                                       'neither is 1), construction '
                                                       'raises '
                                                       'IntegratorMechanismError.',
                                        'oneOf': [ {'type': 'number'},
                                                   {'type': 'array'}]},
                  'function': { 'description': 'Handle id of a previously created '
                                               'IntegratorFunction (e.g. '
                                               'AdaptiveIntegrator, SimpleIntegrator, '
                                               'LeakyCompetingIntegrator, '
                                               'FitzHughNagumoIntegrator, '
                                               'AccumulatorIntegrator, '
                                               'OrnsteinUhlenbeckIntegrator). Must '
                                               'take a single numeric value (or '
                                               'list/array) and return the same form. '
                                               'Defaults to '
                                               '`AdaptiveIntegrator(rate=0.5)` if '
                                               'omitted. NOTE: do not pass '
                                               'DriftOnASphereIntegrator here — its '
                                               'variable shape is (dimension-1,) but '
                                               'its output shape is (dimension,), and '
                                               "the IntegratorMechanism's port wiring "
                                               'assumes input and output share a '
                                               'shape, which causes a `matmul: size 1 '
                                               'is different from N` ValueError at '
                                               'construction regardless of '
                                               '`default_variable`. Use a '
                                               'Cartesian-shaped IntegratorFunction '
                                               'instead.',
                                'type': 'string'},
                  'input_ports': { 'description': 'Optional InputPort spec — list of '
                                                  'names/specs or a dict. Use the '
                                                  'default unless you need to rename '
                                                  'or shape ports explicitly.',
                                   'oneOf': [{'type': 'array'}, {'type': 'object'}]},
                  'input_shapes': { 'description': 'Alternative to `default_variable`: '
                                                   'integer or list of integers giving '
                                                   'the size of each InputPort. Pass '
                                                   'either this or `default_variable`, '
                                                   'not both.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Identifier for this Mechanism instance '
                                           '(used by Composition wiring and logs).',
                            'type': 'string'},
                  'output_ports': { 'description': 'Optional OutputPort spec — string '
                                                   'name or iterable of port specs.',
                                    'oneOf': [{'type': 'string'}, {'type': 'array'}]},
                  'params': { 'description': 'Optional dict of parameter overrides; '
                                             'rarely needed — prefer named arguments.',
                              'type': 'object'},
                  'prefs': { 'description': 'Optional PreferenceSet override; rarely '
                                            'needed.',
                             'type': 'object'},
                  'reset_default': { 'description': 'Default value of the `reset` '
                                                    'Parameter (number, list, or 1-D '
                                                    'array; default 0). At execute '
                                                    'time, if the current `reset` '
                                                    'value is non-zero/non-empty the '
                                                    "function's stateful value is "
                                                    'reset to its initializer before '
                                                    'returning. Leave at 0 unless you '
                                                    'intend control-driven resets.',
                                     'oneOf': [{'type': 'number'}, {'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Stateful: same instance produces different outputs across executions because the wrapped IntegratorFunction carries hidden state — never share one handle between Compositions you intend to run independently. The Mechanism reshapes its variable to match an instantiated `function`'s inner dimension when its own `default_variable` was not user-specified, but if both are user-specified and inner lengths differ (and neither is 1) construction raises IntegratorMechanismError — set `default_variable` to match the function's variable shape, not 1-wider/narrower. The `reset` Parameter is checked every execute; setting `reset_default` to non-zero will fire a reset on the first non-initialization execute. DriftOnASphereIntegrator is currently incompatible as the `function` argument because of an input/output shape asymmetry (variable is (dimension-1,), value is (dimension,)) that the Mechanism's default port wiring does not handle — this fails at construction with a numpy matmul dimension-mismatch error and cannot be worked around via `default_variable` (1-D, 2-D, or omitted all fail the same way). For `Composition`-level usage and how this handle is wired into pathways, see the Composition tool."


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
        'Creates a PsyNeuLink IntegratorMechanism — a ProcessingMechanism whose `function` is an IntegratorFunction (default `AdaptiveIntegrator(rate=0.5)`), so its output accumulates / decays across executions instead of being a pure function of the current input.'
        return _impl(args or {})
