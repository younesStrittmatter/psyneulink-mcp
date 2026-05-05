"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7081f1eeb1933720e671dd08ceb3cec5cad8b6c6d65c93db3bceb89a4a51959a'
__pnl_qualname__ = 'psyneulink.SoftMax'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_soft_max'
TOOL_DESCRIPTION = 'Call this tool to create a SoftMax transfer function that applies the softmax transformation (e^(gain*x_i) / sum(e^(gain*x))) to a numeric array. Use it when assigning a SoftMax function to a PsyNeuLink mechanism\'s function parameter — for example, to implement a winner-take-all soft selection, probabilistic choice, or temperature-scaled competition over a set of activations. The tool returns a configured SoftMax Function object.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "adapt_base": {\n      "description": "Base offset used in adaptive gain computation. Only relevant when gain=\'ADAPTIVE\'. Default 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_entropy_weighting": {\n      "description": "Weight applied to the entropy term in adaptive gain computation. Only relevant when gain=\'ADAPTIVE\'. Default 0.1.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_scale": {\n      "description": "Scale factor used in adaptive gain computation: gain = adapt_scale * (adapt_base + entropy_weighting * log(entropy)). Only relevant when gain=\'ADAPTIVE\'. Default 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template 1d (or 2d if per_item=true) numeric array specifying the shape of inputs to be transformed.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "gain": {\n      "description": "Inverse temperature scaling applied before softmax. Must be a positive number, or the string \'ADAPTIVE\' to dynamically adjust gain based on variable entropy and length. Defaults to 1.0.",\n      "oneOf": [\n        {\n          "exclusiveMinimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "mask_threshold": {\n      "description": "If set, elements whose absolute value (after gain scaling) is below this threshold are set to -inf before softmax, effectively masking them. Only applies when gain is a scalar; ignored when gain=\'ADAPTIVE\'. Default is None (no masking).",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the SoftMax function instance.",\n      "type": "string"\n    },\n    "output": {\n      "default": "ALL",\n      "description": "Format of the returned array. ALL returns full softmax distribution (default). ARG_MAX/ARG_MAX_INDICATOR returns 1 for the single argmax element, 0 elsewhere. MAX_VAL/MAX_INDICATOR returns the softmax value (or 1) for all maximal elements, 0 elsewhere. PROB returns a probabilistically sampled one-hot based on the softmax distribution.",\n      "enum": [\n        "ALL",\n        "ARG_MAX",\n        "ARG_MAX_INDICATOR",\n        "MAX_VAL",\n        "MAX_INDICATOR",\n        "PROB"\n      ],\n      "type": "string"\n    },\n    "per_item": {\n      "default": true,\n      "description": "For 2d input variables, if true (default) applies softmax independently to each row; if false applies softmax across the entire variable.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- When gain=\'ADAPTIVE\', mask_threshold is silently ignored — do not pass both.\n- The softmax of an all-zeros input returns all zeros (not a uniform distribution).\n- ARG_MAX and ARG_MAX_INDICATOR produce identical output (both return 1 for the single max-index, 0 elsewhere); they differ only in how derivatives are computed.\n- MAX_VAL returns the actual softmax probability for all tied maxima; MAX_INDICATOR returns 1 for all tied maxima.\n- PROB output cannot be used with the derivative method — it raises FunctionError.\n- gain must be strictly greater than 0 when specified as a scalar; passing 0 raises a validation error.\n- mask_threshold is applied to the magnitude (abs) of gain-scaled values, so it interacts with negative inputs in a potentially surprising way: a warning is issued but the masking proceeds on abs values.\n- adapt_entropy_weighting in the source Parameter default is 0.95 (not 0.1 as stated in the docstring); use source default when precision matters.\n- For sparse one-hot style inputs over long vectors, prefer gain=\'ADAPTIVE\' or a tuned mask_threshold to avoid softmax mass dilution across zero-valued entries.'
TOOL_PARAMETERS = { 'properties': { 'adapt_base': { 'description': 'Base offset used in adaptive gain '
                                                 'computation. Only relevant when '
                                                 "gain='ADAPTIVE'. Default 1.0.",
                                  'exclusiveMinimum': 0,
                                  'type': 'number'},
                  'adapt_entropy_weighting': { 'description': 'Weight applied to the '
                                                              'entropy term in '
                                                              'adaptive gain '
                                                              'computation. Only '
                                                              'relevant when '
                                                              "gain='ADAPTIVE'. "
                                                              'Default 0.1.',
                                               'exclusiveMinimum': 0,
                                               'type': 'number'},
                  'adapt_scale': { 'description': 'Scale factor used in adaptive gain '
                                                  'computation: gain = adapt_scale * '
                                                  '(adapt_base + entropy_weighting * '
                                                  'log(entropy)). Only relevant when '
                                                  "gain='ADAPTIVE'. Default 1.0.",
                                   'exclusiveMinimum': 0,
                                   'type': 'number'},
                  'default_variable': { 'description': 'Template 1d (or 2d if '
                                                       'per_item=true) numeric array '
                                                       'specifying the shape of inputs '
                                                       'to be transformed.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'gain': { 'description': 'Inverse temperature scaling applied before '
                                           'softmax. Must be a positive number, or the '
                                           "string 'ADAPTIVE' to dynamically adjust "
                                           'gain based on variable entropy and length. '
                                           'Defaults to 1.0.',
                            'oneOf': [ {'exclusiveMinimum': 0, 'type': 'number'},
                                       {'enum': ['ADAPTIVE'], 'type': 'string'}]},
                  'mask_threshold': { 'description': 'If set, elements whose absolute '
                                                     'value (after gain scaling) is '
                                                     'below this threshold are set to '
                                                     '-inf before softmax, effectively '
                                                     'masking them. Only applies when '
                                                     'gain is a scalar; ignored when '
                                                     "gain='ADAPTIVE'. Default is None "
                                                     '(no masking).',
                                      'exclusiveMinimum': 0,
                                      'type': 'number'},
                  'name': { 'description': 'Optional name for the SoftMax function '
                                           'instance.',
                            'type': 'string'},
                  'output': { 'default': 'ALL',
                              'description': 'Format of the returned array. ALL '
                                             'returns full softmax distribution '
                                             '(default). ARG_MAX/ARG_MAX_INDICATOR '
                                             'returns 1 for the single argmax element, '
                                             '0 elsewhere. MAX_VAL/MAX_INDICATOR '
                                             'returns the softmax value (or 1) for all '
                                             'maximal elements, 0 elsewhere. PROB '
                                             'returns a probabilistically sampled '
                                             'one-hot based on the softmax '
                                             'distribution.',
                              'enum': [ 'ALL',
                                        'ARG_MAX',
                                        'ARG_MAX_INDICATOR',
                                        'MAX_VAL',
                                        'MAX_INDICATOR',
                                        'PROB'],
                              'type': 'string'},
                  'per_item': { 'default': True,
                                'description': 'For 2d input variables, if true '
                                               '(default) applies softmax '
                                               'independently to each row; if false '
                                               'applies softmax across the entire '
                                               'variable.',
                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- When gain='ADAPTIVE', mask_threshold is silently ignored — do not pass both.\n- The softmax of an all-zeros input returns all zeros (not a uniform distribution).\n- ARG_MAX and ARG_MAX_INDICATOR produce identical output (both return 1 for the single max-index, 0 elsewhere); they differ only in how derivatives are computed.\n- MAX_VAL returns the actual softmax probability for all tied maxima; MAX_INDICATOR returns 1 for all tied maxima.\n- PROB output cannot be used with the derivative method — it raises FunctionError.\n- gain must be strictly greater than 0 when specified as a scalar; passing 0 raises a validation error.\n- mask_threshold is applied to the magnitude (abs) of gain-scaled values, so it interacts with negative inputs in a potentially surprising way: a warning is issued but the masking proceeds on abs values.\n- adapt_entropy_weighting in the source Parameter default is 0.95 (not 0.1 as stated in the docstring); use source default when precision matters.\n- For sparse one-hot style inputs over long vectors, prefer gain='ADAPTIVE' or a tuned mask_threshold to avoid softmax mass dilution across zero-valued entries."


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
        'Call this tool to create a SoftMax transfer function that applies the softmax transformation (e^(gain*x_i) / sum(e^(gain*x))) to a numeric array.'
        return _impl(args or {})
