"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd97bfb3692cb8accde7fd1664d259fca01c7d11590a22cd19ebd0ece20d621ca'
__pnl_qualname__ = 'psyneulink.get_mdf_serialized'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_mdf_serialized'
TOOL_DESCRIPTION = 'Call this tool after you have built one or more PsyNeuLink Compositions and want to export them to a portable MDF (Model Description Framework) representation. Returns a JSON or YAML string encoding the full graph structure — nodes, edges, parameters — suitable for saving to disk, sharing, or loading into other MDF-compatible tools. Use this when the user asks to "export", "serialize", or "save" a Composition as MDF.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "compositions": {\n      "description": "Names of the Composition objects (already created in the PsyNeuLink session) to serialize. All listed Compositions must be fully disjoint \\u2014 they must share no Mechanisms, Projections, or other Components.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "fmt": {\n      "default": "json",\n      "description": "Output format. \'json\' returns a JSON string; \'yml\' or \'yaml\' returns a YAML string.",\n      "enum": [\n        "json",\n        "yml",\n        "yaml"\n      ],\n      "type": "string"\n    },\n    "simple_edge_format": {\n      "default": true,\n      "description": "When true, edges are written in the compact MDF simple-edge format. Set to false for the verbose edge representation.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "compositions"\n  ],\n  "type": "object"\n}\n\nNotes:\nMultiple Compositions are supported but must be fully disjoint — sharing any Component (Mechanism, Projection, etc.) across listed Compositions will produce incorrect output or an error. This restriction is a known limitation and may be lifted in a future PsyNeuLink release. The default output is JSON (`fmt=\'json\'`). \'yml\' and \'yaml\' are treated identically. `simple_edge_format` defaults to True; the verbose format (False) produces larger but more explicit edge objects.'
TOOL_PARAMETERS = { 'properties': { 'compositions': { 'description': 'Names of the Composition objects '
                                                   '(already created in the PsyNeuLink '
                                                   'session) to serialize. All listed '
                                                   'Compositions must be fully '
                                                   'disjoint — they must share no '
                                                   'Mechanisms, Projections, or other '
                                                   'Components.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'fmt': { 'default': 'json',
                           'description': "Output format. 'json' returns a JSON "
                                          "string; 'yml' or 'yaml' returns a YAML "
                                          'string.',
                           'enum': ['json', 'yml', 'yaml'],
                           'type': 'string'},
                  'simple_edge_format': { 'default': True,
                                          'description': 'When true, edges are written '
                                                         'in the compact MDF '
                                                         'simple-edge format. Set to '
                                                         'false for the verbose edge '
                                                         'representation.',
                                          'type': 'boolean'}},
  'required': ['compositions'],
  'type': 'object'}
TOOL_NOTES = "Multiple Compositions are supported but must be fully disjoint — sharing any Component (Mechanism, Projection, etc.) across listed Compositions will produce incorrect output or an error. This restriction is a known limitation and may be lifted in a future PsyNeuLink release. The default output is JSON (`fmt='json'`). 'yml' and 'yaml' are treated identically. `simple_edge_format` defaults to True; the verbose format (False) produces larger but more explicit edge objects."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_mdf_serialized
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
    def get_mdf_serialized(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after you have built one or more PsyNeuLink Compositions and want to export them to a portable MDF (Model Description Framework) representation.'
        return _impl(args or {})
