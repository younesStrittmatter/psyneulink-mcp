"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b18fb0a115314fa366d2155b4c5968bd3cc662bd2e0b424e5283028d1de70b63'
__pnl_qualname__ = 'psyneulink.ParameterEstimationComposition'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_parameter_estimation_composition'
TOOL_DESCRIPTION = 'Call this tool to construct a ParameterEstimationComposition when you need to fit a PsyNeuLink model\'s parameters to observed behavioral data via maximum likelihood estimation, or to optimize parameters to maximize/minimize a custom objective function. The returned object must then be executed via `.run(inputs=...)` to perform the estimation; results are available on `.optimized_parameter_values` (dict of best-fit parameter values) and `.optimal_value` (scalar score).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "data": {\n      "description": "pandas DataFrame of observed data for data-fitting mode. Each column must correspond to one outcome_variable in the same order. Mutually exclusive with objective_function.",\n      "type": "object"\n    },\n    "data_categorical_dims": {\n      "description": "Marks which data dimensions are categorical. Provide a list of booleans (mask, same length as data columns) or a list of integer column indices. Overridden automatically by pandas Categorical dtype columns. If None, all dimensions are treated as continuous.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "boolean"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "depends_on": {\n      "description": "Maps parameter keys (matching keys in `parameters`) to column names in the data DataFrame. Each unique categorical value in that column becomes its own condition with a separately estimated parameter. Requires data to be a pandas DataFrame with categorical or string columns.",\n      "type": "object"\n    },\n    "initial_seed": {\n      "description": "Seed for the random number generator at construction, forwarded to the internal OptimizationControlMechanism. Use for reproducible results.",\n      "type": "integer"\n    },\n    "model": {\n      "description": "External Composition whose parameters are estimated. If omitted, pass nodes/pathways kwargs to build the model inline; PEC wraps it internally.",\n      "type": "object"\n    },\n    "name": {\n      "description": "Optional name for the ParameterEstimationComposition instance.",\n      "type": "string"\n    },\n    "num_estimates": {\n      "default": 1,\n      "description": "Number of stochastic simulation runs per parameter combination. Increase to reduce Monte Carlo variance at the cost of runtime.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "num_trials_per_estimate": {\n      "description": "Exact number of trials executed per model run during estimation. If None and data is provided, automatically set to len(data). Distinct from num_trials in .run(), which controls how many full fits are performed.",\n      "type": "integer"\n    },\n    "objective_function": {\n      "description": "Callable for optimization mode; receives an array of outcome_variable values and returns a scalar. Input shape must match the concatenated values of outcome_variables. Mutually exclusive with data.",\n      "type": "object"\n    },\n    "optimization_function": {\n      "description": "Search strategy over parameter combinations. Pass \'grid_search\' for exhaustive enumeration, \'differential_evolution\' for global stochastic optimization, or a PECOptimizationFunction instance. Omitting raises a warning and defaults to grid_search.",\n      "oneOf": [\n        {\n          "enum": [\n            "grid_search",\n            "differential_evolution"\n          ],\n          "type": "string"\n        },\n        {\n          "description": "A PECOptimizationFunction instance",\n          "type": "object"\n        }\n      ]\n    },\n    "outcome_variables": {\n      "description": "List of OUTPUT Mechanism or OutputPort objects from the model whose values are compared to data (fitting) or scored by the objective function (optimization). Must be a subset of the terminal Mechanism\'s output ports in the model.",\n      "items": {},\n      "type": "array"\n    },\n    "parameters": {\n      "description": "Maps each parameter-to-estimate to a list of candidate values. Keys must be (param_name, mechanism) Python tuples (encode as 2-element JSON arrays); values are arrays of numbers to sample. Example: {(\\"drift_rate\\", my_ddm): [0.1, 0.2, 0.3]}.",\n      "type": "object"\n    },\n    "same_seed_for_all_parameter_combinations": {\n      "default": false,\n      "description": "If true, re-initializes the RNG to the same seed for every parameter combination, enabling fair stochastic comparison across combinations.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "parameters",\n    "outcome_variables",\n    "optimization_function"\n  ],\n  "type": "object"\n}\n\nNotes:\nMUTUAL EXCLUSION: specifying both `data` and `objective_function` raises an error — use `data` for fitting mode and `objective_function` for optimization mode; omitting both silently defaults to grid_search with no objective.\n\nPARAMETERS KEYS: must be Python (param_name, mechanism) tuples, not plain strings. JSON encodes these as 2-element arrays but the tool call must reconstruct them as tuples before passing to the constructor.\n\nOUTCOME VARIABLES CONSTRAINT: must be a subset of the *terminal* Mechanism\'s output ports in the model; referencing output ports from non-terminal nodes raises a KeyError at construction time.\n\nNUM_TRIALS_PER_ESTIMATE vs NUM_TRIALS: `num_trials_per_estimate` controls trials *within* each parameter combination\'s simulation run; `num_trials` in `.run()` controls how many full estimation passes the PEC itself performs.\n\nCONTROLLER: the `controller` kwarg is forbidden — PEC constructs its own OptimizationControlMechanism internally; passing it raises ValueError.\n\nDEPENDS_ON: triggers per-condition parameter estimation; each unique value in the referenced DataFrame column becomes a separate estimated parameter. Warn if a column has more than 5 unique values (exponential parameter blowup).\n\nLIKELIHOOD_INCLUDE_MASK: an undocumented boolean numpy array parameter (`likelihood_include_mask`, same length as `data`) that masks which rows contribute to the likelihood during fitting. Useful for hold-out evaluation.\n\nPOST-RUN RESULTS: after `.run()`, `optimized_parameter_values` is a plain dict keyed by parameter name strings (not the original (name, mech) tuples); `optimal_value` is the scalar objective score for those values.'
TOOL_PARAMETERS = { 'properties': { 'data': { 'description': 'pandas DataFrame of observed data for '
                                           'data-fitting mode. Each column must '
                                           'correspond to one outcome_variable in the '
                                           'same order. Mutually exclusive with '
                                           'objective_function.',
                            'type': 'object'},
                  'data_categorical_dims': { 'description': 'Marks which data '
                                                            'dimensions are '
                                                            'categorical. Provide a '
                                                            'list of booleans (mask, '
                                                            'same length as data '
                                                            'columns) or a list of '
                                                            'integer column indices. '
                                                            'Overridden automatically '
                                                            'by pandas Categorical '
                                                            'dtype columns. If None, '
                                                            'all dimensions are '
                                                            'treated as continuous.',
                                             'oneOf': [ { 'items': {'type': 'boolean'},
                                                          'type': 'array'},
                                                        { 'items': {'type': 'integer'},
                                                          'type': 'array'}]},
                  'depends_on': { 'description': 'Maps parameter keys (matching keys '
                                                 'in `parameters`) to column names in '
                                                 'the data DataFrame. Each unique '
                                                 'categorical value in that column '
                                                 'becomes its own condition with a '
                                                 'separately estimated parameter. '
                                                 'Requires data to be a pandas '
                                                 'DataFrame with categorical or string '
                                                 'columns.',
                                  'type': 'object'},
                  'initial_seed': { 'description': 'Seed for the random number '
                                                   'generator at construction, '
                                                   'forwarded to the internal '
                                                   'OptimizationControlMechanism. Use '
                                                   'for reproducible results.',
                                    'type': 'integer'},
                  'model': { 'description': 'External Composition whose parameters are '
                                            'estimated. If omitted, pass '
                                            'nodes/pathways kwargs to build the model '
                                            'inline; PEC wraps it internally.',
                             'type': 'object'},
                  'name': { 'description': 'Optional name for the '
                                           'ParameterEstimationComposition instance.',
                            'type': 'string'},
                  'num_estimates': { 'default': 1,
                                     'description': 'Number of stochastic simulation '
                                                    'runs per parameter combination. '
                                                    'Increase to reduce Monte Carlo '
                                                    'variance at the cost of runtime.',
                                     'minimum': 1,
                                     'type': 'integer'},
                  'num_trials_per_estimate': { 'description': 'Exact number of trials '
                                                              'executed per model run '
                                                              'during estimation. If '
                                                              'None and data is '
                                                              'provided, automatically '
                                                              'set to len(data). '
                                                              'Distinct from '
                                                              'num_trials in .run(), '
                                                              'which controls how many '
                                                              'full fits are '
                                                              'performed.',
                                               'type': 'integer'},
                  'objective_function': { 'description': 'Callable for optimization '
                                                         'mode; receives an array of '
                                                         'outcome_variable values and '
                                                         'returns a scalar. Input '
                                                         'shape must match the '
                                                         'concatenated values of '
                                                         'outcome_variables. Mutually '
                                                         'exclusive with data.',
                                          'type': 'object'},
                  'optimization_function': { 'description': 'Search strategy over '
                                                            'parameter combinations. '
                                                            "Pass 'grid_search' for "
                                                            'exhaustive enumeration, '
                                                            "'differential_evolution' "
                                                            'for global stochastic '
                                                            'optimization, or a '
                                                            'PECOptimizationFunction '
                                                            'instance. Omitting raises '
                                                            'a warning and defaults to '
                                                            'grid_search.',
                                             'oneOf': [ { 'enum': [ 'grid_search',
                                                                    'differential_evolution'],
                                                          'type': 'string'},
                                                        { 'description': 'A '
                                                                         'PECOptimizationFunction '
                                                                         'instance',
                                                          'type': 'object'}]},
                  'outcome_variables': { 'description': 'List of OUTPUT Mechanism or '
                                                        'OutputPort objects from the '
                                                        'model whose values are '
                                                        'compared to data (fitting) or '
                                                        'scored by the objective '
                                                        'function (optimization). Must '
                                                        'be a subset of the terminal '
                                                        "Mechanism's output ports in "
                                                        'the model.',
                                         'items': {},
                                         'type': 'array'},
                  'parameters': { 'description': 'Maps each parameter-to-estimate to a '
                                                 'list of candidate values. Keys must '
                                                 'be (param_name, mechanism) Python '
                                                 'tuples (encode as 2-element JSON '
                                                 'arrays); values are arrays of '
                                                 'numbers to sample. Example: '
                                                 '{("drift_rate", my_ddm): [0.1, 0.2, '
                                                 '0.3]}.',
                                  'type': 'object'},
                  'same_seed_for_all_parameter_combinations': { 'default': False,
                                                                'description': 'If '
                                                                               'true, '
                                                                               're-initializes '
                                                                               'the '
                                                                               'RNG to '
                                                                               'the '
                                                                               'same '
                                                                               'seed '
                                                                               'for '
                                                                               'every '
                                                                               'parameter '
                                                                               'combination, '
                                                                               'enabling '
                                                                               'fair '
                                                                               'stochastic '
                                                                               'comparison '
                                                                               'across '
                                                                               'combinations.',
                                                                'type': 'boolean'}},
  'required': ['parameters', 'outcome_variables', 'optimization_function'],
  'type': 'object'}
