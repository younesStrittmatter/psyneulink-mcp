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
TOOL_DESCRIPTION = 'Create a TransferMechanism: a ProcessingMechanism that applies a simple transform (its `function`, e.g. Linear/Logistic/SoftMax) to its input, with optional integration over time. Call this when you want a stateless or leaky-integrator unit (set `integrator_mode=True` for the latter); for stateful drift/accumulator dynamics, the integrator behavior must go through `integrator_function`, not `function`. Returns a node handle to feed into a Composition. See the parent ProcessingMechanism / Mechanism tools for `default_variable`, `input_shapes`, `input_ports`, `params`, `name`, `prefs`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "[min, max] clamp applied elementwise to the function output. First must be < second.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "default_variable": {\n      "description": "Default input value/shape; a 1d list (single input port) or a 2d list (one row per input port)."\n    },\n    "function": {\n      "description": "The transform function applied to the input. MUST be a TransferFunction (e.g. Linear, Logistic, ReLU, Exponential, Tanh) or SelectionFunction (e.g. SoftMax, OneHot), or a Python callable whose output shape equals its input shape. IntegratorFunctions (e.g. AdaptiveIntegrator, DriftOnASphereIntegrator, DriftDiffusionIntegrator) are NOT allowed here \\u2014 pass them via `integrator_function` and set `integrator_mode=True` instead. Default: Linear."\n    },\n    "initial_value": {\n      "description": "Starting value for the integrator when `integrator_mode=True`; must match the shape of `default_variable`."\n    },\n    "input_ports": {\n      "description": "Optional input port spec (str, list, or port-like)."\n    },\n    "input_shapes": {\n      "description": "Alternative to default_variable; integer or list of ints giving the size of each input port."\n    },\n    "integration_rate": {\n      "description": "Rate of leaky integration in [0, 1] when `integrator_mode=True`; higher = faster. Must be a scalar or have the same shape as variable. Default: 0.5.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "integrator_function": {\n      "description": "An IntegratorFunction class or instance used when `integrator_mode=True` (e.g. AdaptiveIntegrator, DriftDiffusionIntegrator, OrnsteinUhlenbeckIntegrator). Default: AdaptiveIntegrator. Note: DriftOnASphereIntegrator changes the output dimensionality and is generally not compatible here \\u2014 use a dedicated mechanism for that."\n    },\n    "integrator_mode": {\n      "description": "If True, input is first passed through `integrator_function` (leaky integration by default) before `function`. Default: False.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Name for the mechanism node.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Float, function (e.g. a DistributionFunction instance for stochastic noise), or array of these. Added to the function input each execution. If specified as a scalar/function in the constructor it cannot later be set to an array, and vice versa. Default: 0.0."\n    },\n    "on_resume_integrator_mode": {\n      "description": "Behavior when integration is resumed after being paused. Default: CURRENT_VALUE.",\n      "enum": [\n        "CURRENT_VALUE",\n        "LAST_INTEGRATED_VALUE",\n        "RESET"\n      ],\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "OutputPort spec; the keyword \'RESULTS\' (default) makes one OutputPort per InputPort. The standard output port \'COMBINE\' (Hadamard sum across value items) is also available."\n    },\n    "params": {\n      "description": "Optional dict of parameter overrides.",\n      "type": "object"\n    },\n    "prefs": {\n      "description": "Optional PreferenceSet."\n    },\n    "termination_comparison_op": {\n      "description": "Comparator applied between termination_measure_value and termination_threshold. Default: LESS_THAN_OR_EQUAL.",\n      "enum": [\n        "<",\n        "<=",\n        ">",\n        ">=",\n        "==",\n        "!=",\n        "LESS_THAN",\n        "LESS_THAN_OR_EQUAL",\n        "GREATER_THAN",\n        "GREATER_THAN_OR_EQUAL",\n        "EQUAL",\n        "NOT_EQUAL"\n      ],\n      "type": "string"\n    },\n    "termination_measure": {\n      "description": "Function (e.g. Distance(metric=MAX_ABS_DIFF), or `max`) or TimeScale used to decide when execution is finished if `execute_until_finished=True`. Default: Distance(metric=MAX_ABS_DIFF)."\n    },\n    "termination_threshold": {\n      "description": "Float threshold compared against `termination_measure_value`. None disables the threshold (single-cycle execution).",\n      "type": [\n        "number",\n        "null"\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — `function` vs `integrator_function`: TransferMechanism\'s `function` must be a TransferFunction or SelectionFunction. Passing an IntegratorFunction (e.g. DriftOnASphereIntegrator, AdaptiveIntegrator, DriftDiffusionIntegrator) as `function` raises TransferError at construction. Integrators belong in `integrator_function` together with `integrator_mode=True`. Note that DriftOnASphereIntegrator alters output dimensionality (n+1 → n via angular projection) and is typically not safely usable as an `integrator_function` here — a dedicated mechanism handles that case.\n\nShape gotchas: `default_variable` is 2d (list of input-port vectors) — pass `[[0,0,...]]` for a single port, not `[0,0,...]`. `initial_value` must match `default_variable`\'s shape. `integration_rate` is either a scalar in [0,1] or an array matching variable shape.\n\nNoise locking: once `noise` is set as scalar/function it cannot later be set as list/array (and vice versa) — choose the right form upfront. For execution-varying randomness, use a DistributionFunction instance, not a fixed float.\n\n`output_ports` is read-only after construction — set it here. The default `RESULTS` keyword auto-expands to one OutputPort per item of `variable`.\n\n`termination_threshold=None` (default) means single-cycle execution regardless of `termination_measure`.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': '[min, max] clamp applied elementwise to '
                                           'the function output. First must be < '
                                           'second.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'default_variable': { 'description': 'Default input value/shape; a '
                                                       '1d list (single input port) or '
                                                       'a 2d list (one row per input '
                                                       'port).'},
                  'function': { 'description': 'The transform function applied to the '
                                               'input. MUST be a TransferFunction '
                                               '(e.g. Linear, Logistic, ReLU, '
                                               'Exponential, Tanh) or '
                                               'SelectionFunction (e.g. SoftMax, '
                                               'OneHot), or a Python callable whose '
                                               'output shape equals its input shape. '
                                               'IntegratorFunctions (e.g. '
                                               'AdaptiveIntegrator, '
                                               'DriftOnASphereIntegrator, '
                                               'DriftDiffusionIntegrator) are NOT '
                                               'allowed here — pass them via '
                                               '`integrator_function` and set '
                                               '`integrator_mode=True` instead. '
                                               'Default: Linear.'},
                  'initial_value': { 'description': 'Starting value for the integrator '
                                                    'when `integrator_mode=True`; must '
                                                    'match the shape of '
                                                    '`default_variable`.'},
                  'input_ports': { 'description': 'Optional input port spec (str, '
                                                  'list, or port-like).'},
                  'input_shapes': { 'description': 'Alternative to default_variable; '
                                                   'integer or list of ints giving the '
                                                   'size of each input port.'},
                  'integration_rate': { 'description': 'Rate of leaky integration in '
                                                       '[0, 1] when '
                                                       '`integrator_mode=True`; higher '
                                                       '= faster. Must be a scalar or '
                                                       'have the same shape as '
                                                       'variable. Default: 0.5.',
                                        'maximum': 1,
                                        'minimum': 0,
                                        'type': 'number'},
                  'integrator_function': { 'description': 'An IntegratorFunction class '
                                                          'or instance used when '
                                                          '`integrator_mode=True` '
                                                          '(e.g. AdaptiveIntegrator, '
                                                          'DriftDiffusionIntegrator, '
                                                          'OrnsteinUhlenbeckIntegrator). '
                                                          'Default: '
                                                          'AdaptiveIntegrator. Note: '
                                                          'DriftOnASphereIntegrator '
                                                          'changes the output '
                                                          'dimensionality and is '
                                                          'generally not compatible '
                                                          'here — use a dedicated '
                                                          'mechanism for that.'},
                  'integrator_mode': { 'description': 'If True, input is first passed '
                                                      'through `integrator_function` '
                                                      '(leaky integration by default) '
                                                      'before `function`. Default: '
                                                      'False.',
                                       'type': 'boolean'},
                  'name': { 'description': 'Name for the mechanism node.',
                            'type': 'string'},
                  'noise': { 'description': 'Float, function (e.g. a '
                                            'DistributionFunction instance for '
                                            'stochastic noise), or array of these. '
                                            'Added to the function input each '
                                            'execution. If specified as a '
                                            'scalar/function in the constructor it '
                                            'cannot later be set to an array, and vice '
                                            'versa. Default: 0.0.'},
                  'on_resume_integrator_mode': { 'description': 'Behavior when '
                                                                'integration is '
                                                                'resumed after being '
                                                                'paused. Default: '
                                                                'CURRENT_VALUE.',
                                                 'enum': [ 'CURRENT_VALUE',
                                                           'LAST_INTEGRATED_VALUE',
                                                           'RESET'],
                                                 'type': 'string'},
                  'output_ports': { 'description': 'OutputPort spec; the keyword '
                                                   "'RESULTS' (default) makes one "
                                                   'OutputPort per InputPort. The '
                                                   "standard output port 'COMBINE' "
                                                   '(Hadamard sum across value items) '
                                                   'is also available.'},
                  'params': { 'description': 'Optional dict of parameter overrides.',
                              'type': 'object'},
                  'prefs': {'description': 'Optional PreferenceSet.'},
                  'termination_comparison_op': { 'description': 'Comparator applied '
                                                                'between '
                                                                'termination_measure_value '
                                                                'and '
                                                                'termination_threshold. '
                                                                'Default: '
                                                                'LESS_THAN_OR_EQUAL.',
                                                 'enum': [ '<',
                                                           '<=',
                                                           '>',
                                                           '>=',
                                                           '==',
                                                           '!=',
                                                           'LESS_THAN',
                                                           'LESS_THAN_OR_EQUAL',
                                                           'GREATER_THAN',
                                                           'GREATER_THAN_OR_EQUAL',
                                                           'EQUAL',
                                                           'NOT_EQUAL'],
                                                 'type': 'string'},
                  'termination_measure': { 'description': 'Function (e.g. '
                                                          'Distance(metric=MAX_ABS_DIFF), '
                                                          'or `max`) or TimeScale used '
                                                          'to decide when execution is '
                                                          'finished if '
                                                          '`execute_until_finished=True`. '
                                                          'Default: '
                                                          'Distance(metric=MAX_ABS_DIFF).'},
                  'termination_threshold': { 'description': 'Float threshold compared '
                                                            'against '
                                                            '`termination_measure_value`. '
                                                            'None disables the '
                                                            'threshold (single-cycle '
                                                            'execution).',
                                             'type': ['number', 'null']}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL — `function` vs `integrator_function`: TransferMechanism's `function` must be a TransferFunction or SelectionFunction. Passing an IntegratorFunction (e.g. DriftOnASphereIntegrator, AdaptiveIntegrator, DriftDiffusionIntegrator) as `function` raises TransferError at construction. Integrators belong in `integrator_function` together with `integrator_mode=True`. Note that DriftOnASphereIntegrator alters output dimensionality (n+1 → n via angular projection) and is typically not safely usable as an `integrator_function` here — a dedicated mechanism handles that case.\n\nShape gotchas: `default_variable` is 2d (list of input-port vectors) — pass `[[0,0,...]]` for a single port, not `[0,0,...]`. `initial_value` must match `default_variable`'s shape. `integration_rate` is either a scalar in [0,1] or an array matching variable shape.\n\nNoise locking: once `noise` is set as scalar/function it cannot later be set as list/array (and vice versa) — choose the right form upfront. For execution-varying randomness, use a DistributionFunction instance, not a fixed float.\n\n`output_ports` is read-only after construction — set it here. The default `RESULTS` keyword auto-expands to one OutputPort per item of `variable`.\n\n`termination_threshold=None` (default) means single-cycle execution regardless of `termination_measure`."


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
        'Create a TransferMechanism: a ProcessingMechanism that applies a simple transform (its `function`, e.g.'
        return _impl(args or {})
