"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'b93ef29604e81bfd4325513dbe8d17113f0980922d364761340e21fad9eefb9b'
__pnl_qualname__ = 'psyneulink.Composition.remove_projection'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'remove_projection'
TOOL_DESCRIPTION = 'Call this tool to remove a Projection from a Composition, including its vertex from the graph and any associated learning components. Use it when you need to disconnect two nodes that are currently linked, or to tear down a learning pathway that was added via add_backpropagation_learning_pathway or similar. The removal cascades: any LearningMechanism projections onto the removed projection\'s parameter ports—and the learning mechanisms themselves—are also cleaned up automatically.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the Composition instance (returned by create_composition) from which the projection should be removed.",\n      "type": "string"\n    },\n    "projection": {\n      "description": "Handle string for the Projection to remove. Must be a projection currently registered in the composition.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "projection"\n  ],\n  "type": "object"\n}\n\nNotes:\nRemoval cascades deeply: for each parameter port on the removed projection, any modulatory (learning) projections targeting it are also removed recursively. If their sender is a LearningMechanism that belongs to a learning pathway, the full set of learning components for that pathway (learning mechanisms, objective mechanism, target mechanism) are removed via remove_node as well. This means removing a single projection can silently dismantle an entire learning pathway—confirm this is intentional before calling. There is no return value. Step 5 (removing the projection from afferent/efferent lists of connected nodes) is listed as TBI in the source, so some node metadata may be stale after this call.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the Composition '
                                                  'instance (returned by '
                                                  'create_composition) from which the '
                                                  'projection should be removed.',
                                   'type': 'string'},
                  'projection': { 'description': 'Handle string for the Projection to '
                                                 'remove. Must be a projection '
                                                 'currently registered in the '
                                                 'composition.',
                                  'type': 'string'}},
  'required': ['composition', 'projection'],
  'type': 'object'}
TOOL_NOTES = 'Removal cascades deeply: for each parameter port on the removed projection, any modulatory (learning) projections targeting it are also removed recursively. If their sender is a LearningMechanism that belongs to a learning pathway, the full set of learning components for that pathway (learning mechanisms, objective mechanism, target mechanism) are removed via remove_node as well. This means removing a single projection can silently dismantle an entire learning pathway—confirm this is intentional before calling. There is no return value. Step 5 (removing the projection from afferent/efferent lists of connected nodes) is listed as TBI in the source, so some node metadata may be stale after this call.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='remove_projection',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def remove_projection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to remove a Projection from a Composition, including its vertex from the graph and any associated learning components.'
        return _impl(args or {})