TOOL_NOTES = "MUTUAL EXCLUSION: specifying both `data` and `objective_function` raises an error — use `data` for fitting mode and `objective_function` for optimization mode; omitting both silently defaults to grid_search with no objective.\n\nPARAMETERS KEYS: must be Python (param_name, mechanism) tuples, not plain strings. JSON encodes these as 2-element arrays but the tool call must reconstruct them as tuples before passing to the constructor.\n\nOUTCOME VARIABLES CONSTRAINT: must be a subset of the *terminal* Mechanism's output ports in the model; referencing output ports from non-terminal nodes raises a KeyError at construction time.\n\nNUM_TRIALS_PER_ESTIMATE vs NUM_TRIALS: `num_trials_per_estimate` controls trials *within* each parameter combination's simulation run; `num_trials` in `.run()` controls how many full estimation passes the PEC itself performs.\n\nCONTROLLER: the `controller` kwarg is forbidden — PEC constructs its own OptimizationControlMechanism internally; passing it raises ValueError.\n\nDEPENDS_ON: triggers per-condition parameter estimation; each unique value in the referenced DataFrame column becomes a separate estimated parameter. Warn if a column has more than 5 unique values (exponential parameter blowup).\n\nLIKELIHOOD_INCLUDE_MASK: an undocumented boolean numpy array parameter (`likelihood_include_mask`, same length as `data`) that masks which rows contribute to the likelihood during fitting. Useful for hold-out evaluation.\n\nPOST-RUN RESULTS: after `.run()`, `optimized_parameter_values` is a plain dict keyed by parameter name strings (not the original (name, mech) tuples); `optimal_value` is the scalar objective score for those values."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ParameterEstimationComposition
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
    def create_parameter_estimation_composition(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to construct a ParameterEstimationComposition when you need to fit a PsyNeuLink model's parameters to observed behavioral data via maximum likelihood estimation, or to optimize parameters to maximize/minimize a custom objective function."
        return _impl(args or {})
