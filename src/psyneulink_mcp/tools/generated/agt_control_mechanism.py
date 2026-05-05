"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e6c3bd53cb9e22dd0e5c010066a5d6bc240faf178e41f2979f4499c535f92b89'
__pnl_qualname__ = 'psyneulink.AGTControlMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_agt_control_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create an AGTControlMechanism — a control mechanism that uses a dual adaptive integrator (short-term and long-term utility tracking) to automatically modulate the multiplicative parameter of one or more Mechanism functions. Use it when you want gain-modulation of processing units driven by adaptive utility signals, similar to an attentional gating (AGT) model. Returns a configured AGTControlMechanism ready to be added to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "control_signals": {\n      "description": "List specifying which Mechanism parameters to modulate. Each entry can be a ParameterPort, a (param_name, Mechanism) tuple, or a dict. A ControlSignal is created for each entry.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "modulation": {\n      "description": "Modulation mode for all ControlSignals \\u2014 overrides the default (MULTIPLICATIVE). Rarely needed; omit to accept the default multiplicative modulation.",\n      "type": "string"\n    },\n    "monitored_output_ports": {\n      "description": "List of OutputPorts, Mechanisms, or their string names whose values will be monitored to drive control. Each item can also be a dict or tuple with weight/exponent for the DualAdaptiveIntegrator.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional string name for the AGTControlMechanism instance. If omitted, PsyNeuLink auto-generates one.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe ObjectiveMechanism is created automatically and always uses DualAdaptiveIntegrator as its function — you cannot pass a custom function. The objective mechanism\'s name is set to `{name}_ObjectiveMechanism`. AGTControlMechanism modulates only the `multiplicative_param` of target Mechanism functions; if the target function lacks a multiplicative parameter, adding it will fail at validation. The `monitored_output_ports` items passed here are forwarded to the internal ObjectiveMechanism, not held directly on the AGTControlMechanism itself. Fine-grained DualAdaptiveIntegrator parameters (short_term_gain, long_term_gain, short_term_rate, long_term_rate, short_term_bias, long_term_bias, initial_short_term_utility, initial_long_term_utility, operation) can only be set post-construction via attribute assignment on the returned instance.'
TOOL_PARAMETERS = { 'properties': { 'control_signals': { 'description': 'List specifying which Mechanism '
                                                      'parameters to modulate. Each '
                                                      'entry can be a ParameterPort, a '
                                                      '(param_name, Mechanism) tuple, '
                                                      'or a dict. A ControlSignal is '
                                                      'created for each entry.',
                                       'items': {'type': 'object'},
                                       'type': 'array'},
                  'modulation': { 'description': 'Modulation mode for all '
                                                 'ControlSignals — overrides the '
                                                 'default (MULTIPLICATIVE). Rarely '
                                                 'needed; omit to accept the default '
                                                 'multiplicative modulation.',
                                  'type': 'string'},
                  'monitored_output_ports': { 'description': 'List of OutputPorts, '
                                                             'Mechanisms, or their '
                                                             'string names whose '
                                                             'values will be monitored '
                                                             'to drive control. Each '
                                                             'item can also be a dict '
                                                             'or tuple with '
                                                             'weight/exponent for the '
                                                             'DualAdaptiveIntegrator.',
                                              'items': {'type': 'string'},
                                              'type': 'array'},
                  'name': { 'description': 'Optional string name for the '
                                           'AGTControlMechanism instance. If omitted, '
                                           'PsyNeuLink auto-generates one.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "The ObjectiveMechanism is created automatically and always uses DualAdaptiveIntegrator as its function — you cannot pass a custom function. The objective mechanism's name is set to `{name}_ObjectiveMechanism`. AGTControlMechanism modulates only the `multiplicative_param` of target Mechanism functions; if the target function lacks a multiplicative parameter, adding it will fail at validation. The `monitored_output_ports` items passed here are forwarded to the internal ObjectiveMechanism, not held directly on the AGTControlMechanism itself. Fine-grained DualAdaptiveIntegrator parameters (short_term_gain, long_term_gain, short_term_rate, long_term_rate, short_term_bias, long_term_bias, initial_short_term_utility, initial_long_term_utility, operation) can only be set post-construction via attribute assignment on the returned instance."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.AGTControlMechanism
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
    def create_agt_control_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an AGTControlMechanism — a control mechanism that uses a dual adaptive integrator (short-term and long-term utility tracking) to automatically modulate the multiplicative parameter of one or more Mechanism functions.'
        return _impl(args or {})
