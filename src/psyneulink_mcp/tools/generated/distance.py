"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '782598fd62b19cbfe0010a364ae738ba89ae92167898febb4434695f40e772f3'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.lcamechanism.Distance'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_distance'
TOOL_DESCRIPTION = 'Call this tool to instantiate a Distance function that computes a scalar distance or similarity between two equal-length vectors using a specified metric. Returns a Distance object suitable for use as an ObjectiveFunction in PsyNeuLink mechanisms. Do NOT pass `variable` to the constructor — input vectors are supplied at execution time (via `default_variable` only if you need to fix the array shape at construction).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Optional 2-element array [[v1...], [v2...]] that fixes the expected input shape at construction time. Both inner arrays must have equal length. Omit in most cases \\u2014 input is provided at execution time.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "metric": {\n      "default": "euclidean",\n      "description": "Distance metric to use. Must be lowercase. \'euclidean\': L2 norm; \'cosine\': 1 - |cosine similarity|; \'correlation\': 1 - |Pearson r|; \'difference\': sum of absolute differences; \'dot_product\': inner product; \'energy\': -0.5 * dot product; \'cross-entropy\': cross-entropy of v1 w.r.t. v2; \'max_abs_diff\': maximum elementwise absolute difference; \'normed_L0_similarity\': L0 similarity normalized to [0,1].",\n      "enum": [\n        "max_abs_diff",\n        "difference",\n        "dot_product",\n        "normed_L0_similarity",\n        "euclidean",\n        "angle",\n        "correlation",\n        "cosine",\n        "entropy",\n        "cross-entropy",\n        "energy"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "If true, divides the result by the length of the input vectors. Has no effect for \'max_abs_diff\', \'correlation\', \'cosine\', or \'angle\' metrics.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL: Do NOT pass `variable` as a constructor argument — Distance.__init__() rejects it with TypeError. The input vectors are provided at execution time. If you need to pre-declare the input shape, use `default_variable` instead (a 2-item list of equal-length numeric lists).\n\nMetric values are case-sensitive and must be lowercase (e.g., `\'cosine\'`, not `\'COSINE\'`). Passing an uppercase metric string raises a BeartypeCallHintParamViolation. The valid set is exactly: \'max_abs_diff\', \'difference\', \'dot_product\', \'normed_L0_similarity\', \'euclidean\', \'angle\', \'correlation\', \'cosine\', \'entropy\', \'cross-entropy\', \'energy\'.\n\nThe internal default metric in Parameters is DIFFERENCE, but the docstring advertises EUCLIDEAN — when in doubt, specify explicitly.\n\n`normalize` is silently ignored for \'max_abs_diff\', \'correlation\', \'cosine\', and \'angle\' metrics.\n\nFor \'energy\': result = -0.5 * dot(v1, v2); normalization divides by len(v1)^2. For \'cosine\'/\'correlation\': result is 1 - |similarity|, so 0 means identical, 1 means orthogonal/uncorrelated.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Optional 2-element array '
                                                       '[[v1...], [v2...]] that fixes '
                                                       'the expected input shape at '
                                                       'construction time. Both inner '
                                                       'arrays must have equal length. '
                                                       'Omit in most cases — input is '
                                                       'provided at execution time.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'maxItems': 2,
                                        'minItems': 2,
                                        'type': 'array'},
                  'metric': { 'default': 'euclidean',
                              'description': 'Distance metric to use. Must be '
                                             "lowercase. 'euclidean': L2 norm; "
                                             "'cosine': 1 - |cosine similarity|; "
                                             "'correlation': 1 - |Pearson r|; "
                                             "'difference': sum of absolute "
                                             "differences; 'dot_product': inner "
                                             "product; 'energy': -0.5 * dot product; "
                                             "'cross-entropy': cross-entropy of v1 "
                                             "w.r.t. v2; 'max_abs_diff': maximum "
                                             'elementwise absolute difference; '
                                             "'normed_L0_similarity': L0 similarity "
                                             'normalized to [0,1].',
                              'enum': [ 'max_abs_diff',
                                        'difference',
                                        'dot_product',
                                        'normed_L0_similarity',
                                        'euclidean',
                                        'angle',
                                        'correlation',
                                        'cosine',
                                        'entropy',
                                        'cross-entropy',
                                        'energy'],
                              'type': 'string'},
                  'normalize': { 'default': False,
                                 'description': 'If true, divides the result by the '
                                                'length of the input vectors. Has no '
                                                "effect for 'max_abs_diff', "
                                                "'correlation', 'cosine', or 'angle' "
                                                'metrics.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL: Do NOT pass `variable` as a constructor argument — Distance.__init__() rejects it with TypeError. The input vectors are provided at execution time. If you need to pre-declare the input shape, use `default_variable` instead (a 2-item list of equal-length numeric lists).\n\nMetric values are case-sensitive and must be lowercase (e.g., `'cosine'`, not `'COSINE'`). Passing an uppercase metric string raises a BeartypeCallHintParamViolation. The valid set is exactly: 'max_abs_diff', 'difference', 'dot_product', 'normed_L0_similarity', 'euclidean', 'angle', 'correlation', 'cosine', 'entropy', 'cross-entropy', 'energy'.\n\nThe internal default metric in Parameters is DIFFERENCE, but the docstring advertises EUCLIDEAN — when in doubt, specify explicitly.\n\n`normalize` is silently ignored for 'max_abs_diff', 'correlation', 'cosine', and 'angle' metrics.\n\nFor 'energy': result = -0.5 * dot(v1, v2); normalization divides by len(v1)^2. For 'cosine'/'correlation': result is 1 - |similarity|, so 0 means identical, 1 means orthogonal/uncorrelated."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Distance
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
    def create_distance(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a Distance function that computes a scalar distance or similarity between two equal-length vectors using a specified metric.'
        return _impl(args or {})
