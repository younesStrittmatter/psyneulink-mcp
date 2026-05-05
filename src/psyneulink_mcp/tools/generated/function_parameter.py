"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'dc1af3b4e144afb2f9991d0865a9ccc1840637bc662e110535e3f7ccf80a0416'
__pnl_qualname__ = 'psyneulink.FunctionParameter'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_function_parameter'
TOOL_DESCRIPTION = 'Call this tool when defining a PsyNeuLink Component\'s `Parameters` class and you need to expose one of the component\'s function\'s parameters as a top-level parameter on the Component itself. Use it instead of a plain `Parameter` whenever the value should stay in sync with a named parameter on an inner function (e.g., `noise`, `gain`, `rate` on a `TransferMechanism`\'s `function`). Returns a `FunctionParameter` descriptor instance that wires the component-level attribute to the function-level attribute automatically.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_value": {\n      "description": "Default value for this parameter. Passed through to the underlying Parameter. Use None to inherit the function parameter\'s default.",\n      "type": [\n        "number",\n        "boolean",\n        "string",\n        "array",\n        "object",\n        "null"\n      ]\n    },\n    "function_name": {\n      "default": "function",\n      "description": "Name of the Component attribute that holds the function whose parameter is being shared. Almost always \'function\' (the default).",\n      "type": "string"\n    },\n    "function_parameter_name": {\n      "description": "Name of the target parameter on the function referred to by function_name. Defaults to the name of this FunctionParameter itself (i.e., the attribute name in the Parameters class).",\n      "type": "string"\n    },\n    "primary": {\n      "default": true,\n      "description": "Whether this is the primary (authoritative) shared parameter. Defaults to True. Set to False when multiple FunctionParameters alias the same underlying function parameter.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `function_parameter_name` silently defaults to `Parameter.name`, meaning the name of the attribute in the enclosing `Parameters` class. Only set it explicitly when the component-level name differs from the function-level name.\n- This is a *class-definition-time* descriptor used inside a Component\'s nested `Parameters` class; it does not meaningfully stand alone outside that pattern.\n- `**kwargs` are forwarded to `SharedParameter` / `Parameter` (e.g., `aliases`, `modulable`, `read_only`) — include them as additional top-level properties if needed.\n- Setting `primary=False` on all aliases or on none can cause unexpected sync behavior; leave it `True` unless you understand PNL\'s shared-parameter resolution order.'
TOOL_PARAMETERS = { 'properties': { 'default_value': { 'description': 'Default value for this parameter. '
                                                    'Passed through to the underlying '
                                                    'Parameter. Use None to inherit '
                                                    "the function parameter's default.",
                                     'type': [ 'number',
                                               'boolean',
                                               'string',
                                               'array',
                                               'object',
                                               'null']},
                  'function_name': { 'default': 'function',
                                     'description': 'Name of the Component attribute '
                                                    'that holds the function whose '
                                                    'parameter is being shared. Almost '
                                                    "always 'function' (the default).",
                                     'type': 'string'},
                  'function_parameter_name': { 'description': 'Name of the target '
                                                              'parameter on the '
                                                              'function referred to by '
                                                              'function_name. Defaults '
                                                              'to the name of this '
                                                              'FunctionParameter '
                                                              'itself (i.e., the '
                                                              'attribute name in the '
                                                              'Parameters class).',
                                               'type': 'string'},
                  'primary': { 'default': True,
                               'description': 'Whether this is the primary '
                                              '(authoritative) shared parameter. '
                                              'Defaults to True. Set to False when '
                                              'multiple FunctionParameters alias the '
                                              'same underlying function parameter.',
                               'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- `function_parameter_name` silently defaults to `Parameter.name`, meaning the name of the attribute in the enclosing `Parameters` class. Only set it explicitly when the component-level name differs from the function-level name.\n- This is a *class-definition-time* descriptor used inside a Component's nested `Parameters` class; it does not meaningfully stand alone outside that pattern.\n- `**kwargs` are forwarded to `SharedParameter` / `Parameter` (e.g., `aliases`, `modulable`, `read_only`) — include them as additional top-level properties if needed.\n- Setting `primary=False` on all aliases or on none can cause unexpected sync behavior; leave it `True` unless you understand PNL's shared-parameter resolution order."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.FunctionParameter
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
    def create_function_parameter(args: dict[str, Any] | None = None) -> Any:
        "Call this tool when defining a PsyNeuLink Component's `Parameters` class and you need to expose one of the component's function's parameters as a top-level parameter on the Component itself."
        return _impl(args or {})
