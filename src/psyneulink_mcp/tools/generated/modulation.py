"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6402576dbbe4a059146c7a303f45d61e0d456e5c79a5d26a888045066f685c81'
__pnl_qualname__ = 'psyneulink.Modulation'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_modulation'
TOOL_DESCRIPTION = 'Call this tool when you need to select a modulation strategy for a PsyNeuLink modulatory signal (ControlSignal, GatingSignal, LearningSignal, etc.) and want to specify or verify how the runtime signal value should combine with a parameter\'s default. Returns the Modulation enum member corresponding to the chosen strategy: MULTIPLY (runtime × default), ADD (runtime + default), OVERRIDE (runtime replaces default), or DISABLE (no modulation). Pass the result name string as the `modulation` argument to mechanism or projection constructor tools.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "member": {\n      "description": "Name of the modulation strategy to retrieve. MULTIPLY: scales the parameter by the signal value; ADD: offsets the parameter by the signal value; OVERRIDE: replaces the parameter entirely with the signal value; DISABLE: signal has no effect on the parameter.",\n      "enum": [\n        "MULTIPLY",\n        "ADD",\n        "OVERRIDE",\n        "DISABLE"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "member"\n  ],\n  "type": "object"\n}\n\nNotes:\nDISABLE is the only integer-valued member (0); MULTIPLY, ADD, and OVERRIDE are lambda functions — do not attempt to pass their values directly in JSON. Always reference members by name string. The default modulation for most PsyNeuLink modulatory signals is MULTIPLY; only specify a different strategy when the modeling intent requires additive offsets (ADD), hard overrides (OVERRIDE), or disabling modulation entirely (DISABLE). When passing modulation to a component tool, use the bare string name (e.g., "MULTIPLY") or the qualified enum reference psyneulink.Modulation.MULTIPLY — the component constructors accept both.'
TOOL_PARAMETERS = { 'properties': { 'member': { 'description': 'Name of the modulation strategy to '
                                             'retrieve. MULTIPLY: scales the parameter '
                                             'by the signal value; ADD: offsets the '
                                             'parameter by the signal value; OVERRIDE: '
                                             'replaces the parameter entirely with the '
                                             'signal value; DISABLE: signal has no '
                                             'effect on the parameter.',
                              'enum': ['MULTIPLY', 'ADD', 'OVERRIDE', 'DISABLE'],
                              'type': 'string'}},
  'required': ['member'],
  'type': 'object'}
TOOL_NOTES = 'DISABLE is the only integer-valued member (0); MULTIPLY, ADD, and OVERRIDE are lambda functions — do not attempt to pass their values directly in JSON. Always reference members by name string. The default modulation for most PsyNeuLink modulatory signals is MULTIPLY; only specify a different strategy when the modeling intent requires additive offsets (ADD), hard overrides (OVERRIDE), or disabling modulation entirely (DISABLE). When passing modulation to a component tool, use the bare string name (e.g., "MULTIPLY") or the qualified enum reference psyneulink.Modulation.MULTIPLY — the component constructors accept both.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Modulation
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
    def create_modulation(args: dict[str, Any] | None = None) -> Any:
        "Call this tool when you need to select a modulation strategy for a PsyNeuLink modulatory signal (ControlSignal, GatingSignal, LearningSignal, etc.) and want to specify or verify how the runtime signal value should combine with a parameter's default."
        return _impl(args or {})
