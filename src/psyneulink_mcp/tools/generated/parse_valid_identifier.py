"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '15785744001b2727cd1bb41677626aaabbf6567d6c3ddeb4ee945142010c75f8'
__pnl_qualname__ = 'psyneulink.core.components.functions.stateful.integratorfunctions.parse_valid_identifier'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'parse_valid_identifier'
TOOL_DESCRIPTION = 'Call this tool when you have a string that may contain characters invalid for a Python identifier (spaces, hyphens, leading digits, special characters) and need a sanitized version safe to use as a variable name, parameter name, or PsyNeuLink component name. Returns the input string with all invalid characters replaced by underscores, and a leading underscore prepended if the string starts with a digit or other non-letter/underscore character.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "orig_identifier": {\n      "description": "The string to sanitize into a valid Python identifier. Any character that is not a letter, digit, or underscore will be replaced with an underscore; a leading non-letter/underscore character will also get a prepended underscore.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "orig_identifier"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function does not guarantee uniqueness — two different input strings can map to the same output (e.g., "a-b" and "a_b" both become "a_b"). Leading digits are handled by prepending an underscore (e.g., "3foo" → "_3foo"), not by removing the digit. The result is always a non-empty string as long as the input is non-empty.'
TOOL_PARAMETERS = { 'properties': { 'orig_identifier': { 'description': 'The string to sanitize into a '
                                                      'valid Python identifier. Any '
                                                      'character that is not a letter, '
                                                      'digit, or underscore will be '
                                                      'replaced with an underscore; a '
                                                      'leading non-letter/underscore '
                                                      'character will also get a '
                                                      'prepended underscore.',
                                       'type': 'string'}},
  'required': ['orig_identifier'],
  'type': 'object'}
TOOL_NOTES = 'The function does not guarantee uniqueness — two different input strings can map to the same output (e.g., "a-b" and "a_b" both become "a_b"). Leading digits are handled by prepending an underscore (e.g., "3foo" → "_3foo"), not by removing the digit. The result is always a non-empty string as long as the input is non-empty.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.parse_valid_identifier
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
    def parse_valid_identifier(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you have a string that may contain characters invalid for a Python identifier (spaces, hyphens, leading digits, special characters) and need a sanitized version safe to use as a variable name, parameter name, or PsyNeuLink component name.'
        return _impl(args or {})
