"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4661c8b67b7fc6bdc76b37025ef3d3e1cfd66bb6dab4ba351f49fe4c5193577f'
__pnl_qualname__ = 'psyneulink.OutputPort'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_output_port'
TOOL_DESCRIPTION = 'Call this tool to create a custom OutputPort when you need to override a Mechanism\'s default output behavior — for example, to apply a non-linear transform to the output, route output to specific receivers, or name the port explicitly. Returns an OutputPort object that can be passed in a Mechanism\'s output_ports argument. Most Mechanisms auto-create Standard OutputPorts, so only call this when customization is needed.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "description": "Name of the PsyNeuLink Function to transform the OutputPort\'s variable into its value (e.g., \'Linear\', \'Logistic\', \'ReLU\'). Defaults to Linear (identity pass-through). May be modulated at runtime by ControlProjections or GatingProjections.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for the OutputPort. If omitted, the PortRegistry assigns a default. Standard OutputPorts on built-in Mechanisms have pre-specified names (e.g., \'RESULT\').",\n      "type": "string"\n    },\n    "projections": {\n      "description": "List of Projection specifications. Outgoing MappingProjections are sent to InputPorts of other Mechanisms; incoming ControlProjections or GatingProjections modulate this OutputPort\'s function. Specify as Mechanism names, Port names, or Projection specs.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "reference_value": {\n      "description": "Template specifying the format (shape and type) of the OutputPort\'s variable. Used to validate compatibility with the source feeding into it. If omitted, inferred from the owner Mechanism\'s value.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "variable": {\n      "description": "Specifies which attribute(s) of the owner Mechanism to use as input to the OutputPort\'s function. Typically a tuple (OWNER_VALUE, index) to select a specific item of the owner\'s value array, or the string \'OWNER_VALUE\' for the entire value. If omitted, defaults to the first item of the owner\'s value.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nOutputPort initialization is deferred (DEFERRED_INIT status) when no owner is provided; full instantiation happens when the port is assigned to a Mechanism. If any output_ports are explicitly specified in a Mechanism\'s constructor, they REPLACE all Standard OutputPorts — the Mechanism will have only those ports. The variable argument accepts special string constants like \'OWNER_VALUE\' or tuples like (\'OWNER_VALUE\', 0) to index into the owner\'s value array; plain numeric arrays are treated as reference_value stand-ins. The projections argument distinguishes outgoing (MappingProjection) vs incoming (ModulatoryProjection) specs automatically by type. The calculate/assign attribute is deprecated — use function instead.'
TOOL_PARAMETERS = { 'properties': { 'function': { 'description': 'Name of the PsyNeuLink Function to '
                                               "transform the OutputPort's variable "
                                               "into its value (e.g., 'Linear', "
                                               "'Logistic', 'ReLU'). Defaults to "
                                               'Linear (identity pass-through). May be '
                                               'modulated at runtime by '
                                               'ControlProjections or '
                                               'GatingProjections.',
                                'type': 'string'},
                  'name': { 'description': 'Name for the OutputPort. If omitted, the '
                                           'PortRegistry assigns a default. Standard '
                                           'OutputPorts on built-in Mechanisms have '
                                           "pre-specified names (e.g., 'RESULT').",
                            'type': 'string'},
                  'projections': { 'description': 'List of Projection specifications. '
                                                  'Outgoing MappingProjections are '
                                                  'sent to InputPorts of other '
                                                  'Mechanisms; incoming '
                                                  'ControlProjections or '
                                                  'GatingProjections modulate this '
                                                  "OutputPort's function. Specify as "
                                                  'Mechanism names, Port names, or '
                                                  'Projection specs.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'reference_value': { 'description': 'Template specifying the format '
                                                      '(shape and type) of the '
                                                      "OutputPort's variable. Used to "
                                                      'validate compatibility with the '
                                                      'source feeding into it. If '
                                                      'omitted, inferred from the '
                                                      "owner Mechanism's value.",
                                       'items': {'type': 'number'},
                                       'type': 'array'},
                  'variable': { 'description': 'Specifies which attribute(s) of the '
                                               'owner Mechanism to use as input to the '
                                               "OutputPort's function. Typically a "
                                               'tuple (OWNER_VALUE, index) to select a '
                                               "specific item of the owner's value "
                                               "array, or the string 'OWNER_VALUE' for "
                                               'the entire value. If omitted, defaults '
                                               "to the first item of the owner's "
                                               'value.',
                                'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "OutputPort initialization is deferred (DEFERRED_INIT status) when no owner is provided; full instantiation happens when the port is assigned to a Mechanism. If any output_ports are explicitly specified in a Mechanism's constructor, they REPLACE all Standard OutputPorts — the Mechanism will have only those ports. The variable argument accepts special string constants like 'OWNER_VALUE' or tuples like ('OWNER_VALUE', 0) to index into the owner's value array; plain numeric arrays are treated as reference_value stand-ins. The projections argument distinguishes outgoing (MappingProjection) vs incoming (ModulatoryProjection) specs automatically by type. The calculate/assign attribute is deprecated — use function instead."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.OutputPort
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
    def create_output_port(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to create a custom OutputPort when you need to override a Mechanism's default output behavior — for example, to apply a non-linear transform to the output, route output to specific receivers, or name the port explicitly."
        return _impl(args or {})
