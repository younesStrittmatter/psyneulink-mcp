"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5da2e20f4d603969874ba261242777482cca18accfc9c123245b40df2c0ae7ca'
__pnl_qualname__ = 'psyneulink.ReportSimulations'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_report_simulations'
TOOL_DESCRIPTION = 'Call this tool to obtain a ReportSimulations enum value when you need to set the report_simulations argument on Composition.run() or Composition.learn(). Use ReportSimulations.ON to include controller simulation output in progress reporting, or ReportSimulations.OFF to suppress it. Returns the enum member corresponding to the selected option.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Which simulation reporting mode to select: \'OFF\' suppresses all simulation output and progress, \'ON\' enables it. Pass the result as the report_simulations argument to Composition.run() or Composition.learn().",\n      "enum": [\n        "OFF",\n        "ON"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nReportSimulations is an Enum with integer backing values (OFF=0, ON=1). The host instantiates it as ReportSimulations[value] or ReportSimulations(int). Simulations here refer specifically to the optimization trials run by the Composition\'s controller (OptimizationControlMechanism), not the main execution — setting this to ON can produce substantial extra output when a controller is present.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Which simulation reporting mode to '
                                            "select: 'OFF' suppresses all simulation "
                                            "output and progress, 'ON' enables it. "
                                            'Pass the result as the report_simulations '
                                            'argument to Composition.run() or '
                                            'Composition.learn().',
                             'enum': ['OFF', 'ON'],
                             'type': 'string'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = "ReportSimulations is an Enum with integer backing values (OFF=0, ON=1). The host instantiates it as ReportSimulations[value] or ReportSimulations(int). Simulations here refer specifically to the optimization trials run by the Composition's controller (OptimizationControlMechanism), not the main execution — setting this to ON can produce substantial extra output when a controller is present."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ReportSimulations
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
    def create_report_simulations(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to obtain a ReportSimulations enum value when you need to set the report_simulations argument on Composition.run() or Composition.learn().'
        return _impl(args or {})
