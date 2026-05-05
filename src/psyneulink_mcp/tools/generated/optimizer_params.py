"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '37a731c19f798217159f87535a373e8f1315e94a5a843448ada2bf5a5775ac4b'
__pnl_qualname__ = 'psyneulink.OptimizerParams'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_optimizer_params'
TOOL_DESCRIPTION = 'Call this tool to create an OptimizerParams object that configures gradient-based optimization hyperparameters (currently just learning rate) for a PsyNeuLink Composition or Component before running learning. The result is an OptimizerParams namespace that can be passed wherever PsyNeuLink expects optimizer configuration.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "learning_rate": {\n      "description": "The learning rate for the optimizer (mapped to param group name \'lr\'). Must be a positive float (e.g. 0.01). Scalars and 0-d numpy arrays are both accepted; the value is extracted automatically.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "learning_rate"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `learning_rate` is the only currently supported optimizer parameter; the class is designed for future extension but only exposes `lr` today.\n- Passing `NotImplemented` as `learning_rate` leaves the param unset so PsyNeuLink falls back to the component\'s own default (DEFAULT_LEARNING_RATE). The tool schema marks it required because an agent calling this tool almost always wants to set a concrete value; if you genuinely want the component default, use `OptimizerParams.from_component_defaults(component)` instead of calling this tool.\n- 0-d numpy arrays are silently unwrapped via `try_extract_0d_array_item`; pass a plain Python float for clarity.\n- The class is in `psyneulink.core.compositions.composition` but exported at the top-level `psyneulink` namespace.'
TOOL_PARAMETERS = { 'properties': { 'learning_rate': { 'description': 'The learning rate for the '
                                                    'optimizer (mapped to param group '
                                                    "name 'lr'). Must be a positive "
                                                    'float (e.g. 0.01). Scalars and '
                                                    '0-d numpy arrays are both '
                                                    'accepted; the value is extracted '
                                                    'automatically.',
                                     'type': 'number'}},
  'required': ['learning_rate'],
  'type': 'object'}
TOOL_NOTES = "- `learning_rate` is the only currently supported optimizer parameter; the class is designed for future extension but only exposes `lr` today.\n- Passing `NotImplemented` as `learning_rate` leaves the param unset so PsyNeuLink falls back to the component's own default (DEFAULT_LEARNING_RATE). The tool schema marks it required because an agent calling this tool almost always wants to set a concrete value; if you genuinely want the component default, use `OptimizerParams.from_component_defaults(component)` instead of calling this tool.\n- 0-d numpy arrays are silently unwrapped via `try_extract_0d_array_item`; pass a plain Python float for clarity.\n- The class is in `psyneulink.core.compositions.composition` but exported at the top-level `psyneulink` namespace."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.OptimizerParams
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
    def create_optimizer_params(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an OptimizerParams object that configures gradient-based optimization hyperparameters (currently just learning rate) for a PsyNeuLink Composition or Component before running learning.'
        return _impl(args or {})
