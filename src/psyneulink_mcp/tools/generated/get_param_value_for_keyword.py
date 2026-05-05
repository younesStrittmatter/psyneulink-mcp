"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '914ab9088be78f2a8146e57d2ff02fd41a8ff8254bb806a207ad9d2763386d74'
__pnl_qualname__ = 'psyneulink.get_param_value_for_keyword'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_param_value_for_keyword'
TOOL_DESCRIPTION = 'Call this tool to retrieve the current value associated with a named keyword parameter on a PsyNeuLink Component\'s function. Use it when you need to inspect a keyword-driven parameter (e.g., a transfer function\'s gain or slope keyword) without navigating the full parameter hierarchy. Returns the resolved value, or None if the keyword is unrecognized and verbose mode is off.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "keyword": {\n      "description": "The keyword string recognized by the Component\'s function subclass (e.g., \'GAIN\', \'SLOPE\', \'ADDITIVE_PARAM\').",\n      "type": "string"\n    },\n    "owner": {\n      "description": "The name or reference of the PsyNeuLink Component whose function\'s keyword value you want to retrieve.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "owner",\n    "keyword"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns None silently if the keyword is unrecognized AND the owner\'s verbosePref is False — the agent will not get an error, just a None result. Only raises FunctionError when verbosePref is False and the function itself raises one (not AttributeError/ParameterNoValueError). The owner argument must be a live Component instance with a `.function` attribute; passing a class rather than an instance will cause an AttributeError. Keyword strings are typically uppercase constants defined in the PsyNeuLink keywords module.'
TOOL_PARAMETERS = { 'properties': { 'keyword': { 'description': 'The keyword string recognized by the '
                                              "Component's function subclass (e.g., "
                                              "'GAIN', 'SLOPE', 'ADDITIVE_PARAM').",
                               'type': 'string'},
                  'owner': { 'description': 'The name or reference of the PsyNeuLink '
                                            "Component whose function's keyword value "
                                            'you want to retrieve.',
                             'type': 'string'}},
  'required': ['owner', 'keyword'],
  'type': 'object'}
TOOL_NOTES = "Returns None silently if the keyword is unrecognized AND the owner's verbosePref is False — the agent will not get an error, just a None result. Only raises FunctionError when verbosePref is False and the function itself raises one (not AttributeError/ParameterNoValueError). The owner argument must be a live Component instance with a `.function` attribute; passing a class rather than an instance will cause an AttributeError. Keyword strings are typically uppercase constants defined in the PsyNeuLink keywords module."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_param_value_for_keyword
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
    def get_param_value_for_keyword(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to retrieve the current value associated with a named keyword parameter on a PsyNeuLink Component's function."
        return _impl(args or {})
