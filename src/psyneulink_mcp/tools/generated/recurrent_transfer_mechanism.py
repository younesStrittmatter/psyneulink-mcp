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
TOOL_DESCRIPTION = 'Call this tool to create a RecurrentTransferMechanism — a single-layer network whose output feeds back to its own input through a configurable recurrent weight matrix. Use it when a model needs winner-take-all competition, sustained activation, or Hebbian self-organization (e.g., lateral inhibition between representations, attractor dynamics, or memory buffers). Returns a handle to the created mechanism that can be added to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "auto": {\n      "description": "Diagonal (self-connection) entries. A scalar sets all diagonal entries equally; a 1-D array sets them individually. When auto and hetero are both given, matrix is auto+hetero and the matrix arg is ignored.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "clip": {\n      "description": "[min, max] hard bounds applied to output after the transfer function.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "enable_learning": {\n      "default": false,\n      "description": "If true, configures a Hebbian AutoAssociativeLearningMechanism on the recurrent projection at construction time. Learning only takes effect when the mechanism is run inside a Composition.",\n      "type": "boolean"\n    },\n    "has_recurrent_input_port": {\n      "default": false,\n      "description": "If true, the recurrent feedback and external input arrive on separate InputPorts and are summed by combination_function before the transfer function. Required when you need to scale or weight the two streams independently.",\n      "type": "boolean"\n    },\n    "hetero": {\n      "description": "Off-diagonal (lateral) entries. A scalar (e.g. -1 for inhibition) sets all off-diagonal entries; a 2-D array sets them individually (diagonal entries are zeroed). When auto and hetero are both given, the matrix arg is ignored.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initial_value": {\n      "description": "Initial activation state vector (length must match input_shapes). Used when integrator_mode is true.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Size of the input (and output) vector. Determines the dimensions of the recurrent matrix.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "integration_rate": {\n      "default": 0.5,\n      "description": "Smoothing factor when integrator_mode is true (0 = no update, 1 = instant). Equivalent to the time constant of a leaky integrator.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "integrator_mode": {\n      "default": false,\n      "description": "If true, activation accumulates over time via AdaptiveIntegrator (exponential moving average). Use for leaky-integrator dynamics.",\n      "type": "boolean"\n    },\n    "learning_condition": {\n      "default": "UPDATE",\n      "description": "When the learning mechanism fires: UPDATE = after every execution (default); CONVERGENCE = only when the mechanism\'s termination_threshold is met.",\n      "enum": [\n        "UPDATE",\n        "CONVERGENCE"\n      ],\n      "type": "string"\n    },\n    "learning_rate": {\n      "description": "Step size for the learning function. Ignored if enable_learning is false.",\n      "minimum": 0,\n      "type": "number"\n    },\n    "matrix": {\n      "description": "Recurrent weight matrix. Accepts a keyword string (\'HOLLOW_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'IDENTITY_MATRIX\') or a 2-D numeric array. Must be square with side length equal to input_shapes. Overridden by auto/hetero when both are present.",\n      "oneOf": [\n        {\n          "enum": [\n            "HOLLOW_MATRIX",\n            "FULL_CONNECTIVITY_MATRIX",\n            "IDENTITY_MATRIX",\n            "ZERO_MATRIX"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for the mechanism (used in logging and graph display).",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Gaussian noise standard deviation added to the output on each execution.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — do NOT pass `function` as a string (e.g. \'Logistic\'). This causes `TypeError: issubclass() arg 1 must be a class` deep in TransferMechanism._validate_params because PsyNeuLink tries issubclass() on the raw string. The transfer function cannot be changed through this MCP tool; it defaults to Linear. If you need a nonlinear transfer function (e.g. Logistic), use a different construction path or file a feature request.\n\nPriority rules for matrix construction: (1) if auto AND hetero are both given, matrix = auto_diag + hetero_offdiag (matrix arg ignored); (2) if only auto is given, diagonal of matrix is replaced by auto; (3) if only hetero is given, off-diagonal of matrix is replaced by hetero; (4) otherwise matrix is used as-is (default: HOLLOW_MATRIX = zeros with zero diagonal).\n\nThe recurrent matrix must be square with side length equal to input_shapes. Mismatched sizes raise RecurrentTransferError at construction.\n\nenable_learning=True adds an AutoAssociativeLearningMechanism plus two auxiliary projections as aux_components; these are only wired up when the mechanism is added to a Composition — calling run() on the mechanism in isolation will not trigger learning.\n\nlearning_condition=\'CONVERGENCE\' requires a termination_threshold to be set on the mechanism or the enclosing Composition; without it the learning mechanism never fires.'
TOOL_PARAMETERS = { 'properties': { 'auto': { 'description': 'Diagonal (self-connection) entries. A '
                                           'scalar sets all diagonal entries equally; '
                                           'a 1-D array sets them individually. When '
                                           'auto and hetero are both given, matrix is '
                                           'auto+hetero and the matrix arg is ignored.',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'clip': { 'description': '[min, max] hard bounds applied to output '
                                           'after the transfer function.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'enable_learning': { 'default': False,
                                       'description': 'If true, configures a Hebbian '
                                                      'AutoAssociativeLearningMechanism '
                                                      'on the recurrent projection at '
                                                      'construction time. Learning '
                                                      'only takes effect when the '
                                                      'mechanism is run inside a '
                                                      'Composition.',
                                       'type': 'boolean'},
                  'has_recurrent_input_port': { 'default': False,
                                                'description': 'If true, the recurrent '
                                                               'feedback and external '
                                                               'input arrive on '
                                                               'separate InputPorts '
                                                               'and are summed by '
                                                               'combination_function '
                                                               'before the transfer '
                                                               'function. Required '
                                                               'when you need to scale '
                                                               'or weight the two '
                                                               'streams independently.',
                                                'type': 'boolean'},
                  'hetero': { 'description': 'Off-diagonal (lateral) entries. A scalar '
                                             '(e.g. -1 for inhibition) sets all '
                                             'off-diagonal entries; a 2-D array sets '
                                             'them individually (diagonal entries are '
                                             'zeroed). When auto and hetero are both '
                                             'given, the matrix arg is ignored.',
                              'oneOf': [ {'type': 'number'},
                                         { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'}]},
                  'initial_value': { 'description': 'Initial activation state vector '
                                                    '(length must match input_shapes). '
                                                    'Used when integrator_mode is '
                                                    'true.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Size of the input (and output) '
                                                   'vector. Determines the dimensions '
                                                   'of the recurrent matrix.',
                                    'minimum': 1,
                                    'type': 'integer'},
                  'integration_rate': { 'default': 0.5,
                                        'description': 'Smoothing factor when '
                                                       'integrator_mode is true (0 = '
                                                       'no update, 1 = instant). '
                                                       'Equivalent to the time '
                                                       'constant of a leaky '
                                                       'integrator.',
                                        'maximum': 1,
                                        'minimum': 0,
                                        'type': 'number'},
                  'integrator_mode': { 'default': False,
                                       'description': 'If true, activation accumulates '
                                                      'over time via '
                                                      'AdaptiveIntegrator (exponential '
                                                      'moving average). Use for '
                                                      'leaky-integrator dynamics.',
                                       'type': 'boolean'},
                  'learning_condition': { 'default': 'UPDATE',
                                          'description': 'When the learning mechanism '
                                                         'fires: UPDATE = after every '
                                                         'execution (default); '
                                                         'CONVERGENCE = only when the '
                                                         "mechanism's "
                                                         'termination_threshold is '
                                                         'met.',
                                          'enum': ['UPDATE', 'CONVERGENCE'],
                                          'type': 'string'},
                  'learning_rate': { 'description': 'Step size for the learning '
                                                    'function. Ignored if '
                                                    'enable_learning is false.',
                                     'minimum': 0,
                                     'type': 'number'},
                  'matrix': { 'description': 'Recurrent weight matrix. Accepts a '
                                             "keyword string ('HOLLOW_MATRIX', "
                                             "'FULL_CONNECTIVITY_MATRIX', "
                                             "'IDENTITY_MATRIX') or a 2-D numeric "
                                             'array. Must be square with side length '
                                             'equal to input_shapes. Overridden by '
                                             'auto/hetero when both are present.',
                              'oneOf': [ { 'enum': [ 'HOLLOW_MATRIX',
                                                     'FULL_CONNECTIVITY_MATRIX',
                                                     'IDENTITY_MATRIX',
                                                     'ZERO_MATRIX'],
                                           'type': 'string'},
                                         { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'}]},
                  'name': { 'description': 'Name for the mechanism (used in logging '
                                           'and graph display).',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Gaussian noise standard deviation added '
                                            'to the output on each execution.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL — do NOT pass `function` as a string (e.g. 'Logistic'). This causes `TypeError: issubclass() arg 1 must be a class` deep in TransferMechanism._validate_params because PsyNeuLink tries issubclass() on the raw string. The transfer function cannot be changed through this MCP tool; it defaults to Linear. If you need a nonlinear transfer function (e.g. Logistic), use a different construction path or file a feature request.\n\nPriority rules for matrix construction: (1) if auto AND hetero are both given, matrix = auto_diag + hetero_offdiag (matrix arg ignored); (2) if only auto is given, diagonal of matrix is replaced by auto; (3) if only hetero is given, off-diagonal of matrix is replaced by hetero; (4) otherwise matrix is used as-is (default: HOLLOW_MATRIX = zeros with zero diagonal).\n\nThe recurrent matrix must be square with side length equal to input_shapes. Mismatched sizes raise RecurrentTransferError at construction.\n\nenable_learning=True adds an AutoAssociativeLearningMechanism plus two auxiliary projections as aux_components; these are only wired up when the mechanism is added to a Composition — calling run() on the mechanism in isolation will not trigger learning.\n\nlearning_condition='CONVERGENCE' requires a termination_threshold to be set on the mechanism or the enclosing Composition; without it the learning mechanism never fires."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.RecurrentTransferMechanism
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
    def create_recurrent_transfer_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a RecurrentTransferMechanism — a single-layer network whose output feeds back to its own input through a configurable recurrent weight matrix.'
        return _impl(args or {})
