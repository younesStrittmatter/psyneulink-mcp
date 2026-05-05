"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '3538b036ab9e72916959ceb70e953a704c684b2be7b9d6e78785256bc8a656f0'
__pnl_qualname__ = 'psyneulink.is_component'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_component'
TOOL_DESCRIPTION = 'Call this tool to check whether a given value is an instance of a PsyNeuLink Component. Returns true if the value is a Component, false otherwise. Useful for runtime validation or conditional logic when you need to confirm an object is a Component before passing it to Component-specific operations.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "val": {\n      "description": "The value to test. Should be a reference or representation of a Python object to check for Component membership.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "val"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a simple isinstance check against PsyNeuLink\'s Component base class. Because MCP communication is JSON-based, `val` will arrive as a string; the underlying Python check will almost always return false unless the server maintains a Python object registry mapping names/IDs to live objects. This tool has limited utility for agents operating purely through JSON-serialized calls — it is more useful for internal server-side or code-generation contexts where a Python object reference can be passed directly.'
TOOL_PARAMETERS = { 'properties': { 'val': { 'description': 'The value to test. Should be a reference or '
                                          'representation of a Python object to check '
                                          'for Component membership.',
                           'type': 'string'}},
  'required': ['val'],
  'type': 'object'}
TOOL_NOTES = "This is a simple isinstance check against PsyNeuLink's Component base class. Because MCP communication is JSON-based, `val` will arrive as a string; the underlying Python check will almost always return false unless the server maintains a Python object registry mapping names/IDs to live objects. This tool has limited utility for agents operating purely through JSON-serialized calls — it is more useful for internal server-side or code-generation contexts where a Python object reference can be passed directly."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_component
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
    def is_component(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a given value is an instance of a PsyNeuLink Component.'
        return _impl(args or {})
