"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5e251c67921a291bd9bc38725c6a38a8b4ff5438ce8f609ae14d47df83d81856'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.recurrenttransfermechanism.TransferMechanism'
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

TOOL_NAME = 'create_transfer_mechanism'
TOOL_DESCRIPTION = 'Create a TransferMechanism — the standard PNL processing node for a simple element-wise transform of its input (e.g., Linear, Logistic, ReLU, Tanh). Use this as the default building block for non-recurrent layers in a Composition; reach for it whenever you need "apply f(x) to a vector, optionally with integration over time, noise, or clipping". Returns a Mechanism handle to wire into a Composition via projections. Adds to ProcessingMechanism_Base/Mechanism_Base: the integrator_mode toggle (run input through an IntegratorFunction before the primary function), noise injection, clip range, and a termination_measure/threshold pair for execute-until-finished semantics.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "Two-element [min, max] tuple/list bounding the function output element-wise. Either entry may be null to disable that side. min must be < max.",\n      "items": {\n        "anyOf": [\n          {\n            "type": "number"\n          },\n          {\n            "type": "null"\n          }\n        ]\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "default_variable": {\n      "anyOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {},\n          "type": "array"\n        }\n      ],\n      "description": "Template for the input shape (number/list/2-D list). Use this OR input_shapes, not both. Pass the actual array shape the mechanism should accept (e.g., [0]*80 for an 80-dim layer)."\n    },\n    "function": {\n      "description": "Primary transfer function applied to (possibly integrated) input. Pass either a Function CLASS (e.g., \'Linear\', \'Logistic\', \'ReLU\', \'Tanh\') OR an instance whose default_variable matches the mechanism\'s input shape. Defaults to Linear. See notes about shape compatibility."\n    },\n    "initial_value": {\n      "description": "Starting value for integration when integrator_mode is True; must broadcast to the mechanism\'s variable shape. Default None (zeros)."\n    },\n    "input_ports": {\n      "description": "Optional list of InputPort specifications (names, dicts, or existing InputPort/OutputPort/Mechanism handles).",\n      "items": {},\n      "type": "array"\n    },\n    "input_shapes": {\n      "anyOf": [\n        {\n          "minimum": 1,\n          "type": "integer"\n        },\n        {\n          "items": {\n            "minimum": 1,\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ],\n      "description": "Convenience for setting the input dimensionality when each element is scalar. Integer N means a single InputPort of length N; list of ints means one InputPort per entry. Use this OR default_variable."\n    },\n    "integration_rate": {\n      "default": 0.5,\n      "description": "Rate of integration when integrator_mode is True; must be in [0, 1] (higher = faster). Default 0.5.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "integrator_function": {\n      "description": "IntegratorFunction class or instance used when integrator_mode is True. Defaults to AdaptiveIntegrator."\n    },\n    "integrator_mode": {\n      "default": false,\n      "description": "If True, run input through integrator_function before the primary function (leaky integration / time integration). Default False.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Human-readable name for this Mechanism; used in Compositions and error messages.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Scalar, function (DistributionFunction for stochastic noise), list, or array. Added to function input when integrator_mode is False, otherwise passed to integrator_function. Default 0.0. If specified as scalar/function in constructor, cannot later be set to a list/array (and vice versa)."\n    },\n    "on_resume_integrator_mode": {\n      "default": "CURRENT_VALUE",\n      "description": "What value to use when integration is resumed after being paused.",\n      "enum": [\n        "CURRENT_VALUE",\n        "LAST_INTEGRATED_VALUE",\n        "RESET"\n      ],\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "OutputPort spec(s). Default \'RESULTS\' yields one OutputPort per InputPort. The keyword \'COMBINE\' adds an element-wise sum of all value items."\n    },\n    "params": {\n      "description": "Optional dict of additional parameters (advanced; usually leave unset).",\n      "type": "object"\n    },\n    "termination_comparison_op": {\n      "default": "<=",\n      "description": "Comparator used between termination_measure_value and termination_threshold.",\n      "enum": [\n        "<",\n        "<=",\n        ">",\n        ">=",\n        "==",\n        "!="\n      ],\n      "type": "string"\n    },\n    "termination_measure": {\n      "description": "Function or TimeScale used to decide when execute_until_finished stops. If a function, it is passed (value, previous_value). Default Distance(metric=MAX_ABS_DIFF)."\n    },\n    "termination_threshold": {\n      "anyOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "null"\n        }\n      ],\n      "default": null,\n      "description": "Float compared with termination_measure\'s output via termination_comparison_op to decide is_finished. None disables threshold-based termination."\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nSHAPE GOTCHA (recent feedback issue #28): if you pass `function` as an *instance* (e.g., a ReLU created earlier with its default variable [[0]]) AND set `input_shapes`/`default_variable` to something larger (e.g., 80), you\'ll get `ComponentError: Variable format ([[0]]) of ReLU Function-0 is not compatible with the variable format ([[0,...]]) of \'<name>\'`. Two safe patterns: (1) pass the function as a CLASS (e.g., function=ReLU) so it auto-shapes to the mechanism\'s variable, or (2) construct the function instance with default_variable matching the mechanism\'s input shape. Do NOT reuse the same function instance across mechanisms with different input dimensionalities.\n\nOther caveats:\n- `default_variable` and `input_shapes` are mutually exclusive — use one.\n- `noise`\'s "shape commitment" is sticky: scalar/function at construction → can\'t later become list/array (and vice versa). Use a DistributionFunction for stochastic per-element-per-step noise; a plain float is just a constant offset.\n- `integration_rate` must be in [0, 1]; out-of-range values raise.\n- `clip` requires min < max and exactly two entries (each may be None to disable that side).\n- `termination_threshold=None` disables execute_until_finished termination entirely.\n- When the primary function returns an array, `clip` is applied element-wise.\n- When `integrator_mode=False`, `integrator_function`, `initial_value`, `integration_rate`, and `on_resume_integrator_mode` have no effect at runtime.\n- Returned object is a Mechanism — feed it to a Composition (add_node / projections); this tool does not run anything.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': 'Two-element [min, max] tuple/list bounding '
                                           'the function output element-wise. Either '
                                           'entry may be null to disable that side. '
                                           'min must be < max.',
                            'items': {'anyOf': [{'type': 'number'}, {'type': 'null'}]},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'default_variable': { 'anyOf': [ {'type': 'number'},
                                                   {'items': {}, 'type': 'array'}],
                                        'description': 'Template for the input shape '
                                                       '(number/list/2-D list). Use '
                                                       'this OR input_shapes, not '
                                                       'both. Pass the actual array '
                                                       'shape the mechanism should '
                                                       'accept (e.g., [0]*80 for an '
                                                       '80-dim layer).'},
                  'function': { 'description': 'Primary transfer function applied to '
                                               '(possibly integrated) input. Pass '
                                               'either a Function CLASS (e.g., '
                                               "'Linear', 'Logistic', 'ReLU', 'Tanh') "
                                               'OR an instance whose default_variable '
                                               "matches the mechanism's input shape. "
                                               'Defaults to Linear. See notes about '
                                               'shape compatibility.'},
                  'initial_value': { 'description': 'Starting value for integration '
                                                    'when integrator_mode is True; '
                                                    "must broadcast to the mechanism's "
                                                    'variable shape. Default None '
                                                    '(zeros).'},
                  'input_ports': { 'description': 'Optional list of InputPort '
                                                  'specifications (names, dicts, or '
                                                  'existing '
                                                  'InputPort/OutputPort/Mechanism '
                                                  'handles).',
                                   'items': {},
                                   'type': 'array'},
                  'input_shapes': { 'anyOf': [ {'minimum': 1, 'type': 'integer'},
                                               { 'items': { 'minimum': 1,
                                                            'type': 'integer'},
                                                 'type': 'array'}],
                                    'description': 'Convenience for setting the input '
                                                   'dimensionality when each element '
                                                   'is scalar. Integer N means a '
                                                   'single InputPort of length N; list '
                                                   'of ints means one InputPort per '
                                                   'entry. Use this OR '
                                                   'default_variable.'},
                  'integration_rate': { 'default': 0.5,
                                        'description': 'Rate of integration when '
                                                       'integrator_mode is True; must '
                                                       'be in [0, 1] (higher = '
                                                       'faster). Default 0.5.',
                                        'maximum': 1,
                                        'minimum': 0,
                                        'type': 'number'},
                  'integrator_function': { 'description': 'IntegratorFunction class or '
                                                          'instance used when '
                                                          'integrator_mode is True. '
                                                          'Defaults to '
                                                          'AdaptiveIntegrator.'},
                  'integrator_mode': { 'default': False,
                                       'description': 'If True, run input through '
                                                      'integrator_function before the '
                                                      'primary function (leaky '
                                                      'integration / time '
                                                      'integration). Default False.',
                                       'type': 'boolean'},
                  'name': { 'description': 'Human-readable name for this Mechanism; '
                                           'used in Compositions and error messages.',
                            'type': 'string'},
                  'noise': { 'description': 'Scalar, function (DistributionFunction '
                                            'for stochastic noise), list, or array. '
                                            'Added to function input when '
                                            'integrator_mode is False, otherwise '
                                            'passed to integrator_function. Default '
                                            '0.0. If specified as scalar/function in '
                                            'constructor, cannot later be set to a '
                                            'list/array (and vice versa).'},
                  'on_resume_integrator_mode': { 'default': 'CURRENT_VALUE',
                                                 'description': 'What value to use '
                                                                'when integration is '
                                                                'resumed after being '
                                                                'paused.',
                                                 'enum': [ 'CURRENT_VALUE',
                                                           'LAST_INTEGRATED_VALUE',
                                                           'RESET'],
                                                 'type': 'string'},
                  'output_ports': { 'description': 'OutputPort spec(s). Default '
                                                   "'RESULTS' yields one OutputPort "
                                                   'per InputPort. The keyword '
                                                   "'COMBINE' adds an element-wise sum "
                                                   'of all value items.'},
                  'params': { 'description': 'Optional dict of additional parameters '
                                             '(advanced; usually leave unset).',
                              'type': 'object'},
                  'termination_comparison_op': { 'default': '<=',
                                                 'description': 'Comparator used '
                                                                'between '
                                                                'termination_measure_value '
                                                                'and '
                                                                'termination_threshold.',
                                                 'enum': [ '<',
                                                           '<=',
                                                           '>',
                                                           '>=',
                                                           '==',
                                                           '!='],
                                                 'type': 'string'},
                  'termination_measure': { 'description': 'Function or TimeScale used '
                                                          'to decide when '
                                                          'execute_until_finished '
                                                          'stops. If a function, it is '
                                                          'passed (value, '
                                                          'previous_value). Default '
                                                          'Distance(metric=MAX_ABS_DIFF).'},
                  'termination_threshold': { 'anyOf': [ {'type': 'number'},
                                                        {'type': 'null'}],
                                             'default': None,
                                             'description': 'Float compared with '
                                                            "termination_measure's "
                                                            'output via '
                                                            'termination_comparison_op '
                                                            'to decide is_finished. '
                                                            'None disables '
                                                            'threshold-based '
                                                            'termination.'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'SHAPE GOTCHA (recent feedback issue #28): if you pass `function` as an *instance* (e.g., a ReLU created earlier with its default variable [[0]]) AND set `input_shapes`/`default_variable` to something larger (e.g., 80), you\'ll get `ComponentError: Variable format ([[0]]) of ReLU Function-0 is not compatible with the variable format ([[0,...]]) of \'<name>\'`. Two safe patterns: (1) pass the function as a CLASS (e.g., function=ReLU) so it auto-shapes to the mechanism\'s variable, or (2) construct the function instance with default_variable matching the mechanism\'s input shape. Do NOT reuse the same function instance across mechanisms with different input dimensionalities.\n\nOther caveats:\n- `default_variable` and `input_shapes` are mutually exclusive — use one.\n- `noise`\'s "shape commitment" is sticky: scalar/function at construction → can\'t later become list/array (and vice versa). Use a DistributionFunction for stochastic per-element-per-step noise; a plain float is just a constant offset.\n- `integration_rate` must be in [0, 1]; out-of-range values raise.\n- `clip` requires min < max and exactly two entries (each may be None to disable that side).\n- `termination_threshold=None` disables execute_until_finished termination entirely.\n- When the primary function returns an array, `clip` is applied element-wise.\n- When `integrator_mode=False`, `integrator_function`, `initial_value`, `integration_rate`, and `on_resume_integrator_mode` have no effect at runtime.\n- Returned object is a Mechanism — feed it to a Composition (add_node / projections); this tool does not run anything.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.TransferMechanism
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
    def create_transfer_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Create a TransferMechanism — the standard PNL processing node for a simple element-wise transform of its input (e.g., Linear, Logistic, ReLU, Tanh).'
        return _impl(args or {})
