"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '3010d32a844f612fa42159e6150492c4557f4d68efb9a29dfbd88c234ed55667'
__pnl_qualname__ = 'psyneulink.LogCondition'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_log_condition'
TOOL_DESCRIPTION = 'Use this tool when you need to construct a LogCondition flag value to pass to Component.log.set_log_conditions() or similar logging configuration calls. Call it to get a LogCondition instance representing one or more recording phases (e.g., only during EXECUTION, at the end of each TRIAL, or across ALL_ASSIGNMENTS). The result is an IntFlag instance suitable anywhere PsyNeuLink expects a LogCondition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Bitwise integer representing the desired combination of logging phases. Combine multiple phases with bitwise OR on their integer values. Named single-phase shortcuts: OFF=0, INITIALIZATION=2, VALIDATION=4, EXECUTION=8, PROCESSING=16, LEARNING=32, CONTROL=64, SIMULATION=128, TRIAL=256, RUN=512. ALL_ASSIGNMENTS combines all non-OFF members.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nLogCondition is an IntFlag enum; its constructor accepts a single integer positional argument. Passing value=0 yields LogCondition.OFF (no logging). The TRIAL and RUN members are bit-shifted beyond ContextFlags.SIMULATION_MODE, so their integer values are higher than the other phase flags — do not assume they are contiguous with SIMULATION. ALL_ASSIGNMENTS is a convenience composite that enables every phase simultaneously; prefer it over manually OR-ing all flags. The SIMULATION member records values during Composition.controller simulation passes, which is distinct from normal EXECUTION.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Bitwise integer representing the desired '
                                            'combination of logging phases. Combine '
                                            'multiple phases with bitwise OR on their '
                                            'integer values. Named single-phase '
                                            'shortcuts: OFF=0, INITIALIZATION=2, '
                                            'VALIDATION=4, EXECUTION=8, PROCESSING=16, '
                                            'LEARNING=32, CONTROL=64, SIMULATION=128, '
                                            'TRIAL=256, RUN=512. ALL_ASSIGNMENTS '
                                            'combines all non-OFF members.',
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'LogCondition is an IntFlag enum; its constructor accepts a single integer positional argument. Passing value=0 yields LogCondition.OFF (no logging). The TRIAL and RUN members are bit-shifted beyond ContextFlags.SIMULATION_MODE, so their integer values are higher than the other phase flags — do not assume they are contiguous with SIMULATION. ALL_ASSIGNMENTS is a convenience composite that enables every phase simultaneously; prefer it over manually OR-ing all flags. The SIMULATION member records values during Composition.controller simulation passes, which is distinct from normal EXECUTION.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LogCondition
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
    def create_log_condition(args: dict[str, Any] | None = None) -> Any:
        'Use this tool when you need to construct a LogCondition flag value to pass to Component.log.set_log_conditions() or similar logging configuration calls.'
        return _impl(args or {})
