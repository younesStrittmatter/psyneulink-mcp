"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'fc25861e53c25b9181292bd168b5170cfcfaf4e56c615b00ccaff72b1fc30d1b'
__pnl_qualname__ = 'psyneulink.get_param_value_for_function'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_param_value_for_function'
TOOL_DESCRIPTION = 'Call this tool to retrieve the value that a PsyNeuLink owner component\'s function returns for a given parameter function. Use it when you need to evaluate what a component\'s `param_function` would produce for a specific function argument. Returns the computed value, or `null` if the owner\'s function does not support `param_function` or a `FunctionError` occurs.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "description": "The name or identifier of the function to pass to the owner\'s param_function method.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "The name of the PsyNeuLink component whose function.param_function will be evaluated (e.g., a Mechanism or Projection name).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "owner",\n    "function"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a low-level internal utility. It silently returns `null` on both `FunctionError` and `AttributeError` — if verbose preferences are enabled on the owner it will print an error message, but the tool itself will still return `null` with no exception raised. Only works when the owner already exists in the PsyNeuLink runtime context and its `.function` attribute exposes a `param_function` method; most standard functions do not.'
TOOL_PARAMETERS = { 'properties': { 'function': { 'description': 'The name or identifier of the function '
                                               "to pass to the owner's param_function "
                                               'method.',
                                'type': 'string'},
                  'owner': { 'description': 'The name of the PsyNeuLink component '
                                            'whose function.param_function will be '
                                            'evaluated (e.g., a Mechanism or '
                                            'Projection name).',
                             'type': 'string'}},
  'required': ['owner', 'function'],
  'type': 'object'}
TOOL_NOTES = 'This is a low-level internal utility. It silently returns `null` on both `FunctionError` and `AttributeError` — if verbose preferences are enabled on the owner it will print an error message, but the tool itself will still return `null` with no exception raised. Only works when the owner already exists in the PsyNeuLink runtime context and its `.function` attribute exposes a `param_function` method; most standard functions do not.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_param_value_for_function
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
    def get_param_value_for_function(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to retrieve the value that a PsyNeuLink owner component's function returns for a given parameter function."
        return _impl(args or {})
