"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ac45a93ff3ee2ba8907795102f7b518ee00ffbb69b438f8b3a7b27f4ed2445f5'
__pnl_qualname__ = 'psyneulink.SchedulingMode'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_scheduling_mode'
TOOL_DESCRIPTION = 'Call this tool to obtain a `SchedulingMode` enum member that governs how a PsyNeuLink `Scheduler` sequences node execution. Pass the result to a `Scheduler`\'s `mode` parameter. Use `STANDARD` (1) for normal condition-based scheduling and `EXACT_TIME` (2) when execution must be pinned to precise simulation time steps.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Enum value: 1 = STANDARD (default condition-based scheduling), 2 = EXACT_TIME (time-step-precise execution)",\n      "enum": [\n        1,\n        2\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nMembers use `enum.auto()`, so STANDARD=1 and EXACT_TIME=2. These integer values are the only valid inputs. You can also access members directly as `psyneulink.SchedulingMode.STANDARD` or `psyneulink.SchedulingMode.EXACT_TIME` without calling this tool — prefer direct attribute access when composing Scheduler arguments in Python.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Enum value: 1 = STANDARD (default '
                                            'condition-based scheduling), 2 = '
                                            'EXACT_TIME (time-step-precise execution)',
                             'enum': [1, 2],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'Members use `enum.auto()`, so STANDARD=1 and EXACT_TIME=2. These integer values are the only valid inputs. You can also access members directly as `psyneulink.SchedulingMode.STANDARD` or `psyneulink.SchedulingMode.EXACT_TIME` without calling this tool — prefer direct attribute access when composing Scheduler arguments in Python.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.SchedulingMode
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
    def create_scheduling_mode(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to obtain a `SchedulingMode` enum member that governs how a PsyNeuLink `Scheduler` sequences node execution.'
        return _impl(args or {})
