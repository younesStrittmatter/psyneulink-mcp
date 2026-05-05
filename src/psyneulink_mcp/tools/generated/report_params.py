"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '30be724e07ffbb5bebdaec27f7053af4dda55580f5e36139cc1530009e46aa58'
__pnl_qualname__ = 'psyneulink.ReportParams'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_report_params'
TOOL_DESCRIPTION = 'Call this tool to obtain a ReportParams enum value for use as the report_params argument when running a Composition\'s execution methods (run, learn, execute). Returns the enum member controlling which parameter values are reported during execution — useful when you need finer control than the default (e.g., suppress all output with OFF, or surface only ControlMechanism-modulated parameters with CONTROLLED).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "member": {\n      "description": "The ReportParams member to retrieve. OFF suppresses all param reporting; USE_PREFS defers to each Component\'s reportOutputPref; CONTROLLED/MODULATED (identical) reports params being modulated by a ControlMechanism; MONITORED reports values of Mechanisms monitored by a ControlMechanism or ObjectiveMechanism; LOGGED reports params set to log with LogCondition.EXECUTION; ALL reports every parameter of the Composition and its Nodes.",\n      "enum": [\n        "OFF",\n        "USE_PREFS",\n        "CONTROLLED",\n        "MODULATED",\n        "MONITORED",\n        "LOGGED",\n        "ALL"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "member"\n  ],\n  "type": "object"\n}\n\nNotes:\nCONTROLLED and MODULATED are aliases — both refer to the same enum member (MODULATED = auto(), CONTROLLED = MODULATED). Passing either name produces the same result. This enum is only meaningful as the value of report_params in Composition execution calls; it has no effect outside that context. USE_PREFS is not shown as an enum literal in the source but is documented as a valid option — verify availability in the installed PNL version if needed.'
TOOL_PARAMETERS = { 'properties': { 'member': { 'description': 'The ReportParams member to retrieve. OFF '
                                             'suppresses all param reporting; '
                                             "USE_PREFS defers to each Component's "
                                             'reportOutputPref; CONTROLLED/MODULATED '
                                             '(identical) reports params being '
                                             'modulated by a ControlMechanism; '
                                             'MONITORED reports values of Mechanisms '
                                             'monitored by a ControlMechanism or '
                                             'ObjectiveMechanism; LOGGED reports '
                                             'params set to log with '
                                             'LogCondition.EXECUTION; ALL reports '
                                             'every parameter of the Composition and '
                                             'its Nodes.',
                              'enum': [ 'OFF',
                                        'USE_PREFS',
                                        'CONTROLLED',
                                        'MODULATED',
                                        'MONITORED',
                                        'LOGGED',
                                        'ALL'],
                              'type': 'string'}},
  'required': ['member'],
  'type': 'object'}
TOOL_NOTES = 'CONTROLLED and MODULATED are aliases — both refer to the same enum member (MODULATED = auto(), CONTROLLED = MODULATED). Passing either name produces the same result. This enum is only meaningful as the value of report_params in Composition execution calls; it has no effect outside that context. USE_PREFS is not shown as an enum literal in the source but is documented as a valid option — verify availability in the installed PNL version if needed.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ReportParams
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
    def create_report_params(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to obtain a ReportParams enum value for use as the report_params argument when running a Composition's execution methods (run, learn, execute)."
        return _impl(args or {})
