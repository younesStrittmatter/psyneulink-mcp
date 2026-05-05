"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '725f1f8a7a3cef72724d839e6002500831a11867ad6f65adf0778520cdddae7e'
__pnl_qualname__ = 'psyneulink.PNLStrEnum'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pnl_str_enum'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — PNLStrEnum is an abstract base class for PsyNeuLink string enumerations and has no members of its own. Instantiating it will raise an error. Use the specific enum subclasses (e.g., ExecutionMode, NodeRole, EdgeType) instead, which inherit this class\'s case-insensitive lookup behavior.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "The string value to normalize and look up in the enum. Matching is case-insensitive; the stored value will be lowercased.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nPNLStrEnum is a base class — it has no enum members and cannot be instantiated directly; doing so will raise a TypeError or return None from _missing_. All comparisons and lookups are case-insensitive (values are lowercased via _normalize_value). When passing enum-typed arguments to other PsyNeuLink tools, you can pass plain lowercase strings instead of enum instances since __eq__ compares by lowercased value.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'The string value to normalize and look up '
                                            'in the enum. Matching is '
                                            'case-insensitive; the stored value will '
                                            'be lowercased.',
                             'type': 'string'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'PNLStrEnum is a base class — it has no enum members and cannot be instantiated directly; doing so will raise a TypeError or return None from _missing_. All comparisons and lookups are case-insensitive (values are lowercased via _normalize_value). When passing enum-typed arguments to other PsyNeuLink tools, you can pass plain lowercase strings instead of enum instances since __eq__ compares by lowercased value.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PNLStrEnum
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
    def create_pnl_str_enum(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — PNLStrEnum is an abstract base class for PsyNeuLink string enumerations and has no members of its own.'
        return _impl(args or {})
