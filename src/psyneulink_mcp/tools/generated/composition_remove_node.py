"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = '5ad04ed8d3cce39cb5036108f598c9784dd3d702887a3925894ad94c6932cfc0'
__pnl_qualname__ = 'psyneulink.Composition.remove_node'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'remove_node'
TOOL_DESCRIPTION = 'Call this tool to remove a node (Mechanism or nested Composition) from an existing Composition. Use it when you need to restructure a model by detaching a component — for example, after adding a node experimentally or before replacing it with a different one. Any projections involving the removed node may also be affected.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the Composition instance (returned by create_composition) from which the node will be removed.",\n      "type": "string"\n    },\n    "node": {\n      "description": "Handle string of the Mechanism or nested Composition to remove from the Composition.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "node"\n  ],\n  "type": "object"\n}\n\nNotes:\nRemoving a node does not explicitly remove its associated Projections — projections to/from the node may be left in an inconsistent state or silently dropped depending on PsyNeuLink internals. Verify the Composition\'s graph state after removal if Projections to neighboring nodes matter. There is no return value; the operation mutates the Composition in place.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the Composition '
                                                  'instance (returned by '
                                                  'create_composition) from which the '
                                                  'node will be removed.',
                                   'type': 'string'},
                  'node': { 'description': 'Handle string of the Mechanism or nested '
                                           'Composition to remove from the '
                                           'Composition.',
                            'type': 'string'}},
  'required': ['composition', 'node'],
  'type': 'object'}
TOOL_NOTES = "Removing a node does not explicitly remove its associated Projections — projections to/from the node may be left in an inconsistent state or silently dropped depending on PsyNeuLink internals. Verify the Composition's graph state after removal if Projections to neighboring nodes matter. There is no return value; the operation mutates the Composition in place."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='remove_node',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def remove_node(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to remove a node (Mechanism or nested Composition) from an existing Composition.'
        return _impl(args or {})
