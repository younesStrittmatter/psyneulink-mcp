"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b16330e5e165fdd8d587c248368f2f9435cbbeb47c41ccd8d4af5507817a2ec7'
__pnl_qualname__ = 'psyneulink.is_number'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_number'
TOOL_DESCRIPTION = 'Call this tool to check whether a value qualifies as a numeric type in PsyNeuLink\'s type system — i.e., it is an instance of Python\'s `numbers.Number` but is neither a `bool` nor an `Enum`. Returns `true` if the value is a plain number (int, float, complex, Decimal, etc.) and `false` otherwise. Use this before passing a value to a PNL parameter that requires a strict numeric type to avoid silent type coercion errors.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "x": {\n      "description": "The value to test. Typically a number, boolean, or other scalar. Pass the raw value you want to validate before using it as a PNL numeric parameter.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "integer"\n        },\n        {\n          "type": "string"\n        },\n        {\n          "type": "boolean"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nBooleans return `false` even though Python\'s `bool` is a subclass of `int` — this is intentional. Enum members also return `false`. Complex numbers and `decimal.Decimal` instances return `true` if they reach Python (JSON does not support complex literals, so complex values cannot be passed via MCP). The function has no docstring; behavior is derived entirely from source inspection.'
TOOL_PARAMETERS = { 'properties': { 'x': { 'description': 'The value to test. Typically a number, '
                                        'boolean, or other scalar. Pass the raw value '
                                        'you want to validate before using it as a PNL '
                                        'numeric parameter.',
                         'oneOf': [ {'type': 'number'},
                                    {'type': 'integer'},
                                    {'type': 'string'},
                                    {'type': 'boolean'},
                                    {'type': 'null'}]}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = "Booleans return `false` even though Python's `bool` is a subclass of `int` — this is intentional. Enum members also return `false`. Complex numbers and `decimal.Decimal` instances return `true` if they reach Python (JSON does not support complex literals, so complex values cannot be passed via MCP). The function has no docstring; behavior is derived entirely from source inspection."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_number
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
    def is_number(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to check whether a value qualifies as a numeric type in PsyNeuLink's type system — i.e., it is an instance of Python's `numbers.Number` but is neither a `bool` nor an `Enum`."
        return _impl(args or {})
