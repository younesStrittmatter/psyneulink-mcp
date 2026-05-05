"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '00a69c79e36bb99c48655b21ef72263455199927243218f92062448914a5f27b'
__pnl_qualname__ = 'psyneulink.sinusoid'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'sinusoid'
TOOL_DESCRIPTION = 'Call this tool to evaluate a sinusoidal function at one or more input values. Returns amplitude * sin(2π * frequency * x + phase) — a scalar or NumPy array matching the shape of x. Use it when constructing periodic input signals, transfer functions, or oscillatory stimuli for PsyNeuLink mechanisms.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "amplitude": {\n      "default": 1,\n      "description": "Peak value of the sinusoid. Scales the output linearly.",\n      "type": "number"\n    },\n    "frequency": {\n      "default": 1,\n      "description": "Number of full cycles per unit of x (i.e., cycles per second if x is in seconds).",\n      "type": "number"\n    },\n    "phase": {\n      "default": 0,\n      "description": "Phase offset in radians added inside the sin() call.",\n      "type": "number"\n    },\n    "x": {\n      "description": "Input value(s) at which to evaluate the sinusoid. Can be a scalar number or a list of numbers (treated as a NumPy array).",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nPhase is in radians, not degrees. Frequency is in cycles per unit of x — it multiplies x inside 2π*frequency*x, so a frequency of 1 gives one full cycle over x ∈ [0, 1]. Passing a list for x returns a NumPy array; passing a scalar returns a scalar (or 0-d array depending on NumPy version).'
TOOL_PARAMETERS = { 'properties': { 'amplitude': { 'default': 1,
                                 'description': 'Peak value of the sinusoid. Scales '
                                                'the output linearly.',
                                 'type': 'number'},
                  'frequency': { 'default': 1,
                                 'description': 'Number of full cycles per unit of x '
                                                '(i.e., cycles per second if x is in '
                                                'seconds).',
                                 'type': 'number'},
                  'phase': { 'default': 0,
                             'description': 'Phase offset in radians added inside the '
                                            'sin() call.',
                             'type': 'number'},
                  'x': { 'description': 'Input value(s) at which to evaluate the '
                                        'sinusoid. Can be a scalar number or a list of '
                                        'numbers (treated as a NumPy array).',
                         'oneOf': [ {'type': 'number'},
                                    {'items': {'type': 'number'}, 'type': 'array'}]}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = 'Phase is in radians, not degrees. Frequency is in cycles per unit of x — it multiplies x inside 2π*frequency*x, so a frequency of 1 gives one full cycle over x ∈ [0, 1]. Passing a list for x returns a NumPy array; passing a scalar returns a scalar (or 0-d array depending on NumPy version).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.sinusoid
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
    def sinusoid(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to evaluate a sinusoidal function at one or more input values.'
        return _impl(args or {})
