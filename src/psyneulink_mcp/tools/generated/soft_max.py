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
TOOL_DESCRIPTION = 'Call this tool to create a PsyNeuLink `SoftMax` Function instance that applies the softmax transformation to a numeric array. Use it when you need a softmax activation function for a Mechanism\'s `function` parameter — the result is a configured `SoftMax` object ready to be passed as `function=` to a TransferMechanism or similar. Supports scalar gain (sharpness/temperature), adaptive gain for sparse vectors, pre-softmax thresholding, and multiple output formats (full distribution, argmax indicator, probabilistic sampling).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "adapt_base": {\n      "default": 1,\n      "description": "Base offset used by the adaptive gain computation (only relevant when gain=\'ADAPTIVE\'). Must be positive. Defaults to 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_entropy_weighting": {\n      "default": 0.95,\n      "description": "Entropy weighting factor used by the adaptive gain computation (only relevant when gain=\'ADAPTIVE\'). Must be positive. Defaults to 0.95.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_scale": {\n      "default": 1,\n      "description": "Scale factor used by the adaptive gain computation (only relevant when gain=\'ADAPTIVE\'). Must be positive. Defaults to 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template array defining the shape of the input the function expects. Provide a 1d array of numbers to fix the input dimensionality. Optional \\u2014 omit to accept any 1d input.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "gain": {\n      "default": 1,\n      "description": "Inverse temperature scaling applied before the softmax. Must be a positive number, or the string \'ADAPTIVE\' to dynamically adjust gain based on the entropy of the input (useful for sparse/one-hot vectors). Defaults to 1.0.",\n      "oneOf": [\n        {\n          "exclusiveMinimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "mask_threshold": {\n      "default": null,\n      "description": "If provided, elements of the scaled input whose absolute value is below this threshold are set to -inf before softmax (effectively masked out). Must be a positive scalar. Only applies when gain is a scalar \\u2014 ignored when gain is \'ADAPTIVE\'. Defaults to null (no thresholding).",\n      "oneOf": [\n        {\n          "exclusiveMinimum": 0,\n          "type": "number"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "output": {\n      "default": "ALL",\n      "description": "Format of the returned array. \'ALL\' returns the full softmax distribution. \'ARG_MAX\'/\'ARG_MAX_INDICATOR\' return 1 at the single highest-value element, 0 elsewhere. \'MAX_VAL\' returns the softmax value at the max position(s), 0 elsewhere. \'MAX_INDICATOR\' returns 1 at all max-value positions. \'PROB\' stochastically selects one element proportional to softmax probabilities.",\n      "enum": [\n        "ALL",\n        "ARG_MAX",\n        "ARG_MAX_INDICATOR",\n        "MAX_VAL",\n        "MAX_INDICATOR",\n        "PROB"\n      ],\n      "type": "string"\n    },\n    "per_item": {\n      "default": true,\n      "description": "For 2d input arrays, whether to apply softmax independently to each row (true) or across the entire 2d array as a flat vector (false). Defaults to true.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL: `name` is NOT a valid constructor argument for SoftMax despite appearing in the docstring. Passing `name` causes `TypeError: SoftMax.__init__() got an unexpected keyword argument \'name\'` — do not include it.\n\nThe `adapt_entropy_weighting` default in the source code is 0.95, not 0.1 as stated in the docstring — use 0.95.\n\nWhen `gain=\'ADAPTIVE\'`, `mask_threshold` is silently ignored regardless of its value.\n\nWhen `output` is anything other than `\'ALL\'`, the derivative method will raise an error for `\'PROB\'` — avoid calling derivative on a PROB-output SoftMax.\n\nIf the input variable is all zeros, SoftMax returns all zeros (not a uniform distribution).\n\nFor sparse/one-hot inputs, the max value after softmax shrinks as vector length grows (e.g., [1,0] → 0.73 but [1,0,0,0] → 0.48 at the max). Use `gain=\'ADAPTIVE\'` or `mask_threshold` to compensate.'
TOOL_PARAMETERS = { 'properties': { 'adapt_base': { 'default': 1,
                                  'description': 'Base offset used by the adaptive '
                                                 'gain computation (only relevant when '
                                                 "gain='ADAPTIVE'). Must be positive. "
                                                 'Defaults to 1.0.',
                                  'exclusiveMinimum': 0,
                                  'type': 'number'},
                  'adapt_entropy_weighting': { 'default': 0.95,
                                               'description': 'Entropy weighting '
                                                              'factor used by the '
                                                              'adaptive gain '
                                                              'computation (only '
                                                              'relevant when '
                                                              "gain='ADAPTIVE'). Must "
                                                              'be positive. Defaults '
                                                              'to 0.95.',
                                               'exclusiveMinimum': 0,
                                               'type': 'number'},
                  'adapt_scale': { 'default': 1,
                                   'description': 'Scale factor used by the adaptive '
                                                  'gain computation (only relevant '
                                                  "when gain='ADAPTIVE'). Must be "
                                                  'positive. Defaults to 1.0.',
                                   'exclusiveMinimum': 0,
                                   'type': 'number'},
                  'default_variable': { 'description': 'Template array defining the '
                                                       'shape of the input the '
                                                       'function expects. Provide a 1d '
                                                       'array of numbers to fix the '
                                                       'input dimensionality. Optional '
                                                       '— omit to accept any 1d input.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'gain': { 'default': 1,
                            'description': 'Inverse temperature scaling applied before '
                                           'the softmax. Must be a positive number, or '
                                           "the string 'ADAPTIVE' to dynamically "
                                           'adjust gain based on the entropy of the '
                                           'input (useful for sparse/one-hot vectors). '
                                           'Defaults to 1.0.',
                            'oneOf': [ {'exclusiveMinimum': 0, 'type': 'number'},
                                       {'enum': ['ADAPTIVE'], 'type': 'string'}]},
                  'mask_threshold': { 'default': None,
                                      'description': 'If provided, elements of the '
                                                     'scaled input whose absolute '
                                                     'value is below this threshold '
                                                     'are set to -inf before softmax '
                                                     '(effectively masked out). Must '
                                                     'be a positive scalar. Only '
                                                     'applies when gain is a scalar — '
                                                     "ignored when gain is 'ADAPTIVE'. "
                                                     'Defaults to null (no '
                                                     'thresholding).',
                                      'oneOf': [ { 'exclusiveMinimum': 0,
                                                   'type': 'number'},
                                                 {'type': 'null'}]},
                  'output': { 'default': 'ALL',
                              'description': "Format of the returned array. 'ALL' "
                                             'returns the full softmax distribution. '
                                             "'ARG_MAX'/'ARG_MAX_INDICATOR' return 1 "
                                             'at the single highest-value element, 0 '
                                             "elsewhere. 'MAX_VAL' returns the softmax "
                                             'value at the max position(s), 0 '
                                             "elsewhere. 'MAX_INDICATOR' returns 1 at "
                                             "all max-value positions. 'PROB' "
                                             'stochastically selects one element '
                                             'proportional to softmax probabilities.',
                              'enum': [ 'ALL',
                                        'ARG_MAX',
                                        'ARG_MAX_INDICATOR',
                                        'MAX_VAL',
                                        'MAX_INDICATOR',
                                        'PROB'],
                              'type': 'string'},
                  'per_item': { 'default': True,
                                'description': 'For 2d input arrays, whether to apply '
                                               'softmax independently to each row '
                                               '(true) or across the entire 2d array '
                                               'as a flat vector (false). Defaults to '
                                               'true.',
                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL: `name` is NOT a valid constructor argument for SoftMax despite appearing in the docstring. Passing `name` causes `TypeError: SoftMax.__init__() got an unexpected keyword argument 'name'` — do not include it.\n\nThe `adapt_entropy_weighting` default in the source code is 0.95, not 0.1 as stated in the docstring — use 0.95.\n\nWhen `gain='ADAPTIVE'`, `mask_threshold` is silently ignored regardless of its value.\n\nWhen `output` is anything other than `'ALL'`, the derivative method will raise an error for `'PROB'` — avoid calling derivative on a PROB-output SoftMax.\n\nIf the input variable is all zeros, SoftMax returns all zeros (not a uniform distribution).\n\nFor sparse/one-hot inputs, the max value after softmax shrinks as vector length grows (e.g., [1,0] → 0.73 but [1,0,0,0] → 0.48 at the max). Use `gain='ADAPTIVE'` or `mask_threshold` to compensate."


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
        'Call this tool to create a PsyNeuLink `SoftMax` Function instance that applies the softmax transformation to a numeric array.'
        return _impl(args or {})
