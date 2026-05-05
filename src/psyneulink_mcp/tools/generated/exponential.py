"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '08395694853ab06e078e32d28a78edcc40b988685fc2d9910df00b28ea21b217'
__pnl_qualname__ = 'psyneulink.Exponential'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_exponential'
TOOL_DESCRIPTION = 'Use this tool to create a PsyNeuLink Exponential transfer function that computes `scale * e^(rate*variable + bias) + offset`. Call it when you need to assign an exponential activation function to a Mechanism (e.g., via `function=Exponential(...)`) or when modeling neural populations with exponential gain. Returns an Exponential Function object ready to be passed as the `function` argument of a Mechanism or used standalone.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "default": 0,\n      "description": "Additive offset applied to (rate * variable) before exponentiation. Shifts the curve horizontally. Default: 0.0.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the Function instance. If omitted, FunctionRegistry assigns a default.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Additive constant applied after scaling. Shifts the output vertically. Default: 0.0.",\n      "type": "number"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplier applied to the input variable before exponentiation. Acts as the gain/slope of the exponential. Default: 1.0.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplier applied to the exponential result before adding offset. Scales the output amplitude. Default: 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe `default_variable` constructor argument is only a shape template (not the value to transform) — do not pass it unless you need to constrain input dimensionality. The natural output range is (0, ∞); adding a negative `offset` or negative `scale` can produce negative values, but be aware that PNL records `range = (0, None)` and some downstream components may rely on that constraint. The `rate` parameter doubles as `MULTIPLICATIVE_PARAM` and `bias` as `ADDITIVE_PARAM`, so ModulatorySignals targeting those aliases will work. Do not pass `params` or `owner` — the host template handles component wiring.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'default': 0,
                            'description': 'Additive offset applied to (rate * '
                                           'variable) before exponentiation. Shifts '
                                           'the curve horizontally. Default: 0.0.',
                            'type': 'number'},
                  'name': { 'description': 'Optional name for the Function instance. '
                                           'If omitted, FunctionRegistry assigns a '
                                           'default.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Additive constant applied after scaling. '
                                             'Shifts the output vertically. Default: '
                                             '0.0.',
                              'type': 'number'},
                  'rate': { 'default': 1,
                            'description': 'Multiplier applied to the input variable '
                                           'before exponentiation. Acts as the '
                                           'gain/slope of the exponential. Default: '
                                           '1.0.',
                            'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplier applied to the exponential '
                                            'result before adding offset. Scales the '
                                            'output amplitude. Default: 1.0.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The `default_variable` constructor argument is only a shape template (not the value to transform) — do not pass it unless you need to constrain input dimensionality. The natural output range is (0, ∞); adding a negative `offset` or negative `scale` can produce negative values, but be aware that PNL records `range = (0, None)` and some downstream components may rely on that constraint. The `rate` parameter doubles as `MULTIPLICATIVE_PARAM` and `bias` as `ADDITIVE_PARAM`, so ModulatorySignals targeting those aliases will work. Do not pass `params` or `owner` — the host template handles component wiring.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Exponential
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
    def create_exponential(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a PsyNeuLink Exponential transfer function that computes `scale * e^(rate*variable + bias) + offset`.'
        return _impl(args or {})
