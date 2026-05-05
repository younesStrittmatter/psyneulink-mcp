"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'e5f8d1e2878d9b28a481fd8786f62febc317dd6515635abf479352119d7dac70'
__pnl_qualname__ = 'psyneulink.Composition.add_projections'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_projections'
TOOL_DESCRIPTION = 'Call this tool when you need to add multiple pre-built Projections to a Composition in one operation — it is the batch form of `add_projection`. Each Projection handle passed must already have its `sender` and `receiver` assigned; the tool iterates the list and registers each connection. Use instead of repeated `add_projection` calls when wiring several pathways at once.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "projections": {\n      "description": "List of Projection handle strings to add. Each Projection must already have its sender and receiver set. Nested lists are allowed and will be processed recursively.",\n      "items": {\n        "description": "Handle string of a Projection whose sender and receiver are already specified.",\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "composition",\n    "projections"\n  ],\n  "type": "object"\n}\n\nNotes:\nEvery Projection in the list must have its sender and receiver attributes already set before calling this tool — the method does not accept sender/receiver arguments here. Passing a Projection without both attributes raises CompositionError. Nested lists (lists of lists of Projection handles) are supported and processed recursively, so you can pass a structured pathway list directly. Duplicate-handling behavior follows add_projection rules; see that tool\'s notes for details.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'projections': { 'description': 'List of Projection handle strings '
                                                  'to add. Each Projection must '
                                                  'already have its sender and '
                                                  'receiver set. Nested lists are '
                                                  'allowed and will be processed '
                                                  'recursively.',
                                   'items': { 'description': 'Handle string of a '
                                                             'Projection whose sender '
                                                             'and receiver are already '
                                                             'specified.',
                                              'type': 'string'},
                                   'type': 'array'}},
  'required': ['composition', 'projections'],
  'type': 'object'}
TOOL_NOTES = "Every Projection in the list must have its sender and receiver attributes already set before calling this tool — the method does not accept sender/receiver arguments here. Passing a Projection without both attributes raises CompositionError. Nested lists (lists of lists of Projection handles) are supported and processed recursively, so you can pass a structured pathway list directly. Duplicate-handling behavior follows add_projection rules; see that tool's notes for details."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_projections',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_projections(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to add multiple pre-built Projections to a Composition in one operation — it is the batch form of `add_projection`.'
        return _impl(args or {})
