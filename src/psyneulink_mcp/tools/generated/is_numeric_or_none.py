"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a126386aa9db0a49dc27e2128fb3398bdbb537c084841e3713d23c977bc6df45'
__pnl_qualname__ = 'psyneulink.is_numeric_or_none'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_numeric_or_none'
TOOL_DESCRIPTION = 'Call this tool to validate whether a value is acceptable as a numeric PsyNeuLink parameter — it returns True if the value is None (treated as "unset") or is numeric (int, float, numpy scalar, or numeric array), and False otherwise. Use it before passing a value to a PsyNeuLink component when you need to confirm the value satisfies a numeric-or-none constraint.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "x": {\n      "description": "The value to test. Pass None, a number (int or float), a numeric list/array, or any candidate value whose numeric-or-None status is uncertain.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "integer"\n        },\n        {\n          "type": "null"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "type": "boolean"\n        }\n      ]\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nNone is explicitly accepted and returns True — it is treated as "no value specified", not as a failed check. The underlying is_numeric check covers scalars and numpy numeric arrays; plain Python strings that look like numbers (e.g. "3.14") will return False. Boolean values may return True because bool is a subclass of int in Python — avoid passing booleans if you intend a strict numeric check.'
TOOL_PARAMETERS = { 'properties': { 'x': { 'description': 'The value to test. Pass None, a number (int '
                                        'or float), a numeric list/array, or any '
                                        'candidate value whose numeric-or-None status '
                                        'is uncertain.',
                         'oneOf': [ {'type': 'number'},
                                    {'type': 'integer'},
                                    {'type': 'null'},
                                    {'items': {'type': 'number'}, 'type': 'array'},
                                    {'type': 'boolean'}]}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = 'None is explicitly accepted and returns True — it is treated as "no value specified", not as a failed check. The underlying is_numeric check covers scalars and numpy numeric arrays; plain Python strings that look like numbers (e.g. "3.14") will return False. Boolean values may return True because bool is a subclass of int in Python — avoid passing booleans if you intend a strict numeric check.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_numeric_or_none
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
    def is_numeric_or_none(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to validate whether a value is acceptable as a numeric PsyNeuLink parameter — it returns True if the value is None (treated as "unset") or is numeric (int, float, numpy scalar, or numeric array), and False otherwise.'
        return _impl(args or {})
