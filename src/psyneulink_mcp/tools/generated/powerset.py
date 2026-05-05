"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f55a9e689db29be32f027de47aff9d8fe8fb3a3b0b58dcf22ac091e037e6a487'
__pnl_qualname__ = 'psyneulink.powerset'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'powerset'
TOOL_DESCRIPTION = 'Call this tool when you need all possible subsets (the power set) of a list of elements — for example, to enumerate every combination of components, parameters, or conditions. The result is an iterator of tuples, starting with the empty tuple and ending with the full set, ordered by subset size.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "iterable": {\n      "description": "The list of elements to compute the power set of. Elements should be strings; the function converts the input to a list internally.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "iterable"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns a lazy iterator (chain object), not a list — iterate or wrap in list() to materialize results. The empty set () is always the first element. Output grows as 2^n subsets for n input elements, so avoid large inputs (n > 20 will produce over 1 million subsets). Elements are treated by identity/equality as in standard Python itertools — duplicates in input produce duplicate subsets.'
TOOL_PARAMETERS = { 'properties': { 'iterable': { 'description': 'The list of elements to compute the '
                                               'power set of. Elements should be '
                                               'strings; the function converts the '
                                               'input to a list internally.',
                                'items': {'type': 'string'},
                                'type': 'array'}},
  'required': ['iterable'],
  'type': 'object'}
TOOL_NOTES = 'Returns a lazy iterator (chain object), not a list — iterate or wrap in list() to materialize results. The empty set () is always the first element. Output grows as 2^n subsets for n input elements, so avoid large inputs (n > 20 will produce over 1 million subsets). Elements are treated by identity/equality as in standard Python itertools — duplicates in input produce duplicate subsets.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.powerset
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
    def powerset(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need all possible subsets (the power set) of a list of elements — for example, to enumerate every combination of components, parameters, or conditions.'
        return _impl(args or {})
