"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7081f1eeb1933720e671dd08ceb3cec5cad8b6c6d65c93db3bceb89a4a51959a'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.processing.processingmechanism.SoftMax'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_soft_max'
TOOL_DESCRIPTION = 'Call this tool to create a PsyNeuLink SoftMax Function object that applies a softmax (normalized exponential) transformation to a 1D array. Use it when you need a transfer function for a mechanism (e.g., as the `function` argument of a TransferMechanism) or wherever a softmax-style normalization is needed. The result is a SoftMax instance whose output format is controlled by the `output` parameter (full distribution, argmax indicator, max value, or probabilistic selection).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "adapt_base": {\n      "description": "Base offset used by the adaptive gain calculation when gain=\'ADAPTIVE\'. Default 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_entropy_weighting": {\n      "description": "Entropy weighting factor used by the adaptive gain calculation when gain=\'ADAPTIVE\'. Default 0.1.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_scale": {\n      "description": "Scale factor used by the adaptive gain calculation when gain=\'ADAPTIVE\'. Default 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template 1D array specifying the shape of input to be transformed.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "gain": {\n      "description": "Inverse temperature (sharpness) of the softmax. Must be a positive number or the string \'ADAPTIVE\'. With \'ADAPTIVE\', gain is computed dynamically from the input\'s entropy to keep distribution mass consistent across differently-sized vectors. Defaults to 1.0.",\n      "oneOf": [\n        {\n          "exclusiveMinimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "mask_threshold": {\n      "description": "If set, each element is first scaled by gain, then elements whose absolute value is below this threshold are set to -inf (masked out) before softmax is applied. Only applies when gain is a scalar; ignored when gain is \'ADAPTIVE\'.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "output": {\n      "description": "Format of the returned array. ALL: full softmax distribution (default). ARG_MAX / ARG_MAX_INDICATOR: 1 at the single highest-valued element, 0 elsewhere. MAX_VAL: softmax value at the maximum element(s), 0 elsewhere. MAX_INDICATOR: 1 at all maximum-valued elements, 0 elsewhere. PROB: probabilistic one-hot selection weighted by softmax values.",\n      "enum": [\n        "ALL",\n        "ARG_MAX",\n        "ARG_MAX_INDICATOR",\n        "MAX_VAL",\n        "MAX_INDICATOR",\n        "PROB"\n      ],\n      "type": "string"\n    },\n    "per_item": {\n      "description": "For 2D input arrays, whether to apply softmax independently to each row (True, default) or across the entire array (False).",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nSoftMax.__init__() does NOT accept a `name` parameter — passing `name` raises TypeError. Do not include it. The `output` parameter takes PsyNeuLink string constants (e.g., \'ALL\', \'ARG_MAX\'); the enum values above are the correct string literals to pass. `mask_threshold` and the `adapt_*` parameters are mutually exclusive in effect: mask_threshold is silently ignored when gain=\'ADAPTIVE\', and adapt_* parameters are only used when gain=\'ADAPTIVE\'. The derivative of SoftMax is undefined when output=\'PROB\'. If variable is all zeros, the function returns all zeros rather than a uniform distribution.'
TOOL_PARAMETERS = { 'properties': { 'adapt_base': { 'description': 'Base offset used by the adaptive '
                                                 'gain calculation when '
                                                 "gain='ADAPTIVE'. Default 1.0.",
                                  'exclusiveMinimum': 0,
                                  'type': 'number'},
                  'adapt_entropy_weighting': { 'description': 'Entropy weighting '
                                                              'factor used by the '
                                                              'adaptive gain '
                                                              'calculation when '
                                                              "gain='ADAPTIVE'. "
                                                              'Default 0.1.',
                                               'exclusiveMinimum': 0,
                                               'type': 'number'},
                  'adapt_scale': { 'description': 'Scale factor used by the adaptive '
                                                  'gain calculation when '
                                                  "gain='ADAPTIVE'. Default 1.0.",
                                   'exclusiveMinimum': 0,
                                   'type': 'number'},
                  'default_variable': { 'description': 'Template 1D array specifying '
                                                       'the shape of input to be '
                                                       'transformed.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'gain': { 'description': 'Inverse temperature (sharpness) of the '
                                           'softmax. Must be a positive number or the '
                                           "string 'ADAPTIVE'. With 'ADAPTIVE', gain "
                                           "is computed dynamically from the input's "
                                           'entropy to keep distribution mass '
                                           'consistent across differently-sized '
                                           'vectors. Defaults to 1.0.',
                            'oneOf': [ {'exclusiveMinimum': 0, 'type': 'number'},
                                       {'enum': ['ADAPTIVE'], 'type': 'string'}]},
                  'mask_threshold': { 'description': 'If set, each element is first '
                                                     'scaled by gain, then elements '
                                                     'whose absolute value is below '
                                                     'this threshold are set to -inf '
                                                     '(masked out) before softmax is '
                                                     'applied. Only applies when gain '
                                                     'is a scalar; ignored when gain '
                                                     "is 'ADAPTIVE'.",
                                      'exclusiveMinimum': 0,
                                      'type': 'number'},
                  'output': { 'description': 'Format of the returned array. ALL: full '
                                             'softmax distribution (default). ARG_MAX '
                                             '/ ARG_MAX_INDICATOR: 1 at the single '
                                             'highest-valued element, 0 elsewhere. '
                                             'MAX_VAL: softmax value at the maximum '
                                             'element(s), 0 elsewhere. MAX_INDICATOR: '
                                             '1 at all maximum-valued elements, 0 '
                                             'elsewhere. PROB: probabilistic one-hot '
                                             'selection weighted by softmax values.',
                              'enum': [ 'ALL',
                                        'ARG_MAX',
                                        'ARG_MAX_INDICATOR',
                                        'MAX_VAL',
                                        'MAX_INDICATOR',
                                        'PROB'],
                              'type': 'string'},
                  'per_item': { 'description': 'For 2D input arrays, whether to apply '
                                               'softmax independently to each row '
                                               '(True, default) or across the entire '
                                               'array (False).',
                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "SoftMax.__init__() does NOT accept a `name` parameter — passing `name` raises TypeError. Do not include it. The `output` parameter takes PsyNeuLink string constants (e.g., 'ALL', 'ARG_MAX'); the enum values above are the correct string literals to pass. `mask_threshold` and the `adapt_*` parameters are mutually exclusive in effect: mask_threshold is silently ignored when gain='ADAPTIVE', and adapt_* parameters are only used when gain='ADAPTIVE'. The derivative of SoftMax is undefined when output='PROB'. If variable is all zeros, the function returns all zeros rather than a uniform distribution."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.SoftMax
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
    def create_soft_max(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a PsyNeuLink SoftMax Function object that applies a softmax (normalized exponential) transformation to a 1D array.'
        return _impl(args or {})
