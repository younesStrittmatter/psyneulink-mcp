"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e9132097be5200e1bdb840ad8c5604fbc1b593598414809da7820424be0fddf4'
__pnl_qualname__ = 'psyneulink.Tanh'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_tanh'
TOOL_DESCRIPTION = 'Use this tool to create a PsyNeuLink Tanh (hyperbolic tangent) transfer function, typically assigned as the `function` parameter of a TransferMechanism or other component that needs a smooth, bounded (-1 to 1) nonlinearity. Returns a configured Tanh function object; the output range shifts to (-scale+offset, scale+offset) when scale/offset are set.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "default": 0,\n      "description": "Value added to each input element before gain and tanh are applied. Equivalent to x_0 with the opposite sign; prefer one or the other, not both.",\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template for the input value(s); sets the expected shape. Accepts a number or list of numbers.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "gain": {\n      "default": 1,\n      "description": "Multiplier applied to (variable + bias - x_0) before the tanh transform. Higher gain steepens the sigmoid curve.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the function instance; auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Value added to the scaled tanh output. Shifts the entire output range.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Scalar multiplier applied to the tanh output before offset is added. Expands the output range to (-scale, scale).",\n      "type": "number"\n    },\n    "x_0": {\n      "default": 0,\n      "description": "Value subtracted from each input element before gain and tanh are applied. Equivalent to bias with the opposite sign.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nbias and x_0 are redundant — both shift the input breakpoint but with opposite signs (bias adds, x_0 subtracts). Using both simultaneously compounds their effects; pick one. Default output range is (-1, 1); applying scale and/or offset changes it to (-scale+offset, scale+offset). params dict can override any parameter at construction time and takes precedence over constructor arguments.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'default': 0,
                            'description': 'Value added to each input element before '
                                           'gain and tanh are applied. Equivalent to '
                                           'x_0 with the opposite sign; prefer one or '
                                           'the other, not both.',
                            'type': 'number'},
                  'default_variable': { 'description': 'Template for the input '
                                                       'value(s); sets the expected '
                                                       'shape. Accepts a number or '
                                                       'list of numbers.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'gain': { 'default': 1,
                            'description': 'Multiplier applied to (variable + bias - '
                                           'x_0) before the tanh transform. Higher '
                                           'gain steepens the sigmoid curve.',
                            'type': 'number'},
                  'name': { 'description': 'Optional name for the function instance; '
                                           'auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Value added to the scaled tanh output. '
                                             'Shifts the entire output range.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Scalar multiplier applied to the tanh '
                                            'output before offset is added. Expands '
                                            'the output range to (-scale, scale).',
                             'type': 'number'},
                  'x_0': { 'default': 0,
                           'description': 'Value subtracted from each input element '
                                          'before gain and tanh are applied. '
                                          'Equivalent to bias with the opposite sign.',
                           'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'bias and x_0 are redundant — both shift the input breakpoint but with opposite signs (bias adds, x_0 subtracts). Using both simultaneously compounds their effects; pick one. Default output range is (-1, 1); applying scale and/or offset changes it to (-scale+offset, scale+offset). params dict can override any parameter at construction time and takes precedence over constructor arguments.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Tanh
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
    def create_tanh(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a PsyNeuLink Tanh (hyperbolic tangent) transfer function, typically assigned as the `function` parameter of a TransferMechanism or other component that needs a smooth, bounded (-1 to 1) nonlinearity.'
        return _impl(args or {})
