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
TOOL_DESCRIPTION = 'Call this tool to remove a Projection from a Composition, deactivating it and cleaning up any associated learning components. The tool returns None on success. Note: this operation is irreversible — the projection is fully deregistered from the composition\'s graph and projection list.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the Composition to remove the projection from, as returned by create_composition.",\n      "type": "string"\n    },\n    "projection": {\n      "description": "Handle string of the Projection to remove (e.g. a MappingProjection handle returned when the projection was created or retrieved).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "projection"\n  ],\n  "type": "object"\n}\n\nNotes:\nKnown bug in PsyNeuLink <= 0.18.0 (devel as of 2026-05): calling remove_projection on a MappingProjection raises `AttributeError: \'MappingProjection\' object has no attribute \'compositions\'` inside PNL\'s own `_remove_from_composition`. This is a PNL-side bug, not a schema issue — the tool call itself is correct. If you hit this error, the projection was already removed from the graph and projection list (steps 1-2 succeed) but the internal bookkeeping call fails. As a workaround, verify the projection is no longer in composition.projections after the error. Also removes any associated LearningMechanism nodes and learning pathway components (objective mechanism, target mechanism) if learning was attached to the projection.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the Composition to '
                                                  'remove the projection from, as '
                                                  'returned by create_composition.',
                                   'type': 'string'},
                  'projection': { 'description': 'Handle string of the Projection to '
                                                 'remove (e.g. a MappingProjection '
                                                 'handle returned when the projection '
                                                 'was created or retrieved).',
                                  'type': 'string'}},
  'required': ['composition', 'projection'],
  'type': 'object'}
TOOL_NOTES = "Known bug in PsyNeuLink <= 0.18.0 (devel as of 2026-05): calling remove_projection on a MappingProjection raises `AttributeError: 'MappingProjection' object has no attribute 'compositions'` inside PNL's own `_remove_from_composition`. This is a PNL-side bug, not a schema issue — the tool call itself is correct. If you hit this error, the projection was already removed from the graph and projection list (steps 1-2 succeed) but the internal bookkeeping call fails. As a workaround, verify the projection is no longer in composition.projections after the error. Also removes any associated LearningMechanism nodes and learning pathway components (objective mechanism, target mechanism) if learning was attached to the projection."


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
        'Call this tool to remove a Projection from a Composition, deactivating it and cleaning up any associated learning components.'
        return _impl(args or {})
