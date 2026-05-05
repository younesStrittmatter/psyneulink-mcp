"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '99392ff90fa70bee4475a06b74e4f5a052af099279aded6c01c66fadf170e88c'
__pnl_qualname__ = 'psyneulink.Port_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_port__base'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — Port_Base is an abstract class and instantiating it will raise an error. Call this tool only when you need to inspect the shared Port interface (attributes like `all_afferents`, `mod_afferents`, `path_afferents`, `efferents`, `projections`, `value`, `function`, `owner`, `name`) on an already-existing Port object, or when you need documentation on the Port base-class contract. To create a Port, use InputPort, OutputPort, ParameterPort, or another concrete subclass instead.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "description": "TransferFunction used to compute the Port\'s value from its afferent Projections. Defaults to Linear. Parameters tagged ADDITIVE or MULTIPLICATIVE in the function are subject to modulation by ModulatorySignals.",\n      "type": "string"\n    },\n    "input_shapes": {\n      "description": "Sets variable to an array of zeros with this shape when variable is not specified. An integer or list of integers.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this Port. Scoped to the owner Mechanism \\u2014 the same name may exist on different Mechanisms but not twice on the same one; duplicates within a Mechanism get an indexed suffix.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "Name or reference to the Mechanism (or Projection) to which this Port belongs. Required at construction time; if not determinable from context, initialization is deferred.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Additional parameter overrides passed as a dict. Rarely needed; prefer named arguments.",\n      "type": "object"\n    },\n    "prefs": {\n      "description": "PreferenceSet or specification dict for Port-level preferences. Defaults to classPreferences defined in __init__.py.",\n      "type": "object"\n    },\n    "projections": {\n      "description": "Projection(s) to/from this Port. Can be a Projection object, class, specification dict, or list of any of those.",\n      "oneOf": [\n        {\n          "type": "object"\n        },\n        {\n          "items": {\n            "type": "object"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "variable": {\n      "description": "The Port\'s input value \\u2014 a number, list, or array. Determines the shape passed to the Port\'s function.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nPort_Base is decorated with @abc.abstractmethod on __init__ — calling psyneulink.Port_Base(...) directly raises a TypeError. Always use a concrete subclass: InputPort, OutputPort, ParameterPort, ControlSignal, LearningSignal, or GatingSignal. The `owner` argument is effectively required; omitting it puts the Port into deferred-initialization status with a temporary name, and many methods will fail until initialization is completed by a Mechanism or Composition. `path_afferents` is only populated for InputPorts; `efferents` is only populated for OutputPorts and ModulatorySignals; accessing these on the wrong subtype raises PortError. Port names are registry-scoped to their owner Mechanism, not globally unique.'
TOOL_PARAMETERS = { 'properties': { 'function': { 'description': 'TransferFunction used to compute the '
                                               "Port's value from its afferent "
                                               'Projections. Defaults to Linear. '
                                               'Parameters tagged ADDITIVE or '
                                               'MULTIPLICATIVE in the function are '
                                               'subject to modulation by '
                                               'ModulatorySignals.',
                                'type': 'string'},
                  'input_shapes': { 'description': 'Sets variable to an array of zeros '
                                                   'with this shape when variable is '
                                                   'not specified. An integer or list '
                                                   'of integers.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Name for this Port. Scoped to the owner '
                                           'Mechanism — the same name may exist on '
                                           'different Mechanisms but not twice on the '
                                           'same one; duplicates within a Mechanism '
                                           'get an indexed suffix.',
                            'type': 'string'},
                  'owner': { 'description': 'Name or reference to the Mechanism (or '
                                            'Projection) to which this Port belongs. '
                                            'Required at construction time; if not '
                                            'determinable from context, initialization '
                                            'is deferred.',
                             'type': 'string'},
                  'params': { 'description': 'Additional parameter overrides passed as '
                                             'a dict. Rarely needed; prefer named '
                                             'arguments.',
                              'type': 'object'},
                  'prefs': { 'description': 'PreferenceSet or specification dict for '
                                            'Port-level preferences. Defaults to '
                                            'classPreferences defined in __init__.py.',
                             'type': 'object'},
                  'projections': { 'description': 'Projection(s) to/from this Port. '
                                                  'Can be a Projection object, class, '
                                                  'specification dict, or list of any '
                                                  'of those.',
                                   'oneOf': [ {'type': 'object'},
                                              { 'items': {'type': 'object'},
                                                'type': 'array'}]},
                  'variable': { 'description': "The Port's input value — a number, "
                                               'list, or array. Determines the shape '
                                               "passed to the Port's function.",
                                'oneOf': [ {'type': 'number'},
                                           { 'items': {'type': 'number'},
                                             'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Port_Base is decorated with @abc.abstractmethod on __init__ — calling psyneulink.Port_Base(...) directly raises a TypeError. Always use a concrete subclass: InputPort, OutputPort, ParameterPort, ControlSignal, LearningSignal, or GatingSignal. The `owner` argument is effectively required; omitting it puts the Port into deferred-initialization status with a temporary name, and many methods will fail until initialization is completed by a Mechanism or Composition. `path_afferents` is only populated for InputPorts; `efferents` is only populated for OutputPorts and ModulatorySignals; accessing these on the wrong subtype raises PortError. Port names are registry-scoped to their owner Mechanism, not globally unique.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Port_Base
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
    def create_port__base(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — Port_Base is an abstract class and instantiating it will raise an error.'
        return _impl(args or {})
