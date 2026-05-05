"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e135ae8afbaab5247c54d44d75fbf9b111b93d4096a7e84c7c74beffcde29e53'
__pnl_qualname__ = 'psyneulink.PECOptimizationFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pec_optimization_function'
TOOL_DESCRIPTION = 'Call this to configure the search algorithm for a ParameterEstimationComposition (PEC) — either for parameter optimization or data fitting. Pass the resulting PECOptimizationFunction instance as the `function` argument when constructing a PEC. The tool returns a configured function object that drives either scipy\'s differential_evolution or an optuna study during PEC execution.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "direction": {\n      "default": "maximize",\n      "description": "Whether to maximize or minimize the objective function value.",\n      "enum": [\n        "maximize",\n        "minimize"\n      ],\n      "type": "string"\n    },\n    "max_iterations": {\n      "default": 500,\n      "description": "Maximum number of search iterations. For differential_evolution this is the number of generations; for optuna this is the number of trials.",\n      "type": "integer"\n    },\n    "method": {\n      "description": "Search algorithm to use. Pass \'differential_evolution\' to use scipy.optimize.differential_evolution. To use an optuna sampler, pass the sampler class name as a string (e.g., \'TPESampler\') \\u2014 note that non-string optuna values require Python-level construction and cannot be passed through this tool.",\n      "enum": [\n        "differential_evolution"\n      ],\n      "type": "string"\n    },\n    "optuna_kwargs": {\n      "additionalProperties": true,\n      "description": "Extra keyword arguments forwarded to the optuna sampler constructor. Only used when method is an optuna sampler class (not an already-instantiated instance). Ignored for differential_evolution.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "method"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `method` is required — there is no default. Only \'differential_evolution\' can be expressed as a plain JSON string; optuna BaseSampler classes/instances require Python-level construction and cannot be passed through this JSON tool.\n- `objective_function` (a callable taking a 3D array of shape (num_estimates, num_trials, num_outcome_variables)) cannot be expressed in JSON and must be set programmatically after construction via `set_pec_objective_function()`.\n- `optuna_kwargs` is silently ignored when `method` is an already-instantiated optuna sampler instance; it is only applied when `method` is a sampler class.\n- When using an optuna sampler class, the PEC\'s `initial_seed` is automatically forwarded to the sampler as `seed`; if `optuna_kwargs` already contains a `seed` key, it is overwritten with a warning.\n- Do not set `outcome_variable_indices` manually — the PEC populates it automatically when the function is assigned.\n- This class does NOT define the optimization problem (that is `objective_function`); it only specifies the search method. The docstring\'s use of "objective_function" is an overloaded term — the function passed here is the PEC-level scoring function, distinct from the OCM\'s internal `objective_function`.'
TOOL_PARAMETERS = { 'properties': { 'direction': { 'default': 'maximize',
                                 'description': 'Whether to maximize or minimize the '
                                                'objective function value.',
                                 'enum': ['maximize', 'minimize'],
                                 'type': 'string'},
                  'max_iterations': { 'default': 500,
                                      'description': 'Maximum number of search '
                                                     'iterations. For '
                                                     'differential_evolution this is '
                                                     'the number of generations; for '
                                                     'optuna this is the number of '
                                                     'trials.',
                                      'type': 'integer'},
                  'method': { 'description': 'Search algorithm to use. Pass '
                                             "'differential_evolution' to use "
                                             'scipy.optimize.differential_evolution. '
                                             'To use an optuna sampler, pass the '
                                             'sampler class name as a string (e.g., '
                                             "'TPESampler') — note that non-string "
                                             'optuna values require Python-level '
                                             'construction and cannot be passed '
                                             'through this tool.',
                              'enum': ['differential_evolution'],
                              'type': 'string'},
                  'optuna_kwargs': { 'additionalProperties': True,
                                     'description': 'Extra keyword arguments forwarded '
                                                    'to the optuna sampler '
                                                    'constructor. Only used when '
                                                    'method is an optuna sampler class '
                                                    '(not an already-instantiated '
                                                    'instance). Ignored for '
                                                    'differential_evolution.',
                                     'type': 'object'}},
  'required': ['method'],
  'type': 'object'}
TOOL_NOTES = '- `method` is required — there is no default. Only \'differential_evolution\' can be expressed as a plain JSON string; optuna BaseSampler classes/instances require Python-level construction and cannot be passed through this JSON tool.\n- `objective_function` (a callable taking a 3D array of shape (num_estimates, num_trials, num_outcome_variables)) cannot be expressed in JSON and must be set programmatically after construction via `set_pec_objective_function()`.\n- `optuna_kwargs` is silently ignored when `method` is an already-instantiated optuna sampler instance; it is only applied when `method` is a sampler class.\n- When using an optuna sampler class, the PEC\'s `initial_seed` is automatically forwarded to the sampler as `seed`; if `optuna_kwargs` already contains a `seed` key, it is overwritten with a warning.\n- Do not set `outcome_variable_indices` manually — the PEC populates it automatically when the function is assigned.\n- This class does NOT define the optimization problem (that is `objective_function`); it only specifies the search method. The docstring\'s use of "objective_function" is an overloaded term — the function passed here is the PEC-level scoring function, distinct from the OCM\'s internal `objective_function`.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PECOptimizationFunction
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
    def create_pec_optimization_function(args: dict[str, Any] | None = None) -> Any:
        'Call this to configure the search algorithm for a ParameterEstimationComposition (PEC) — either for parameter optimization or data fitting.'
        return _impl(args or {})
