"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c78577cc4149e9530716633a8e1d380272b1f3d6215f80693680201b4c471f13'
__pnl_qualname__ = 'psyneulink.is_comparison_operator'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_comparison_operator'
TOOL_DESCRIPTION = 'Call this tool to verify whether a given value is a recognized PsyNeuLink comparison operator before passing it to a parameter that expects one. Returns true if the value matches an entry in PsyNeuLink\'s internal comparison_operators dictionary, false otherwise. Use this as a validation check when constructing conditions or scheduling expressions that require a comparison operator argument.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "o": {\n      "description": "The comparison operator identifier to test \\u2014 e.g. \'EQUAL\', \'GREATER_THAN\'. Must correspond to a value in PsyNeuLink\'s comparison_operators dictionary.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "o"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function checks membership in comparison_operators.values() (the operator function objects), not the keys (string names). Over MCP/JSON the agent can only pass serializable values, so passing a raw Python callable is not possible — only string identifiers that PsyNeuLink can resolve to an operator function will work. If the host template cannot translate the string to the actual operator value before calling this function, the result will always be False. Treat this tool as best-effort validation; confirm with PsyNeuLink\'s keyword documentation which string names are valid comparison operators.'
TOOL_PARAMETERS = { 'properties': { 'o': { 'description': 'The comparison operator identifier to test — '
                                        "e.g. 'EQUAL', 'GREATER_THAN'. Must correspond "
                                        "to a value in PsyNeuLink's "
                                        'comparison_operators dictionary.',
                         'type': 'string'}},
  'required': ['o'],
  'type': 'object'}
TOOL_NOTES = "The function checks membership in comparison_operators.values() (the operator function objects), not the keys (string names). Over MCP/JSON the agent can only pass serializable values, so passing a raw Python callable is not possible — only string identifiers that PsyNeuLink can resolve to an operator function will work. If the host template cannot translate the string to the actual operator value before calling this function, the result will always be False. Treat this tool as best-effort validation; confirm with PsyNeuLink's keyword documentation which string names are valid comparison operators."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_comparison_operator
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
    def is_comparison_operator(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to verify whether a given value is a recognized PsyNeuLink comparison operator before passing it to a parameter that expects one.'
        return _impl(args or {})
