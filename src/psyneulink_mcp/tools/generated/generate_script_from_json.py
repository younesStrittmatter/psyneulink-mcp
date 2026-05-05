"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '3055f99b0fafa658a9049533efffe2cae1e652c224c5d287f1dede1b739529b6'
__pnl_qualname__ = 'psyneulink.generate_script_from_json'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'generate_script_from_json'
TOOL_DESCRIPTION = 'Call this tool to convert a PsyNeuLink model described in JSON (MDF general format) into a Python script. Pass either a JSON string directly or a path to a JSON file; the tool returns the generated Python script text as a string. Prefer `generate_script_from_mdf` instead — this function is deprecated and will be removed in a future version.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "model_input": {\n      "description": "A JSON string in PsyNeuLink\'s general JSON/MDF format, or a filesystem path to a file containing such JSON.",\n      "type": "string"\n    },\n    "outfile": {\n      "description": "Optional path to write the generated Python script to disk. If omitted, the script text is only returned, not written.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "model_input"\n  ],\n  "type": "object"\n}\n\nNotes:\nDEPRECATED: this function emits a FutureWarning and delegates to `generate_script_from_mdf`. Use `generate_script_from_mdf` directly for new code. Security warning: if `model_input` is a filename, its contents are executed via `exec` internally — only pass files from trusted, known-safe sources to avoid arbitrary code execution.'
TOOL_PARAMETERS = { 'properties': { 'model_input': { 'description': "A JSON string in PsyNeuLink's "
                                                  'general JSON/MDF format, or a '
                                                  'filesystem path to a file '
                                                  'containing such JSON.',
                                   'type': 'string'},
                  'outfile': { 'description': 'Optional path to write the generated '
                                              'Python script to disk. If omitted, the '
                                              'script text is only returned, not '
                                              'written.',
                               'type': 'string'}},
  'required': ['model_input'],
  'type': 'object'}
TOOL_NOTES = 'DEPRECATED: this function emits a FutureWarning and delegates to `generate_script_from_mdf`. Use `generate_script_from_mdf` directly for new code. Security warning: if `model_input` is a filename, its contents are executed via `exec` internally — only pass files from trusted, known-safe sources to avoid arbitrary code execution.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.generate_script_from_json
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
    def generate_script_from_json(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to convert a PsyNeuLink model described in JSON (MDF general format) into a Python script.'
        return _impl(args or {})
