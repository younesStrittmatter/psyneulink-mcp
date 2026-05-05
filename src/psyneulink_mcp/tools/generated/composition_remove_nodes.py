"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = '0eb94d877430941c30d0ab5f83fc40933df259383fb026d02d03184877374200'
__pnl_qualname__ = 'psyneulink.Composition.remove_nodes'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'remove_nodes'
TOOL_DESCRIPTION = 'Call this tool to remove one or more nodes (Mechanisms or nested Compositions) from an existing Composition. Use it when restructuring a model after initial construction — e.g., pruning unused pathways or rebuilding a subgraph. The graph is re-analyzed automatically after removal, so subsequent queries about graph structure will reflect the change.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the Composition instance to remove nodes from, as returned by create_composition.",\n      "type": "string"\n    },\n    "nodes": {\n      "description": "Handle string of a single Mechanism or Composition to remove, or an array of such handle strings. Mixed lists of Mechanisms and Compositions are allowed.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "composition",\n    "nodes"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `nodes` argument must resolve to a Mechanism, a Composition, or a list of either — any other type triggers an AssertionError. Removing a node does not automatically remove its associated Projections; dangling projections may cause issues in subsequent runs. Graph re-analysis (`_analyze_graph`) runs after all removals, so intermediate graph state during a multi-node removal is not exposed.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the Composition '
                                                  'instance to remove nodes from, as '
                                                  'returned by create_composition.',
                                   'type': 'string'},
                  'nodes': { 'description': 'Handle string of a single Mechanism or '
                                            'Composition to remove, or an array of '
                                            'such handle strings. Mixed lists of '
                                            'Mechanisms and Compositions are allowed.',
                             'oneOf': [ {'type': 'string'},
                                        { 'items': {'type': 'string'},
                                          'type': 'array'}]}},
  'required': ['composition', 'nodes'],
  'type': 'object'}
TOOL_NOTES = 'The `nodes` argument must resolve to a Mechanism, a Composition, or a list of either — any other type triggers an AssertionError. Removing a node does not automatically remove its associated Projections; dangling projections may cause issues in subsequent runs. Graph re-analysis (`_analyze_graph`) runs after all removals, so intermediate graph state during a multi-node removal is not exposed.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='remove_nodes',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def remove_nodes(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to remove one or more nodes (Mechanisms or nested Compositions) from an existing Composition.'
        return _impl(args or {})
