"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '513c938b1f2c60e4360b71cf5cd242b4eac72303e49c24d4a19b218b330de0fe'
__pnl_qualname__ = 'psyneulink.train_leabra_network'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'train_leabra_network'
TOOL_DESCRIPTION = 'Call this tool to run a single supervised training trial on a Leabra network, pairing an input pattern with a target output pattern. The tool temporarily enables training mode if needed, executes the trial, and returns the output layer\'s plus-phase activations as a numeric array — use the result to monitor learning progress across trials.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "input_pattern": {\n      "description": "Activation values for the input layer. Length must exactly match the number of units in network.layers[0].",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "network": {\n      "description": "A Leabra network object previously created by build_leabra_network. Must have at least two layers; the first is treated as the input layer and the last as the output layer.",\n      "type": "object"\n    },\n    "output_pattern": {\n      "description": "Target (teaching) activation values for the output layer. Length must exactly match the number of units in network.layers[-1].",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "network",\n    "input_pattern",\n    "output_pattern"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function asserts (hard crash, not a soft error) that len(input_pattern) == len(network.layers[0].units) and len(output_pattern) == len(network.layers[-1].units) — mismatched sizes raise AssertionError, not a friendly ValueError. If the network\'s training flag is currently False, the function silently flips it to True for the trial and then back to False; this side-effect is invisible to the caller but means the network\'s training state after the call always mirrors its state before the call. The returned array contains plus-phase (act_m) activations, not raw predictions — these reflect the network state after the supervised settling phase.'
TOOL_PARAMETERS = { 'properties': { 'input_pattern': { 'description': 'Activation values for the input '
                                                    'layer. Length must exactly match '
                                                    'the number of units in '
                                                    'network.layers[0].',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'network': { 'description': 'A Leabra network object previously '
                                              'created by build_leabra_network. Must '
                                              'have at least two layers; the first is '
                                              'treated as the input layer and the last '
                                              'as the output layer.',
                               'type': 'object'},
                  'output_pattern': { 'description': 'Target (teaching) activation '
                                                     'values for the output layer. '
                                                     'Length must exactly match the '
                                                     'number of units in '
                                                     'network.layers[-1].',
                                      'items': {'type': 'number'},
                                      'type': 'array'}},
  'required': ['network', 'input_pattern', 'output_pattern'],
  'type': 'object'}
TOOL_NOTES = "The function asserts (hard crash, not a soft error) that len(input_pattern) == len(network.layers[0].units) and len(output_pattern) == len(network.layers[-1].units) — mismatched sizes raise AssertionError, not a friendly ValueError. If the network's training flag is currently False, the function silently flips it to True for the trial and then back to False; this side-effect is invisible to the caller but means the network's training state after the call always mirrors its state before the call. The returned array contains plus-phase (act_m) activations, not raw predictions — these reflect the network state after the supervised settling phase."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.train_leabra_network
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
    def train_leabra_network(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to run a single supervised training trial on a Leabra network, pairing an input pattern with a target output pattern.'
        return _impl(args or {})
