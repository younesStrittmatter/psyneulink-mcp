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
TOOL_DESCRIPTION = 'Call this tool to remove an existing Projection from a Composition, disconnecting two nodes and deactivating any associated learning components. The tool returns None on success; the Projection is removed from the graph, the Composition\'s projection list, and any associated LearningMechanism pathway nodes are also removed.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the Composition (returned by create_composition) from which the projection will be removed.",\n      "type": "string"\n    },\n    "projection": {\n      "description": "Handle string of the Projection (e.g. MappingProjection) to remove. Must already be registered in the Composition.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "projection"\n  ],\n  "type": "object"\n}\n\nNotes:\nKNOWN BUG (PsyNeuLink devel as of v0.18.0): Calling this tool with a MappingProjection that was not fully initialized into the Composition raises `AttributeError: \'MappingProjection\' object has no attribute \'compositions\'`. This occurs inside `projection._remove_from_composition()`. Workaround: only call remove_projection on projections that were explicitly added via add_projection or add_linear_processing_pathway and whose handle was returned by those calls. Do not call on projections retrieved by introspecting node ports directly. Removal also cascades: any LearningMechanism projections onto the removed projection\'s ParameterPorts are removed recursively, and associated learning pathway nodes (objective mechanism, target mechanism) are also removed from the Composition.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the Composition '
                                                  '(returned by create_composition) '
                                                  'from which the projection will be '
                                                  'removed.',
                                   'type': 'string'},
                  'projection': { 'description': 'Handle string of the Projection '
                                                 '(e.g. MappingProjection) to remove. '
                                                 'Must already be registered in the '
                                                 'Composition.',
                                  'type': 'string'}},
  'required': ['composition', 'projection'],
  'type': 'object'}
TOOL_NOTES = "KNOWN BUG (PsyNeuLink devel as of v0.18.0): Calling this tool with a MappingProjection that was not fully initialized into the Composition raises `AttributeError: 'MappingProjection' object has no attribute 'compositions'`. This occurs inside `projection._remove_from_composition()`. Workaround: only call remove_projection on projections that were explicitly added via add_projection or add_linear_processing_pathway and whose handle was returned by those calls. Do not call on projections retrieved by introspecting node ports directly. Removal also cascades: any LearningMechanism projections onto the removed projection's ParameterPorts are removed recursively, and associated learning pathway nodes (objective mechanism, target mechanism) are also removed from the Composition."


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
        'Call this tool to remove an existing Projection from a Composition, disconnecting two nodes and deactivating any associated learning components.'
        return _impl(args or {})
