"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6dd511463825ab750873111bbe9a97bad41947aa3a1231da5c234bbfc7d2405d'
__pnl_qualname__ = 'psyneulink.RecurrentTransferMechanism'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_recurrent_transfer_mechanism'
TOOL_DESCRIPTION = 'Use this tool to create a RecurrentTransferMechanism — a single-layer auto-recurrent neural network node that feeds its own output back as input via a weighted self-projection. Call it when modeling attractor dynamics, working memory, competitive inhibition (e.g., lateral inhibition with negative hetero), or any network requiring recurrent connectivity. Returns a configured RecurrentTransferMechanism instance ready to add to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "auto": {\n      "description": "Value(s) for the diagonal of the recurrent matrix (self-connections). A scalar applies uniformly; a 1D array of length input_shapes sets a non-uniform diagonal. If both auto and hetero are given, the final matrix = auto_diag + hetero_offdiag.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "clip": {\n      "description": "Two-element [min, max] range to clip output values. E.g. [0, 1] for a unit interval.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "combination_function": {\n      "default": "LinearCombination",\n      "description": "Name of the function used to combine RECURRENT and EXTERNAL InputPorts when has_recurrent_input_port is true. Default is \'LinearCombination\' (simple addition).",\n      "type": "string"\n    },\n    "default_variable": {\n      "description": "Default input vector. Use input_shapes for simple size specification instead.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "enable_learning": {\n      "default": false,\n      "description": "If true, configures the mechanism for Hebbian learning on its recurrent projection at construction time. If false (default), learning can be enabled later by calling configure_learning().",\n      "type": "boolean"\n    },\n    "function": {\n      "description": "Transfer function applied to the (combined) input. Common values: \'Linear\', \'Logistic\', \'ReLU\', \'Tanh\'. Inherited from TransferMechanism.",\n      "type": "string"\n    },\n    "has_recurrent_input_port": {\n      "default": false,\n      "description": "If true, recurrent input arrives at a separate InputPort (named RECURRENT) and is combined with external input via combination_function before passing to the transfer function. If false (default), recurrent input is added directly to the primary InputPort.",\n      "type": "boolean"\n    },\n    "hetero": {\n      "description": "Value(s) for the off-diagonal entries of the recurrent matrix (lateral connections). A scalar applies uniformly to all off-diagonal positions; a 2D array of shape [n x n] sets non-uniform lateral weights (diagonal entries are zeroed out). If both auto and hetero are given, the final matrix = auto_diag + hetero_offdiag.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initial_value": {\n      "description": "Initial value for the mechanism\'s output, used when integrator_mode is true.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Size of the input (and recurrent) layer. Equivalent to setting default_variable shape.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "description": "Rate of integration (smoothing factor) when integrator_mode is true. Value between 0 and 1; higher = faster integration. Default is 0.5.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "integrator_function": {\n      "default": "AdaptiveIntegrator",\n      "description": "Function used for temporal integration when integrator_mode is true. Default is \'AdaptiveIntegrator\'.",\n      "type": "string"\n    },\n    "integrator_mode": {\n      "default": false,\n      "description": "If true, output is integrated over time using integrator_function before being passed to the transfer function.",\n      "type": "boolean"\n    },\n    "learning_condition": {\n      "default": "UPDATE",\n      "description": "When the LearningMechanism executes. \'UPDATE\' (default): after every execution of this mechanism. \'CONVERGENCE\': only when termination_threshold is satisfied (WhenFinished condition).",\n      "enum": [\n        "UPDATE",\n        "CONVERGENCE"\n      ],\n      "type": "string"\n    },\n    "learning_function": {\n      "default": "Hebbian",\n      "description": "Name of the learning function for the LearningMechanism. Default is \'Hebbian\'. Only relevant when enable_learning is true.",\n      "type": "string"\n    },\n    "learning_rate": {\n      "description": "Learning rate for the LearningMechanism. Only relevant when enable_learning is true. If null, the LearningMechanism default is used.",\n      "type": "number"\n    },\n    "matrix": {\n      "description": "Recurrent weight matrix. Can be a 2D array (list of lists), or a keyword string such as \'HOLLOW_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'IDENTITY_MATRIX\'. Diagonal terms are overridden by auto if specified; off-diagonal terms are overridden by hetero if specified. Ignored entirely if both auto and hetero are specified.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for the mechanism.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Noise added to the output on each execution. Default is 0.0.",\n      "type": "number"\n    },\n    "output_ports": {\n      "description": "List of output ports to include. Standard options beyond TransferMechanism defaults: \'ENERGY\', \'ENTROPY\'. Default is [\'RESULT\'].",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMatrix precedence rules are non-obvious and critical: (1) if auto AND hetero are both specified, matrix is ignored entirely — final matrix = diagonal(auto) + hollow(hetero); (2) if only auto is specified with matrix, auto overrides the diagonal of matrix; (3) if only hetero is specified with matrix, hetero overrides the off-diagonal of matrix; (4) any non-zero diagonal values in a hetero 2D array are silently zeroed before use. Default matrix is HOLLOW_MATRIX (all zeros, including diagonal), not an identity or full matrix. Learning is completely inert unless enable_learning=True at construction or configure_learning() is called afterward — setting learning_enabled=True on an unconfigured mechanism only raises a warning and is ignored. The recurrent projection is an AutoAssociativeProjection from the mechanism\'s primary OutputPort back to its input; it is automatically added as an aux_component to any Composition the mechanism joins. has_recurrent_input_port=True changes the InputPort topology (adds a separate RECURRENT port and renames the primary port EXTERNAL), which affects how external inputs must be provided. LLVM/compiled execution does not support has_recurrent_input_port=True (combination_function path).'
TOOL_PARAMETERS = { 'properties': { 'auto': { 'description': 'Value(s) for the diagonal of the recurrent '
                                           'matrix (self-connections). A scalar '
                                           'applies uniformly; a 1D array of length '
                                           'input_shapes sets a non-uniform diagonal. '
                                           'If both auto and hetero are given, the '
                                           'final matrix = auto_diag + hetero_offdiag.',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'clip': { 'description': 'Two-element [min, max] range to clip '
                                           'output values. E.g. [0, 1] for a unit '
                                           'interval.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'combination_function': { 'default': 'LinearCombination',
                                            'description': 'Name of the function used '
                                                           'to combine RECURRENT and '
                                                           'EXTERNAL InputPorts when '
                                                           'has_recurrent_input_port '
                                                           'is true. Default is '
                                                           "'LinearCombination' "
                                                           '(simple addition).',
                                            'type': 'string'},
                  'default_variable': { 'description': 'Default input vector. Use '
                                                       'input_shapes for simple size '
                                                       'specification instead.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'enable_learning': { 'default': False,
                                       'description': 'If true, configures the '
                                                      'mechanism for Hebbian learning '
                                                      'on its recurrent projection at '
                                                      'construction time. If false '
                                                      '(default), learning can be '
                                                      'enabled later by calling '
                                                      'configure_learning().',
                                       'type': 'boolean'},
                  'function': { 'description': 'Transfer function applied to the '
                                               '(combined) input. Common values: '
                                               "'Linear', 'Logistic', 'ReLU', 'Tanh'. "
                                               'Inherited from TransferMechanism.',
                                'type': 'string'},
                  'has_recurrent_input_port': { 'default': False,
                                                'description': 'If true, recurrent '
                                                               'input arrives at a '
                                                               'separate InputPort '
                                                               '(named RECURRENT) and '
                                                               'is combined with '
                                                               'external input via '
                                                               'combination_function '
                                                               'before passing to the '
                                                               'transfer function. If '
                                                               'false (default), '
                                                               'recurrent input is '
                                                               'added directly to the '
                                                               'primary InputPort.',
                                                'type': 'boolean'},
                  'hetero': { 'description': 'Value(s) for the off-diagonal entries of '
                                             'the recurrent matrix (lateral '
                                             'connections). A scalar applies uniformly '
                                             'to all off-diagonal positions; a 2D '
                                             'array of shape [n x n] sets non-uniform '
                                             'lateral weights (diagonal entries are '
                                             'zeroed out). If both auto and hetero are '
                                             'given, the final matrix = auto_diag + '
                                             'hetero_offdiag.',
                              'oneOf': [ {'type': 'number'},
                                         { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'}]},
                  'initial_value': { 'description': "Initial value for the mechanism's "
                                                    'output, used when integrator_mode '
                                                    'is true.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Size of the input (and recurrent) '
                                                   'layer. Equivalent to setting '
                                                   'default_variable shape.',
                                    'type': 'integer'},
                  'integration_rate': { 'description': 'Rate of integration (smoothing '
                                                       'factor) when integrator_mode '
                                                       'is true. Value between 0 and '
                                                       '1; higher = faster '
                                                       'integration. Default is 0.5.',
                                        'maximum': 1,
                                        'minimum': 0,
                                        'type': 'number'},
                  'integrator_function': { 'default': 'AdaptiveIntegrator',
                                           'description': 'Function used for temporal '
                                                          'integration when '
                                                          'integrator_mode is true. '
                                                          'Default is '
                                                          "'AdaptiveIntegrator'.",
                                           'type': 'string'},
                  'integrator_mode': { 'default': False,
                                       'description': 'If true, output is integrated '
                                                      'over time using '
                                                      'integrator_function before '
                                                      'being passed to the transfer '
                                                      'function.',
                                       'type': 'boolean'},
                  'learning_condition': { 'default': 'UPDATE',
                                          'description': 'When the LearningMechanism '
                                                         "executes. 'UPDATE' "
                                                         '(default): after every '
                                                         'execution of this mechanism. '
                                                         "'CONVERGENCE': only when "
                                                         'termination_threshold is '
                                                         'satisfied (WhenFinished '
                                                         'condition).',
                                          'enum': ['UPDATE', 'CONVERGENCE'],
                                          'type': 'string'},
                  'learning_function': { 'default': 'Hebbian',
                                         'description': 'Name of the learning function '
                                                        'for the LearningMechanism. '
                                                        "Default is 'Hebbian'. Only "
                                                        'relevant when enable_learning '
                                                        'is true.',
                                         'type': 'string'},
                  'learning_rate': { 'description': 'Learning rate for the '
                                                    'LearningMechanism. Only relevant '
                                                    'when enable_learning is true. If '
                                                    'null, the LearningMechanism '
                                                    'default is used.',
                                     'type': 'number'},
                  'matrix': { 'description': 'Recurrent weight matrix. Can be a 2D '
                                             'array (list of lists), or a keyword '
                                             "string such as 'HOLLOW_MATRIX', "
                                             "'FULL_CONNECTIVITY_MATRIX', "
                                             "'IDENTITY_MATRIX'. Diagonal terms are "
                                             'overridden by auto if specified; '
                                             'off-diagonal terms are overridden by '
                                             'hetero if specified. Ignored entirely if '
                                             'both auto and hetero are specified.',
                              'oneOf': [ {'type': 'string'},
                                         { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'}]},
                  'name': {'description': 'Name for the mechanism.', 'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Noise added to the output on each '
                                            'execution. Default is 0.0.',
                             'type': 'number'},
                  'output_ports': { 'description': 'List of output ports to include. '
                                                   'Standard options beyond '
                                                   'TransferMechanism defaults: '
                                                   "'ENERGY', 'ENTROPY'. Default is "
                                                   "['RESULT'].",
                                    'items': {'type': 'string'},
                                    'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Matrix precedence rules are non-obvious and critical: (1) if auto AND hetero are both specified, matrix is ignored entirely — final matrix = diagonal(auto) + hollow(hetero); (2) if only auto is specified with matrix, auto overrides the diagonal of matrix; (3) if only hetero is specified with matrix, hetero overrides the off-diagonal of matrix; (4) any non-zero diagonal values in a hetero 2D array are silently zeroed before use. Default matrix is HOLLOW_MATRIX (all zeros, including diagonal), not an identity or full matrix. Learning is completely inert unless enable_learning=True at construction or configure_learning() is called afterward — setting learning_enabled=True on an unconfigured mechanism only raises a warning and is ignored. The recurrent projection is an AutoAssociativeProjection from the mechanism's primary OutputPort back to its input; it is automatically added as an aux_component to any Composition the mechanism joins. has_recurrent_input_port=True changes the InputPort topology (adds a separate RECURRENT port and renames the primary port EXTERNAL), which affects how external inputs must be provided. LLVM/compiled execution does not support has_recurrent_input_port=True (combination_function path)."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.RecurrentTransferMechanism
    resolved = handles.resolve_in(kwargs)
    result = target(**resolved)
    try:
        json.dumps(result)
    except (TypeError, ValueError):
        return handles.register_handle(result)
    return result


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_recurrent_transfer_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a RecurrentTransferMechanism — a single-layer auto-recurrent neural network node that feeds its own output back as input via a weighted self-projection.'
        return _impl(args or {})
