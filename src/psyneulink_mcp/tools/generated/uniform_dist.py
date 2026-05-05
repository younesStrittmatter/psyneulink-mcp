"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e1cf12655d9ead692e467004e85f7724545ff3691a5032fb2068628c05e737e2'
__pnl_qualname__ = 'psyneulink.UniformDist'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_uniform_dist'
TOOL_DESCRIPTION = 'Use this tool to create a UniformDist function that samples from a uniform distribution over [low, high). Attach it to a TransferMechanism or other Component as its function parameter when you need uniformly-distributed random noise or stochastic input. Returns a single float scalar drawn via numpy.random.uniform.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "high": {\n      "default": 1,\n      "description": "Upper bound (exclusive) of the uniform distribution. Defaults to 1.0.",\n      "type": "number"\n    },\n    "low": {\n      "default": 0,\n      "description": "Lower bound (inclusive) of the uniform distribution. Defaults to 0.0.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the function instance.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are PsyNeuLink parameter keywords.",\n      "type": "object"\n    },\n    "seed": {\n      "description": "Integer seed for the internal numpy RandomState, enabling reproducible sampling. Omit for non-deterministic behavior.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe interval is half-open: [low, high). Ensure low < high or numpy.random.uniform will raise. The function returns a scalar float, not an array — if the owner Component expects a vector output, wrap accordingly. random_state is managed internally and not directly settable; use `seed` for reproducibility. Both `low` and `high` are modulable parameters, meaning they can be modified at runtime via ParameterPorts if needed.'
TOOL_PARAMETERS = { 'properties': { 'high': { 'default': 1,
                            'description': 'Upper bound (exclusive) of the uniform '
                                           'distribution. Defaults to 1.0.',
                            'type': 'number'},
                  'low': { 'default': 0,
                           'description': 'Lower bound (inclusive) of the uniform '
                                          'distribution. Defaults to 0.0.',
                           'type': 'number'},
                  'name': { 'description': 'Optional name for the function instance.',
                            'type': 'string'},
                  'params': { 'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'PsyNeuLink parameter keywords.',
                              'type': 'object'},
                  'seed': { 'description': 'Integer seed for the internal numpy '
                                           'RandomState, enabling reproducible '
                                           'sampling. Omit for non-deterministic '
                                           'behavior.',
                            'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The interval is half-open: [low, high). Ensure low < high or numpy.random.uniform will raise. The function returns a scalar float, not an array — if the owner Component expects a vector output, wrap accordingly. random_state is managed internally and not directly settable; use `seed` for reproducibility. Both `low` and `high` are modulable parameters, meaning they can be modified at runtime via ParameterPorts if needed.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.UniformDist
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
    def create_uniform_dist(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a UniformDist function that samples from a uniform distribution over [low, high).'
        return _impl(args or {})
