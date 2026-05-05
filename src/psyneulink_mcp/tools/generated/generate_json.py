"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c44b89badb36f8c2fd76b77480685c2caa3e04aef7f8073eef79234249a2e38d'
__pnl_qualname__ = 'psyneulink.generate_json'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'generate_json'
TOOL_DESCRIPTION = 'Call this tool to serialize one or more PsyNeuLink Compositions into MDF-compatible JSON. The result is a JSON string representing the model graph, suitable for export or interchange. DEPRECATED: prefer `get_mdf_serialized` with `fmt=\'json\'` — this function emits a FutureWarning and will be removed in a future PsyNeuLink release.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "compositions": {\n      "description": "Names of the Composition objects to serialize. All listed Compositions must already exist in the current PsyNeuLink session. If more than one is provided, they must be fully disjoint (no shared Mechanisms or Projections).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "simple_edge_format": {\n      "default": true,\n      "description": "When true (default), edges are written in simplified MDF format. Set to false to emit the full edge-parameter representation.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "compositions"\n  ],\n  "type": "object"\n}\n\nNotes:\nDEPRECATED: `generate_json` is replaced by `get_mdf_serialized` and will be removed in a future version — a FutureWarning is raised on every call. Prefer calling `get_mdf_serialized` with `fmt=\'json\'` directly. Multiple Compositions are only supported if they are fully disjoint; shared Components (Mechanisms, Projections, etc.) across Compositions will produce incorrect output with no error raised.'
TOOL_PARAMETERS = { 'properties': { 'compositions': { 'description': 'Names of the Composition objects '
                                                   'to serialize. All listed '
                                                   'Compositions must already exist in '
                                                   'the current PsyNeuLink session. If '
                                                   'more than one is provided, they '
                                                   'must be fully disjoint (no shared '
                                                   'Mechanisms or Projections).',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'simple_edge_format': { 'default': True,
                                          'description': 'When true (default), edges '
                                                         'are written in simplified '
                                                         'MDF format. Set to false to '
                                                         'emit the full edge-parameter '
                                                         'representation.',
                                          'type': 'boolean'}},
  'required': ['compositions'],
  'type': 'object'}
TOOL_NOTES = "DEPRECATED: `generate_json` is replaced by `get_mdf_serialized` and will be removed in a future version — a FutureWarning is raised on every call. Prefer calling `get_mdf_serialized` with `fmt='json'` directly. Multiple Compositions are only supported if they are fully disjoint; shared Components (Mechanisms, Projections, etc.) across Compositions will produce incorrect output with no error raised."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.generate_json
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
    def generate_json(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to serialize one or more PsyNeuLink Compositions into MDF-compatible JSON.'
        return _impl(args or {})
