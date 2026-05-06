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
TOOL_DESCRIPTION = 'Call this tool to remove a Projection from a Composition, cleaning up its graph vertex, internal projections list, and any associated learning components (LearningMechanism, objective mechanism, TARGET_MECHANISM). Use this when restructuring a network — e.g., before rewiring nodes or tearing down a learning pathway. The tool returns None on success; raises AttributeError if the projection was not properly registered in the composition (known PNL issue with MappingProjection.compositions attribute missing — see notes).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the Composition to remove the projection from, as returned by create_composition.",\n      "type": "string"\n    },\n    "projection": {\n      "description": "Handle string of the Projection to remove (e.g., a MappingProjection handle returned by add_projection or retrieved from the composition\'s projections list).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "projection"\n  ],\n  "type": "object"\n}\n\nNotes:\nKNOWN BUG (PNL ≤ 0.18.0, confirmed in feedback): calling remove_projection on a MappingProjection that lacks a `compositions` attribute raises `AttributeError: \'MappingProjection\' object has no attribute \'compositions\'`. This occurs inside `projection._remove_from_composition()`. Workaround: only remove projections that were explicitly added via `add_projection` (not implicit projections created during pathway construction), and verify the projection handle is valid and still registered in the composition before calling this tool. Projections created as part of `add_linear_processing_pathway` may not have the `compositions` attribute populated correctly in this PNL version. If you receive this error, the network graph state may be partially modified — inspect the composition\'s projections list before continuing.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the Composition to '
                                                  'remove the projection from, as '
                                                  'returned by create_composition.',
                                   'type': 'string'},
                  'projection': { 'description': 'Handle string of the Projection to '
                                                 'remove (e.g., a MappingProjection '
                                                 'handle returned by add_projection or '
                                                 "retrieved from the composition's "
                                                 'projections list).',
                                  'type': 'string'}},
  'required': ['composition', 'projection'],
  'type': 'object'}
TOOL_NOTES = "KNOWN BUG (PNL ≤ 0.18.0, confirmed in feedback): calling remove_projection on a MappingProjection that lacks a `compositions` attribute raises `AttributeError: 'MappingProjection' object has no attribute 'compositions'`. This occurs inside `projection._remove_from_composition()`. Workaround: only remove projections that were explicitly added via `add_projection` (not implicit projections created during pathway construction), and verify the projection handle is valid and still registered in the composition before calling this tool. Projections created as part of `add_linear_processing_pathway` may not have the `compositions` attribute populated correctly in this PNL version. If you receive this error, the network graph state may be partially modified — inspect the composition's projections list before continuing."


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
        'Call this tool to remove a Projection from a Composition, cleaning up its graph vertex, internal projections list, and any associated learning components (LearningMechanism, objective mechanism, TARGET_MECHANISM).'
        return _impl(args or {})
