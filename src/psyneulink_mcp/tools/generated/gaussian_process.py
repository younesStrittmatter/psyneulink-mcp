"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd8c05b9be8fa0890bfcec74fc6ecd94a87316b3746157b37be93fba61ea4cf0b'
__pnl_qualname__ = 'psyneulink.GaussianProcess'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gaussian_process'
TOOL_DESCRIPTION = 'Use this tool to instantiate a GaussianProcess optimization function when you need to find an input sample (within bounded search dimensions) that maximizes or minimizes a scalar-valued objective function. Returns the optimal sample, its objective value, and optionally all evaluated samples and values. Call this when setting up a Mechanism\'s function for black-box optimization over a continuous bounded search space.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template defining the shape of samples to evaluate. Each element corresponds to one search dimension. Example: [[0], [0]] for 2 dimensions.",\n      "items": {},\n      "type": "array"\n    },\n    "direction": {\n      "default": "maximize",\n      "description": "Whether to seek the highest (\'maximize\') or lowest (\'minimize\') value of objective_function. Defaults to \'maximize\'.",\n      "enum": [\n        "maximize",\n        "minimize"\n      ],\n      "type": "string"\n    },\n    "objective_function": {\n      "description": "Name or reference to the function used to score each sample. Must return a scalar. Required for the optimization to run.",\n      "type": "string"\n    },\n    "save_values": {\n      "default": false,\n      "description": "If true, the function returns all objective values evaluated during the search in addition to the optimum. Defaults to false.",\n      "type": "boolean"\n    },\n    "search_space": {\n      "description": "List of [lower_bound, upper_bound] pairs, one per search dimension. Each entry bounds sampling along that dimension. Length must match the dimensionality of default_variable.",\n      "items": {\n        "maxItems": 2,\n        "minItems": 2,\n        "prefixItems": [\n          {\n            "description": "Lower bound",\n            "type": "number"\n          },\n          {\n            "description": "Upper bound",\n            "type": "number"\n          }\n        ],\n        "type": "array"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "objective_function",\n    "search_space"\n  ],\n  "type": "object"\n}\n\nNotes:\n**Implementation is a stub**: `_gaussian_process_sample` currently returns the previous sample unchanged (no real GP surrogate model), and `_gaussian_process_satisfied` terminates after exactly 2 iterations regardless of `max_iterations`. Effective optimization does not occur — only 2 samples are drawn.\n\n`save_samples` is always `True` internally (hardcoded in `super().__init__`); passing it has no effect. Do not include `save_samples` in the call.\n\n`max_iterations` appears in the docstring but is absent from the constructor signature and will be ignored if passed.\n\n`search_space` entries must be `[lower, upper]` pairs (lower strictly less than upper); the length must equal the number of elements in `default_variable`.\n\n`objective_function` must return a scalar; non-scalar returns will cause errors upstream.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template defining the shape of '
                                                       'samples to evaluate. Each '
                                                       'element corresponds to one '
                                                       'search dimension. Example: '
                                                       '[[0], [0]] for 2 dimensions.',
                                        'items': {},
                                        'type': 'array'},
                  'direction': { 'default': 'maximize',
                                 'description': 'Whether to seek the highest '
                                                "('maximize') or lowest ('minimize') "
                                                'value of objective_function. Defaults '
                                                "to 'maximize'.",
                                 'enum': ['maximize', 'minimize'],
                                 'type': 'string'},
                  'objective_function': { 'description': 'Name or reference to the '
                                                         'function used to score each '
                                                         'sample. Must return a '
                                                         'scalar. Required for the '
                                                         'optimization to run.',
                                          'type': 'string'},
                  'save_values': { 'default': False,
                                   'description': 'If true, the function returns all '
                                                  'objective values evaluated during '
                                                  'the search in addition to the '
                                                  'optimum. Defaults to false.',
                                   'type': 'boolean'},
                  'search_space': { 'description': 'List of [lower_bound, upper_bound] '
                                                   'pairs, one per search dimension. '
                                                   'Each entry bounds sampling along '
                                                   'that dimension. Length must match '
                                                   'the dimensionality of '
                                                   'default_variable.',
                                    'items': { 'maxItems': 2,
                                               'minItems': 2,
                                               'prefixItems': [ { 'description': 'Lower '
                                                                                 'bound',
                                                                  'type': 'number'},
                                                                { 'description': 'Upper '
                                                                                 'bound',
                                                                  'type': 'number'}],
                                               'type': 'array'},
                                    'type': 'array'}},
  'required': ['objective_function', 'search_space'],
  'type': 'object'}
TOOL_NOTES = '**Implementation is a stub**: `_gaussian_process_sample` currently returns the previous sample unchanged (no real GP surrogate model), and `_gaussian_process_satisfied` terminates after exactly 2 iterations regardless of `max_iterations`. Effective optimization does not occur — only 2 samples are drawn.\n\n`save_samples` is always `True` internally (hardcoded in `super().__init__`); passing it has no effect. Do not include `save_samples` in the call.\n\n`max_iterations` appears in the docstring but is absent from the constructor signature and will be ignored if passed.\n\n`search_space` entries must be `[lower, upper]` pairs (lower strictly less than upper); the length must equal the number of elements in `default_variable`.\n\n`objective_function` must return a scalar; non-scalar returns will cause errors upstream.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.GaussianProcess
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
    def create_gaussian_process(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to instantiate a GaussianProcess optimization function when you need to find an input sample (within bounded search dimensions) that maximizes or minimizes a scalar-valued objective function.'
        return _impl(args or {})
