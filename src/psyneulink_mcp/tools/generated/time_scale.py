"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '02398d951fe43f3b1d0a1faf1053ff068a2b8766161a9854a9d7e79f130e8d91'
__pnl_qualname__ = 'psyneulink.TimeScale'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_time_scale'
TOOL_DESCRIPTION = 'Call this tool to retrieve a specific TimeScale enum constant when you need to pass a granularity level to a Scheduler, Condition, or any PsyNeuLink API that accepts a TimeScale argument (e.g., `num_trials_in_run`, condition thresholds, or clock queries). Returns the corresponding `TimeScale` enum member (e.g., `TimeScale.PASS`).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Integer index of the desired TimeScale level: 0=CONSIDERATION_SET_EXECUTION (single consideration-set execution, finest grain), 1=PASS (full sweep through all consideration sets), 2=ENVIRONMENT_STATE_UPDATE (one Scheduler.run call), 3=ENVIRONMENT_SEQUENCE (batch of ENVIRONMENT_STATE_UPDATEs), 4=LIFE (since object creation, coarsest grain).",\n      "enum": [\n        0,\n        1,\n        2,\n        3,\n        4\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe PsyNeuLink docstring uses older aliases (TIME_STEP, TRIAL, RUN) that no longer match the actual enum member names, which come from the underlying graph_scheduler library (CONSIDERATION_SET_EXECUTION, ENVIRONMENT_STATE_UPDATE, ENVIRONMENT_SEQUENCE). Use the integer values or the graph_scheduler names — the legacy PNL aliases may not resolve. `TimeScale` supports `<` ordering so members can be compared directly. `TimeScale.get_parent(ts)` and `TimeScale.get_child(ts)` return adjacent levels; calling these on the coarsest (LIFE) or finest (CONSIDERATION_SET_EXECUTION) level respectively will raise a ValueError.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Integer index of the desired TimeScale '
                                            'level: 0=CONSIDERATION_SET_EXECUTION '
                                            '(single consideration-set execution, '
                                            'finest grain), 1=PASS (full sweep through '
                                            'all consideration sets), '
                                            '2=ENVIRONMENT_STATE_UPDATE (one '
                                            'Scheduler.run call), '
                                            '3=ENVIRONMENT_SEQUENCE (batch of '
                                            'ENVIRONMENT_STATE_UPDATEs), 4=LIFE (since '
                                            'object creation, coarsest grain).',
                             'enum': [0, 1, 2, 3, 4],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'The PsyNeuLink docstring uses older aliases (TIME_STEP, TRIAL, RUN) that no longer match the actual enum member names, which come from the underlying graph_scheduler library (CONSIDERATION_SET_EXECUTION, ENVIRONMENT_STATE_UPDATE, ENVIRONMENT_SEQUENCE). Use the integer values or the graph_scheduler names — the legacy PNL aliases may not resolve. `TimeScale` supports `<` ordering so members can be compared directly. `TimeScale.get_parent(ts)` and `TimeScale.get_child(ts)` return adjacent levels; calling these on the coarsest (LIFE) or finest (CONSIDERATION_SET_EXECUTION) level respectively will raise a ValueError.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.TimeScale
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
    def create_time_scale(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to retrieve a specific TimeScale enum constant when you need to pass a granularity level to a Scheduler, Condition, or any PsyNeuLink API that accepts a TimeScale argument (e.g., `num_trials_in_run`, condition thresholds, or clock queries).'
        return _impl(args or {})
