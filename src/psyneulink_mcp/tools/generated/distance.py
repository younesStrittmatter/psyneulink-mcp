"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '782598fd62b19cbfe0010a364ae738ba89ae92167898febb4434695f40e772f3'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.processing.transfermechanism.Distance'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_distance'
TOOL_DESCRIPTION = 'Call this tool to create a `Distance` function object that computes a scalar distance between two equal-length numeric vectors. Use it when you need a reusable distance-metric function to attach to a PsyNeuLink component (e.g., as an objective function for a mechanism). The constructed object can then be called with a 2-item 2d array to produce a scalar distance value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "A 2-element array containing the two numeric vectors to compare, e.g. [[1,0,0],[0,1,0]]. Both inner arrays must have equal length. NOTE: use \'default_variable\', NOT \'variable\' \\u2014 passing \'variable\' raises TypeError.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "metric": {\n      "description": "Distance metric to use. Must be an exact lowercase string from the allowed set. Common choices: \'euclidean\' (L2 norm), \'cosine\' (1 - |cosine similarity|), \'correlation\' (1 - |Pearson r|), \'difference\' (L1 sum of abs diff), \'energy\' (-0.5 * dot product). Default is \'difference\'.",\n      "enum": [\n        "max_abs_diff",\n        "difference",\n        "dot_product",\n        "normed_L0_similarity",\n        "euclidean",\n        "angle",\n        "correlation",\n        "cosine",\n        "entropy",\n        "cross-entropy",\n        "energy"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "If true, divides the result by the vector length (or length^2 for \'energy\'). Has NO effect for \'max_abs_diff\', \'correlation\', \'cosine\', or \'angle\' metrics. Default is false.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — two bugs have been confirmed in production:\n1. Pass the two-vector input as `default_variable`, NOT `variable`. The constructor parameter is named `default_variable`; passing `variable` raises `TypeError: Distance.__init__() got an unexpected keyword argument \'variable\'`.\n2. The `metric` string must be lowercase exactly as listed in the enum (e.g. `\'cosine\'`, NOT `\'COSINE\'`). PNL uses beartype to enforce a Literal type — any uppercase or misspelled value raises `BeartypeCallHintParamViolation`.\nThe docstring incorrectly states the default metric is EUCLIDEAN; the actual default (from the Parameters class) is `\'difference\'` (L1 sum of absolute differences).\n`normalize` is silently ignored for `\'max_abs_diff\'`, `\'correlation\'`, `\'cosine\'`, and `\'angle\'` — no error is raised.\n`\'cross-entropy\'` requires all values to be in [0, 1]; zeros are replaced with EPSILON internally to avoid log(0).'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'A 2-element array containing '
                                                       'the two numeric vectors to '
                                                       'compare, e.g. '
                                                       '[[1,0,0],[0,1,0]]. Both inner '
                                                       'arrays must have equal length. '
                                                       "NOTE: use 'default_variable', "
                                                       "NOT 'variable' — passing "
                                                       "'variable' raises TypeError.",
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'maxItems': 2,
                                        'minItems': 2,
                                        'type': 'array'},
                  'metric': { 'description': 'Distance metric to use. Must be an exact '
                                             'lowercase string from the allowed set. '
                                             "Common choices: 'euclidean' (L2 norm), "
                                             "'cosine' (1 - |cosine similarity|), "
                                             "'correlation' (1 - |Pearson r|), "
                                             "'difference' (L1 sum of abs diff), "
                                             "'energy' (-0.5 * dot product). Default "
                                             "is 'difference'.",
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
                                                'vector length (or length^2 for '
                                                "'energy'). Has NO effect for "
                                                "'max_abs_diff', 'correlation', "
                                                "'cosine', or 'angle' metrics. Default "
                                                'is false.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL — two bugs have been confirmed in production:\n1. Pass the two-vector input as `default_variable`, NOT `variable`. The constructor parameter is named `default_variable`; passing `variable` raises `TypeError: Distance.__init__() got an unexpected keyword argument 'variable'`.\n2. The `metric` string must be lowercase exactly as listed in the enum (e.g. `'cosine'`, NOT `'COSINE'`). PNL uses beartype to enforce a Literal type — any uppercase or misspelled value raises `BeartypeCallHintParamViolation`.\nThe docstring incorrectly states the default metric is EUCLIDEAN; the actual default (from the Parameters class) is `'difference'` (L1 sum of absolute differences).\n`normalize` is silently ignored for `'max_abs_diff'`, `'correlation'`, `'cosine'`, and `'angle'` — no error is raised.\n`'cross-entropy'` requires all values to be in [0, 1]; zeros are replaced with EPSILON internally to avoid log(0)."


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
        'Call this tool to create a `Distance` function object that computes a scalar distance between two equal-length numeric vectors.'
        return _impl(args or {})
