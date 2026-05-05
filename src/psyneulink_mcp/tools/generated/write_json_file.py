"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c4e84fbbcc27442e11ab8fbc802fcd0e87d21e0d8b41ef8c915cbc1335793c22'
__pnl_qualname__ = 'psyneulink.write_json_file'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'write_json_file'
TOOL_DESCRIPTION = 'Call this tool to serialize one or more PsyNeuLink Composition objects to a JSON file on disk. Use it when you need to export a model for inspection, sharing, or later reload via MDF/JSON format. The tool writes a JSON specification file and returns nothing meaningful — side effect is the file at the specified path.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "compositions": {\n      "description": "One or more Composition variable names to serialize. If passing multiple, they must be fully disjoint \\u2014 no shared Mechanisms or Projections.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "filename": {\n      "description": "Name of the output file (e.g. \'my_model.json\'). Do not include the path here.",\n      "type": "string"\n    },\n    "path": {\n      "description": "Directory path for the output file. Defaults to the current working directory if omitted.",\n      "type": "string"\n    },\n    "simple_edge_format": {\n      "default": true,\n      "description": "Whether to use simplified edge format in the JSON output. Defaults to true.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "compositions",\n    "filename"\n  ],\n  "type": "object"\n}\n\nNotes:\nDEPRECATED: `write_json_file` is replaced by `write_mdf_file` and will be removed in a future PsyNeuLink version. Prefer calling `write_mdf_file` with `format=\'json\'` instead. If writing multiple Compositions, they must be fully disjoint — sharing any Component (Mechanism, Projection, etc.) between them will fail; this limitation is expected to be resolved in a future update. `simple_edge_format` is a source-level parameter not documented in the docstring but defaults to True.'
TOOL_PARAMETERS = { 'properties': { 'compositions': { 'description': 'One or more Composition variable '
                                                   'names to serialize. If passing '
                                                   'multiple, they must be fully '
                                                   'disjoint — no shared Mechanisms or '
                                                   'Projections.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'filename': { 'description': 'Name of the output file (e.g. '
                                               "'my_model.json'). Do not include the "
                                               'path here.',
                                'type': 'string'},
                  'path': { 'description': 'Directory path for the output file. '
                                           'Defaults to the current working directory '
                                           'if omitted.',
                            'type': 'string'},
                  'simple_edge_format': { 'default': True,
                                          'description': 'Whether to use simplified '
                                                         'edge format in the JSON '
                                                         'output. Defaults to true.',
                                          'type': 'boolean'}},
  'required': ['compositions', 'filename'],
  'type': 'object'}
TOOL_NOTES = "DEPRECATED: `write_json_file` is replaced by `write_mdf_file` and will be removed in a future PsyNeuLink version. Prefer calling `write_mdf_file` with `format='json'` instead. If writing multiple Compositions, they must be fully disjoint — sharing any Component (Mechanism, Projection, etc.) between them will fail; this limitation is expected to be resolved in a future update. `simple_edge_format` is a source-level parameter not documented in the docstring but defaults to True."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.write_json_file
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
    def write_json_file(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to serialize one or more PsyNeuLink Composition objects to a JSON file on disk.'
        return _impl(args or {})
