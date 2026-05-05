"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5bce6ac2803c1a2d1d135ab79569414cdfbf1dbb81c7abb2c79a3661988957cb'
__pnl_qualname__ = 'psyneulink.ReportDevices'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_report_devices'
TOOL_DESCRIPTION = 'Call this tool when you need to select which output devices receive PsyNeuLink execution reports — use it to build the value for the `report_to_devices` argument of a Composition\'s `run`, `learn`, or `execute` methods, or a Mechanism\'s `execute` method. Pass one or more device names; they are combined into a single `ReportDevices` Flag value. Omit `devices` entirely to get `CONSOLE` (the default).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "devices": {\n      "default": [\n        "CONSOLE"\n      ],\n      "description": "One or more reporting targets to enable. CONSOLE: print live progress to the terminal. RECORD: capture final output in memory (retrieve via Report._recorded_reports). PNL_VIEW: send to the PsyNeuLinkView GUI (under development). Multiple values are OR-combined into a single Flag.",\n      "items": {\n        "enum": [\n          "CONSOLE",\n          "RECORD",\n          "PNL_VIEW"\n        ],\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nReportDevices is a Flag enum, so values combine with bitwise OR — passing ["CONSOLE", "RECORD"] yields both. RECORD alone suppresses console output; to keep console output while also capturing, pass both explicitly. DIVERT is intentionally excluded from the schema — it is an internal testing device that captures rich-console markup strings and should not be used in agent workflows. PNL_VIEW is listed but marked UNDER DEVELOPMENT and will silently do nothing in most PNL builds.'
TOOL_PARAMETERS = { 'properties': { 'devices': { 'default': ['CONSOLE'],
                               'description': 'One or more reporting targets to '
                                              'enable. CONSOLE: print live progress to '
                                              'the terminal. RECORD: capture final '
                                              'output in memory (retrieve via '
                                              'Report._recorded_reports). PNL_VIEW: '
                                              'send to the PsyNeuLinkView GUI (under '
                                              'development). Multiple values are '
                                              'OR-combined into a single Flag.',
                               'items': { 'enum': ['CONSOLE', 'RECORD', 'PNL_VIEW'],
                                          'type': 'string'},
                               'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'ReportDevices is a Flag enum, so values combine with bitwise OR — passing ["CONSOLE", "RECORD"] yields both. RECORD alone suppresses console output; to keep console output while also capturing, pass both explicitly. DIVERT is intentionally excluded from the schema — it is an internal testing device that captures rich-console markup strings and should not be used in agent workflows. PNL_VIEW is listed but marked UNDER DEVELOPMENT and will silently do nothing in most PNL builds.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ReportDevices
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
    def create_report_devices(args: dict[str, Any] | None = None) -> Any:
        "Call this tool when you need to select which output devices receive PsyNeuLink execution reports — use it to build the value for the `report_to_devices` argument of a Composition's `run`, `learn`, or `execute` methods, or a Mechanism's `execute` method."
        return _impl(args or {})
