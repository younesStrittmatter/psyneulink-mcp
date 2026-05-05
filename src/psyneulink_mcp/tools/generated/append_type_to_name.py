"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '562c307e27f7dc248670c5a11019575e08321ab660d1f43c7d5cd98d78f2ed4a'
__pnl_qualname__ = 'psyneulink.append_type_to_name'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'append_type_to_name'
TOOL_DESCRIPTION = 'Call this tool to format a PsyNeuLink component\'s display name by appending its type label. Returns either the bare name (if the type word already appears in it) or a string like `\'name\' typename`. Use it when you need a human-readable label for a component and want to avoid redundant type suffixes.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "object": {\n      "description": "The PsyNeuLink component instance to format. Must have a `.name` string attribute and a resolvable class hierarchy. This is a live Python object \\u2014 pass a reference to an already-constructed PsyNeuLink component.",\n      "type": "object"\n    },\n    "type": {\n      "description": "Optional override for the type label appended to the name. If omitted, the function uses the immediate parent class name (`object.__class__.__base__.__name__`). Provide this when the inferred class name is wrong or too generic.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "object"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `object` argument must be a live PsyNeuLink component instance — it cannot be a string or dict. This makes the tool nearly uncallable from a pure JSON MCP context; it is intended as an internal utility. If you need a formatted name, construct the component first via the appropriate mechanism tool, then pass it here. The type-collision check is case-insensitive across three variants (lower, upper, capitalize), so `\'TransferMechanism\' mechanism` will NOT be produced — the bare name is returned instead. The returned string wraps the name in single quotes only when the type suffix is appended.'
TOOL_PARAMETERS = { 'properties': { 'object': { 'description': 'The PsyNeuLink component instance to '
                                             'format. Must have a `.name` string '
                                             'attribute and a resolvable class '
                                             'hierarchy. This is a live Python object '
                                             '— pass a reference to an '
                                             'already-constructed PsyNeuLink '
                                             'component.',
                              'type': 'object'},
                  'type': { 'description': 'Optional override for the type label '
                                           'appended to the name. If omitted, the '
                                           'function uses the immediate parent class '
                                           'name '
                                           '(`object.__class__.__base__.__name__`). '
                                           'Provide this when the inferred class name '
                                           'is wrong or too generic.',
                            'type': 'string'}},
  'required': ['object'],
  'type': 'object'}
TOOL_NOTES = "The `object` argument must be a live PsyNeuLink component instance — it cannot be a string or dict. This makes the tool nearly uncallable from a pure JSON MCP context; it is intended as an internal utility. If you need a formatted name, construct the component first via the appropriate mechanism tool, then pass it here. The type-collision check is case-insensitive across three variants (lower, upper, capitalize), so `'TransferMechanism' mechanism` will NOT be produced — the bare name is returned instead. The returned string wraps the name in single quotes only when the type suffix is appended."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.append_type_to_name
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
    def append_type_to_name(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to format a PsyNeuLink component's display name by appending its type label."
        return _impl(args or {})
