"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'da85b620c841154fe6068bf170dae92ea068c0ba402d11ab7acad913e77ad323'
__pnl_qualname__ = 'psyneulink.BackPropagation'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_back_propagation'
TOOL_DESCRIPTION = 'Use this tool to instantiate a BackPropagation learning function when configuring a LearningMechanism to train connection weights via the generalized delta rule. Call it to attach a backprop function to a LearningMechanism\'s `function` parameter, specifying the activation derivative and learning rate; the result is a BackPropagation Function object that computes weight_change_matrix and a weighted error signal each time the mechanism executes.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "activation_derivative_fct": {\n      "description": "Python expression string for the derivative of the activation function generating activation_output (e.g., \'psyneulink.Logistic().derivative\', \'psyneulink.ReLU().derivative\'). Defaults to Logistic().derivative.",\n      "type": "string"\n    },\n    "covariates": {\n      "description": "Template (shape only) for extra arguments required by activation_derivative_fct beyond activation_input and activation_output. Provide only when the activation derivative takes additional keyword arguments.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "default_variable": {\n      "description": "Template for the three input arrays: [[activation_input], [activation_output], [error_signal]]. Must have exactly 3 rows. Defaults to [[0],[0],[0]].",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "learning_rate": {\n      "description": "Scalar multiplier applied to the weight change matrix. If omitted, inherits from the owning LearningMechanism or Composition; falls back to the function-class default.",\n      "type": "number"\n    },\n    "loss_spec": {\n      "description": "Loss function used to scale the error derivative before computing weight changes. \'MSE\' divides by number of output units and multiplies by 2; \'SSE\' multiplies by 2; omit or use \'L0\' for the standard dot-product (used for hidden layers).",\n      "enum": [\n        "MSE",\n        "SSE",\n        "L0"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for this BackPropagation function instance.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nerror_matrix is NOT a constructor argument — it must be supplied at call time via the params dict passed to the LearningMechanism\'s _function method. Omitting it during normal (non-initializing) execution raises FunctionError. The variable layout is strictly ordered: index 0 = activation_input, index 1 = activation_output, index 2 = error_signal; wrong ordering silently produces incorrect weight updates. loss_spec should be set to \'MSE\' or \'SSE\' only for the output layer; hidden layers should leave it None/L0. When covariates are needed, provide only a shape template in the constructor and actual values at call time via params. The function returns a list of two arrays: [weight_change_matrix (2d), weighted_error_signal (1d)], not a single array.'
TOOL_PARAMETERS = { 'properties': { 'activation_derivative_fct': { 'description': 'Python expression '
                                                                'string for the '
                                                                'derivative of the '
                                                                'activation function '
                                                                'generating '
                                                                'activation_output '
                                                                '(e.g., '
                                                                "'psyneulink.Logistic().derivative', "
                                                                "'psyneulink.ReLU().derivative'). "
                                                                'Defaults to '
                                                                'Logistic().derivative.',
                                                 'type': 'string'},
                  'covariates': { 'description': 'Template (shape only) for extra '
                                                 'arguments required by '
                                                 'activation_derivative_fct beyond '
                                                 'activation_input and '
                                                 'activation_output. Provide only when '
                                                 'the activation derivative takes '
                                                 'additional keyword arguments.',
                                  'items': { 'items': {'type': 'number'},
                                             'type': 'array'},
                                  'type': 'array'},
                  'default_variable': { 'description': 'Template for the three input '
                                                       'arrays: [[activation_input], '
                                                       '[activation_output], '
                                                       '[error_signal]]. Must have '
                                                       'exactly 3 rows. Defaults to '
                                                       '[[0],[0],[0]].',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'learning_rate': { 'description': 'Scalar multiplier applied to the '
                                                    'weight change matrix. If omitted, '
                                                    'inherits from the owning '
                                                    'LearningMechanism or Composition; '
                                                    'falls back to the function-class '
                                                    'default.',
                                     'type': 'number'},
                  'loss_spec': { 'description': 'Loss function used to scale the error '
                                                'derivative before computing weight '
                                                "changes. 'MSE' divides by number of "
                                                'output units and multiplies by 2; '
                                                "'SSE' multiplies by 2; omit or use "
                                                "'L0' for the standard dot-product "
                                                '(used for hidden layers).',
                                 'enum': ['MSE', 'SSE', 'L0'],
                                 'type': 'string'},
                  'name': { 'description': 'Optional name for this BackPropagation '
                                           'function instance.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "error_matrix is NOT a constructor argument — it must be supplied at call time via the params dict passed to the LearningMechanism's _function method. Omitting it during normal (non-initializing) execution raises FunctionError. The variable layout is strictly ordered: index 0 = activation_input, index 1 = activation_output, index 2 = error_signal; wrong ordering silently produces incorrect weight updates. loss_spec should be set to 'MSE' or 'SSE' only for the output layer; hidden layers should leave it None/L0. When covariates are needed, provide only a shape template in the constructor and actual values at call time via params. The function returns a list of two arrays: [weight_change_matrix (2d), weighted_error_signal (1d)], not a single array."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.BackPropagation
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
    def create_back_propagation(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to instantiate a BackPropagation learning function when configuring a LearningMechanism to train connection weights via the generalized delta rule.'
        return _impl(args or {})
