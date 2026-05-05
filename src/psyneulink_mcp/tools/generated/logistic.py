"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'de17cf9ecd25c17be6774214f9d9eb24ae9a159e939dee1e5ce23aeee1b6d149'
__pnl_qualname__ = 'psyneulink.Logistic'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_logistic'
TOOL_DESCRIPTION = 'Call this tool to create a Logistic (sigmoid) transfer function for use as a TransferMechanism\'s function or standalone transformation. Returns a PsyNeuLink Logistic object that applies scale * 1/(1 + e^(-gain*(variable + bias - x_0))) + offset element-wise. Use when you need a bounded (0,1) activation function, optionally shifted or scaled.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "default": 0,\n      "description": "Added to each element of variable before gain is applied. Shifts the sigmoid horizontally; equivalent to -x_0 (ML convention).",\n      "type": "number"\n    },\n    "gain": {\n      "default": 1,\n      "description": "Multiplies (variable + bias - x_0) before the exponential; controls steepness of the sigmoid. Corresponds to k in the standard logistic form.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for this Function instance; auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Added to the scaled sigmoid output; translates the result vertically. Not modulated by gain.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplies the sigmoid output before offset is added; stretches the output range from (0,1) to (0,scale). Corresponds to L in the standard logistic form.",\n      "type": "number"\n    },\n    "x_0": {\n      "default": 0,\n      "description": "Subtracted from each element of variable before gain is applied. Shifts the sigmoid horizontally; equivalent to -bias (standard logistic convention).",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nbias and x_0 have identical effects except opposite signs: bias shifts the curve right (ML convention), x_0 shifts it left (standard math convention). Do not set both unless you intend their combined effect (net shift = bias - x_0). The default output range is (0, 1); scale stretches it to (0, scale) and offset then shifts it, so the effective range becomes (offset, scale + offset). The derivative method uses the output value, not the input — pass output= when calling it directly for backprop efficiency.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'default': 0,
                            'description': 'Added to each element of variable before '
                                           'gain is applied. Shifts the sigmoid '
                                           'horizontally; equivalent to -x_0 (ML '
                                           'convention).',
                            'type': 'number'},
                  'gain': { 'default': 1,
                            'description': 'Multiplies (variable + bias - x_0) before '
                                           'the exponential; controls steepness of the '
                                           'sigmoid. Corresponds to k in the standard '
                                           'logistic form.',
                            'type': 'number'},
                  'name': { 'description': 'Optional name for this Function instance; '
                                           'auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Added to the scaled sigmoid output; '
                                             'translates the result vertically. Not '
                                             'modulated by gain.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplies the sigmoid output before '
                                            'offset is added; stretches the output '
                                            'range from (0,1) to (0,scale). '
                                            'Corresponds to L in the standard logistic '
                                            'form.',
                             'type': 'number'},
                  'x_0': { 'default': 0,
                           'description': 'Subtracted from each element of variable '
                                          'before gain is applied. Shifts the sigmoid '
                                          'horizontally; equivalent to -bias (standard '
                                          'logistic convention).',
                           'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'bias and x_0 have identical effects except opposite signs: bias shifts the curve right (ML convention), x_0 shifts it left (standard math convention). Do not set both unless you intend their combined effect (net shift = bias - x_0). The default output range is (0, 1); scale stretches it to (0, scale) and offset then shifts it, so the effective range becomes (offset, scale + offset). The derivative method uses the output value, not the input — pass output= when calling it directly for backprop efficiency.'


def _impl(**kwargs: Any) -> Any:
    target = pnl.Logistic
    instance = target(**kwargs)
    return repr(instance)


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_logistic(**kwargs: Any) -> Any:
        "Call this tool to create a Logistic (sigmoid) transfer function for use as a TransferMechanism's function or standalone transformation."
        return _impl(**kwargs)
