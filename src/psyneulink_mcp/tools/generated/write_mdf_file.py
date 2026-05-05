"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '742b1c290558eb35ff76987f78fa2eb3f029ac9638b753b6c635aeefa3cc8455'
__pnl_qualname__ = 'psyneulink.write_mdf_file'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'write_mdf_file'
TOOL_DESCRIPTION = 'Call this tool to serialize one or more PsyNeuLink Compositions to an MDF (Model Description Format) file on disk in JSON or YAML. Use it after building a model when you need to export it for sharing, visualization, or interoperability with other MDF-compatible tools. The tool writes the file and returns the serialization result.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "compositions": {\n      "description": "Name (string) or list of names of the Composition(s) to export. Multiple compositions must be fully disjoint \\u2014 they must not share any Mechanisms, Projections, or other Components.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "filename": {\n      "description": "Output filename. If no fmt is specified, the file extension determines the format (e.g. \'model.json\' \\u2192 JSON, \'model.yaml\' \\u2192 YAML). Falls back to JSON if no extension is detected.",\n      "type": "string"\n    },\n    "fmt": {\n      "description": "Explicit output format. If omitted, auto-detected from the filename extension. Supported values: \'json\', \'yml\', \'yaml\'.",\n      "enum": [\n        "json",\n        "yml",\n        "yaml"\n      ],\n      "type": "string"\n    },\n    "path": {\n      "description": "Directory path in which to write the file. Defaults to the current working directory if omitted.",\n      "type": "string"\n    },\n    "simple_edge_format": {\n      "default": true,\n      "description": "Whether to use the MDF simple edge format. Defaults to true; set to false only if the consuming tool requires full edge objects.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "compositions",\n    "filename"\n  ],\n  "type": "object"\n}\n\nNotes:\nMultiple compositions must be fully disjoint — shared Components (Mechanisms, Projections, etc.) across compositions will cause errors; this limitation is planned to be removed in a future PNL update. Format is auto-detected from the filename extension and falls back to \'json\' if no extension is present or recognizable. simple_edge_format defaults to True; most downstream MDF tools expect this default. Passing an unsupported fmt string raises ValueError listing the valid options.'
TOOL_PARAMETERS = { 'properties': { 'compositions': { 'description': 'Name (string) or list of names of '
                                                   'the Composition(s) to export. '
                                                   'Multiple compositions must be '
                                                   'fully disjoint — they must not '
                                                   'share any Mechanisms, Projections, '
                                                   'or other Components.',
                                    'oneOf': [ {'type': 'string'},
                                               { 'items': {'type': 'string'},
                                                 'type': 'array'}]},
                  'filename': { 'description': 'Output filename. If no fmt is '
                                               'specified, the file extension '
                                               'determines the format (e.g. '
                                               "'model.json' → JSON, 'model.yaml' → "
                                               'YAML). Falls back to JSON if no '
                                               'extension is detected.',
                                'type': 'string'},
                  'fmt': { 'description': 'Explicit output format. If omitted, '
                                          'auto-detected from the filename extension. '
                                          "Supported values: 'json', 'yml', 'yaml'.",
                           'enum': ['json', 'yml', 'yaml'],
                           'type': 'string'},
                  'path': { 'description': 'Directory path in which to write the file. '
                                           'Defaults to the current working directory '
                                           'if omitted.',
                            'type': 'string'},
                  'simple_edge_format': { 'default': True,
                                          'description': 'Whether to use the MDF '
                                                         'simple edge format. Defaults '
                                                         'to true; set to false only '
                                                         'if the consuming tool '
                                                         'requires full edge objects.',
                                          'type': 'boolean'}},
  'required': ['compositions', 'filename'],
  'type': 'object'}
TOOL_NOTES = "Multiple compositions must be fully disjoint — shared Components (Mechanisms, Projections, etc.) across compositions will cause errors; this limitation is planned to be removed in a future PNL update. Format is auto-detected from the filename extension and falls back to 'json' if no extension is present or recognizable. simple_edge_format defaults to True; most downstream MDF tools expect this default. Passing an unsupported fmt string raises ValueError listing the valid options."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.write_mdf_file
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
    def write_mdf_file(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to serialize one or more PsyNeuLink Compositions to an MDF (Model Description Format) file on disk in JSON or YAML.'
        return _impl(args or {})
