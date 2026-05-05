"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '3cb278cc64d18cbcf4ef58f7b2d061508fc1c0cad620f0da69138ad9378478bd'
__pnl_qualname__ = 'psyneulink.Port'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_port'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — `Port` is an abstract shell class that raises errors on every method call. Use concrete subclasses instead: `create_input_port`, `create_output_port`, or `create_parameter_port` depending on the signal direction. Only reference this tool if you need to check whether an object is a Port instance (isinstance check) or explore the abstract interface.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input to the Port\'s function; also used as the default value when no input is provided. Typically a list or array of numbers.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Specifies shape of default_variable as zero-filled array(s) when default_variable is not provided. Must be compatible with default_variable if both are given.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "integer"\n              },\n              {\n                "items": {\n                  "type": "integer"\n                },\n                "type": "array"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for the Port; assigned by registry if omitted.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Parameter dictionary overriding constructor argument values. Keys are parameter names, values are their settings.",\n      "type": "object"\n    },\n    "prefs": {\n      "description": "PreferenceSet or specification dict for the Port\'s preferences.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n`Port` is a pure abstract shell class in `psyneulink.core.components.shellclasses`. Every method (owner, _validate_variable, _validate_params, _update, set_value, add_observer_for_keypath) raises `ShellClassError` — instantiating or calling it will always fail. The docstring shown is inherited from `Component`, not from `Port` itself. Agents should never invoke this tool; route all Port creation to InputPort, OutputPort, ParameterPort, or ModulatoryPort concrete tools.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input to the '
                                                       "Port's function; also used as "
                                                       'the default value when no '
                                                       'input is provided. Typically a '
                                                       'list or array of numbers.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Specifies shape of '
                                                   'default_variable as zero-filled '
                                                   'array(s) when default_variable is '
                                                   'not provided. Must be compatible '
                                                   'with default_variable if both are '
                                                   'given.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': { 'oneOf': [ { 'type': 'integer'},
                                                                       { 'items': { 'type': 'integer'},
                                                                         'type': 'array'}]},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Name for the Port; assigned by registry if '
                                           'omitted.',
                            'type': 'string'},
                  'params': { 'description': 'Parameter dictionary overriding '
                                             'constructor argument values. Keys are '
                                             'parameter names, values are their '
                                             'settings.',
                              'type': 'object'},
                  'prefs': { 'description': 'PreferenceSet or specification dict for '
                                            "the Port's preferences.",
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '`Port` is a pure abstract shell class in `psyneulink.core.components.shellclasses`. Every method (owner, _validate_variable, _validate_params, _update, set_value, add_observer_for_keypath) raises `ShellClassError` — instantiating or calling it will always fail. The docstring shown is inherited from `Component`, not from `Port` itself. Agents should never invoke this tool; route all Port creation to InputPort, OutputPort, ParameterPort, or ModulatoryPort concrete tools.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Port
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
    def create_port(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — `Port` is an abstract shell class that raises errors on every method call.'
        return _impl(args or {})
