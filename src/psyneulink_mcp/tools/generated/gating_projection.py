"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ad2bcf1f2c23586b28def1acd6cf44f92a376ba8f19789de0ce1748a20361d82'
__pnl_qualname__ = 'psyneulink.GatingProjection'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gating_projection'
TOOL_DESCRIPTION = 'Call this tool to create a GatingProjection that modulates the value of an InputPort or OutputPort of a Mechanism at runtime. Use it when wiring gating control into a composition — typically after creating a GatingMechanism — to connect its GatingSignal to a specific port. The projection carries a scalar gating_signal from its sender that multiplicatively (or otherwise) scales the target port\'s value each execution.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "exponent": {\n      "description": "Exponent applied to the gating signal value before it modulates the receiver port.",\n      "type": "number"\n    },\n    "gating_signal_params": {\n      "additionalProperties": true,\n      "description": "Parameter dictionary for the sender\'s GatingSignal (e.g., modulation type). Keys are GatingSignal parameter names; values are their desired settings.",\n      "type": "object"\n    },\n    "name": {\n      "description": "Optional name for this GatingProjection instance.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name of the Mechanism, InputPort, or OutputPort to gate. If a bare Mechanism name is given, the projection targets its primary InputPort by default. If omitted, initialization is deferred.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name of the GatingMechanism or GatingSignal that provides the gating signal. If omitted, initialization is deferred until PsyNeuLink can infer it from context (e.g., when the projection is added to a Composition).",\n      "type": "string"\n    },\n    "weight": {\n      "description": "Scalar weight applied to the gating signal value before it modulates the receiver port.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDeferred initialization: if either sender or receiver is not specified (or cannot be inferred), the projection object is created but not fully initialized until it is added to a Composition or Port context — no error is raised immediately. If receiver is given as a plain Mechanism name, PsyNeuLink silently redirects to that mechanism\'s primary InputPort (index 0). The sender must resolve to a GatingMechanism; passing any other Mechanism type raises an error. The projection\'s function defaults to a Linear with 0-D array output, producing a scalar float that modulates the target port; override via the standard `function` kwarg if needed (not exposed here because it is rarely user-specified).'
TOOL_PARAMETERS = { 'properties': { 'exponent': { 'description': 'Exponent applied to the gating signal '
                                               'value before it modulates the receiver '
                                               'port.',
                                'type': 'number'},
                  'gating_signal_params': { 'additionalProperties': True,
                                            'description': 'Parameter dictionary for '
                                                           "the sender's GatingSignal "
                                                           '(e.g., modulation type). '
                                                           'Keys are GatingSignal '
                                                           'parameter names; values '
                                                           'are their desired '
                                                           'settings.',
                                            'type': 'object'},
                  'name': { 'description': 'Optional name for this GatingProjection '
                                           'instance.',
                            'type': 'string'},
                  'receiver': { 'description': 'Name of the Mechanism, InputPort, or '
                                               'OutputPort to gate. If a bare '
                                               'Mechanism name is given, the '
                                               'projection targets its primary '
                                               'InputPort by default. If omitted, '
                                               'initialization is deferred.',
                                'type': 'string'},
                  'sender': { 'description': 'Name of the GatingMechanism or '
                                             'GatingSignal that provides the gating '
                                             'signal. If omitted, initialization is '
                                             'deferred until PsyNeuLink can infer it '
                                             'from context (e.g., when the projection '
                                             'is added to a Composition).',
                              'type': 'string'},
                  'weight': { 'description': 'Scalar weight applied to the gating '
                                             'signal value before it modulates the '
                                             'receiver port.',
                              'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Deferred initialization: if either sender or receiver is not specified (or cannot be inferred), the projection object is created but not fully initialized until it is added to a Composition or Port context — no error is raised immediately. If receiver is given as a plain Mechanism name, PsyNeuLink silently redirects to that mechanism's primary InputPort (index 0). The sender must resolve to a GatingMechanism; passing any other Mechanism type raises an error. The projection's function defaults to a Linear with 0-D array output, producing a scalar float that modulates the target port; override via the standard `function` kwarg if needed (not exposed here because it is rarely user-specified)."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.GatingProjection
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
    def create_gating_projection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a GatingProjection that modulates the value of an InputPort or OutputPort of a Mechanism at runtime.'
        return _impl(args or {})
