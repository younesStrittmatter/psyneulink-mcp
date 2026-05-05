"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '3ea8c8a73dddb6ab9f81b3af23e43493cd7a0fbcdbce52228048479a16a3060b'
__pnl_qualname__ = 'psyneulink.ControlProjection'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_control_projection'
TOOL_DESCRIPTION = 'Call this tool to create a ControlProjection that connects a ControlMechanism (or ControlSignal) to a ParameterPort, InputPort, or OutputPort of a Mechanism, thereby modulating that parameter\'s value at runtime. Use it when you need explicit control over a specific parameter — e.g., wiring a controller\'s output to a Mechanism\'s gain or threshold — outside of the automatic projection creation that occurs when you add a controller to a Composition. Returns a ControlProjection object that can be added to a Composition or referenced in controller configuration.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "control_signal_params": {\n      "additionalProperties": true,\n      "description": "Dictionary of parameter keyword-value pairs forwarded to the ControlSignal on the sender side (e.g., modulation type, cost functions, allocation range). Keys are ControlSignal parameter names.",\n      "type": "object"\n    },\n    "exponent": {\n      "description": "Exponent applied to the control signal before it reaches the receiver. Default is None (no exponentiation).",\n      "type": "number"\n    },\n    "function": {\n      "description": "Transfer function applied to the control signal. Defaults to Linear (identity pass-through). Specify as a PsyNeuLink Function name or instance.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the ControlProjection instance.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name or reference to the ParameterPort, InputPort, or OutputPort (or the Mechanism that owns exactly one ParameterPort) that will be modulated. If omitted, initialization is deferred.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name or reference to the ControlMechanism or ControlSignal that is the source of the control signal. If omitted, initialization is deferred until the projection is placed in context (e.g., added to a Composition with a controller).",\n      "type": "string"\n    },\n    "weight": {\n      "description": "Scalar weight applied to the control signal before it reaches the receiver. Default is None (no weighting).",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nInitialization is deferred (no error raised immediately) when sender or receiver is None or not yet fully initialized — the projection completes initialization when added to a Composition that can resolve both endpoints. If receiver is given as a Mechanism rather than a specific Port, that Mechanism must have exactly one ParameterPort or an error is raised. The function defaults to Linear, meaning the control signal passes through unchanged. control_signal_params targets the *sender* ControlSignal, not the projection itself — use it for things like allocation_samples, modulation mode, or cost function settings.'
TOOL_PARAMETERS = { 'properties': { 'control_signal_params': { 'additionalProperties': True,
                                             'description': 'Dictionary of parameter '
                                                            'keyword-value pairs '
                                                            'forwarded to the '
                                                            'ControlSignal on the '
                                                            'sender side (e.g., '
                                                            'modulation type, cost '
                                                            'functions, allocation '
                                                            'range). Keys are '
                                                            'ControlSignal parameter '
                                                            'names.',
                                             'type': 'object'},
                  'exponent': { 'description': 'Exponent applied to the control signal '
                                               'before it reaches the receiver. '
                                               'Default is None (no exponentiation).',
                                'type': 'number'},
                  'function': { 'description': 'Transfer function applied to the '
                                               'control signal. Defaults to Linear '
                                               '(identity pass-through). Specify as a '
                                               'PsyNeuLink Function name or instance.',
                                'type': 'string'},
                  'name': { 'description': 'Optional name for the ControlProjection '
                                           'instance.',
                            'type': 'string'},
                  'receiver': { 'description': 'Name or reference to the '
                                               'ParameterPort, InputPort, or '
                                               'OutputPort (or the Mechanism that owns '
                                               'exactly one ParameterPort) that will '
                                               'be modulated. If omitted, '
                                               'initialization is deferred.',
                                'type': 'string'},
                  'sender': { 'description': 'Name or reference to the '
                                             'ControlMechanism or ControlSignal that '
                                             'is the source of the control signal. If '
                                             'omitted, initialization is deferred '
                                             'until the projection is placed in '
                                             'context (e.g., added to a Composition '
                                             'with a controller).',
                              'type': 'string'},
                  'weight': { 'description': 'Scalar weight applied to the control '
                                             'signal before it reaches the receiver. '
                                             'Default is None (no weighting).',
                              'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Initialization is deferred (no error raised immediately) when sender or receiver is None or not yet fully initialized — the projection completes initialization when added to a Composition that can resolve both endpoints. If receiver is given as a Mechanism rather than a specific Port, that Mechanism must have exactly one ParameterPort or an error is raised. The function defaults to Linear, meaning the control signal passes through unchanged. control_signal_params targets the *sender* ControlSignal, not the projection itself — use it for things like allocation_samples, modulation mode, or cost function settings.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ControlProjection
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
    def create_control_projection(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to create a ControlProjection that connects a ControlMechanism (or ControlSignal) to a ParameterPort, InputPort, or OutputPort of a Mechanism, thereby modulating that parameter's value at runtime."
        return _impl(args or {})
