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
TOOL_DESCRIPTION = 'Call this tool to instantiate a PsyNeuLink `Distance` function that computes a scalar distance or similarity between two equal-length numeric vectors using a configurable metric (euclidean, cosine, correlation, energy, etc.). Use it when you need a standalone distance computation or when assigning a distance objective to a Stability mechanism. Returns a Distance instance handle ready to be called or wired into a composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "A 2-element list of equal-length numeric arrays defining the default input shape, e.g. [[0,0,0],[0,0,0]]. CRITICAL: this parameter is named \'default_variable\', NOT \'variable\' \\u2014 passing \'variable\' raises TypeError.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "metric": {\n      "description": "Distance metric to use. MUST be an exact lowercase string from the enum \\u2014 uppercase values (e.g. \'COSINE\') raise BeartypeCallHintParamViolation. Default is \'difference\' (sum of absolute elementwise differences). \'euclidean\' = L2 norm; \'cosine\' returns 1-|cosine_similarity|; \'energy\' returns -dot(v1,v2)/2; \'cross-entropy\' expects values in (0,1].",\n      "enum": [\n        "euclidean",\n        "difference",\n        "max_abs_diff",\n        "dot_product",\n        "normed_L0_similarity",\n        "cosine",\n        "correlation",\n        "cross-entropy",\n        "energy",\n        "angle",\n        "entropy"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "description": "If true, divide the result by vector length. Silently ignored for max_abs_diff, correlation, cosine, and angle metrics. For energy, divides by len(v1)^2 instead of len(v1). Default false.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — two confirmed failure modes from runtime feedback:\n1. The constructor parameter for input arrays is `default_variable`, NOT `variable`. Passing `variable` raises `TypeError: Distance.__init__() got an unexpected keyword argument \'variable\'`.\n2. Metric values must be lowercase and match the enum exactly (e.g. `\'cosine\'` not `\'COSINE\'`, `\'euclidean\'` not `\'EUCLIDEAN\'`). Uppercase raises BeartypeCallHintParamViolation.\n\nAdditional caveats:\n- Both arrays in `default_variable` must have identical lengths; mismatched lengths raise FunctionError.\n- `normalize` is silently ignored for `max_abs_diff`, `correlation`, `cosine`, and `angle` metrics.\n- For `energy` with `normalize=True`, the divisor is `len(v1)^2`, not `len(v1)`.\n- `cross-entropy` inputs should be probabilities in (0,1]; zeros are replaced with EPSILON internally.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'A 2-element list of '
                                                       'equal-length numeric arrays '
                                                       'defining the default input '
                                                       'shape, e.g. [[0,0,0],[0,0,0]]. '
                                                       'CRITICAL: this parameter is '
                                                       "named 'default_variable', NOT "
                                                       "'variable' — passing "
                                                       "'variable' raises TypeError.",
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'maxItems': 2,
                                        'minItems': 2,
                                        'type': 'array'},
                  'metric': { 'description': 'Distance metric to use. MUST be an exact '
                                             'lowercase string from the enum — '
                                             "uppercase values (e.g. 'COSINE') raise "
                                             'BeartypeCallHintParamViolation. Default '
                                             "is 'difference' (sum of absolute "
                                             "elementwise differences). 'euclidean' = "
                                             "L2 norm; 'cosine' returns "
                                             "1-|cosine_similarity|; 'energy' returns "
                                             "-dot(v1,v2)/2; 'cross-entropy' expects "
                                             'values in (0,1].',
                              'enum': [ 'euclidean',
                                        'difference',
                                        'max_abs_diff',
                                        'dot_product',
                                        'normed_L0_similarity',
                                        'cosine',
                                        'correlation',
                                        'cross-entropy',
                                        'energy',
                                        'angle',
                                        'entropy'],
                              'type': 'string'},
                  'normalize': { 'description': 'If true, divide the result by vector '
                                                'length. Silently ignored for '
                                                'max_abs_diff, correlation, cosine, '
                                                'and angle metrics. For energy, '
                                                'divides by len(v1)^2 instead of '
                                                'len(v1). Default false.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL — two confirmed failure modes from runtime feedback:\n1. The constructor parameter for input arrays is `default_variable`, NOT `variable`. Passing `variable` raises `TypeError: Distance.__init__() got an unexpected keyword argument 'variable'`.\n2. Metric values must be lowercase and match the enum exactly (e.g. `'cosine'` not `'COSINE'`, `'euclidean'` not `'EUCLIDEAN'`). Uppercase raises BeartypeCallHintParamViolation.\n\nAdditional caveats:\n- Both arrays in `default_variable` must have identical lengths; mismatched lengths raise FunctionError.\n- `normalize` is silently ignored for `max_abs_diff`, `correlation`, `cosine`, and `angle` metrics.\n- For `energy` with `normalize=True`, the divisor is `len(v1)^2`, not `len(v1)`.\n- `cross-entropy` inputs should be probabilities in (0,1]; zeros are replaced with EPSILON internally."


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
        'Call this tool to instantiate a PsyNeuLink `Distance` function that computes a scalar distance or similarity between two equal-length numeric vectors using a configurable metric (euclidean, cosine, correlation, energy, etc.).'
        return _impl(args or {})
