"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '97142d7a77b1f5906d3cf70be15c896ddb1d217e93f8433dfe381cb7abac89ee'
__pnl_qualname__ = 'psyneulink.parse_context'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'parse_context'
TOOL_DESCRIPTION = 'Call this tool to normalize an execution context into its canonical context ID. Use it when you have a Composition object or a raw context value and need the underlying execution context identifier — for example, before passing a context to parameter lookups or execution APIs that expect a plain context ID. Returns the `default_execution_id` if given a Composition, or the input unchanged if it is already a plain context value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "context": {\n      "description": "An execution context identifier or the name/reference of a Composition whose default_execution_id should be extracted. Pass a raw context ID string if you already have one; pass a Composition reference string if you need its default execution context.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "context"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function silently returns the input unchanged when the passed value has no `default_execution_id` attribute — it will never raise on an unrecognized input, so type errors produce a silent no-op rather than a clear error. In MCP usage the context must be serializable as a string; Composition objects cannot be passed directly over the wire and must be referenced by name or ID.'
TOOL_PARAMETERS = { 'properties': { 'context': { 'description': 'An execution context identifier or the '
                                              'name/reference of a Composition whose '
                                              'default_execution_id should be '
                                              'extracted. Pass a raw context ID string '
                                              'if you already have one; pass a '
                                              'Composition reference string if you '
                                              'need its default execution context.',
                               'type': 'string'}},
  'required': ['context'],
  'type': 'object'}
TOOL_NOTES = 'The function silently returns the input unchanged when the passed value has no `default_execution_id` attribute — it will never raise on an unrecognized input, so type errors produce a silent no-op rather than a clear error. In MCP usage the context must be serializable as a string; Composition objects cannot be passed directly over the wire and must be referenced by name or ID.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.parse_context
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
    def parse_context(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to normalize an execution context into its canonical context ID.'
        return _impl(args or {})
