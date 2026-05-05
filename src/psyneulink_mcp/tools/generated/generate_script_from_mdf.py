"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'fdeff82fd0ef01fcb388f84396d941f55c87d818707aca173a26fdf075b40f66'
__pnl_qualname__ = 'psyneulink.generate_script_from_mdf'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'generate_script_from_mdf'
TOOL_DESCRIPTION = 'Call this tool when you have an MDF model (as a file path, JSON string, or YAML string) and need to convert it into a runnable PsyNeuLink Python script. The result is a string containing importable Python code (or the file is written to `outfile` if specified, in which case the return value is None). Use this as the bridge from MDF-format model definitions to executable PsyNeuLink code.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "model_input": {\n      "description": "The MDF model to convert. Accepts: (1) a file path to a .json or .yml MDF file, (2) a raw JSON string encoding the model, or (3) a raw YAML string encoding the model. The function auto-detects the format.",\n      "type": "string"\n    },\n    "outfile": {\n      "description": "Optional file path to write the generated Python script. If omitted, the script text is returned as a string. If provided, the script is written to this path and the function returns None.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "model_input"\n  ],\n  "type": "object"\n}\n\nNotes:\nSECURITY WARNING: This function internally calls exec() to discover importable modules. Only pass MDF models from trusted, known-secure sources. Do not pass user-supplied or untrusted MDF content.\n\nWhen `outfile` is provided, the function returns None (not the script string) — do not expect a return value in that case.\n\n`model_input` is flexible: it can be a filesystem path, a JSON string, or a YAML string; the function tries each in order. If the file does not exist and JSON parsing fails, it falls back to writing a temp YAML file and loading it.\n\nThe generated script uses abbreviated import aliases: `psyneulink as pnl`, `numpy as np`, `dill as dill`.'
TOOL_PARAMETERS = { 'properties': { 'model_input': { 'description': 'The MDF model to convert. Accepts: '
                                                  '(1) a file path to a .json or .yml '
                                                  'MDF file, (2) a raw JSON string '
                                                  'encoding the model, or (3) a raw '
                                                  'YAML string encoding the model. The '
                                                  'function auto-detects the format.',
                                   'type': 'string'},
                  'outfile': { 'description': 'Optional file path to write the '
                                              'generated Python script. If omitted, '
                                              'the script text is returned as a '
                                              'string. If provided, the script is '
                                              'written to this path and the function '
                                              'returns None.',
                               'type': 'string'}},
  'required': ['model_input'],
  'type': 'object'}
TOOL_NOTES = 'SECURITY WARNING: This function internally calls exec() to discover importable modules. Only pass MDF models from trusted, known-secure sources. Do not pass user-supplied or untrusted MDF content.\n\nWhen `outfile` is provided, the function returns None (not the script string) — do not expect a return value in that case.\n\n`model_input` is flexible: it can be a filesystem path, a JSON string, or a YAML string; the function tries each in order. If the file does not exist and JSON parsing fails, it falls back to writing a temp YAML file and loading it.\n\nThe generated script uses abbreviated import aliases: `psyneulink as pnl`, `numpy as np`, `dill as dill`.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.generate_script_from_mdf
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
    def generate_script_from_mdf(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you have an MDF model (as a file path, JSON string, or YAML string) and need to convert it into a runnable PsyNeuLink Python script.'
        return _impl(args or {})
