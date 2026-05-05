"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9c96e179130c326fc527699b8c5a5724e1dff94aa3c958a3296b2c598dea757c'
__pnl_qualname__ = 'psyneulink.ModulatoryMechanism_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_modulatory_mechanism__base'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — ModulatoryMechanism_Base is an abstract class that must never be instantiated. Use a concrete subclass tool instead (e.g., ControlMechanism, GatingMechanism, LearningMechanism). This tool exists only as a reference for shared modulation parameters common to all modulatory mechanisms.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Default input value(s) for the mechanism; sets the shape of the input.",\n      "type": "array"\n    },\n    "function": {\n      "description": "Function used to compute the mechanism\'s output; subclass default applies if omitted.",\n      "type": "object"\n    },\n    "input_shapes": {\n      "description": "Shape(s) of the mechanism\'s input ports as integer(s); alternative to default_variable.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "modulation": {\n      "description": "Specifies how ModulatorySignal output is applied to modulate target Port values (e.g., \'multiplicative\', \'additive\', \'override\', \'disable\'). Defaults to None (subclass default applies).",\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for the mechanism instance; auto-generated if omitted.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Dictionary of parameter overrides; keys are parameter names, values are settings.",\n      "type": "object"\n    },\n    "prefs": {\n      "description": "Preference settings for the mechanism; rarely needed.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis is an abstract class — calling it directly will raise an error or produce an unusable object. Always use a concrete subclass: ControlMechanism, LCControlMechanism, GatingMechanism, LearningMechanism, or AutoAssociativeLearningMechanism. The `modulation` parameter\'s valid string values are subclass-dependent; common values are \'multiplicative\', \'additive\', \'override\', and \'disable\'. The `modulation` default is None, which means the subclass picks its own default at init time.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Default input value(s) for the '
                                                       'mechanism; sets the shape of '
                                                       'the input.',
                                        'type': 'array'},
                  'function': { 'description': 'Function used to compute the '
                                               "mechanism's output; subclass default "
                                               'applies if omitted.',
                                'type': 'object'},
                  'input_shapes': { 'description': "Shape(s) of the mechanism's input "
                                                   'ports as integer(s); alternative '
                                                   'to default_variable.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'}]},
                  'modulation': { 'description': 'Specifies how ModulatorySignal '
                                                 'output is applied to modulate target '
                                                 "Port values (e.g., 'multiplicative', "
                                                 "'additive', 'override', 'disable'). "
                                                 'Defaults to None (subclass default '
                                                 'applies).',
                                  'type': 'string'},
                  'name': { 'description': 'Name for the mechanism instance; '
                                           'auto-generated if omitted.',
                            'type': 'string'},
                  'params': { 'description': 'Dictionary of parameter overrides; keys '
                                             'are parameter names, values are '
                                             'settings.',
                              'type': 'object'},
                  'prefs': { 'description': 'Preference settings for the mechanism; '
                                            'rarely needed.',
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "This is an abstract class — calling it directly will raise an error or produce an unusable object. Always use a concrete subclass: ControlMechanism, LCControlMechanism, GatingMechanism, LearningMechanism, or AutoAssociativeLearningMechanism. The `modulation` parameter's valid string values are subclass-dependent; common values are 'multiplicative', 'additive', 'override', and 'disable'. The `modulation` default is None, which means the subclass picks its own default at init time."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ModulatoryMechanism_Base
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
    def create_modulatory_mechanism__base(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — ModulatoryMechanism_Base is an abstract class that must never be instantiated.'
        return _impl(args or {})
