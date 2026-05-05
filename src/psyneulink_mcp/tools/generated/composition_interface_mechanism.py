"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7d5dc3a45146b3ceb1cbb5a6892285f636d55c4cc79795ec273c5dbe369a4158'
__pnl_qualname__ = 'psyneulink.CompositionInterfaceMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_composition_interface_mechanism'
TOOL_DESCRIPTION = 'Call this tool only when you need to explicitly instantiate a CompositionInterfaceMechanism (CIM) for advanced, low-level use — for example, when constructing a Composition manually and needing to reference or configure its input_CIM, output_CIM, or parameter_CIM. In normal modeling workflows, PsyNeuLink creates and manages CIMs automatically when a Composition is built; direct instantiation is rarely needed. Returns a CIM object that bridges a Composition\'s internal nodes to external inputs/outputs or to a parent Composition when nested.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "The Composition this CIM belongs to. Set automatically when a Composition creates its CIMs; only supply when constructing a CIM manually.",\n      "type": "object"\n    },\n    "default_variable": {\n      "description": "Initial value(s) for the mechanism\'s input; sets the shape of the variable processed. Defaults to a single scalar if omitted.",\n      "items": {},\n      "type": "array"\n    },\n    "function": {\n      "description": "The InterfaceFunction used to transform inputs before assigning to OutputPorts. Defaults to Identity (pass-through). Rarely changed in practice.",\n      "type": "string"\n    },\n    "input_ports": {\n      "description": "Specification of InputPort(s) for the mechanism. Accepts a list of port specs, a Mechanism, an OutputPort, or an InputPort. Managed automatically in normal use.",\n      "items": {},\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Shape(s) of the input(s) as integers or a list of integers. Alternative to default_variable for specifying input dimensionality.",\n      "items": {\n        "type": "integer"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "String name for this mechanism instance. Auto-generated if omitted.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Additional parameter overrides passed to the parent Mechanism class.",\n      "type": "object"\n    },\n    "port_map": {\n      "description": "Dict mapping external Port keys to (InputPort, OutputPort) tuples. Managed automatically by the owning Composition; do not set manually unless you fully understand the CIM structure.",\n      "type": "object"\n    },\n    "prefs": {\n      "description": "PreferenceSet or dict of preference settings for this instance. Omit to use class defaults.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCompositionInterfaceMechanism instances (input_CIM, output_CIM, parameter_CIM) are created and fully managed by PsyNeuLink\'s Composition class — agents should almost never call this tool directly. Calling add_ports on a CIM from user code raises a CompositionError; ports are added only via Composition internals. The port_map is populated automatically and its structure is intricate (keys = external Component, values = (InputPort, OutputPort) tuples); manual construction is fragile. The function parameter defaults to Identity (transparent pass-through) and should only be changed if you understand how InterfaceFunctions interact with port routing. Nested Composition scenarios involve chains of CIMs — inspect the owning Composition\'s input_CIM/output_CIM/parameter_CIM attributes rather than instantiating new ones.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'The Composition this CIM belongs '
                                                  'to. Set automatically when a '
                                                  'Composition creates its CIMs; only '
                                                  'supply when constructing a CIM '
                                                  'manually.',
                                   'type': 'object'},
                  'default_variable': { 'description': 'Initial value(s) for the '
                                                       "mechanism's input; sets the "
                                                       'shape of the variable '
                                                       'processed. Defaults to a '
                                                       'single scalar if omitted.',
                                        'items': {},
                                        'type': 'array'},
                  'function': { 'description': 'The InterfaceFunction used to '
                                               'transform inputs before assigning to '
                                               'OutputPorts. Defaults to Identity '
                                               '(pass-through). Rarely changed in '
                                               'practice.',
                                'type': 'string'},
                  'input_ports': { 'description': 'Specification of InputPort(s) for '
                                                  'the mechanism. Accepts a list of '
                                                  'port specs, a Mechanism, an '
                                                  'OutputPort, or an InputPort. '
                                                  'Managed automatically in normal '
                                                  'use.',
                                   'items': {},
                                   'type': 'array'},
                  'input_shapes': { 'description': 'Shape(s) of the input(s) as '
                                                   'integers or a list of integers. '
                                                   'Alternative to default_variable '
                                                   'for specifying input '
                                                   'dimensionality.',
                                    'items': {'type': 'integer'},
                                    'type': 'array'},
                  'name': { 'description': 'String name for this mechanism instance. '
                                           'Auto-generated if omitted.',
                            'type': 'string'},
                  'params': { 'description': 'Additional parameter overrides passed to '
                                             'the parent Mechanism class.',
                              'type': 'object'},
                  'port_map': { 'description': 'Dict mapping external Port keys to '
                                               '(InputPort, OutputPort) tuples. '
                                               'Managed automatically by the owning '
                                               'Composition; do not set manually '
                                               'unless you fully understand the CIM '
                                               'structure.',
                                'type': 'object'},
                  'prefs': { 'description': 'PreferenceSet or dict of preference '
                                            'settings for this instance. Omit to use '
                                            'class defaults.',
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CompositionInterfaceMechanism instances (input_CIM, output_CIM, parameter_CIM) are created and fully managed by PsyNeuLink's Composition class — agents should almost never call this tool directly. Calling add_ports on a CIM from user code raises a CompositionError; ports are added only via Composition internals. The port_map is populated automatically and its structure is intricate (keys = external Component, values = (InputPort, OutputPort) tuples); manual construction is fragile. The function parameter defaults to Identity (transparent pass-through) and should only be changed if you understand how InterfaceFunctions interact with port routing. Nested Composition scenarios involve chains of CIMs — inspect the owning Composition's input_CIM/output_CIM/parameter_CIM attributes rather than instantiating new ones."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.CompositionInterfaceMechanism
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
    def create_composition_interface_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to explicitly instantiate a CompositionInterfaceMechanism (CIM) for advanced, low-level use — for example, when constructing a Composition manually and needing to reference or configure its input_CIM, output_CIM, or parameter_CIM.'
        return _impl(args or {})
