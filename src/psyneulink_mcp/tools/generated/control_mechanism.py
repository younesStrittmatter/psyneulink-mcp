"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '29c1062a37a4db2b0653069034f74d3162ab91668d7ac1ef4c88fcf1fa8df0db'
__pnl_qualname__ = 'psyneulink.ControlMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_control_mechanism'
TOOL_DESCRIPTION = 'Call this tool to instantiate a ControlMechanism that modulates parameters of one or more Components in a Composition by sending ControlProjections to their ParameterPorts. Use it when you need a general-purpose controller — i.e., when you are not using a specialized subclass like OptimizationControlMechanism or LCControlMechanism. Returns a ControlMechanism object that can be passed as the `controller` argument to a Composition or added as a node; its `control_signals` attribute lists the ControlSignals it sends.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "allow_probes": {\n      "default": false,\n      "description": "If true, Components that are not OUTPUT Nodes of a nested Composition can be specified in monitor_for_control. Default is false.",\n      "type": "boolean"\n    },\n    "combine_costs": {\n      "description": "Python expression for a function that combines the costs of all control_signals into a single scalar. Must accept a list or 1d array and return a scalar. Default is \'np.sum\'.",\n      "type": "string"\n    },\n    "compute_net_outcome": {\n      "description": "Python expression for a function that combines outcome and cost into a net_outcome scalar. Must accept two 1d arrays (outcome, cost) and return a scalar. Default is \'lambda outcome, cost: outcome - cost\'.",\n      "type": "string"\n    },\n    "compute_reconfiguration_cost": {\n      "description": "Python expression for a function that computes the reconfiguration cost between the current and previous control_allocation. Must accept a 2d array of two allocation vectors and return a scalar. Default is None (reconfiguration cost is not tracked).",\n      "type": "string"\n    },\n    "control": {\n      "description": "ControlSignal specification or list of ControlSignal specifications for the parameters to be controlled. Each entry can be a (parameter_name, Mechanism) tuple, a ControlSignal instance, or a specification dict. A ControlSignal is created for each entry.",\n      "oneOf": [\n        {\n          "description": "Single ControlSignal spec as Python expression.",\n          "type": "string"\n        },\n        {\n          "description": "List of ControlSignal specs as Python expressions.",\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "default_allocation": {\n      "description": "Default allocation value for ControlSignals that do not specify their own. Can be a scalar or list/array. If null, each ControlSignal falls back to its own parameter default.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "function": {\n      "description": "Python expression for the TransferFunction used to map monitored values to control_allocation. Default is Linear(slope=1, intercept=0). Example: \'Linear(slope=2)\'.",\n      "type": "string"\n    },\n    "modulation": {\n      "default": "MULTIPLICATIVE",\n      "description": "Default modulation type applied by all ControlSignals unless individually overridden.",\n      "enum": [\n        "MULTIPLICATIVE",\n        "ADDITIVE",\n        "OVERRIDE",\n        "DISABLE"\n      ],\n      "type": "string"\n    },\n    "monitor_for_control": {\n      "description": "List of OutputPort or Mechanism names/references to monitor. If a Mechanism is specified, its primary OutputPort is used. Monitored values are passed to the ObjectiveMechanism (if specified) or directly to the ControlMechanism\'s input ports.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the ControlMechanism instance.",\n      "type": "string"\n    },\n    "objective_mechanism": {\n      "description": "An ObjectiveMechanism instance to use, OR a list of OutputPort specifications to monitor (a default ObjectiveMechanism is then created automatically). Set to null to have the ControlMechanism monitor directly without an ObjectiveMechanism.",\n      "oneOf": [\n        {\n          "description": "Name/reference to an existing ObjectiveMechanism.",\n          "type": "string"\n        },\n        {\n          "description": "List of OutputPort specs; a default ObjectiveMechanism is created.",\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "description": "False to explicitly disable.",\n          "type": "boolean"\n        }\n      ]\n    },\n    "outcome_input_ports_option": {\n      "default": "SEPARATE",\n      "description": "Only relevant when objective_mechanism is not specified. SEPARATE (default): each monitored item gets its own InputPort. COMBINE: all projections feed a single OUTCOME InputPort via LinearCombination (inputs must have same dimension). CONCATENATE: all projections feed a single OUTCOME InputPort via Concatenate (inputs can differ in length).",\n      "enum": [\n        "SEPARATE",\n        "COMBINE",\n        "CONCATENATE"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `control` is the canonical argument for specifying ControlSignals; the synonyms `control_signals` and `modulatory_signals` are accepted for backward compatibility but raise an error if more than one is specified simultaneously.\n- `default_control_allocation` is a deprecated alias for `default_allocation` and raises a ControlMechanismError if used.\n- When `objective_mechanism` is a list, PNL creates a default ObjectiveMechanism with `LinearCombination(operation=PRODUCT)` as its function — this may be surprising if additive combination is intended.\n- If `objective_mechanism` is an ObjectiveMechanism instance, any items in `monitor_for_control` are *added* to it via `add_to_monitor`, not replaced.\n- `outcome_input_ports_option` is ignored if `objective_mechanism` is specified; it only applies when the ControlMechanism monitors directly.\n- `modulation` defaults to `MULTIPLICATIVE`, meaning ControlSignals scale (multiply) the target parameter value by default; use `ADDITIVE` to shift it instead.\n- When the ControlMechanism\'s function returns one value, all ControlSignals share that value; when it returns N values matching the number of ControlSignals, each ControlSignal gets its own index — mismatches are caught at execution time, not construction time.\n- `reconfiguration_cost` (from `compute_reconfiguration_cost`) is distinct from a ControlSignal\'s `adjustment_cost`; the former is mechanism-level, the latter is per-signal.\n- An ObjectiveMechanism\'s input_ports are marked `internal_only=True`, so they will not receive projections from a Composition\'s input_CIM automatically.'
TOOL_PARAMETERS = { 'properties': { 'allow_probes': { 'default': False,
                                    'description': 'If true, Components that are not '
                                                   'OUTPUT Nodes of a nested '
                                                   'Composition can be specified in '
                                                   'monitor_for_control. Default is '
                                                   'false.',
                                    'type': 'boolean'},
                  'combine_costs': { 'description': 'Python expression for a function '
                                                    'that combines the costs of all '
                                                    'control_signals into a single '
                                                    'scalar. Must accept a list or 1d '
                                                    'array and return a scalar. '
                                                    "Default is 'np.sum'.",
                                     'type': 'string'},
                  'compute_net_outcome': { 'description': 'Python expression for a '
                                                          'function that combines '
                                                          'outcome and cost into a '
                                                          'net_outcome scalar. Must '
                                                          'accept two 1d arrays '
                                                          '(outcome, cost) and return '
                                                          'a scalar. Default is '
                                                          "'lambda outcome, cost: "
                                                          "outcome - cost'.",
                                           'type': 'string'},
                  'compute_reconfiguration_cost': { 'description': 'Python expression '
                                                                   'for a function '
                                                                   'that computes the '
                                                                   'reconfiguration '
                                                                   'cost between the '
                                                                   'current and '
                                                                   'previous '
                                                                   'control_allocation. '
                                                                   'Must accept a 2d '
                                                                   'array of two '
                                                                   'allocation vectors '
                                                                   'and return a '
                                                                   'scalar. Default is '
                                                                   'None '
                                                                   '(reconfiguration '
                                                                   'cost is not '
                                                                   'tracked).',
                                                    'type': 'string'},
                  'control': { 'description': 'ControlSignal specification or list of '
                                              'ControlSignal specifications for the '
                                              'parameters to be controlled. Each entry '
                                              'can be a (parameter_name, Mechanism) '
                                              'tuple, a ControlSignal instance, or a '
                                              'specification dict. A ControlSignal is '
                                              'created for each entry.',
                               'oneOf': [ { 'description': 'Single ControlSignal spec '
                                                           'as Python expression.',
                                            'type': 'string'},
                                          { 'description': 'List of ControlSignal '
                                                           'specs as Python '
                                                           'expressions.',
                                            'items': {'type': 'string'},
                                            'type': 'array'}]},
                  'default_allocation': { 'description': 'Default allocation value for '
                                                         'ControlSignals that do not '
                                                         'specify their own. Can be a '
                                                         'scalar or list/array. If '
                                                         'null, each ControlSignal '
                                                         'falls back to its own '
                                                         'parameter default.',
                                          'oneOf': [ {'type': 'number'},
                                                     { 'items': {'type': 'number'},
                                                       'type': 'array'}]},
                  'function': { 'description': 'Python expression for the '
                                               'TransferFunction used to map monitored '
                                               'values to control_allocation. Default '
                                               'is Linear(slope=1, intercept=0). '
                                               "Example: 'Linear(slope=2)'.",
                                'type': 'string'},
                  'modulation': { 'default': 'MULTIPLICATIVE',
                                  'description': 'Default modulation type applied by '
                                                 'all ControlSignals unless '
                                                 'individually overridden.',
                                  'enum': [ 'MULTIPLICATIVE',
                                            'ADDITIVE',
                                            'OVERRIDE',
                                            'DISABLE'],
                                  'type': 'string'},
                  'monitor_for_control': { 'description': 'List of OutputPort or '
                                                          'Mechanism names/references '
                                                          'to monitor. If a Mechanism '
                                                          'is specified, its primary '
                                                          'OutputPort is used. '
                                                          'Monitored values are passed '
                                                          'to the ObjectiveMechanism '
                                                          '(if specified) or directly '
                                                          "to the ControlMechanism's "
                                                          'input ports.',
                                           'items': {'type': 'string'},
                                           'type': 'array'},
                  'name': { 'description': 'Optional name for the ControlMechanism '
                                           'instance.',
                            'type': 'string'},
                  'objective_mechanism': { 'description': 'An ObjectiveMechanism '
                                                          'instance to use, OR a list '
                                                          'of OutputPort '
                                                          'specifications to monitor '
                                                          '(a default '
                                                          'ObjectiveMechanism is then '
                                                          'created automatically). Set '
                                                          'to null to have the '
                                                          'ControlMechanism monitor '
                                                          'directly without an '
                                                          'ObjectiveMechanism.',
                                           'oneOf': [ { 'description': 'Name/reference '
                                                                       'to an existing '
                                                                       'ObjectiveMechanism.',
                                                        'type': 'string'},
                                                      { 'description': 'List of '
                                                                       'OutputPort '
                                                                       'specs; a '
                                                                       'default '
                                                                       'ObjectiveMechanism '
                                                                       'is created.',
                                                        'items': {'type': 'string'},
                                                        'type': 'array'},
                                                      { 'description': 'False to '
                                                                       'explicitly '
                                                                       'disable.',
                                                        'type': 'boolean'}]},
                  'outcome_input_ports_option': { 'default': 'SEPARATE',
                                                  'description': 'Only relevant when '
                                                                 'objective_mechanism '
                                                                 'is not specified. '
                                                                 'SEPARATE (default): '
                                                                 'each monitored item '
                                                                 'gets its own '
                                                                 'InputPort. COMBINE: '
                                                                 'all projections feed '
                                                                 'a single OUTCOME '
                                                                 'InputPort via '
                                                                 'LinearCombination '
                                                                 '(inputs must have '
                                                                 'same dimension). '
                                                                 'CONCATENATE: all '
                                                                 'projections feed a '
                                                                 'single OUTCOME '
                                                                 'InputPort via '
                                                                 'Concatenate (inputs '
                                                                 'can differ in '
                                                                 'length).',
                                                  'enum': [ 'SEPARATE',
                                                            'COMBINE',
                                                            'CONCATENATE'],
                                                  'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- `control` is the canonical argument for specifying ControlSignals; the synonyms `control_signals` and `modulatory_signals` are accepted for backward compatibility but raise an error if more than one is specified simultaneously.\n- `default_control_allocation` is a deprecated alias for `default_allocation` and raises a ControlMechanismError if used.\n- When `objective_mechanism` is a list, PNL creates a default ObjectiveMechanism with `LinearCombination(operation=PRODUCT)` as its function — this may be surprising if additive combination is intended.\n- If `objective_mechanism` is an ObjectiveMechanism instance, any items in `monitor_for_control` are *added* to it via `add_to_monitor`, not replaced.\n- `outcome_input_ports_option` is ignored if `objective_mechanism` is specified; it only applies when the ControlMechanism monitors directly.\n- `modulation` defaults to `MULTIPLICATIVE`, meaning ControlSignals scale (multiply) the target parameter value by default; use `ADDITIVE` to shift it instead.\n- When the ControlMechanism's function returns one value, all ControlSignals share that value; when it returns N values matching the number of ControlSignals, each ControlSignal gets its own index — mismatches are caught at execution time, not construction time.\n- `reconfiguration_cost` (from `compute_reconfiguration_cost`) is distinct from a ControlSignal's `adjustment_cost`; the former is mechanism-level, the latter is per-signal.\n- An ObjectiveMechanism's input_ports are marked `internal_only=True`, so they will not receive projections from a Composition's input_CIM automatically."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ControlMechanism
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
    def create_control_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a ControlMechanism that modulates parameters of one or more Components in a Composition by sending ControlProjections to their ParameterPorts.'
        return _impl(args or {})
