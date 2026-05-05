"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd795040fbb754c4171d7d4d9f41e10fdd13d22f3984ae4dc177c1f1382fe3988'
__pnl_qualname__ = 'psyneulink.ReportProgress'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_report_progress'
TOOL_DESCRIPTION = 'Call this tool to obtain a ReportProgress enum value that controls whether a Composition prints progress updates during run() or learn() execution. Pass the result as the report_progress argument to Composition.run() or Composition.learn(). Returns a ReportProgress enum member (OFF or ON).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "default": "OFF",\n      "description": "OFF suppresses all progress output; ON enables progress reporting during Composition execution.",\n      "enum": [\n        "OFF",\n        "ON"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nReportProgress is an Enum; the tool instantiates it by name (e.g. ReportProgress["ON"]) or by integer value (0=OFF, 1=ON). Most callers never need this tool directly — Composition.run/learn accept the raw enum member, so you typically write ReportProgress.ON inline. Use this tool only when you need to pass a dynamically chosen value or when the enum reference itself is what another tool expects.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'default': 'OFF',
                             'description': 'OFF suppresses all progress output; ON '
                                            'enables progress reporting during '
                                            'Composition execution.',
                             'enum': ['OFF', 'ON'],
                             'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'ReportProgress is an Enum; the tool instantiates it by name (e.g. ReportProgress["ON"]) or by integer value (0=OFF, 1=ON). Most callers never need this tool directly — Composition.run/learn accept the raw enum member, so you typically write ReportProgress.ON inline. Use this tool only when you need to pass a dynamically chosen value or when the enum reference itself is what another tool expects.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ReportProgress
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
    def create_report_progress(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to obtain a ReportProgress enum value that controls whether a Composition prints progress updates during run() or learn() execution.'
        return _impl(args or {})
