"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '852787a8c33f548343d3c41d9f11cf42b61340ae27f8e0f21b32cdcdff0f4bb3'
__pnl_qualname__ = 'psyneulink.DefaultControlMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_default_control_mechanism'
TOOL_DESCRIPTION = 'Call this tool when you need to explicitly instantiate a DefaultControlMechanism — PsyNeuLink\'s built-in pass-through controller that forwards `defaultControlAllocation` values unchanged to any assigned ControlProjections. Use it only when you want to name, configure, or reference the default controller explicitly; in most Compositions PsyNeuLink auto-assigns one and you do not need to call this tool at all.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "control_signals": {\n      "description": "List of ControlSignal specifications (dicts, tuples, or ParameterPort references) defining which parameters this mechanism controls. Each entry causes a corresponding InputPort/OutputPort pair to be created.",\n      "items": {},\n      "type": "array"\n    },\n    "function": {\n      "description": "Transfer function applied to input before sending to control signals. Defaults to Identity (pass-through). Changing this is unusual for DefaultControlMechanism.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for this DefaultControlMechanism instance. If omitted, PsyNeuLink assigns a default name.",\n      "type": "string"\n    },\n    "objective_mechanism": {\n      "description": "An ObjectiveMechanism instance or a list specification for one. Used to monitor outputs and compute the input to the controller. Rarely needed for DefaultControlMechanism since it passes values through unchanged.",\n      "type": [\n        "object",\n        "array"\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDefaultControlMechanism is a pass-through: it does not compute any policy — it simply forwards `defaultControlAllocation` (a scalar, typically 1.0) to every ControlProjection. Explicitly instantiating it is uncommon; PsyNeuLink assigns one automatically to every ControlProjection that has no explicit sender. If you need adaptive or optimizing control, use OptimizationControlMechanism or another ControlMechanism subclass instead. The `params` and `prefs` constructor arguments exist but are advanced/internal; omit them unless you have a specific reason.'
TOOL_PARAMETERS = { 'properties': { 'control_signals': { 'description': 'List of ControlSignal '
                                                      'specifications (dicts, tuples, '
                                                      'or ParameterPort references) '
                                                      'defining which parameters this '
                                                      'mechanism controls. Each entry '
                                                      'causes a corresponding '
                                                      'InputPort/OutputPort pair to be '
                                                      'created.',
                                       'items': {},
                                       'type': 'array'},
                  'function': { 'description': 'Transfer function applied to input '
                                               'before sending to control signals. '
                                               'Defaults to Identity (pass-through). '
                                               'Changing this is unusual for '
                                               'DefaultControlMechanism.',
                                'type': 'string'},
                  'name': { 'description': 'Name for this DefaultControlMechanism '
                                           'instance. If omitted, PsyNeuLink assigns a '
                                           'default name.',
                            'type': 'string'},
                  'objective_mechanism': { 'description': 'An ObjectiveMechanism '
                                                          'instance or a list '
                                                          'specification for one. Used '
                                                          'to monitor outputs and '
                                                          'compute the input to the '
                                                          'controller. Rarely needed '
                                                          'for DefaultControlMechanism '
                                                          'since it passes values '
                                                          'through unchanged.',
                                           'type': ['object', 'array']}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'DefaultControlMechanism is a pass-through: it does not compute any policy — it simply forwards `defaultControlAllocation` (a scalar, typically 1.0) to every ControlProjection. Explicitly instantiating it is uncommon; PsyNeuLink assigns one automatically to every ControlProjection that has no explicit sender. If you need adaptive or optimizing control, use OptimizationControlMechanism or another ControlMechanism subclass instead. The `params` and `prefs` constructor arguments exist but are advanced/internal; omit them unless you have a specific reason.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DefaultControlMechanism
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
    def create_default_control_mechanism(args: dict[str, Any] | None = None) -> Any:
        "Call this tool when you need to explicitly instantiate a DefaultControlMechanism — PsyNeuLink's built-in pass-through controller that forwards `defaultControlAllocation` values unchanged to any assigned ControlProjections."
        return _impl(args or {})
