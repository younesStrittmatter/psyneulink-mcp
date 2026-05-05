"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = '4ce5952828c6cfe72e31e0ffa79f6a341226f535bca09aa29569425ae768aee2'
__pnl_qualname__ = 'psyneulink.Composition.add_pathway'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_pathway'
TOOL_DESCRIPTION = 'Call this tool to attach a previously-constructed Pathway object to a Composition. Use it when you have already built a Pathway (e.g., via `create_pathway` or by constructing one manually) and need to register it with a target Composition so that its nodes and projections become part of that Composition\'s graph. The tool adds all Mechanism/Composition nodes first, then wires the Projections between them.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "Handle string of the Pathway to add. The Pathway must already exist as a live object; the runtime resolves the handle to the object before dispatch.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe method adds nodes before projections internally, so the graph topology is safe even if the Pathway contains both. This tool is for adding a pre-built Pathway object — not for constructing a new linear processing pathway from a node list; use add_linear_processing_pathway for that instead. The Pathway\'s graph is walked to extract Mechanisms, nested Compositions, and Projections; any component already in the Composition is silently accepted (add_node is idempotent).'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'pathway': { 'description': 'Handle string of the Pathway to add. '
                                              'The Pathway must already exist as a '
                                              'live object; the runtime resolves the '
                                              'handle to the object before dispatch.',
                               'type': 'string'}},
  'required': ['composition', 'pathway'],
  'type': 'object'}
TOOL_NOTES = "The method adds nodes before projections internally, so the graph topology is safe even if the Pathway contains both. This tool is for adding a pre-built Pathway object — not for constructing a new linear processing pathway from a node list; use add_linear_processing_pathway for that instead. The Pathway's graph is walked to extract Mechanisms, nested Compositions, and Projections; any component already in the Composition is silently accepted (add_node is idempotent)."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_pathway',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_pathway(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to attach a previously-constructed Pathway object to a Composition.'
        return _impl(args or {})
