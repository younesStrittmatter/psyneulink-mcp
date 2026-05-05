"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0addba16e0ce6776d61c74c71c391976d5e10b22286a6dc2ffee5546c7f34506'
__pnl_qualname__ = 'psyneulink.ObjectiveMechanism'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_objective_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create an ObjectiveMechanism that monitors the output values of one or more other Mechanisms and combines them into a scalar or vector OUTCOME signal. Use it when you need a dedicated evaluation node — e.g., to feed a ControlMechanism\'s objective_mechanism, compute a loss signal for a LearningMechanism, or track any weighted combination of outputs in a Composition. The tool returns a configured ObjectiveMechanism whose primary OUTCOME OutputPort reflects the result of applying `function` to the monitored values.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Optional explicit default variable (2d array). Usually inferred from `monitor`; only supply if you need to override the inferred shape.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "function": {\n      "default": "LinearCombination",\n      "description": "Name of the function used to evaluate the monitored values. Defaults to \'LinearCombination\'. Any TransformFunction or ObjectiveFunction name accepted by PsyNeuLink works here.",\n      "type": "string"\n    },\n    "input_shapes": {\n      "description": "Optional list of integers specifying the size of each InputPort\'s variable. Alternative to `default_variable` for defining input dimensionality.",\n      "items": {\n        "type": "integer"\n      },\n      "type": "array"\n    },\n    "monitor": {\n      "description": "List of OutputPorts, InputPorts, Mechanisms, strings, values, or dicts identifying the ports whose values will be monitored and passed to `function`. Each Mechanism entry resolves to its primary OutputPort. Required; passing an empty list is treated as None.",\n      "items": {\n        "description": "Name of a Mechanism or OutputPort, or a dict specification",\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the ObjectiveMechanism. Auto-assigned if omitted.",\n      "type": "string"\n    },\n    "output_ports": {\n      "default": [\n        "OUTCOME"\n      ],\n      "description": "OutputPort specifications for the mechanism. Defaults to [\'OUTCOME\']. Override only if you need additional or differently-named output ports.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "monitor"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `monitor` is the only required argument; passing `None` or an empty list is silently normalized to `None`, which will likely cause an error downstream — always provide at least one item.\n- The deprecated keyword `monitored_output_ports` is aliased to `monitor`; do not use it, as a warning is emitted and it will be removed.\n- `output_ports` is normalized: if `None` or the string `\'OUTCOME\'` is passed, it is automatically converted to `[\'OUTCOME\']`.\n- Per-port weights and exponents are set on individual InputPort specs (as tuples or dicts), not directly on this constructor; they are then propagated to `function.weights` / `function.exponents` at instantiation time.\n- When the ObjectiveMechanism is assigned to a ControlMechanism, `modulatory_mechanism` is set automatically by the ControlMechanism — do not set it manually.\n- If any monitored InputPort shadows another Mechanism\'s InputPort that receives multiple Projections, `monitor` may contain more entries than `input_ports`.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Optional explicit default '
                                                       'variable (2d array). Usually '
                                                       'inferred from `monitor`; only '
                                                       'supply if you need to override '
                                                       'the inferred shape.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'function': { 'default': 'LinearCombination',
                                'description': 'Name of the function used to evaluate '
                                               'the monitored values. Defaults to '
                                               "'LinearCombination'. Any "
                                               'TransformFunction or ObjectiveFunction '
                                               'name accepted by PsyNeuLink works '
                                               'here.',
                                'type': 'string'},
                  'input_shapes': { 'description': 'Optional list of integers '
                                                   'specifying the size of each '
                                                   "InputPort's variable. Alternative "
                                                   'to `default_variable` for defining '
                                                   'input dimensionality.',
                                    'items': {'type': 'integer'},
                                    'type': 'array'},
                  'monitor': { 'description': 'List of OutputPorts, InputPorts, '
                                              'Mechanisms, strings, values, or dicts '
                                              'identifying the ports whose values will '
                                              'be monitored and passed to `function`. '
                                              'Each Mechanism entry resolves to its '
                                              'primary OutputPort. Required; passing '
                                              'an empty list is treated as None.',
                               'items': { 'description': 'Name of a Mechanism or '
                                                         'OutputPort, or a dict '
                                                         'specification',
                                          'type': 'string'},
                               'type': 'array'},
                  'name': { 'description': 'Optional name for the ObjectiveMechanism. '
                                           'Auto-assigned if omitted.',
                            'type': 'string'},
                  'output_ports': { 'default': ['OUTCOME'],
                                    'description': 'OutputPort specifications for the '
                                                   'mechanism. Defaults to '
                                                   "['OUTCOME']. Override only if you "
                                                   'need additional or '
                                                   'differently-named output ports.',
                                    'items': {'type': 'string'},
                                    'type': 'array'}},
  'required': ['monitor'],
  'type': 'object'}
TOOL_NOTES = "- `monitor` is the only required argument; passing `None` or an empty list is silently normalized to `None`, which will likely cause an error downstream — always provide at least one item.\n- The deprecated keyword `monitored_output_ports` is aliased to `monitor`; do not use it, as a warning is emitted and it will be removed.\n- `output_ports` is normalized: if `None` or the string `'OUTCOME'` is passed, it is automatically converted to `['OUTCOME']`.\n- Per-port weights and exponents are set on individual InputPort specs (as tuples or dicts), not directly on this constructor; they are then propagated to `function.weights` / `function.exponents` at instantiation time.\n- When the ObjectiveMechanism is assigned to a ControlMechanism, `modulatory_mechanism` is set automatically by the ControlMechanism — do not set it manually.\n- If any monitored InputPort shadows another Mechanism's InputPort that receives multiple Projections, `monitor` may contain more entries than `input_ports`."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ObjectiveMechanism
    resolved = handles.resolve_in(kwargs)
    result = target(**resolved)
    try:
        json.dumps(result)
    except (TypeError, ValueError):
        return handles.register_handle(result)
    return result


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_objective_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an ObjectiveMechanism that monitors the output values of one or more other Mechanisms and combines them into a scalar or vector OUTCOME signal.'
        return _impl(args or {})
