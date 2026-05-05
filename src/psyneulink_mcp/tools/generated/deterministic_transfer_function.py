"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '1daf99136f1f0514df0e5a49c0ff7df2543035627b4c8652b2972001c6b3dc2d'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.transferfunctions.DeterministicTransferFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_deterministic_transfer_function'
TOOL_DESCRIPTION = 'Use this tool when you need to instantiate a DeterministicTransferFunction — the abstract base class for PsyNeuLink transfer functions that apply a deterministic mapping with optional scaling and offset. Call it to configure shared scale/offset behavior before passing the result as a `function` argument to a Mechanism. The result is a configured function object whose output range is derived as `default_range * scale + offset`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "offset": {\n      "default": 0,\n      "description": "Additive constant applied to the function\'s output after scale has been applied. Modulable (can be modified by a ModulatorySignal). Default is 0.0.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplicative scaling factor applied to the function\'s output before offset is added. Modulable (can be modified by a ModulatorySignal). Default is 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDeterministicTransferFunction is an abstract base class — it cannot be instantiated directly and will raise an error if you try. Use a concrete subclass instead (e.g., Linear, Logistic, ReLU, Tanh, SoftMax). The `range` parameter is read-only and computed automatically from `default_range * scale + offset`; do not attempt to set it. Both `scale` and `offset` are modulable, meaning they can be controlled by a ModulatorySignal at runtime.'
TOOL_PARAMETERS = { 'properties': { 'offset': { 'default': 0,
                              'description': 'Additive constant applied to the '
                                             "function's output after scale has been "
                                             'applied. Modulable (can be modified by a '
                                             'ModulatorySignal). Default is 0.0.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplicative scaling factor applied to '
                                            "the function's output before offset is "
                                            'added. Modulable (can be modified by a '
                                            'ModulatorySignal). Default is 1.0.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'DeterministicTransferFunction is an abstract base class — it cannot be instantiated directly and will raise an error if you try. Use a concrete subclass instead (e.g., Linear, Logistic, ReLU, Tanh, SoftMax). The `range` parameter is read-only and computed automatically from `default_range * scale + offset`; do not attempt to set it. Both `scale` and `offset` are modulable, meaning they can be controlled by a ModulatorySignal at runtime.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DeterministicTransferFunction
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
    def create_deterministic_transfer_function(args: dict[str, Any] | None = None) -> Any:
        'Use this tool when you need to instantiate a DeterministicTransferFunction — the abstract base class for PsyNeuLink transfer functions that apply a deterministic mapping with optional scaling and offset.'
        return _impl(args or {})
