"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b878afca9fca90ac1a952605ca8d39a37f25ebebf1411a7f545b9c48a3eaeec3'
__pnl_qualname__ = 'psyneulink.Component'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_component'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — Component is an abstract base class that cannot be instantiated. Use it only as a reference for the constructor arguments shared by all PsyNeuLink subclasses (Mechanisms, Projections, Functions, Ports, Compositions). Call the specific subclass tool instead (e.g., TransferMechanism, MappingProjection, Composition). If you need to inspect the common parameter schema across all components, this entry documents those shared arguments.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input to the Component\'s function; also used as the default input when none is provided at execution. Accepts a scalar, list, or array. Defaults to [[0]] if neither this nor input_shapes is specified.",\n      "type": "array"\n    },\n    "function": {\n      "description": "The function the component executes. Can be a Function class, an instantiated Function object, or a plain Python callable. If omitted, the subclass default function is used.",\n      "type": "string"\n    },\n    "input_shapes": {\n      "description": "Alternative way to set default_variable as an array of zeros with the given shape(s). An int specifies a 1-D input of that length; an iterable of ints/tuples specifies multiple input ports. Ignored if default_variable is also specified (they must be compatible).",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "String name for this component. If omitted, the relevant Registry assigns a default name following Registry_Naming conventions.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Parameter dictionary overriding constructor arguments. Keys are parameter names (strings), values are the desired parameter values. Values here take precedence over named constructor arguments.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nComponent is abstract and raises an error if instantiated directly — always use a concrete subclass. The constructor argument for \'variable\' is \'default_variable\', not \'variable\'; passing \'variable\' will raise an error. The deprecated argument \'size\' has been renamed to \'input_shapes\'; using \'size\' raises a ComponentError. If both default_variable and input_shapes are given, they must be compatible in shape or a ComponentError is raised. The \'params\' dict overrides any named argument for the same parameter — order of precedence: params > kwargs > positional. \'context\' is an internal argument used by PsyNeuLink infrastructure; agents should not pass it.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input to the '
                                                       "Component's function; also "
                                                       'used as the default input when '
                                                       'none is provided at execution. '
                                                       'Accepts a scalar, list, or '
                                                       'array. Defaults to [[0]] if '
                                                       'neither this nor input_shapes '
                                                       'is specified.',
                                        'type': 'array'},
                  'function': { 'description': 'The function the component executes. '
                                               'Can be a Function class, an '
                                               'instantiated Function object, or a '
                                               'plain Python callable. If omitted, the '
                                               'subclass default function is used.',
                                'type': 'string'},
                  'input_shapes': { 'description': 'Alternative way to set '
                                                   'default_variable as an array of '
                                                   'zeros with the given shape(s). An '
                                                   'int specifies a 1-D input of that '
                                                   'length; an iterable of ints/tuples '
                                                   'specifies multiple input ports. '
                                                   'Ignored if default_variable is '
                                                   'also specified (they must be '
                                                   'compatible).',
                                    'oneOf': [{'type': 'integer'}, {'type': 'array'}]},
                  'name': { 'description': 'String name for this component. If '
                                           'omitted, the relevant Registry assigns a '
                                           'default name following Registry_Naming '
                                           'conventions.',
                            'type': 'string'},
                  'params': { 'description': 'Parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter names (strings), values are '
                                             'the desired parameter values. Values '
                                             'here take precedence over named '
                                             'constructor arguments.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Component is abstract and raises an error if instantiated directly — always use a concrete subclass. The constructor argument for 'variable' is 'default_variable', not 'variable'; passing 'variable' will raise an error. The deprecated argument 'size' has been renamed to 'input_shapes'; using 'size' raises a ComponentError. If both default_variable and input_shapes are given, they must be compatible in shape or a ComponentError is raised. The 'params' dict overrides any named argument for the same parameter — order of precedence: params > kwargs > positional. 'context' is an internal argument used by PsyNeuLink infrastructure; agents should not pass it."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Component
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
    def create_component(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — Component is an abstract base class that cannot be instantiated.'
        return _impl(args or {})
