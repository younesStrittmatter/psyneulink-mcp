"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5746c122547ad4677520793dca42cac324d10662dc95dbeeb1765b583b369243'
__pnl_qualname__ = 'psyneulink.get_mdf_model'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_mdf_model'
TOOL_DESCRIPTION = 'Call this tool to export one or more PsyNeuLink Compositions to an MDF (ModECI Model Description Format) Model object, which can then be serialized or passed to downstream MDF tooling. Use it when the agent needs to convert a constructed Composition (or several disjoint ones) into a portable graph representation; the result is an `mdf.Model` instance whose `.graphs` list contains one entry per Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "compositions": {\n      "description": "Names of the Composition(s) to include in the MDF Model. Each name must resolve to an already-constructed Composition in the current PsyNeuLink session. Multiple compositions must be fully disjoint \\u2014 they must share no Mechanisms, Projections, or other Components.",\n      "items": {\n        "type": "string"\n      },\n      "minItems": 1,\n      "type": "array"\n    },\n    "simple_edge_format": {\n      "default": true,\n      "description": "When true (default), uses MDF simple edge format. Set to false to emit the verbose edge representation.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "compositions"\n  ],\n  "type": "object"\n}\n\nNotes:\nRequires the `modeci_mdf` package at runtime; the call will fail if it is not installed. The variadic `*compositions` signature means the host must unpack the array into positional arguments. If more than one Composition is supplied, they must be completely disjoint — sharing even a single Mechanism or Projection raises an error; this limitation is expected to be lifted in a future PsyNeuLink release. The returned object is a live `mdf.Model` Python object, not JSON — downstream code must serialize it explicitly (e.g., `model.to_json()`).'
TOOL_PARAMETERS = { 'properties': { 'compositions': { 'description': 'Names of the Composition(s) to '
                                                   'include in the MDF Model. Each '
                                                   'name must resolve to an '
                                                   'already-constructed Composition in '
                                                   'the current PsyNeuLink session. '
                                                   'Multiple compositions must be '
                                                   'fully disjoint — they must share '
                                                   'no Mechanisms, Projections, or '
                                                   'other Components.',
                                    'items': {'type': 'string'},
                                    'minItems': 1,
                                    'type': 'array'},
                  'simple_edge_format': { 'default': True,
                                          'description': 'When true (default), uses '
                                                         'MDF simple edge format. Set '
                                                         'to false to emit the verbose '
                                                         'edge representation.',
                                          'type': 'boolean'}},
  'required': ['compositions'],
  'type': 'object'}
TOOL_NOTES = 'Requires the `modeci_mdf` package at runtime; the call will fail if it is not installed. The variadic `*compositions` signature means the host must unpack the array into positional arguments. If more than one Composition is supplied, they must be completely disjoint — sharing even a single Mechanism or Projection raises an error; this limitation is expected to be lifted in a future PsyNeuLink release. The returned object is a live `mdf.Model` Python object, not JSON — downstream code must serialize it explicitly (e.g., `model.to_json()`).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_mdf_model
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
    def get_mdf_model(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to export one or more PsyNeuLink Compositions to an MDF (ModECI Model Description Format) Model object, which can then be serialized or passed to downstream MDF tooling.'
        return _impl(args or {})
