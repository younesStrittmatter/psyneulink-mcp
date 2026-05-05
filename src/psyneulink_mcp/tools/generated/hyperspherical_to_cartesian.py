"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '29d64cd25f1a48ca5c4d53255841abd8446ec87742c1b56f11e8a3fd4322d54f'
__pnl_qualname__ = 'psyneulink.HypersphericalToCartesian'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_hyperspherical_to_cartesian'
TOOL_DESCRIPTION = 'Call this tool to convert an n-element array of angular coordinates (in radians) into an (n+1)-dimensional Cartesian point on the unit n-sphere using the standard prefix-sine hyperspherical parameterization. Use it when a model needs to encode directional or orientation data as a unit vector, or when converting from hyperspherical to Cartesian representations. The result is always a unit-length vector of length len(input) + 1.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "A 1D array of n angular values (in radians) to transform. The output will be an (n+1)-element Cartesian unit vector. Must have at least 1 element.",\n      "items": {\n        "type": "number"\n      },\n      "minItems": 1,\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for this function instance. Defaults to a registry-assigned name.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nOutput length is always len(default_variable) + 1 — the dimensionality increases by one. Output is guaranteed to be a unit-length vector regardless of input angle values. Angles are in radians; no degree conversion is performed. The `default_variable` argument acts as a shape template at construction time; the actual transformation input is supplied when the function is called by PsyNeuLink\'s execution machinery. Passing `params`, `owner`, and `prefs` is rarely needed unless wiring the function into a larger Component graph.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'A 1D array of n angular values '
                                                       '(in radians) to transform. The '
                                                       'output will be an '
                                                       '(n+1)-element Cartesian unit '
                                                       'vector. Must have at least 1 '
                                                       'element.',
                                        'items': {'type': 'number'},
                                        'minItems': 1,
                                        'type': 'array'},
                  'name': { 'description': 'Optional name for this function instance. '
                                           'Defaults to a registry-assigned name.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Output length is always len(default_variable) + 1 — the dimensionality increases by one. Output is guaranteed to be a unit-length vector regardless of input angle values. Angles are in radians; no degree conversion is performed. The `default_variable` argument acts as a shape template at construction time; the actual transformation input is supplied when the function is called by PsyNeuLink's execution machinery. Passing `params`, `owner`, and `prefs` is rarely needed unless wiring the function into a larger Component graph."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.HypersphericalToCartesian
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
    def create_hyperspherical_to_cartesian(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to convert an n-element array of angular coordinates (in radians) into an (n+1)-dimensional Cartesian point on the unit n-sphere using the standard prefix-sine hyperspherical parameterization.'
        return _impl(args or {})
