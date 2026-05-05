"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b48f4219d83b5c50ebf7ff485bdd6041e4de7a5c645f65cf17f78be95045381e'
__pnl_qualname__ = 'psyneulink.DefaultsFlexibility'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_defaults_flexibility'
TOOL_DESCRIPTION = 'Call this tool to retrieve a `DefaultsFlexibility` enum member by integer value when you need to pass a flexibility policy to a PsyNeuLink component\'s default-variable assignment logic. Returns the enum member (FLEXIBLE=0, RIGID=1, INCREASE_DIMENSION=2). In practice, most agents will not call this directly — they pass the string name or enum member inline when constructing Mechanisms or Functions — but use this tool when you need to resolve or inspect the enum value programmatically.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Integer value of the enum member to retrieve: 0 = FLEXIBLE (default can be modified freely), 1 = RIGID (cannot be modified), 2 = INCREASE_DIMENSION (can be wrapped in one extra dimension).",\n      "enum": [\n        0,\n        1,\n        2\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a pure enum — it has no keyword arguments. The host instantiates it as `DefaultsFlexibility(value)`, i.e., a single positional integer. FLEXIBLE (0) is the most permissive and is the implicit default when PsyNeuLink infers a default variable from context. RIGID (1) blocks any automatic reshaping, which can cause errors if owner and function shapes disagree. INCREASE_DIMENSION (2) allows only wrapping in one extra array dimension, not arbitrary reshaping. Agents almost never need to instantiate this enum themselves; they encounter it as an attribute on Component class defaults or pass it as a keyword value like `defaults_flexibility=pnl.DefaultsFlexibility.FLEXIBLE`.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Integer value of the enum member to '
                                            'retrieve: 0 = FLEXIBLE (default can be '
                                            'modified freely), 1 = RIGID (cannot be '
                                            'modified), 2 = INCREASE_DIMENSION (can be '
                                            'wrapped in one extra dimension).',
                             'enum': [0, 1, 2],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'This is a pure enum — it has no keyword arguments. The host instantiates it as `DefaultsFlexibility(value)`, i.e., a single positional integer. FLEXIBLE (0) is the most permissive and is the implicit default when PsyNeuLink infers a default variable from context. RIGID (1) blocks any automatic reshaping, which can cause errors if owner and function shapes disagree. INCREASE_DIMENSION (2) allows only wrapping in one extra array dimension, not arbitrary reshaping. Agents almost never need to instantiate this enum themselves; they encounter it as an attribute on Component class defaults or pass it as a keyword value like `defaults_flexibility=pnl.DefaultsFlexibility.FLEXIBLE`.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DefaultsFlexibility
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
    def create_defaults_flexibility(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to retrieve a `DefaultsFlexibility` enum member by integer value when you need to pass a flexibility policy to a PsyNeuLink component's default-variable assignment logic."
        return _impl(args or {})
