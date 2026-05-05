"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '782598fd62b19cbfe0010a364ae738ba89ae92167898febb4434695f40e772f3'
__pnl_qualname__ = 'psyneulink.Distance'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_distance'
TOOL_DESCRIPTION = 'Call this tool to compute a scalar distance (or similarity) between two equal-length numeric vectors. Use it when you need to compare activation patterns, measure representational similarity, or evaluate the closeness of two state vectors using metrics like Euclidean distance, cosine, correlation, cross-entropy, or energy. Returns a single scalar value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "metric": {\n      "default": "DIFFERENCE",\n      "description": "Distance metric to use. EUCLIDEAN: L2 norm; DIFFERENCE: sum of absolute differences (L1); MAX_ABS_DIFF: max elementwise absolute difference; DOT_PRODUCT: raw dot product; COSINE/COSINE_SIMILARITY: 1 - |cosine similarity| (0 = identical direction); CORRELATION: 1 - |Pearson r|; CROSS_ENTROPY: cross-entropy loss (vectors should be in [0,1]); ENERGY: -dot(v1,v2)/2; NORMED_L0_SIMILARITY: specialized for binary vectors.",\n      "enum": [\n        "EUCLIDEAN",\n        "DIFFERENCE",\n        "MAX_ABS_DIFF",\n        "DOT_PRODUCT",\n        "COSINE",\n        "COSINE_SIMILARITY",\n        "CORRELATION",\n        "CROSS_ENTROPY",\n        "ENERGY",\n        "NORMED_L0_SIMILARITY"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "If true, divide the result by the vector length (or length^2 for ENERGY). Silently ignored for MAX_ABS_DIFF, CORRELATION, COSINE, and COSINE_SIMILARITY.",\n      "type": "boolean"\n    },\n    "variable": {\n      "description": "A list of exactly two numeric arrays of equal length \\u2014 the two vectors to compare.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    }\n  },\n  "required": [\n    "variable"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe default metric is DIFFERENCE (L1 sum of absolute differences), NOT EUCLIDEAN — the docstring header is misleading. Both vectors in `variable` must have identical lengths; mismatched lengths or a non-2-item variable raises FunctionError at call time. COSINE and COSINE_SIMILARITY are equivalent and both return 1 - |cosine_sim|, so identical vectors yield 0. The `normalize` flag is silently a no-op for MAX_ABS_DIFF, CORRELATION, COSINE, and COSINE_SIMILARITY regardless of what is passed. For CROSS_ENTROPY, zero values in either vector are replaced with a small epsilon internally to avoid log(0), but very small values near zero may still produce unexpectedly large outputs. DOT_PRODUCT and ENERGY are not true distance metrics and can return negative values.'
TOOL_PARAMETERS = { 'properties': { 'metric': { 'default': 'DIFFERENCE',
                              'description': 'Distance metric to use. EUCLIDEAN: L2 '
                                             'norm; DIFFERENCE: sum of absolute '
                                             'differences (L1); MAX_ABS_DIFF: max '
                                             'elementwise absolute difference; '
                                             'DOT_PRODUCT: raw dot product; '
                                             'COSINE/COSINE_SIMILARITY: 1 - |cosine '
                                             'similarity| (0 = identical direction); '
                                             'CORRELATION: 1 - |Pearson r|; '
                                             'CROSS_ENTROPY: cross-entropy loss '
                                             '(vectors should be in [0,1]); ENERGY: '
                                             '-dot(v1,v2)/2; NORMED_L0_SIMILARITY: '
                                             'specialized for binary vectors.',
                              'enum': [ 'EUCLIDEAN',
                                        'DIFFERENCE',
                                        'MAX_ABS_DIFF',
                                        'DOT_PRODUCT',
                                        'COSINE',
                                        'COSINE_SIMILARITY',
                                        'CORRELATION',
                                        'CROSS_ENTROPY',
                                        'ENERGY',
                                        'NORMED_L0_SIMILARITY'],
                              'type': 'string'},
                  'normalize': { 'default': False,
                                 'description': 'If true, divide the result by the '
                                                'vector length (or length^2 for '
                                                'ENERGY). Silently ignored for '
                                                'MAX_ABS_DIFF, CORRELATION, COSINE, '
                                                'and COSINE_SIMILARITY.',
                                 'type': 'boolean'},
                  'variable': { 'description': 'A list of exactly two numeric arrays '
                                               'of equal length — the two vectors to '
                                               'compare.',
                                'items': {'items': {'type': 'number'}, 'type': 'array'},
                                'maxItems': 2,
                                'minItems': 2,
                                'type': 'array'}},
  'required': ['variable'],
  'type': 'object'}
TOOL_NOTES = 'The default metric is DIFFERENCE (L1 sum of absolute differences), NOT EUCLIDEAN — the docstring header is misleading. Both vectors in `variable` must have identical lengths; mismatched lengths or a non-2-item variable raises FunctionError at call time. COSINE and COSINE_SIMILARITY are equivalent and both return 1 - |cosine_sim|, so identical vectors yield 0. The `normalize` flag is silently a no-op for MAX_ABS_DIFF, CORRELATION, COSINE, and COSINE_SIMILARITY regardless of what is passed. For CROSS_ENTROPY, zero values in either vector are replaced with a small epsilon internally to avoid log(0), but very small values near zero may still produce unexpectedly large outputs. DOT_PRODUCT and ENERGY are not true distance metrics and can return negative values.'


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
        'Call this tool to compute a scalar distance (or similarity) between two equal-length numeric vectors.'
        return _impl(args or {})
