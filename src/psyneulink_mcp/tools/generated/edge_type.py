"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '98c87c1b26fd4b878cdc8f4bb6a92b998fdb337b793532dae0b83d6b0450e3b4'
__pnl_qualname__ = 'psyneulink.EdgeType'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_edge_type'
TOOL_DESCRIPTION = 'Call this tool to obtain an EdgeType enum value when you need to specify how a graph edge should behave during cycle detection in a PsyNeuLink Composition. Returns one of three EdgeType members — NON_FEEDBACK (flattened in cycles), FEEDBACK (immediately pruned), or FLEXIBLE (pruned only if in a cycle) — for use in projection or graph configuration calls.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "The EdgeType member to retrieve. NON_FEEDBACK: standard edge, kept but flattened when part of a cycle. FEEDBACK: immediately pruned to break cycles (use for intentional recurrent/feedback connections). FLEXIBLE: pruned only if it actually participates in a cycle, left intact otherwise.",\n      "enum": [\n        "NON_FEEDBACK",\n        "FEEDBACK",\n        "FLEXIBLE"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nEdgeType is an enum; the underlying values are False (NON_FEEDBACK), True (FEEDBACK), and a MAYBE sentinel (FLEXIBLE) — do not pass raw booleans. Prefer the string name. The from_any classmethod used internally is case-insensitive, but passing the canonical uppercase string avoids any ambiguity. FEEDBACK edges are the standard way to mark intentional feedback projections in a recurrent Composition so PsyNeuLink can build an acyclic execution order without destroying the edge.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'The EdgeType member to retrieve. '
                                            'NON_FEEDBACK: standard edge, kept but '
                                            'flattened when part of a cycle. FEEDBACK: '
                                            'immediately pruned to break cycles (use '
                                            'for intentional recurrent/feedback '
                                            'connections). FLEXIBLE: pruned only if it '
                                            'actually participates in a cycle, left '
                                            'intact otherwise.',
                             'enum': ['NON_FEEDBACK', 'FEEDBACK', 'FLEXIBLE'],
                             'type': 'string'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'EdgeType is an enum; the underlying values are False (NON_FEEDBACK), True (FEEDBACK), and a MAYBE sentinel (FLEXIBLE) — do not pass raw booleans. Prefer the string name. The from_any classmethod used internally is case-insensitive, but passing the canonical uppercase string avoids any ambiguity. FEEDBACK edges are the standard way to mark intentional feedback projections in a recurrent Composition so PsyNeuLink can build an acyclic execution order without destroying the edge.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.EdgeType
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
    def create_edge_type(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to obtain an EdgeType enum value when you need to specify how a graph edge should behave during cycle detection in a PsyNeuLink Composition.'
        return _impl(args or {})
