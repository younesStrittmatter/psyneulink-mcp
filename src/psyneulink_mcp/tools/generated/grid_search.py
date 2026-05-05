"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8f00bd2f2d15aca1fee402c0d1ba54c62b8de051552601a067191d298a6ab9ab'
__pnl_qualname__ = 'psyneulink.GridSearch'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_grid_search'
TOOL_DESCRIPTION = 'Call this tool to configure a GridSearch optimization function that exhaustively evaluates an objective function over all combinations (Cartesian product) of discrete parameter values. Use it when you need guaranteed coverage of a finite parameter space rather than a stochastic search. Returns the parameter combination that maximizes or minimizes the objective, plus optional logs of all samples and values evaluated.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "direction": {\n      "default": "maximize",\n      "description": "Whether to seek the highest (\'maximize\') or lowest (\'minimize\') value returned by the objective function.",\n      "enum": [\n        "maximize",\n        "minimize"\n      ],\n      "type": "string"\n    },\n    "max_iterations": {\n      "default": 1000,\n      "description": "Hard cap on the number of objective function evaluations. If the grid is larger than this limit, a warning is issued and the best sample found so far is returned.",\n      "type": "integer"\n    },\n    "save_samples": {\n      "default": false,\n      "description": "If true, all evaluated parameter combinations are saved and returned alongside the optimal sample.",\n      "type": "boolean"\n    },\n    "save_values": {\n      "default": false,\n      "description": "If true, the objective function value for every evaluated sample is saved and returned.",\n      "type": "boolean"\n    },\n    "search_space": {\n      "description": "List of discrete value arrays, one per parameter dimension. Each inner array is the set of values to try for that dimension. GridSearch evaluates all Cartesian combinations. All dimensions must be finite. Example: [[0.1, 0.5, 1.0], [1, 2, 4]] searches 6 combinations.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "seed": {\n      "description": "Random seed for the internal random state, relevant only when select_randomly_from_optimal_values is true.",\n      "type": "integer"\n    },\n    "select_randomly_from_optimal_values": {\n      "default": false,\n      "description": "If true, uses reservoir sampling to break ties uniformly at random when multiple samples yield the same optimal value. If false, the first optimal sample encountered is returned.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "search_space"\n  ],\n  "type": "object"\n}\n\nNotes:\n**objective_function is not in this schema** because it is a Python callable that cannot be passed through JSON. It must be wired up at the Python level (e.g., via an OptimizationControlMechanism), not supplied by the agent as a literal argument. Attempting to pass it here will fail.\n\n**search_space must be finite**: every dimension must have a bounded, enumerable set of values. Passing infinite iterators raises an OptimizationFunctionError at reset time.\n\n**Total grid size = product of all dimension lengths**. A 5-dimensional space with 10 values each = 100,000 evaluations — set max_iterations defensively.\n\n**save_values in the source always saves regardless**: the internal `_return_values` and `_return_samples` flags are both set from `save_values` in `__init__`, so `save_samples` and `save_values` may behave identically in practice — both control whether all_values/all_samples are returned by `_function`.\n\n**direction accepts lowercase strings** (\'maximize\'/\'minimize\') per the `@beartype` annotation on `__init__`, not the PNL constants MAXIMIZE/MINIMIZE — use the string literals shown in the enum.'
TOOL_PARAMETERS = { 'properties': { 'direction': { 'default': 'maximize',
                                 'description': 'Whether to seek the highest '
                                                "('maximize') or lowest ('minimize') "
                                                'value returned by the objective '
                                                'function.',
                                 'enum': ['maximize', 'minimize'],
                                 'type': 'string'},
                  'max_iterations': { 'default': 1000,
                                      'description': 'Hard cap on the number of '
                                                     'objective function evaluations. '
                                                     'If the grid is larger than this '
                                                     'limit, a warning is issued and '
                                                     'the best sample found so far is '
                                                     'returned.',
                                      'type': 'integer'},
                  'save_samples': { 'default': False,
                                    'description': 'If true, all evaluated parameter '
                                                   'combinations are saved and '
                                                   'returned alongside the optimal '
                                                   'sample.',
                                    'type': 'boolean'},
                  'save_values': { 'default': False,
                                   'description': 'If true, the objective function '
                                                  'value for every evaluated sample is '
                                                  'saved and returned.',
                                   'type': 'boolean'},
                  'search_space': { 'description': 'List of discrete value arrays, one '
                                                   'per parameter dimension. Each '
                                                   'inner array is the set of values '
                                                   'to try for that dimension. '
                                                   'GridSearch evaluates all Cartesian '
                                                   'combinations. All dimensions must '
                                                   'be finite. Example: [[0.1, 0.5, '
                                                   '1.0], [1, 2, 4]] searches 6 '
                                                   'combinations.',
                                    'items': { 'items': {'type': 'number'},
                                               'type': 'array'},
                                    'type': 'array'},
                  'seed': { 'description': 'Random seed for the internal random state, '
                                           'relevant only when '
                                           'select_randomly_from_optimal_values is '
                                           'true.',
                            'type': 'integer'},
                  'select_randomly_from_optimal_values': { 'default': False,
                                                           'description': 'If true, '
                                                                          'uses '
                                                                          'reservoir '
                                                                          'sampling to '
                                                                          'break ties '
                                                                          'uniformly '
                                                                          'at random '
                                                                          'when '
                                                                          'multiple '
                                                                          'samples '
                                                                          'yield the '
                                                                          'same '
                                                                          'optimal '
                                                                          'value. If '
                                                                          'false, the '
                                                                          'first '
                                                                          'optimal '
                                                                          'sample '
                                                                          'encountered '
                                                                          'is '
                                                                          'returned.',
                                                           'type': 'boolean'}},
  'required': ['search_space'],
  'type': 'object'}
TOOL_NOTES = "**objective_function is not in this schema** because it is a Python callable that cannot be passed through JSON. It must be wired up at the Python level (e.g., via an OptimizationControlMechanism), not supplied by the agent as a literal argument. Attempting to pass it here will fail.\n\n**search_space must be finite**: every dimension must have a bounded, enumerable set of values. Passing infinite iterators raises an OptimizationFunctionError at reset time.\n\n**Total grid size = product of all dimension lengths**. A 5-dimensional space with 10 values each = 100,000 evaluations — set max_iterations defensively.\n\n**save_values in the source always saves regardless**: the internal `_return_values` and `_return_samples` flags are both set from `save_values` in `__init__`, so `save_samples` and `save_values` may behave identically in practice — both control whether all_values/all_samples are returned by `_function`.\n\n**direction accepts lowercase strings** ('maximize'/'minimize') per the `@beartype` annotation on `__init__`, not the PNL constants MAXIMIZE/MINIMIZE — use the string literals shown in the enum."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.GridSearch
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
    def create_grid_search(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to configure a GridSearch optimization function that exhaustively evaluates an objective function over all combinations (Cartesian product) of discrete parameter values.'
        return _impl(args or {})
