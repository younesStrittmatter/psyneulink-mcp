"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e9e450fd7cc2c193ab94c06551585c345eb2147b4fd8e35b3c4e7ebbae31fb49'
__pnl_qualname__ = 'psyneulink.DefaultControlAllocationMode'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_default_control_allocation_mode'
TOOL_DESCRIPTION = 'Use this tool to select a DefaultControlAllocationMode enum member when a PsyNeuLink controller setup tool requires a control allocation mode argument. Call it to obtain the correct enum constant (GUMBY_MODE, BADGER_MODE, or TEST_MODE) before passing it to controller configuration calls such as Composition.add_controller. The result is a PsyNeuLink enum member that encodes the chosen allocation strategy.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Numeric value identifying the enum member: GUMBY_MODE=0.0 (passive/zero allocation), BADGER_MODE=1.0 (standard allocation), TEST_MODE=240 (diagnostic/internal use).",\n      "enum": [\n        0,\n        1,\n        240\n      ],\n      "type": "number"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nEnum is instantiated by value: DefaultControlAllocationMode(value=0.0) yields GUMBY_MODE. The semantic difference between GUMBY_MODE and BADGER_MODE is not documented beyond the names; BADGER_MODE (1.0) is the conventional standard mode. TEST_MODE (240) is almost certainly for internal PsyNeuLink testing — avoid in production models. This tool exists primarily to surface the available constants to the agent; in most workflows the caller simply passes the enum member name as a string literal to the controlling tool instead of calling this tool explicitly.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Numeric value identifying the enum '
                                            'member: GUMBY_MODE=0.0 (passive/zero '
                                            'allocation), BADGER_MODE=1.0 (standard '
                                            'allocation), TEST_MODE=240 '
                                            '(diagnostic/internal use).',
                             'enum': [0, 1, 240],
                             'type': 'number'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'Enum is instantiated by value: DefaultControlAllocationMode(value=0.0) yields GUMBY_MODE. The semantic difference between GUMBY_MODE and BADGER_MODE is not documented beyond the names; BADGER_MODE (1.0) is the conventional standard mode. TEST_MODE (240) is almost certainly for internal PsyNeuLink testing — avoid in production models. This tool exists primarily to surface the available constants to the agent; in most workflows the caller simply passes the enum member name as a string literal to the controlling tool instead of calling this tool explicitly.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DefaultControlAllocationMode
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
    def create_default_control_allocation_mode(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to select a DefaultControlAllocationMode enum member when a PsyNeuLink controller setup tool requires a control allocation mode argument.'
        return _impl(args or {})
