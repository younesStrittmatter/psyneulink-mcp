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
TOOL_DESCRIPTION = 'Call this tool to create a SoftMax transfer function object that normalizes a numeric array into a probability distribution. Use it when you need to assign a softmax activation function to a PsyNeuLink mechanism (e.g., as the `function` argument of a TransferMechanism) or when you need to transform logits into probabilities with configurable output format (full distribution, argmax indicator, probabilistic selection, etc.). Returns a SoftMax Function object — not a mechanism.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "adapt_base": {\n      "description": "Base additive term used by the adaptive gain formula. Only relevant when gain=\'ADAPTIVE\'. Default: 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_entropy_weighting": {\n      "description": "Entropy weighting factor used by the adaptive gain formula. Only relevant when gain=\'ADAPTIVE\'. Default: 0.1.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_scale": {\n      "description": "Scale multiplier used by the adaptive gain formula. Only relevant when gain=\'ADAPTIVE\'. Default: 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template 1D array specifying the shape of the input to be transformed. Optional \\u2014 omit to use the default.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "gain": {\n      "description": "Inverse temperature scaling applied before softmax. A positive scalar sharpens/flattens the distribution; \'ADAPTIVE\' dynamically adjusts gain based on entropy and vector length to keep peak mass consistent across different vector sizes. Default: 1.0.",\n      "oneOf": [\n        {\n          "exclusiveMinimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "mask_threshold": {\n      "description": "If provided, elements whose absolute value (after gain scaling) is below this threshold are set to -inf before softmax, effectively masking them. Only applies when gain is a scalar; ignored when gain is \'ADAPTIVE\'. Default: None (no masking).",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "output": {\n      "description": "Format of the returned array. ALL: full softmax distribution. ARG_MAX/ARG_MAX_INDICATOR: 1 at the highest-value element, 0 elsewhere (lowest index wins ties). MAX_VAL: softmax value at the max element(s), 0 elsewhere. MAX_INDICATOR: 1 at all max elements, 0 elsewhere. PROB: probabilistically sampled one-hot based on the softmax distribution. Default: \'ALL\'.",\n      "enum": [\n        "ALL",\n        "ARG_MAX",\n        "ARG_MAX_INDICATOR",\n        "MAX_VAL",\n        "MAX_INDICATOR",\n        "PROB"\n      ],\n      "type": "string"\n    },\n    "per_item": {\n      "description": "For 2D input variables, if true applies softmax independently to each row; if false applies softmax to the entire 2D array. Default: true.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL (from confirmed runtime failures): `SoftMax.__init__()` does NOT accept a `name` argument — passing it raises TypeError. Do not include `name` in the kwargs under any circumstances.\n\n- If the input variable is all zeros, the SoftMax returns all zeros (no error).\n- `mask_threshold` is silently ignored when `gain=\'ADAPTIVE\'`; similarly, `adapt_scale`, `adapt_base`, and `adapt_entropy_weighting` have no effect unless `gain=\'ADAPTIVE\'`.\n- Sparse/one-hot inputs in longer vectors: the softmax peak mass diminishes with vector length (e.g., [1,0] → 0.73 vs [1,0,0,0] → 0.48). Use `mask_threshold` (scalar gain) or `gain=\'ADAPTIVE\'` to compensate.\n- `output=\'PROB\'` raises an exception when calling `.derivative()`, since the chosen element is ambiguous.\n- The LLVM execution path only supports `ARG_MAX`, `ARG_MAX_INDICATOR`, `MAX_VAL`, `MAX_INDICATOR` for derivatives; `ALL` is supported for forward pass.\n- `mask_threshold` requires that gain is a positive scalar; a warning (not error) is issued if the input contains negative values when masking is active.'
TOOL_PARAMETERS = { 'properties': { 'adapt_base': { 'description': 'Base additive term used by the '
                                                 'adaptive gain formula. Only relevant '
                                                 "when gain='ADAPTIVE'. Default: 1.0.",
                                  'exclusiveMinimum': 0,
                                  'type': 'number'},
                  'adapt_entropy_weighting': { 'description': 'Entropy weighting '
                                                              'factor used by the '
                                                              'adaptive gain formula. '
                                                              'Only relevant when '
                                                              "gain='ADAPTIVE'. "
                                                              'Default: 0.1.',
                                               'exclusiveMinimum': 0,
                                               'type': 'number'},
                  'adapt_scale': { 'description': 'Scale multiplier used by the '
                                                  'adaptive gain formula. Only '
                                                  "relevant when gain='ADAPTIVE'. "
                                                  'Default: 1.0.',
                                   'exclusiveMinimum': 0,
                                   'type': 'number'},
                  'default_variable': { 'description': 'Template 1D array specifying '
                                                       'the shape of the input to be '
                                                       'transformed. Optional — omit '
                                                       'to use the default.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'gain': { 'description': 'Inverse temperature scaling applied before '
                                           'softmax. A positive scalar '
                                           'sharpens/flattens the distribution; '
                                           "'ADAPTIVE' dynamically adjusts gain based "
                                           'on entropy and vector length to keep peak '
                                           'mass consistent across different vector '
                                           'sizes. Default: 1.0.',
                            'oneOf': [ {'exclusiveMinimum': 0, 'type': 'number'},
                                       {'enum': ['ADAPTIVE'], 'type': 'string'}]},
                  'mask_threshold': { 'description': 'If provided, elements whose '
                                                     'absolute value (after gain '
                                                     'scaling) is below this threshold '
                                                     'are set to -inf before softmax, '
                                                     'effectively masking them. Only '
                                                     'applies when gain is a scalar; '
                                                     "ignored when gain is 'ADAPTIVE'. "
                                                     'Default: None (no masking).',
                                      'exclusiveMinimum': 0,
                                      'type': 'number'},
                  'output': { 'description': 'Format of the returned array. ALL: full '
                                             'softmax distribution. '
                                             'ARG_MAX/ARG_MAX_INDICATOR: 1 at the '
                                             'highest-value element, 0 elsewhere '
                                             '(lowest index wins ties). MAX_VAL: '
                                             'softmax value at the max element(s), 0 '
                                             'elsewhere. MAX_INDICATOR: 1 at all max '
                                             'elements, 0 elsewhere. PROB: '
                                             'probabilistically sampled one-hot based '
                                             'on the softmax distribution. Default: '
                                             "'ALL'.",
                              'enum': [ 'ALL',
                                        'ARG_MAX',
                                        'ARG_MAX_INDICATOR',
                                        'MAX_VAL',
                                        'MAX_INDICATOR',
                                        'PROB'],
                              'type': 'string'},
                  'per_item': { 'description': 'For 2D input variables, if true '
                                               'applies softmax independently to each '
                                               'row; if false applies softmax to the '
                                               'entire 2D array. Default: true.',
                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL (from confirmed runtime failures): `SoftMax.__init__()` does NOT accept a `name` argument — passing it raises TypeError. Do not include `name` in the kwargs under any circumstances.\n\n- If the input variable is all zeros, the SoftMax returns all zeros (no error).\n- `mask_threshold` is silently ignored when `gain='ADAPTIVE'`; similarly, `adapt_scale`, `adapt_base`, and `adapt_entropy_weighting` have no effect unless `gain='ADAPTIVE'`.\n- Sparse/one-hot inputs in longer vectors: the softmax peak mass diminishes with vector length (e.g., [1,0] → 0.73 vs [1,0,0,0] → 0.48). Use `mask_threshold` (scalar gain) or `gain='ADAPTIVE'` to compensate.\n- `output='PROB'` raises an exception when calling `.derivative()`, since the chosen element is ambiguous.\n- The LLVM execution path only supports `ARG_MAX`, `ARG_MAX_INDICATOR`, `MAX_VAL`, `MAX_INDICATOR` for derivatives; `ALL` is supported for forward pass.\n- `mask_threshold` requires that gain is a positive scalar; a warning (not error) is issued if the input contains negative values when masking is active."


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
        'Call this tool to create a SoftMax transfer function object that normalizes a numeric array into a probability distribution.'
        return _impl(args or {})
