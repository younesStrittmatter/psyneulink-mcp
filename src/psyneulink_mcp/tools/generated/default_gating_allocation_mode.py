"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5b2d5f83c6ae5d02f0d990dc9d2c076d84aadd81cf728b14a1959602bca8dc71'
__pnl_qualname__ = 'psyneulink.DefaultGatingAllocationMode'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_default_gating_allocation_mode'
TOOL_DESCRIPTION = 'Call this tool to retrieve a DefaultGatingAllocationMode enum member by its numeric value — use it when you need to pass a specific gating allocation mode (e.g., PHASIC_MODE, TONIC_MODE, SLEEP_MODE, or TEST_MODE) to a GatingMechanism or related component. The result is the corresponding enum member (e.g., DefaultGatingAllocationMode.PHASIC_MODE).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Numeric value identifying the gating mode: 1.0 = PHASIC_MODE, 0.5 = TONIC_MODE, 0.0 = SLEEP_MODE, 240 = TEST_MODE.",\n      "enum": [\n        1,\n        0.5,\n        0,\n        240\n      ],\n      "type": "number"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is an Enum, not a constructor — calling DefaultGatingAllocationMode(value) performs a value-based lookup and returns the matching member; passing an unrecognized value raises ValueError. TEST_MODE (240) is an integer, while the others are floats; pass exactly 240, not 240.0, to avoid a lookup miss. Most agent use cases only need PHASIC_MODE (1.0) or TONIC_MODE (0.5); SLEEP_MODE (0.0) suppresses gating entirely and TEST_MODE is for internal testing.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Numeric value identifying the gating '
                                            'mode: 1.0 = PHASIC_MODE, 0.5 = '
                                            'TONIC_MODE, 0.0 = SLEEP_MODE, 240 = '
                                            'TEST_MODE.',
                             'enum': [1, 0.5, 0, 240],
                             'type': 'number'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'This is an Enum, not a constructor — calling DefaultGatingAllocationMode(value) performs a value-based lookup and returns the matching member; passing an unrecognized value raises ValueError. TEST_MODE (240) is an integer, while the others are floats; pass exactly 240, not 240.0, to avoid a lookup miss. Most agent use cases only need PHASIC_MODE (1.0) or TONIC_MODE (0.5); SLEEP_MODE (0.0) suppresses gating entirely and TEST_MODE is for internal testing.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DefaultGatingAllocationMode
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
    def create_default_gating_allocation_mode(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to retrieve a DefaultGatingAllocationMode enum member by its numeric value — use it when you need to pass a specific gating allocation mode (e.g., PHASIC_MODE, TONIC_MODE, SLEEP_MODE, or TEST_MODE) to a GatingMechanism or related component.'
        return _impl(args or {})
