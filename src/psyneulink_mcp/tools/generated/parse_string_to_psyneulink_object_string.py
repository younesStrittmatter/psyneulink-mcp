"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f32b7bdad94a5917f4e6221bafedde17c28ab592693692a5b724cdb18f9a4ffd'
__pnl_qualname__ = 'psyneulink.parse_string_to_psyneulink_object_string'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'parse_string_to_psyneulink_object_string'
TOOL_DESCRIPTION = 'Call this tool to validate and normalize a string into a PsyNeuLink attribute name before using it programmatically. Given a candidate string (e.g., a user-supplied class name or keyword), it returns the canonical attribute name that can be passed to `getattr(psyneulink, result)` to retrieve the actual PsyNeuLink object, or returns None if no match exists. Use this as a pre-check when you have an ambiguous string that might be a PsyNeuLink symbol.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "string": {\n      "description": "The candidate string to look up. Can be a direct PsyNeuLink attribute name (e.g., \'TransferMechanism\'), a dotted attribute path (e.g., \'pnl.TransferMechanism\'), a camelCase keyword, or an UPPER_SNAKE_CASE keyword. Class instantiation syntax (with parentheses) is stripped before lookup.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "string"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns None (not an error) when the string does not resolve to any PsyNeuLink attribute — callers must check for None before using the result. The function silently converts camelCase strings to UPPER_SNAKE_CASE (e.g., \'linearCombination\' → \'LINEAR_COMBINATION\') when the literal string fails, so the returned value may differ from the input. Parenthesized expressions are stripped, meaning \'TransferMechanism(size=4)\' is treated the same as \'TransferMechanism\'.'
TOOL_PARAMETERS = { 'properties': { 'string': { 'description': 'The candidate string to look up. Can be '
                                             'a direct PsyNeuLink attribute name '
                                             "(e.g., 'TransferMechanism'), a dotted "
                                             'attribute path (e.g., '
                                             "'pnl.TransferMechanism'), a camelCase "
                                             'keyword, or an UPPER_SNAKE_CASE keyword. '
                                             'Class instantiation syntax (with '
                                             'parentheses) is stripped before lookup.',
                              'type': 'string'}},
  'required': ['string'],
  'type': 'object'}
TOOL_NOTES = "Returns None (not an error) when the string does not resolve to any PsyNeuLink attribute — callers must check for None before using the result. The function silently converts camelCase strings to UPPER_SNAKE_CASE (e.g., 'linearCombination' → 'LINEAR_COMBINATION') when the literal string fails, so the returned value may differ from the input. Parenthesized expressions are stripped, meaning 'TransferMechanism(size=4)' is treated the same as 'TransferMechanism'."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.parse_string_to_psyneulink_object_string
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
    def parse_string_to_psyneulink_object_string(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to validate and normalize a string into a PsyNeuLink attribute name before using it programmatically.'
        return _impl(args or {})
