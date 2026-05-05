"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd248a1114a68af35b39a20ba03a03f80fcdbbf300f31b460376b3a074d74945f'
__pnl_qualname__ = 'psyneulink.LeabraFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_leabra_function'
TOOL_DESCRIPTION = 'Call this tool to instantiate a LeabraFunction that wraps a leabra neural network as a PsyNeuLink Function, typically as the function argument of a LeabraMechanism. Use it when you need a biologically-plausible Leabra-style network integrated into a PsyNeuLink composition; the result is a Function object that runs or trains the leabra network on each call.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the network input as a 2D array: [[input_values], [target_values]]. If omitted, defaults to [zeros(input_size), zeros(output_size)] inferred from the network layers.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "network": {\n      "description": "A leabra.Network instance specifying the Leabra network to use. Required \\u2014 construction fails with LeabraError if omitted. The first layer\'s unit count determines input size; the last layer\'s unit count determines output size.",\n      "type": "object"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter names, values override defaults.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "network"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `network` is mandatory; passing None raises LeabraError immediately at construction time.\n- Input dimensionality is enforced against the network\'s first and last layer unit counts — mismatched arrays raise LeabraError at call time.\n- In inference mode (training_flag=False on the owner), only variable[0] (input) is used; the target vector is ignored.\n- In training mode (training_flag=True), variable must be a length-2 array: [input_pattern, target_pattern], each matching the corresponding layer size.\n- During INITIALIZING executions the function returns zeros without touching leabra network state (HACK to avoid contaminating initial state).\n- `owner` and `prefs` are wired automatically by PsyNeuLink when this Function is passed to a LeabraMechanism; do not set them manually.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the network input '
                                                       'as a 2D array: '
                                                       '[[input_values], '
                                                       '[target_values]]. If omitted, '
                                                       'defaults to '
                                                       '[zeros(input_size), '
                                                       'zeros(output_size)] inferred '
                                                       'from the network layers.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'network': { 'description': 'A leabra.Network instance specifying '
                                              'the Leabra network to use. Required — '
                                              'construction fails with LeabraError if '
                                              "omitted. The first layer's unit count "
                                              "determines input size; the last layer's "
                                              'unit count determines output size.',
                               'type': 'object'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter names, values override '
                                             'defaults.',
                              'type': 'object'}},
  'required': ['network'],
  'type': 'object'}
TOOL_NOTES = "- `network` is mandatory; passing None raises LeabraError immediately at construction time.\n- Input dimensionality is enforced against the network's first and last layer unit counts — mismatched arrays raise LeabraError at call time.\n- In inference mode (training_flag=False on the owner), only variable[0] (input) is used; the target vector is ignored.\n- In training mode (training_flag=True), variable must be a length-2 array: [input_pattern, target_pattern], each matching the corresponding layer size.\n- During INITIALIZING executions the function returns zeros without touching leabra network state (HACK to avoid contaminating initial state).\n- `owner` and `prefs` are wired automatically by PsyNeuLink when this Function is passed to a LeabraMechanism; do not set them manually."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LeabraFunction
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
    def create_leabra_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a LeabraFunction that wraps a leabra neural network as a PsyNeuLink Function, typically as the function argument of a LeabraMechanism.'
        return _impl(args or {})
