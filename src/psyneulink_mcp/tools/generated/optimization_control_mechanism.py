"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '743b1a727fe7282ee247d17de24ec07ecd35876c4fd5e4e6255b506bf713d47e'
__pnl_qualname__ = 'psyneulink.OptimizationControlMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_optimization_control_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create an OptimizationControlMechanism (OCM) that searches over control allocations to maximize a Composition\'s net outcome. Use it when you need model-based adaptive control — the returned object is typically passed as the `controller` argument of a `Composition`. If `agent_rep` is omitted, the OCM enters deferred init and auto-assigns itself when later set as a Composition\'s controller.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "agent_rep": {\n      "description": "Name of the Composition to simulate during optimization. Omit to defer initialization until assigned as a Composition\'s controller (most common usage).",\n      "type": "string"\n    },\n    "combine_costs": {\n      "default": "np.sum",\n      "description": "Name of the function used to combine costs from all ControlSignals into a scalar total cost. Defaults to np.sum.",\n      "type": "string"\n    },\n    "compute_net_outcome": {\n      "description": "Name of a function (outcome, cost) -> scalar used to compute net_outcome. Defaults to outcome - cost.",\n      "type": "string"\n    },\n    "compute_reconfiguration_cost": {\n      "description": "Name of a function to compute the cost of changing from the current to the proposed control allocation.",\n      "type": "string"\n    },\n    "control_signals": {\n      "description": "List of ControlSignal specification dicts defining the parameters to optimize and their search ranges.",\n      "items": {\n        "description": "ControlSignal specification dict with keys like \'name\', \'modulates\', \'allocation_samples\', \'cost_options\', \'intensity_cost_function\', \'adjustment_cost_function\', \'duration_cost_function\'.",\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "function": {\n      "default": "GridSearch",\n      "description": "Name of the OptimizationFunction class used to search over control allocations (e.g., \'GridSearch\', \'GradientOptimization\', \'BayesGlmFit\'). Defaults to GridSearch.",\n      "enum": [\n        "GridSearch",\n        "GradientOptimization",\n        "BayesGlmFit"\n      ],\n      "type": "string"\n    },\n    "initial_seed": {\n      "description": "Seed to initialize the random number generator at construction. If omitted, a random seed is used (runs will differ). Specify for reproducible optimization.",\n      "type": "integer"\n    },\n    "modulation": {\n      "default": "MULTIPLICATIVE",\n      "description": "Default modulation type for all ControlSignals.",\n      "enum": [\n        "MULTIPLICATIVE",\n        "ADDITIVE",\n        "OVERRIDE",\n        "DISABLE"\n      ],\n      "type": "string"\n    },\n    "monitor_for_control": {\n      "description": "Names of Mechanism OutputPorts whose values are used to compute net_outcome. Alternative to specifying an objective_mechanism.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the OptimizationControlMechanism instance.",\n      "type": "string"\n    },\n    "num_estimates": {\n      "description": "Number of independent agent_rep evaluations per control allocation, each using a different random seed. Enables stochastic estimation. Requires agent_rep to have random variables; ignored (with warning) if none exist.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "num_trials_per_estimate": {\n      "description": "Fixed number of trials per agent_rep evaluation run. If null (default), uses the number of inputs or num_trials from the parent Composition\'s run() call.",\n      "type": "integer"\n    },\n    "objective_mechanism": {\n      "description": "Name of an ObjectiveMechanism to monitor; its output determines the outcome used for optimization. If omitted, monitor_for_control is used directly.",\n      "type": "string"\n    },\n    "random_variables": {\n      "description": "Names of Parameters in agent_rep with random variables (seed attributes) to randomize across num_estimates runs. Defaults to ALL randomizable parameters.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "return_results": {\n      "default": false,\n      "description": "If true, evaluate_agent_rep returns full simulation results alongside net_outcome. Required for ParameterEstimationComposition data fitting.",\n      "type": "boolean"\n    },\n    "same_seed_for_all_allocations": {\n      "default": false,\n      "description": "If true, re-initializes the RNG to the same value for each control allocation\'s estimates, isolating the effect of the allocation from intrinsic Composition variability.",\n      "type": "boolean"\n    },\n    "search_function": {\n      "description": "Name of a custom search function to assign to the optimization function\'s search_function parameter. Must accept (control_allocation_array, iteration_int) and return a control_allocation array.",\n      "type": "string"\n    },\n    "search_space": {\n      "description": "Search space for the optimization function. Each element corresponds to one control signal\'s allocation dimension. Overrides allocation_samples from individual control signals.",\n      "items": {\n        "oneOf": [\n          {\n            "description": "SampleSpec dict with \'start\', \'stop\', \'step\' or \'num\' keys",\n            "type": "object"\n          },\n          {\n            "description": "Explicit list of values to sample",\n            "type": "array"\n          }\n        ]\n      },\n      "type": "array"\n    },\n    "search_statefulness": {\n      "default": true,\n      "description": "If true (default), each evaluate_agent_rep call runs in its own execution context (isolated simulation). Set false only for stateless agent_reps.",\n      "type": "boolean"\n    },\n    "search_termination_function": {\n      "description": "Name of a custom termination function for the optimization loop. Must accept (control_allocation_array, net_outcome_int, iteration_int) and return True/False.",\n      "type": "string"\n    },\n    "state_feature_default": {\n      "description": "Default state feature source for INPUT nodes not explicitly listed in state_features. \'SHADOW_INPUTS\' (default) shadows each node\'s actual input; null means use the node\'s default_variable.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "state_feature_function": {\n      "description": "Name of the PsyNeuLink Function class to apply by default to all state_input_ports (e.g., \'LinearCombination\', \'ExponentialDist\'). Applied to each state feature\'s InputPort unless overridden per-feature.",\n      "type": "string"\n    },\n    "state_features": {\n      "description": "Sources of input for agent_rep\'s INPUT nodes during evaluation. \'SHADOW_INPUTS\' (default) mirrors the Composition\'s actual trial inputs. Can also be a list of component names (ordered by INPUT node), a dict mapping INPUT node names to sources, or a set of INPUT node names to shadow.",\n      "oneOf": [\n        {\n          "enum": [\n            "SHADOW_INPUTS"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- Omitting `agent_rep` is the standard pattern: create the OCM without it, then pass it as `controller=ocm` to a Composition, which auto-assigns itself as `agent_rep`.\n- The constructor parameter for reproducible cross-allocation comparisons is `same_seed_for_all_allocations` (not `same_seed_for_all_parameter_combinations` as shown in the class-level docstring signature — that name is outdated).\n- `num_estimates` is silently set to None (with a warning) if `agent_rep` has no random variables; do not specify it in that case.\n- `state_features` defaults to `SHADOW_INPUTS`, which automatically mirrors the Composition\'s actual input on each trial. This is usually correct; only override when you want the OCM to evaluate with different or preprocessed inputs.\n- `control_signals` each need `allocation_samples` specified (via SampleSpec or explicit list) to define the search space for that parameter; without this, GridSearch has nothing to iterate over.\n- `search_space` at the OCM level overrides `allocation_samples` on individual ControlSignals — use one or the other, not both.\n- If `num_estimates` is set, a `RANDOMIZATION_CONTROL_SIGNAL` is automatically added to `control_signals` to manage seed randomization; account for this when indexing `control_signals`.\n- The deprecated kwargs `features` and `feature_function` still work but emit deprecation warnings; use `state_features` and `state_feature_function` instead.'
TOOL_PARAMETERS = { 'properties': { 'agent_rep': { 'description': 'Name of the Composition to simulate '
                                                'during optimization. Omit to defer '
                                                'initialization until assigned as a '
                                                "Composition's controller (most common "
                                                'usage).',
                                 'type': 'string'},
                  'combine_costs': { 'default': 'np.sum',
                                     'description': 'Name of the function used to '
                                                    'combine costs from all '
                                                    'ControlSignals into a scalar '
                                                    'total cost. Defaults to np.sum.',
                                     'type': 'string'},
                  'compute_net_outcome': { 'description': 'Name of a function '
                                                          '(outcome, cost) -> scalar '
                                                          'used to compute '
                                                          'net_outcome. Defaults to '
                                                          'outcome - cost.',
                                           'type': 'string'},
                  'compute_reconfiguration_cost': { 'description': 'Name of a function '
                                                                   'to compute the '
                                                                   'cost of changing '
                                                                   'from the current '
                                                                   'to the proposed '
                                                                   'control '
                                                                   'allocation.',
                                                    'type': 'string'},
                  'control_signals': { 'description': 'List of ControlSignal '
                                                      'specification dicts defining '
                                                      'the parameters to optimize and '
                                                      'their search ranges.',
                                       'items': { 'description': 'ControlSignal '
                                                                 'specification dict '
                                                                 'with keys like '
                                                                 "'name', 'modulates', "
                                                                 "'allocation_samples', "
                                                                 "'cost_options', "
                                                                 "'intensity_cost_function', "
                                                                 "'adjustment_cost_function', "
                                                                 "'duration_cost_function'.",
                                                  'type': 'object'},
                                       'type': 'array'},
                  'function': { 'default': 'GridSearch',
                                'description': 'Name of the OptimizationFunction class '
                                               'used to search over control '
                                               "allocations (e.g., 'GridSearch', "
                                               "'GradientOptimization', "
                                               "'BayesGlmFit'). Defaults to "
                                               'GridSearch.',
                                'enum': [ 'GridSearch',
                                          'GradientOptimization',
                                          'BayesGlmFit'],
                                'type': 'string'},
                  'initial_seed': { 'description': 'Seed to initialize the random '
                                                   'number generator at construction. '
                                                   'If omitted, a random seed is used '
                                                   '(runs will differ). Specify for '
                                                   'reproducible optimization.',
                                    'type': 'integer'},
                  'modulation': { 'default': 'MULTIPLICATIVE',
                                  'description': 'Default modulation type for all '
                                                 'ControlSignals.',
                                  'enum': [ 'MULTIPLICATIVE',
                                            'ADDITIVE',
                                            'OVERRIDE',
                                            'DISABLE'],
                                  'type': 'string'},
                  'monitor_for_control': { 'description': 'Names of Mechanism '
                                                          'OutputPorts whose values '
                                                          'are used to compute '
                                                          'net_outcome. Alternative to '
                                                          'specifying an '
                                                          'objective_mechanism.',
                                           'items': {'type': 'string'},
                                           'type': 'array'},
                  'name': { 'description': 'Optional name for the '
                                           'OptimizationControlMechanism instance.',
                            'type': 'string'},
                  'num_estimates': { 'description': 'Number of independent agent_rep '
                                                    'evaluations per control '
                                                    'allocation, each using a '
                                                    'different random seed. Enables '
                                                    'stochastic estimation. Requires '
                                                    'agent_rep to have random '
                                                    'variables; ignored (with warning) '
                                                    'if none exist.',
                                     'minimum': 1,
                                     'type': 'integer'},
                  'num_trials_per_estimate': { 'description': 'Fixed number of trials '
                                                              'per agent_rep '
                                                              'evaluation run. If null '
                                                              '(default), uses the '
                                                              'number of inputs or '
                                                              'num_trials from the '
                                                              "parent Composition's "
                                                              'run() call.',
                                               'type': 'integer'},
                  'objective_mechanism': { 'description': 'Name of an '
                                                          'ObjectiveMechanism to '
                                                          'monitor; its output '
                                                          'determines the outcome used '
                                                          'for optimization. If '
                                                          'omitted, '
                                                          'monitor_for_control is used '
                                                          'directly.',
                                           'type': 'string'},
                  'random_variables': { 'description': 'Names of Parameters in '
                                                       'agent_rep with random '
                                                       'variables (seed attributes) to '
                                                       'randomize across num_estimates '
                                                       'runs. Defaults to ALL '
                                                       'randomizable parameters.',
                                        'items': {'type': 'string'},
                                        'type': 'array'},
                  'return_results': { 'default': False,
                                      'description': 'If true, evaluate_agent_rep '
                                                     'returns full simulation results '
                                                     'alongside net_outcome. Required '
                                                     'for '
                                                     'ParameterEstimationComposition '
                                                     'data fitting.',
                                      'type': 'boolean'},
                  'same_seed_for_all_allocations': { 'default': False,
                                                     'description': 'If true, '
                                                                    're-initializes '
                                                                    'the RNG to the '
                                                                    'same value for '
                                                                    'each control '
                                                                    "allocation's "
                                                                    'estimates, '
                                                                    'isolating the '
                                                                    'effect of the '
                                                                    'allocation from '
                                                                    'intrinsic '
                                                                    'Composition '
                                                                    'variability.',
                                                     'type': 'boolean'},
                  'search_function': { 'description': 'Name of a custom search '
                                                      'function to assign to the '
                                                      "optimization function's "
                                                      'search_function parameter. Must '
                                                      'accept '
                                                      '(control_allocation_array, '
                                                      'iteration_int) and return a '
                                                      'control_allocation array.',
                                       'type': 'string'},
                  'search_space': { 'description': 'Search space for the optimization '
                                                   'function. Each element corresponds '
                                                   "to one control signal's allocation "
                                                   'dimension. Overrides '
                                                   'allocation_samples from individual '
                                                   'control signals.',
                                    'items': { 'oneOf': [ { 'description': 'SampleSpec '
                                                                           'dict with '
                                                                           "'start', "
                                                                           "'stop', "
                                                                           "'step' or "
                                                                           "'num' keys",
                                                            'type': 'object'},
                                                          { 'description': 'Explicit '
                                                                           'list of '
                                                                           'values to '
                                                                           'sample',
                                                            'type': 'array'}]},
                                    'type': 'array'},
                  'search_statefulness': { 'default': True,
                                           'description': 'If true (default), each '
                                                          'evaluate_agent_rep call '
                                                          'runs in its own execution '
                                                          'context (isolated '
                                                          'simulation). Set false only '
                                                          'for stateless agent_reps.',
                                           'type': 'boolean'},
                  'search_termination_function': { 'description': 'Name of a custom '
                                                                  'termination '
                                                                  'function for the '
                                                                  'optimization loop. '
                                                                  'Must accept '
                                                                  '(control_allocation_array, '
                                                                  'net_outcome_int, '
                                                                  'iteration_int) and '
                                                                  'return True/False.',
                                                   'type': 'string'},
                  'state_feature_default': { 'description': 'Default state feature '
                                                            'source for INPUT nodes '
                                                            'not explicitly listed in '
                                                            'state_features. '
                                                            "'SHADOW_INPUTS' (default) "
                                                            "shadows each node's "
                                                            'actual input; null means '
                                                            "use the node's "
                                                            'default_variable.',
                                             'oneOf': [ {'type': 'string'},
                                                        {'type': 'null'}]},
                  'state_feature_function': { 'description': 'Name of the PsyNeuLink '
                                                             'Function class to apply '
                                                             'by default to all '
                                                             'state_input_ports (e.g., '
                                                             "'LinearCombination', "
                                                             "'ExponentialDist'). "
                                                             'Applied to each state '
                                                             "feature's InputPort "
                                                             'unless overridden '
                                                             'per-feature.',
                                              'type': 'string'},
                  'state_features': { 'description': "Sources of input for agent_rep's "
                                                     'INPUT nodes during evaluation. '
                                                     "'SHADOW_INPUTS' (default) "
                                                     "mirrors the Composition's actual "
                                                     'trial inputs. Can also be a list '
                                                     'of component names (ordered by '
                                                     'INPUT node), a dict mapping '
                                                     'INPUT node names to sources, or '
                                                     'a set of INPUT node names to '
                                                     'shadow.',
                                      'oneOf': [ { 'enum': ['SHADOW_INPUTS'],
                                                   'type': 'string'},
                                                 { 'items': {'type': 'string'},
                                                   'type': 'array'},
                                                 {'type': 'object'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- Omitting `agent_rep` is the standard pattern: create the OCM without it, then pass it as `controller=ocm` to a Composition, which auto-assigns itself as `agent_rep`.\n- The constructor parameter for reproducible cross-allocation comparisons is `same_seed_for_all_allocations` (not `same_seed_for_all_parameter_combinations` as shown in the class-level docstring signature — that name is outdated).\n- `num_estimates` is silently set to None (with a warning) if `agent_rep` has no random variables; do not specify it in that case.\n- `state_features` defaults to `SHADOW_INPUTS`, which automatically mirrors the Composition's actual input on each trial. This is usually correct; only override when you want the OCM to evaluate with different or preprocessed inputs.\n- `control_signals` each need `allocation_samples` specified (via SampleSpec or explicit list) to define the search space for that parameter; without this, GridSearch has nothing to iterate over.\n- `search_space` at the OCM level overrides `allocation_samples` on individual ControlSignals — use one or the other, not both.\n- If `num_estimates` is set, a `RANDOMIZATION_CONTROL_SIGNAL` is automatically added to `control_signals` to manage seed randomization; account for this when indexing `control_signals`.\n- The deprecated kwargs `features` and `feature_function` still work but emit deprecation warnings; use `state_features` and `state_feature_function` instead."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.OptimizationControlMechanism
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
    def create_optimization_control_mechanism(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to create an OptimizationControlMechanism (OCM) that searches over control allocations to maximize a Composition's net outcome."
        return _impl(args or {})
