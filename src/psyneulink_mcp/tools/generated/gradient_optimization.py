"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e40fec66ca69f481d512b444b46d225ab5dcd0cc2f419bec215b3d1d20c1181f'
__pnl_qualname__ = 'psyneulink.GradientOptimization'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gradient_optimization'
TOOL_DESCRIPTION = 'Call this tool to create a GradientOptimization function that finds the optimal input to a scalar-valued objective function by following its gradient. Use it when you need gradient-based parameter search (e.g., tuning weights or inputs to maximize/minimize some scoring function on a PsyNeuLink model). The tool returns an instantiated GradientOptimization object; calling it yields the optimal sample, its objective value, and optionally all intermediate samples and values.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "annealing_function": {\n      "description": "Python expression or reference to a callable(step_size, iteration) -> float that adapts step_size each iteration. If omitted, step_size stays constant.",\n      "type": "string"\n    },\n    "convergence_criterion": {\n      "default": "value",\n      "description": "\'value\': stop when change in objective_function output < convergence_threshold. \'variable\': stop when change in the sample itself < convergence_threshold.",\n      "enum": [\n        "variable",\n        "value"\n      ],\n      "type": "string"\n    },\n    "convergence_threshold": {\n      "default": 0.001,\n      "description": "Stopping threshold for convergence_criterion. Optimization halts when the tracked change falls below this value.",\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template array defining the shape and starting point for the optimization. If omitted, inferred from the first call.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "direction": {\n      "default": "ascent",\n      "description": "Optimization direction. \'ascent\' maximizes the objective; \'descent\' minimizes it.",\n      "enum": [\n        "ascent",\n        "descent"\n      ],\n      "type": "string"\n    },\n    "gradient_function": {\n      "description": "Python expression or reference to a callable that computes the gradient of objective_function with respect to its input. If omitted, PyTorch autograd (torch.func.grad) is used automatically \\u2014 requires PyTorch >= 2.0.",\n      "type": "string"\n    },\n    "max_iterations": {\n      "default": 1000,\n      "description": "Hard cap on iterations. If reached without convergence, a warning is issued and the last evaluated sample is returned.",\n      "type": "integer"\n    },\n    "objective_function": {\n      "description": "Python expression or reference to a callable that takes a sample (ndarray) and returns a scalar. REQUIRED. This is the function being optimized.",\n      "type": "string"\n    },\n    "save_samples": {\n      "default": false,\n      "description": "If true, all intermediate samples are collected and returned alongside the optimal sample.",\n      "type": "boolean"\n    },\n    "save_values": {\n      "default": false,\n      "description": "If true, objective_function values for all intermediate samples are collected and returned.",\n      "type": "boolean"\n    },\n    "search_space": {\n      "description": "List of [lower, upper] bound pairs, one per dimension of the sample. Values that exceed a bound are clipped to the bound. Omit for unconstrained optimization.",\n      "items": {\n        "description": "Two-element [lower, upper] bound pair for the corresponding dimension. Use null for unbounded on one side.",\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "step_size": {\n      "default": 1,\n      "description": "Learning rate \\u2014 how far to move along the gradient each iteration. If annealing_function is provided, this is the initial value.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "objective_function"\n  ],\n  "type": "object"\n}\n\nNotes:\nobjective_function is mandatory and must return a scalar — a non-scalar return will cause an error. If gradient_function is not provided, PyTorch >= 2.0 must be installed; if PyTorch is missing or too old, construction will raise a ValueError at reset time (not at instantiation). search_space items must resolve to exactly 2-element [lower, upper] sequences — more than 2 elements are treated as a set and min/max are used as bounds. step_size applies uniformly across all dimensions; there is no per-dimension learning rate. The returned object\'s function() yields a 4-tuple: (optimal_sample, optimal_value, all_samples, all_values), where the last two are empty lists unless save_samples/save_values are True. Convergence comparison for \'variable\' criterion uses the L∞ norm (np.max(np.abs(...))), not L2.'
TOOL_PARAMETERS = { 'properties': { 'annealing_function': { 'description': 'Python expression or '
                                                         'reference to a '
                                                         'callable(step_size, '
                                                         'iteration) -> float that '
                                                         'adapts step_size each '
                                                         'iteration. If omitted, '
                                                         'step_size stays constant.',
                                          'type': 'string'},
                  'convergence_criterion': { 'default': 'value',
                                             'description': "'value': stop when change "
                                                            'in objective_function '
                                                            'output < '
                                                            'convergence_threshold. '
                                                            "'variable': stop when "
                                                            'change in the sample '
                                                            'itself < '
                                                            'convergence_threshold.',
                                             'enum': ['variable', 'value'],
                                             'type': 'string'},
                  'convergence_threshold': { 'default': 0.001,
                                             'description': 'Stopping threshold for '
                                                            'convergence_criterion. '
                                                            'Optimization halts when '
                                                            'the tracked change falls '
                                                            'below this value.',
                                             'type': 'number'},
                  'default_variable': { 'description': 'Template array defining the '
                                                       'shape and starting point for '
                                                       'the optimization. If omitted, '
                                                       'inferred from the first call.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'direction': { 'default': 'ascent',
                                 'description': "Optimization direction. 'ascent' "
                                                "maximizes the objective; 'descent' "
                                                'minimizes it.',
                                 'enum': ['ascent', 'descent'],
                                 'type': 'string'},
                  'gradient_function': { 'description': 'Python expression or '
                                                        'reference to a callable that '
                                                        'computes the gradient of '
                                                        'objective_function with '
                                                        'respect to its input. If '
                                                        'omitted, PyTorch autograd '
                                                        '(torch.func.grad) is used '
                                                        'automatically — requires '
                                                        'PyTorch >= 2.0.',
                                         'type': 'string'},
                  'max_iterations': { 'default': 1000,
                                      'description': 'Hard cap on iterations. If '
                                                     'reached without convergence, a '
                                                     'warning is issued and the last '
                                                     'evaluated sample is returned.',
                                      'type': 'integer'},
                  'objective_function': { 'description': 'Python expression or '
                                                         'reference to a callable that '
                                                         'takes a sample (ndarray) and '
                                                         'returns a scalar. REQUIRED. '
                                                         'This is the function being '
                                                         'optimized.',
                                          'type': 'string'},
                  'save_samples': { 'default': False,
                                    'description': 'If true, all intermediate samples '
                                                   'are collected and returned '
                                                   'alongside the optimal sample.',
                                    'type': 'boolean'},
                  'save_values': { 'default': False,
                                   'description': 'If true, objective_function values '
                                                  'for all intermediate samples are '
                                                  'collected and returned.',
                                   'type': 'boolean'},
                  'search_space': { 'description': 'List of [lower, upper] bound '
                                                   'pairs, one per dimension of the '
                                                   'sample. Values that exceed a bound '
                                                   'are clipped to the bound. Omit for '
                                                   'unconstrained optimization.',
                                    'items': { 'description': 'Two-element [lower, '
                                                              'upper] bound pair for '
                                                              'the corresponding '
                                                              'dimension. Use null for '
                                                              'unbounded on one side.',
                                               'type': 'array'},
                                    'type': 'array'},
                  'step_size': { 'default': 1,
                                 'description': 'Learning rate — how far to move along '
                                                'the gradient each iteration. If '
                                                'annealing_function is provided, this '
                                                'is the initial value.',
                                 'type': 'number'}},
  'required': ['objective_function'],
  'type': 'object'}
TOOL_NOTES = "objective_function is mandatory and must return a scalar — a non-scalar return will cause an error. If gradient_function is not provided, PyTorch >= 2.0 must be installed; if PyTorch is missing or too old, construction will raise a ValueError at reset time (not at instantiation). search_space items must resolve to exactly 2-element [lower, upper] sequences — more than 2 elements are treated as a set and min/max are used as bounds. step_size applies uniformly across all dimensions; there is no per-dimension learning rate. The returned object's function() yields a 4-tuple: (optimal_sample, optimal_value, all_samples, all_values), where the last two are empty lists unless save_samples/save_values are True. Convergence comparison for 'variable' criterion uses the L∞ norm (np.max(np.abs(...))), not L2."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.GradientOptimization
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
    def create_gradient_optimization(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a GradientOptimization function that finds the optimal input to a scalar-valued objective function by following its gradient.'
        return _impl(args or {})
