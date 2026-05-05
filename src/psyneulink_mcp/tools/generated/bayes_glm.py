"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '942ddea3b6344b0c868d46a8214a27a8a93d93de0651c209639260fbcdb65a6e'
__pnl_qualname__ = 'psyneulink.BayesGLM'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_bayes_glm'
TOOL_DESCRIPTION = 'Call this tool to create a BayesGLM learning function that performs Bayesian linear regression to incrementally update prediction weight distributions. Use it when you need a mechanism\'s learning function to maintain and sample from a normal-gamma posterior over weights, updating beliefs online as new predictor/target pairs arrive. Returns a 1D array of sampled prediction weights drawn from the updated posterior.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "3D array with two items: [0] a 2D array of predictor vectors (shape: n_samples \\u00d7 n_predictors), [1] a 2D array of scalar dependent variables (shape: n_samples \\u00d7 1). If omitted, shape is inferred from mu_0 or sigma_0, or from the first function call.",\n      "items": {\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "gamma_shape_0": {\n      "description": "Initial shape parameter of the gamma distribution used to sample prediction weights. Passed as numpy.random.gamma shape/2. Default: 1.",\n      "type": "number"\n    },\n    "gamma_size_0": {\n      "description": "Initial size (scale) parameter of the gamma distribution used to sample prediction weights. Passed as numpy.random.gamma size/2. Default: 1.",\n      "type": "number"\n    },\n    "mu_0": {\n      "description": "Initial prior mean(s) for the prediction weight distribution. Scalar applies the same value to all weights; 1D array sets per-weight priors and also determines the number of predictors if default_variable is omitted. Default: 0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the BayesGLM function instance.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter names, values override defaults.",\n      "type": "object"\n    },\n    "seed": {\n      "description": "Optional random seed for reproducible weight sampling.",\n      "type": "integer"\n    },\n    "sigma_0": {\n      "description": "Initial prior standard deviation(s) for the prediction weight distribution. Used to compute Lambda_prior (precision matrix) as (1/sigma_0^2)*I. Scalar or 1D array; also determines predictor count if neither default_variable nor mu_0 is specified. Default: 1.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The function updates weight distributions online: each call to function() treats the previous posterior as the new prior, so calling order matters.\n- default_variable[0] must be 2D (n_samples × n_predictors); default_variable[1] must be 2D (n_samples × 1) containing scalar targets — passing 1D arrays will cause dimension errors.\n- If you specify both mu_0 and sigma_0 as arrays, they must be the same length; a mismatch raises FunctionError before any computation.\n- gamma_shape_0 and gamma_size_0 reset to their default values each call (not propagated across calls like mu_n/Lambda_n); only mu_n and Lambda_n accumulate online updates.\n- sigma_0 controls Lambda_prior (precision), not the covariance directly: Lambda_0 = (1/sigma_0²) * I.\n- The returned weights_sample is stochastic; set seed for reproducibility in tests or comparisons.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '3D array with two items: [0] a '
                                                       '2D array of predictor vectors '
                                                       '(shape: n_samples × '
                                                       'n_predictors), [1] a 2D array '
                                                       'of scalar dependent variables '
                                                       '(shape: n_samples × 1). If '
                                                       'omitted, shape is inferred '
                                                       'from mu_0 or sigma_0, or from '
                                                       'the first function call.',
                                        'items': {'type': 'array'},
                                        'type': 'array'},
                  'gamma_shape_0': { 'description': 'Initial shape parameter of the '
                                                    'gamma distribution used to sample '
                                                    'prediction weights. Passed as '
                                                    'numpy.random.gamma shape/2. '
                                                    'Default: 1.',
                                     'type': 'number'},
                  'gamma_size_0': { 'description': 'Initial size (scale) parameter of '
                                                   'the gamma distribution used to '
                                                   'sample prediction weights. Passed '
                                                   'as numpy.random.gamma size/2. '
                                                   'Default: 1.',
                                    'type': 'number'},
                  'mu_0': { 'description': 'Initial prior mean(s) for the prediction '
                                           'weight distribution. Scalar applies the '
                                           'same value to all weights; 1D array sets '
                                           'per-weight priors and also determines the '
                                           'number of predictors if default_variable '
                                           'is omitted. Default: 0.',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'name': { 'description': 'Optional name for the BayesGLM function '
                                           'instance.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter names, values override '
                                             'defaults.',
                              'type': 'object'},
                  'seed': { 'description': 'Optional random seed for reproducible '
                                           'weight sampling.',
                            'type': 'integer'},
                  'sigma_0': { 'description': 'Initial prior standard deviation(s) for '
                                              'the prediction weight distribution. '
                                              'Used to compute Lambda_prior (precision '
                                              'matrix) as (1/sigma_0^2)*I. Scalar or '
                                              '1D array; also determines predictor '
                                              'count if neither default_variable nor '
                                              'mu_0 is specified. Default: 1.',
                               'oneOf': [ {'type': 'number'},
                                          { 'items': {'type': 'number'},
                                            'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The function updates weight distributions online: each call to function() treats the previous posterior as the new prior, so calling order matters.\n- default_variable[0] must be 2D (n_samples × n_predictors); default_variable[1] must be 2D (n_samples × 1) containing scalar targets — passing 1D arrays will cause dimension errors.\n- If you specify both mu_0 and sigma_0 as arrays, they must be the same length; a mismatch raises FunctionError before any computation.\n- gamma_shape_0 and gamma_size_0 reset to their default values each call (not propagated across calls like mu_n/Lambda_n); only mu_n and Lambda_n accumulate online updates.\n- sigma_0 controls Lambda_prior (precision), not the covariance directly: Lambda_0 = (1/sigma_0²) * I.\n- The returned weights_sample is stochastic; set seed for reproducibility in tests or comparisons.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.BayesGLM
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
    def create_bayes_glm(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a BayesGLM learning function that performs Bayesian linear regression to incrementally update prediction weight distributions.'
        return _impl(args or {})
