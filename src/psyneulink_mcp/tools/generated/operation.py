"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '55126ca0e24d371095a64fa2f968b5f3f9fe98e3de8ed7efdc09fdc112143b6e'
__pnl_qualname__ = 'psyneulink.Operation'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_operation'
TOOL_DESCRIPTION = 'Call this tool when you need to select a set-combination rule for use with `GraphStructureCondition`. It resolves to a `psyneulink.Operation` enum member that declares how a source node set (S) and a comparison node set (C) are combined — for example, to restrict scheduling conditions to nodes in the intersection of two sets, or to invert a difference. Pass the returned member as the `operation` argument to `GraphStructureCondition`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "operation": {\n      "description": "Name of the Operation member to retrieve. KEEP \\u2192 S; REPLACE \\u2192 C; DISCARD \\u2192 {}; INTERSECTION \\u2192 S\\u2229C; UNION/MERGE \\u2192 S\\u222aC; DIFFERENCE \\u2192 S\\\\C; INVERSE_DIFFERENCE \\u2192 C\\\\S; SYMMETRIC_DIFFERENCE \\u2192 (S\\u222aC)\\\\(S\\u2229C).",\n      "enum": [\n        "KEEP",\n        "REPLACE",\n        "DISCARD",\n        "INTERSECTION",\n        "UNION",\n        "MERGE",\n        "DIFFERENCE",\n        "INVERSE_DIFFERENCE",\n        "SYMMETRIC_DIFFERENCE"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "operation"\n  ],\n  "type": "object"\n}\n\nNotes:\nOperation is an enum, not a normal class. Members must be accessed by name (e.g., `Operation[\'KEEP\']` or `Operation.KEEP`), not via the constructor `Operation(value)` — calling the constructor with a functools.partial value will raise ValueError. MERGE and UNION are identical in behavior. Once you have an Operation member you can invoke it directly as `op(source_set, comparison_set)` to get the result set; this tool only resolves the enum member, it does not apply it.'
TOOL_PARAMETERS = { 'properties': { 'operation': { 'description': 'Name of the Operation member to '
                                                'retrieve. KEEP → S; REPLACE → C; '
                                                'DISCARD → {}; INTERSECTION → S∩C; '
                                                'UNION/MERGE → S∪C; DIFFERENCE → S\\C; '
                                                'INVERSE_DIFFERENCE → C\\S; '
                                                'SYMMETRIC_DIFFERENCE → (S∪C)\\(S∩C).',
                                 'enum': [ 'KEEP',
                                           'REPLACE',
                                           'DISCARD',
                                           'INTERSECTION',
                                           'UNION',
                                           'MERGE',
                                           'DIFFERENCE',
                                           'INVERSE_DIFFERENCE',
                                           'SYMMETRIC_DIFFERENCE'],
                                 'type': 'string'}},
  'required': ['operation'],
  'type': 'object'}
TOOL_NOTES = "Operation is an enum, not a normal class. Members must be accessed by name (e.g., `Operation['KEEP']` or `Operation.KEEP`), not via the constructor `Operation(value)` — calling the constructor with a functools.partial value will raise ValueError. MERGE and UNION are identical in behavior. Once you have an Operation member you can invoke it directly as `op(source_set, comparison_set)` to get the result set; this tool only resolves the enum member, it does not apply it."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Operation
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
    def create_operation(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to select a set-combination rule for use with `GraphStructureCondition`.'
        return _impl(args or {})
