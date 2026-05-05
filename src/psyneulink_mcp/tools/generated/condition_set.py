"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ff5cf7910306599cd068cc563b0d9fc7371fa4385477684937f67ff83f044871'
__pnl_qualname__ = 'psyneulink.ConditionSet'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_condition_set'
TOOL_DESCRIPTION = 'Call this tool to create a ConditionSet that bundles scheduling conditions for multiple nodes before passing it to a Scheduler or Composition. Use it when you need to define when each node in a graph is allowed to execute (e.g., "run A only after B finishes twice"). Returns a ConditionSet object that can be directly supplied to a Scheduler\'s `condition_set` argument.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "conditions": {\n      "additionalProperties": {\n        "description": "A Condition object or list of Condition objects governing when this node executes."\n      },\n      "description": "A mapping from node names (or node references) to their scheduling condition(s). Each value is either a single Condition object or a list of Condition objects. Basic conditions (non-structural) overwrite any existing basic condition for the same owner; use a Composite Condition (e.g., All, Any) if you need multiple basic conditions on one node.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe constructor signature is `ConditionSet(*condition_sets, conditions=None)`. Because MCP tools pass keyword arguments only, the variadic positional `*condition_sets` cannot be supplied through this tool — use the `conditions` keyword argument instead, which accepts the same dict-of-node→condition mapping. The `conditions` kwarg is explicitly marked as a backwards-compatibility alias; it calls `add_condition_set` internally, so behavior is identical to a positional dict. If a node already has a basic Condition and you add another, the old one is silently replaced with a warning — use a Composite Condition (All/Any) to combine multiple basic conditions on a single node. GraphStructureConditions (structural) are accumulated rather than replaced.'
TOOL_PARAMETERS = { 'properties': { 'conditions': { 'additionalProperties': { 'description': 'A '
                                                                           'Condition '
                                                                           'object or '
                                                                           'list of '
                                                                           'Condition '
                                                                           'objects '
                                                                           'governing '
                                                                           'when this '
                                                                           'node '
                                                                           'executes.'},
                                  'description': 'A mapping from node names (or node '
                                                 'references) to their scheduling '
                                                 'condition(s). Each value is either a '
                                                 'single Condition object or a list of '
                                                 'Condition objects. Basic conditions '
                                                 '(non-structural) overwrite any '
                                                 'existing basic condition for the '
                                                 'same owner; use a Composite '
                                                 'Condition (e.g., All, Any) if you '
                                                 'need multiple basic conditions on '
                                                 'one node.',
                                  'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The constructor signature is `ConditionSet(*condition_sets, conditions=None)`. Because MCP tools pass keyword arguments only, the variadic positional `*condition_sets` cannot be supplied through this tool — use the `conditions` keyword argument instead, which accepts the same dict-of-node→condition mapping. The `conditions` kwarg is explicitly marked as a backwards-compatibility alias; it calls `add_condition_set` internally, so behavior is identical to a positional dict. If a node already has a basic Condition and you add another, the old one is silently replaced with a warning — use a Composite Condition (All/Any) to combine multiple basic conditions on a single node. GraphStructureConditions (structural) are accumulated rather than replaced.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ConditionSet
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
    def create_condition_set(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a ConditionSet that bundles scheduling conditions for multiple nodes before passing it to a Scheduler or Composition.'
        return _impl(args or {})
