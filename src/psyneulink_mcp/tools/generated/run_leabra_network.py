"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '241684e13630aa6bc536caf23132c794c9f23ce8c321cc2a7f6d82877d7d046c'
__pnl_qualname__ = 'psyneulink.run_leabra_network'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'run_leabra_network'
TOOL_DESCRIPTION = 'Call this tool to run a single forward-pass inference trial on a pre-built Leabra network. Pass the network object returned by `build_leabra_network` and a numeric input pattern whose length matches the network\'s input layer. Returns a numpy array of post-minus-phase activations (`act_m`) from the final layer.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "input_pattern": {\n      "description": "Activation values to clamp onto the input layer. Length must exactly match the number of units in network.layers[0].",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "network": {\n      "description": "A Leabra network object previously constructed by build_leabra_network. Must have at least two layers; the first layer\'s unit count must equal the length of input_pattern.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "network",\n    "input_pattern"\n  ],\n  "type": "object"\n}\n\nNotes:\nIf the network\'s training flag is currently True, this function temporarily disables training for the trial and re-enables it afterward — the caller does not need to manage this. The function asserts that len(input_pattern) == len(network.layers[0].units); mismatched lengths raise AssertionError, not a descriptive exception. The return value is a numpy array, not a plain Python list. Only the last layer\'s act_m values are returned; intermediate layer activations are not exposed.'
TOOL_PARAMETERS = { 'properties': { 'input_pattern': { 'description': 'Activation values to clamp onto '
                                                    'the input layer. Length must '
                                                    'exactly match the number of units '
                                                    'in network.layers[0].',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'network': { 'description': 'A Leabra network object previously '
                                              'constructed by build_leabra_network. '
                                              'Must have at least two layers; the '
                                              "first layer's unit count must equal the "
                                              'length of input_pattern.',
                               'type': 'object'}},
  'required': ['network', 'input_pattern'],
  'type': 'object'}
TOOL_NOTES = "If the network's training flag is currently True, this function temporarily disables training for the trial and re-enables it afterward — the caller does not need to manage this. The function asserts that len(input_pattern) == len(network.layers[0].units); mismatched lengths raise AssertionError, not a descriptive exception. The return value is a numpy array, not a plain Python list. Only the last layer's act_m values are returned; intermediate layer activations are not exposed."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.run_leabra_network
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
    def run_leabra_network(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to run a single forward-pass inference trial on a pre-built Leabra network.'
        return _impl(args or {})
