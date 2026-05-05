"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '520a3d8632ebb2162bd47c51b18f51f7ec46933a3ef0ff5353566a4ca3ceea5e'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.transferfunctions.is_matrix_keyword'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_matrix_keyword'
TOOL_DESCRIPTION = 'Call this tool to check whether a given string is a valid PsyNeuLink matrix keyword (e.g., "IDENTITY_MATRIX", "FULL_CONNECTIVITY_MATRIX"). Returns True if the value is a recognized matrix keyword constant, False otherwise. Use this before passing a string as a matrix argument to validate that it will be interpreted as a keyword rather than a literal matrix.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "m": {\n      "description": "The value to test. Must be a string; non-strings always return False.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "m"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function returns False for any non-string input without raising an error, so passing a number or array will silently return False rather than signaling a type mismatch. The valid keyword set is defined by MATRIX_KEYWORD_VALUES in psyneulink.core.globals.keywords; common values include IDENTITY_MATRIX, FULL_CONNECTIVITY_MATRIX, RANDOM_CONNECTIVITY_MATRIX, AUTO_ASSIGN_MATRIX, and DEFAULT_MATRIX.'
TOOL_PARAMETERS = { 'properties': { 'm': { 'description': 'The value to test. Must be a string; '
                                        'non-strings always return False.',
                         'type': 'string'}},
  'required': ['m'],
  'type': 'object'}
TOOL_NOTES = 'The function returns False for any non-string input without raising an error, so passing a number or array will silently return False rather than signaling a type mismatch. The valid keyword set is defined by MATRIX_KEYWORD_VALUES in psyneulink.core.globals.keywords; common values include IDENTITY_MATRIX, FULL_CONNECTIVITY_MATRIX, RANDOM_CONNECTIVITY_MATRIX, AUTO_ASSIGN_MATRIX, and DEFAULT_MATRIX.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_matrix_keyword
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
    def is_matrix_keyword(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a given string is a valid PsyNeuLink matrix keyword (e.g., "IDENTITY_MATRIX", "FULL_CONNECTIVITY_MATRIX").'
        return _impl(args or {})
