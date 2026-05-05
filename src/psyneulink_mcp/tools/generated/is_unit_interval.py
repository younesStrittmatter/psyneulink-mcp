"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6ec6d08662e2a45c410871175db1c9adeb6461da9bea125755626840d3d60e7a'
__pnl_qualname__ = 'psyneulink.is_unit_interval'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_unit_interval'
TOOL_DESCRIPTION = 'Call this tool to validate whether a numeric value qualifies as a unit-interval value — i.e., is an integer or float in the closed range [0, 1]. Use it before passing a probability, gain, or normalized weight to a PsyNeuLink parameter that requires a unit-interval value. Returns true if valid, false otherwise.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "spec": {\n      "description": "The numeric value (int or float) to test. Returns true if it is >= 0 and <= 1, false for any other numeric value or non-numeric type.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "spec"\n  ],\n  "type": "object"\n}\n\nNotes:\nNon-numeric types (strings, lists, None, etc.) return false silently rather than raising an error. Both endpoints 0 and 1 are inclusive. The check is strict about type: only int and float pass; numpy scalars or booleans are not explicitly handled and may behave unexpectedly depending on Python\'s isinstance resolution at runtime.'
TOOL_PARAMETERS = { 'properties': { 'spec': { 'description': 'The numeric value (int or float) to test. '
                                           'Returns true if it is >= 0 and <= 1, false '
                                           'for any other numeric value or non-numeric '
                                           'type.',
                            'type': 'number'}},
  'required': ['spec'],
  'type': 'object'}
TOOL_NOTES = "Non-numeric types (strings, lists, None, etc.) return false silently rather than raising an error. Both endpoints 0 and 1 are inclusive. The check is strict about type: only int and float pass; numpy scalars or booleans are not explicitly handled and may behave unexpectedly depending on Python's isinstance resolution at runtime."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_unit_interval
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
    def is_unit_interval(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to validate whether a numeric value qualifies as a unit-interval value — i.e., is an integer or float in the closed range [0, 1].'
        return _impl(args or {})
