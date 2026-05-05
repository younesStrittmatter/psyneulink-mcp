"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b878afca9fca90ac1a952605ca8d39a37f25ebebf1411a7f545b9c48a3eaeec3'
__pnl_qualname__ = 'psyneulink.COMPONENT_BASE_CLASS'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_component_base_class'
TOOL_DESCRIPTION = 'DO NOT call this tool to create a PsyNeuLink component — Component is an abstract base class that cannot be instantiated directly and will raise an error. Call a subclass-specific tool instead (e.g., TransferMechanism, RecurrentTransferMechanism, Composition, LCAMechanism, etc.). This entry exists only so agents can inspect the shared constructor arguments that every PsyNeuLink component accepts; the parameter names and semantics documented here apply to all subclass tools.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input to the component\'s function, and the default value used when no input is provided on execution. Must be a scalar, list, or array. If omitted, the subclass default is used.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "array"\n        }\n      ]\n    },\n    "input_shapes": {\n      "description": "Alternative to default_variable: specifies the shape of the input as an int (single port) or list of ints/tuples (multiple ports). numpy.zeros(input_shapes) is used to construct the variable. Conflicts with default_variable if both specify incompatible shapes.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "integer"\n              },\n              {\n                "type": "array"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "String name for the component. If omitted, a default name is assigned by the relevant Registry (e.g., \'TransferMechanism-0\').",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Parameter dictionary mapping parameter keyword strings to values. Entries override values set by constructor arguments. Can include a \'function\' key to specify or override the component\'s function.",\n      "type": "object"\n    },\n    "prefs": {\n      "additionalProperties": true,\n      "description": "PreferenceSet or specification dict controlling verbosity, parameter validation, output reporting, and logging. Rarely needed; omit to use class defaults.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nComponent is abstract — instantiating it directly raises an error. Always use a concrete subclass tool. The `input_shapes` and `default_variable` arguments conflict if both are provided with incompatible shapes; prefer one or the other. The `params` dict entries override identically-named constructor arguments, so a value in `params` silently wins over an explicit keyword argument. The `context` argument accepted by the real constructor is an internal PNL construct and should never be passed by an agent. The deprecated `size` argument (renamed to `input_shapes`) will raise an error if used.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input to the '
                                                       "component's function, and the "
                                                       'default value used when no '
                                                       'input is provided on '
                                                       'execution. Must be a scalar, '
                                                       'list, or array. If omitted, '
                                                       'the subclass default is used.',
                                        'oneOf': [ {'type': 'number'},
                                                   {'type': 'array'}]},
                  'input_shapes': { 'description': 'Alternative to default_variable: '
                                                   'specifies the shape of the input '
                                                   'as an int (single port) or list of '
                                                   'ints/tuples (multiple ports). '
                                                   'numpy.zeros(input_shapes) is used '
                                                   'to construct the variable. '
                                                   'Conflicts with default_variable if '
                                                   'both specify incompatible shapes.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': { 'oneOf': [ { 'type': 'integer'},
                                                                       { 'type': 'array'}]},
                                                 'type': 'array'}]},
                  'name': { 'description': 'String name for the component. If omitted, '
                                           'a default name is assigned by the relevant '
                                           "Registry (e.g., 'TransferMechanism-0').",
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Parameter dictionary mapping parameter '
                                             'keyword strings to values. Entries '
                                             'override values set by constructor '
                                             "arguments. Can include a 'function' key "
                                             "to specify or override the component's "
                                             'function.',
                              'type': 'object'},
                  'prefs': { 'additionalProperties': True,
                             'description': 'PreferenceSet or specification dict '
                                            'controlling verbosity, parameter '
                                            'validation, output reporting, and '
                                            'logging. Rarely needed; omit to use class '
                                            'defaults.',
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Component is abstract — instantiating it directly raises an error. Always use a concrete subclass tool. The `input_shapes` and `default_variable` arguments conflict if both are provided with incompatible shapes; prefer one or the other. The `params` dict entries override identically-named constructor arguments, so a value in `params` silently wins over an explicit keyword argument. The `context` argument accepted by the real constructor is an internal PNL construct and should never be passed by an agent. The deprecated `size` argument (renamed to `input_shapes`) will raise an error if used.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.COMPONENT_BASE_CLASS
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
    def create_component_base_class(args: dict[str, Any] | None = None) -> Any:
        'DO NOT call this tool to create a PsyNeuLink component — Component is an abstract base class that cannot be instantiated directly and will raise an error.'
        return _impl(args or {})
