"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'aca073cd885e6dbf8e0e2322b1dcc255cd72272efcf8aa9cbcc390bbb05a3bb3'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.objectivefunctions.is_iterable'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_iterable'
TOOL_DESCRIPTION = 'Call this tool to check whether a value is iterable before passing it to PsyNeuLink functions that expect sequences or arrays. Returns `true` if the value supports iteration, `false` otherwise. Use `exclude_str=true` when you want strings treated as non-iterable (e.g., to distinguish scalar text from lists of items).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "exclude_str": {\n      "default": false,\n      "description": "If true, strings are treated as non-iterable and the function returns false for them. Defaults to false.",\n      "type": "boolean"\n    },\n    "x": {\n      "description": "The value to test for iterability. Can be any type: list, array, string, number, object, etc.",\n      "type": [\n        "array",\n        "boolean",\n        "integer",\n        "number",\n        "object",\n        "string"\n      ]\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nStrings are iterable in Python, so `is_iterable("hello")` returns `true` by default. Set `exclude_str=true` to suppress this. Numbers, booleans, and None are not iterable and will return `false`. The JSON schema cannot represent Python\'s `None`/null as a valid input for `x`, but passing null will correctly return `false`.'
TOOL_PARAMETERS = { 'properties': { 'exclude_str': { 'default': False,
                                   'description': 'If true, strings are treated as '
                                                  'non-iterable and the function '
                                                  'returns false for them. Defaults to '
                                                  'false.',
                                   'type': 'boolean'},
                  'x': { 'description': 'The value to test for iterability. Can be any '
                                        'type: list, array, string, number, object, '
                                        'etc.',
                         'type': [ 'array',
                                   'boolean',
                                   'integer',
                                   'number',
                                   'object',
                                   'string']}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = 'Strings are iterable in Python, so `is_iterable("hello")` returns `true` by default. Set `exclude_str=true` to suppress this. Numbers, booleans, and None are not iterable and will return `false`. The JSON schema cannot represent Python\'s `None`/null as a valid input for `x`, but passing null will correctly return `false`.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_iterable
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
    def is_iterable(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a value is iterable before passing it to PsyNeuLink functions that expect sequences or arrays.'
        return _impl(args or {})
