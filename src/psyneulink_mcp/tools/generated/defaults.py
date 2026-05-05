"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a6090e98e2fff6b926570b0ce6c05f23a95c58024ad9b3367dda826cf2ea63d4'
__pnl_qualname__ = 'psyneulink.Defaults'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_defaults'
TOOL_DESCRIPTION = 'Call this tool to read or bulk-override default parameter values on a PsyNeuLink Parameters object. Use it when you need to inspect current defaults before a run, or to set multiple parameter defaults at once without touching individual Parameter objects. The result is a live Defaults proxy: reading an attribute returns that parameter\'s current default_value; writing an attribute immediately mutates it on the owning Parameters object.\n\nParameters (JSON Schema):\n{\n  "additionalProperties": {\n    "description": "Optional per-parameter overrides: key is the parameter name, value is the new default_value to apply at construction time.",\n    "type": [\n      "number",\n      "boolean",\n      "string",\n      "array",\n      "object"\n    ]\n  },\n  "properties": {\n    "owner": {\n      "description": "Python expression that resolves to the Parameters object whose defaults you want to manage, e.g. \'my_mechanism.parameters\' or \'my_composition.parameters\'.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "owner"\n  ],\n  "type": "object"\n}\n\nNotes:\nowner must be a Parameters instance (e.g., component.parameters) — it cannot be a raw dict. The owner argument is marked as a string in the schema for JSON transport; the host must resolve it to the actual Python object before instantiation. Keyword overrides are applied silently: an unrecognised key is ignored with no error (KeyError is caught internally). The proxy is live — any attribute set after construction immediately changes the owning Parameters object\'s default_value, which affects all future runs. Use values(show_all=False) to enumerate only user-facing parameters; pass show_all=True to include internal ones.'
TOOL_PARAMETERS = { 'additionalProperties': { 'description': 'Optional per-parameter overrides: key is '
                                           'the parameter name, value is the new '
                                           'default_value to apply at construction '
                                           'time.',
                            'type': ['number', 'boolean', 'string', 'array', 'object']},
  'properties': { 'owner': { 'description': 'Python expression that resolves to the '
                                            'Parameters object whose defaults you want '
                                            "to manage, e.g. 'my_mechanism.parameters' "
                                            "or 'my_composition.parameters'.",
                             'type': 'string'}},
  'required': ['owner'],
  'type': 'object'}
TOOL_NOTES = "owner must be a Parameters instance (e.g., component.parameters) — it cannot be a raw dict. The owner argument is marked as a string in the schema for JSON transport; the host must resolve it to the actual Python object before instantiation. Keyword overrides are applied silently: an unrecognised key is ignored with no error (KeyError is caught internally). The proxy is live — any attribute set after construction immediately changes the owning Parameters object's default_value, which affects all future runs. Use values(show_all=False) to enumerate only user-facing parameters; pass show_all=True to include internal ones."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Defaults
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
    def create_defaults(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to read or bulk-override default parameter values on a PsyNeuLink Parameters object.'
        return _impl(args or {})
