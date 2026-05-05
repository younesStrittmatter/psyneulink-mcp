"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '60bce9135df6777087ee38a9a35ae6ed3aeb32f2aa0685d58642d3e5f9227143'
__pnl_qualname__ = 'psyneulink.ReportOutput'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_report_output'
TOOL_DESCRIPTION = 'Call this tool when you need to obtain a ReportOutput enum constant to pass as the `report_output` argument to a Composition execution method (e.g., `run`, `learn`, `execute`) or `Mechanism.execute()`. Pass the integer value corresponding to the desired verbosity level; the tool returns the matching enum member.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "default": 0,\n      "description": "Enum member value: 0=OFF (suppress all output), 1=TERSE/ON (line-by-line reporting for all Compositions/Mechanisms regardless of preferences), 2=USE_PREFS (respect each object\'s reportOutputPref setting), 3=FULL (formatted panel output at end of each TRIAL for all Compositions/Mechanisms regardless of preferences).",\n      "enum": [\n        0,\n        1,\n        2,\n        3\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nTERSE and ON are aliases (both value=1). FULL uses rich Panel formatting and reports at the end of each TRIAL, not inline during execution — choose TERSE if you want live line-by-line output during a run. USE_PREFS defers to per-object `reportOutputPref` settings, which may suppress output entirely if those preferences are off.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'default': 0,
                             'description': 'Enum member value: 0=OFF (suppress all '
                                            'output), 1=TERSE/ON (line-by-line '
                                            'reporting for all Compositions/Mechanisms '
                                            'regardless of preferences), 2=USE_PREFS '
                                            "(respect each object's reportOutputPref "
                                            'setting), 3=FULL (formatted panel output '
                                            'at end of each TRIAL for all '
                                            'Compositions/Mechanisms regardless of '
                                            'preferences).',
                             'enum': [0, 1, 2, 3],
                             'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'TERSE and ON are aliases (both value=1). FULL uses rich Panel formatting and reports at the end of each TRIAL, not inline during execution — choose TERSE if you want live line-by-line output during a run. USE_PREFS defers to per-object `reportOutputPref` settings, which may suppress output entirely if those preferences are off.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ReportOutput
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
    def create_report_output(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to obtain a ReportOutput enum constant to pass as the `report_output` argument to a Composition execution method (e.g., `run`, `learn`, `execute`) or `Mechanism.execute()`.'
        return _impl(args or {})
