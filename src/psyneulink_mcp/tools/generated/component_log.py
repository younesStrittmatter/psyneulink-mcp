"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '646231a97df0e8e490365c7b7dbd506760ddd0e0dc6cc3a1fe5e6837e54f26d8'
__pnl_qualname__ = 'psyneulink.ComponentLog'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_component_log'
TOOL_DESCRIPTION = 'Call this tool to obtain a ComponentLog enum value for use when configuring the `log_condition` or logging settings of a PsyNeuLink Component (Mechanism, Projection, Composition, etc.). Returns an IntEnum instance representing a logging verbosity level. Pass the resulting value wherever PsyNeuLink expects a ComponentLog argument.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "default": 0,\n      "description": "Integer value of the desired ComponentLog member. Valid values: 0 (NONE / ALL / DEFAULTS \\u2014 all three map to 0 in the current implementation).",\n      "enum": [\n        0\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nAll three named members (NONE, ALL, DEFAULTS) resolve to the integer 0 — they are currently identical. The enum exists as a forward-compatibility placeholder; a richer set of bit-flag values may be added in future PNL versions. Calling ComponentLog(0) is equivalent to referencing ComponentLog.NONE, ComponentLog.ALL, or ComponentLog.DEFAULTS. Passing any integer other than 0 will raise a ValueError.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'default': 0,
                             'description': 'Integer value of the desired ComponentLog '
                                            'member. Valid values: 0 (NONE / ALL / '
                                            'DEFAULTS — all three map to 0 in the '
                                            'current implementation).',
                             'enum': [0],
                             'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'All three named members (NONE, ALL, DEFAULTS) resolve to the integer 0 — they are currently identical. The enum exists as a forward-compatibility placeholder; a richer set of bit-flag values may be added in future PNL versions. Calling ComponentLog(0) is equivalent to referencing ComponentLog.NONE, ComponentLog.ALL, or ComponentLog.DEFAULTS. Passing any integer other than 0 will raise a ValueError.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ComponentLog
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
    def create_component_log(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to obtain a ComponentLog enum value for use when configuring the `log_condition` or logging settings of a PsyNeuLink Component (Mechanism, Projection, Composition, etc.).'
        return _impl(args or {})
