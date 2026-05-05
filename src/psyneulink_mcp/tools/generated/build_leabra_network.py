"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c115f6e43266963ee21b2e0df01d3067048b424f6a55fd40aca9ef7889646391'
__pnl_qualname__ = 'psyneulink.build_leabra_network'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'build_leabra_network'
TOOL_DESCRIPTION = 'Call this tool to construct a leabra.Network for use with PsyNeuLink\'s LeabraMechanism. Returns a configured leabra Network object with an input layer, one or more hidden layers, and an output layer, all connected with full uniform-weight projections. Use this before instantiating a LeabraMechanism that requires a pre-built leabra network.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "hidden_sizes": {\n      "description": "Size(s) of hidden layers. A single number applies the same size to all hidden layers; an array specifies sizes per layer in order. If omitted, each hidden layer defaults to n_input units.",\n      "items": {\n        "type": "number"\n      },\n      "type": [\n        "number",\n        "array"\n      ]\n    },\n    "n_hidden": {\n      "description": "Number of hidden layers to create between input and output.",\n      "type": "integer"\n    },\n    "n_input": {\n      "description": "Number of units in the input layer.",\n      "type": "integer"\n    },\n    "n_output": {\n      "description": "Number of units in the output layer.",\n      "type": "integer"\n    },\n    "quarter_size": {\n      "default": 50,\n      "description": "Number of time steps per quarter cycle in the leabra network\'s NetworkSpec. Defaults to 50.",\n      "type": "integer"\n    },\n    "training_flag": {\n      "description": "Set to true to enable the Leabra learning rule on all connections. Any other value (false or omitted) disables learning.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "n_input",\n    "n_output",\n    "n_hidden"\n  ],\n  "type": "object"\n}\n\nNotes:\nAll layers use LayerSpec(lay_inhib=True) and UnitSpec(adapt_on=True, noisy_act=True) — these are hardcoded and not configurable via this tool. Connections use full projections with uniform random weights (mean=0.75, var=0.2). Only training_flag=True (boolean True, not a truthy value) activates the Leabra learning rule; None or False both result in no learning rule. If hidden_sizes is a single number it is broadcast to all n_hidden layers. The returned object is a leabra.Network, not a PsyNeuLink Composition; pass it to LeabraMechanism\'s network argument.'
TOOL_PARAMETERS = { 'properties': { 'hidden_sizes': { 'description': 'Size(s) of hidden layers. A single '
                                                   'number applies the same size to '
                                                   'all hidden layers; an array '
                                                   'specifies sizes per layer in '
                                                   'order. If omitted, each hidden '
                                                   'layer defaults to n_input units.',
                                    'items': {'type': 'number'},
                                    'type': ['number', 'array']},
                  'n_hidden': { 'description': 'Number of hidden layers to create '
                                               'between input and output.',
                                'type': 'integer'},
                  'n_input': { 'description': 'Number of units in the input layer.',
                               'type': 'integer'},
                  'n_output': { 'description': 'Number of units in the output layer.',
                                'type': 'integer'},
                  'quarter_size': { 'default': 50,
                                    'description': 'Number of time steps per quarter '
                                                   "cycle in the leabra network's "
                                                   'NetworkSpec. Defaults to 50.',
                                    'type': 'integer'},
                  'training_flag': { 'description': 'Set to true to enable the Leabra '
                                                    'learning rule on all connections. '
                                                    'Any other value (false or '
                                                    'omitted) disables learning.',
                                     'type': 'boolean'}},
  'required': ['n_input', 'n_output', 'n_hidden'],
  'type': 'object'}
TOOL_NOTES = "All layers use LayerSpec(lay_inhib=True) and UnitSpec(adapt_on=True, noisy_act=True) — these are hardcoded and not configurable via this tool. Connections use full projections with uniform random weights (mean=0.75, var=0.2). Only training_flag=True (boolean True, not a truthy value) activates the Leabra learning rule; None or False both result in no learning rule. If hidden_sizes is a single number it is broadcast to all n_hidden layers. The returned object is a leabra.Network, not a PsyNeuLink Composition; pass it to LeabraMechanism's network argument."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.build_leabra_network
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
    def build_leabra_network(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to construct a leabra.Network for use with PsyNeuLink's LeabraMechanism."
        return _impl(args or {})
