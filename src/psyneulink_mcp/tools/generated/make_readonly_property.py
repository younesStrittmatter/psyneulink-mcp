"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6d755d0a7fc6727f4f468b01f19c5e47f8e90c930e95f9cff94d21ffc00270e1'
__pnl_qualname__ = 'psyneulink.make_readonly_property'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'make_readonly_property'
TOOL_DESCRIPTION = 'Call this tool when you need to create a read-only property descriptor for embedding in a PsyNeuLink class definition — for example, when building a custom Component subclass that should expose a constant value as an attribute but block any assignment to it. The tool returns a Python `property` object whose getter always returns `val` and whose setter raises `UtilitiesError`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Human-readable name for the property, used only in the UtilitiesError message on set attempts. Defaults to `val` when omitted.",\n      "type": "string"\n    },\n    "val": {\n      "description": "The value the property will always return when accessed. Also used as the display name in error messages if `name` is not provided.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "val"\n  ],\n  "type": "object"\n}\n\nNotes:\nBecause `name` defaults to `val`, if `val` is not a plain string the auto-generated error message may be hard to read — pass an explicit `name` string in that case. The setter raises `UtilitiesError`, not the standard `AttributeError`, so callers catching `AttributeError` will not intercept assignment attempts. This is a meta-programming helper intended for class-body use; calling it outside a class definition produces a property object with no host class and limited practical utility as a standalone MCP result.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Human-readable name for the property, used '
                                           'only in the UtilitiesError message on set '
                                           'attempts. Defaults to `val` when omitted.',
                            'type': 'string'},
                  'val': { 'description': 'The value the property will always return '
                                          'when accessed. Also used as the display '
                                          'name in error messages if `name` is not '
                                          'provided.',
                           'type': 'string'}},
  'required': ['val'],
  'type': 'object'}
TOOL_NOTES = 'Because `name` defaults to `val`, if `val` is not a plain string the auto-generated error message may be hard to read — pass an explicit `name` string in that case. The setter raises `UtilitiesError`, not the standard `AttributeError`, so callers catching `AttributeError` will not intercept assignment attempts. This is a meta-programming helper intended for class-body use; calling it outside a class definition produces a property object with no host class and limited practical utility as a standalone MCP result.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.make_readonly_property
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
    def make_readonly_property(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to create a read-only property descriptor for embedding in a PsyNeuLink class definition — for example, when building a custom Component subclass that should expose a constant value as an attribute but block any assignment to it.'
        return _impl(args or {})
