"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0035db1206b9519c73855e0854acd88e33390b71194ed402f2532b53021b8afc'
__pnl_qualname__ = 'psyneulink.KohonenLearningMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_kohonen_learning_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a KohonenLearningMechanism, the unsupervised learning mechanism that updates connection weights for a KohonenMechanism (self-organizing map). Use it when you need to explicitly construct or configure the learning component of a Kohonen/SOM network — in most cases KohonenMechanism creates this automatically, so call this directly only when you need custom learning rate, function, or modulation settings that cannot be specified on the KohonenMechanism itself. Returns a KohonenLearningMechanism instance whose output is a 2D weight-change matrix applied to the associated MappingProjection.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Two-item list of 1d numeric arrays: [ACTIVATION_INPUT, ACTIVATION_OUTPUT], matching the input and output activation vectors of the associated KohonenMechanism. Must be a list with exactly two 1d arrays or a 2d numpy array.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "function": {\n      "default": "Kohonen",\n      "description": "Learning function to compute the weight-change matrix. Defaults to Kohonen (not Hebbian despite the docstring signature). Must accept a variable of [1d array, 1d array, 2d matrix] and return a 2D square matrix matching the third item\'s dimensions. Pass as a PsyNeuLink LearningFunction name string (e.g., \'Kohonen\', \'Hebbian\').",\n      "type": "string"\n    },\n    "input_shapes": {\n      "description": "Shape of the input arrays; alternative to specifying default_variable directly.",\n      "items": {\n        "type": "integer"\n      },\n      "type": "array"\n    },\n    "learning_rate": {\n      "description": "Scales the weight-change matrix returned by the function. A scalar multiplies the whole matrix; a 1d array Hadamard-multiplies the ACTIVATION_INPUT (scaling per-unit contributions); a 2d array Hadamard-multiplies the weight matrix (scaling per-connection contributions). If None, inherits from the enclosing Composition, then from the function\'s default_learning_rate.",\n      "type": "number"\n    },\n    "learning_signals": {\n      "description": "Specifies which MappingProjection matrix parameter(s) to train. Defaults to the single learning_projection of the associated KohonenMechanism. Each item can be a Projection, ParameterPort, tuple of (str, Projection), or dict.",\n      "items": {},\n      "type": "array"\n    },\n    "matrix": {\n      "description": "The weight matrix to be learned; must match the matrix parameter of the MappingProjection associated with the KohonenMechanism. Passed as a 2D numeric array.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "modulation": {\n      "default": "ADDITIVE",\n      "description": "Default modulation mode for LearningSignals: how the learning signal modifies the trained parameter. Default is \'ADDITIVE\'.",\n      "enum": [\n        "ADDITIVE",\n        "MULTIPLICATIVE",\n        "OVERRIDE",\n        "DISABLE"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for the KohonenLearningMechanism instance.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "default_variable"\n  ],\n  "type": "object"\n}\n\nNotes:\n1. KohonenMechanism typically auto-creates its KohonenLearningMechanism — instantiate this directly only when you need to override learning configuration that KohonenMechanism does not expose.\n2. The docstring signature says `function=Hebbian` but the Parameters class sets `function = Parameter(Hebbian, ...)` while the actual intended default is `Kohonen`; treat Kohonen as the correct default — Hebbian in the signature is a documentation error in PNL source.\n3. `default_variable` must be exactly two 1d numeric arrays; passing anything else raises a KohonenLearningMechanismError.\n4. The internal `_parse_function_variable` method appends the current matrix as a third element before calling the function — your custom function must accept [1d, 1d, 2d] but you only supply [1d, 1d] as variable.\n5. `learning_rate` semantics change with shape: scalar → whole-matrix scale; 1d → per-unit (input) scale; 2d → per-connection scale. Be explicit about which you intend.\n6. This mechanism runs during EXECUTION_PHASE with UNSUPERVISED learning type; it is incompatible with supervised learning pipelines that expect error signals from a target.\n7. Weights are updated within the same trial they are learned (not deferred to the next trial), because `_update_output_ports` executes the learned_projection immediately.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Two-item list of 1d numeric '
                                                       'arrays: [ACTIVATION_INPUT, '
                                                       'ACTIVATION_OUTPUT], matching '
                                                       'the input and output '
                                                       'activation vectors of the '
                                                       'associated KohonenMechanism. '
                                                       'Must be a list with exactly '
                                                       'two 1d arrays or a 2d numpy '
                                                       'array.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'maxItems': 2,
                                        'minItems': 2,
                                        'type': 'array'},
                  'function': { 'default': 'Kohonen',
                                'description': 'Learning function to compute the '
                                               'weight-change matrix. Defaults to '
                                               'Kohonen (not Hebbian despite the '
                                               'docstring signature). Must accept a '
                                               'variable of [1d array, 1d array, 2d '
                                               'matrix] and return a 2D square matrix '
                                               "matching the third item's dimensions. "
                                               'Pass as a PsyNeuLink LearningFunction '
                                               "name string (e.g., 'Kohonen', "
                                               "'Hebbian').",
                                'type': 'string'},
                  'input_shapes': { 'description': 'Shape of the input arrays; '
                                                   'alternative to specifying '
                                                   'default_variable directly.',
                                    'items': {'type': 'integer'},
                                    'type': 'array'},
                  'learning_rate': { 'description': 'Scales the weight-change matrix '
                                                    'returned by the function. A '
                                                    'scalar multiplies the whole '
                                                    'matrix; a 1d array '
                                                    'Hadamard-multiplies the '
                                                    'ACTIVATION_INPUT (scaling '
                                                    'per-unit contributions); a 2d '
                                                    'array Hadamard-multiplies the '
                                                    'weight matrix (scaling '
                                                    'per-connection contributions). If '
                                                    'None, inherits from the enclosing '
                                                    'Composition, then from the '
                                                    "function's default_learning_rate.",
                                     'type': 'number'},
                  'learning_signals': { 'description': 'Specifies which '
                                                       'MappingProjection matrix '
                                                       'parameter(s) to train. '
                                                       'Defaults to the single '
                                                       'learning_projection of the '
                                                       'associated KohonenMechanism. '
                                                       'Each item can be a Projection, '
                                                       'ParameterPort, tuple of (str, '
                                                       'Projection), or dict.',
                                        'items': {},
                                        'type': 'array'},
                  'matrix': { 'description': 'The weight matrix to be learned; must '
                                             'match the matrix parameter of the '
                                             'MappingProjection associated with the '
                                             'KohonenMechanism. Passed as a 2D numeric '
                                             'array.',
                              'items': {'items': {'type': 'number'}, 'type': 'array'},
                              'type': 'array'},
                  'modulation': { 'default': 'ADDITIVE',
                                  'description': 'Default modulation mode for '
                                                 'LearningSignals: how the learning '
                                                 'signal modifies the trained '
                                                 "parameter. Default is 'ADDITIVE'.",
                                  'enum': [ 'ADDITIVE',
                                            'MULTIPLICATIVE',
                                            'OVERRIDE',
                                            'DISABLE'],
                                  'type': 'string'},
                  'name': { 'description': 'Name for the KohonenLearningMechanism '
                                           'instance.',
                            'type': 'string'}},
  'required': ['default_variable'],
  'type': 'object'}
TOOL_NOTES = '1. KohonenMechanism typically auto-creates its KohonenLearningMechanism — instantiate this directly only when you need to override learning configuration that KohonenMechanism does not expose.\n2. The docstring signature says `function=Hebbian` but the Parameters class sets `function = Parameter(Hebbian, ...)` while the actual intended default is `Kohonen`; treat Kohonen as the correct default — Hebbian in the signature is a documentation error in PNL source.\n3. `default_variable` must be exactly two 1d numeric arrays; passing anything else raises a KohonenLearningMechanismError.\n4. The internal `_parse_function_variable` method appends the current matrix as a third element before calling the function — your custom function must accept [1d, 1d, 2d] but you only supply [1d, 1d] as variable.\n5. `learning_rate` semantics change with shape: scalar → whole-matrix scale; 1d → per-unit (input) scale; 2d → per-connection scale. Be explicit about which you intend.\n6. This mechanism runs during EXECUTION_PHASE with UNSUPERVISED learning type; it is incompatible with supervised learning pipelines that expect error signals from a target.\n7. Weights are updated within the same trial they are learned (not deferred to the next trial), because `_update_output_ports` executes the learned_projection immediately.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.KohonenLearningMechanism
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
    def create_kohonen_learning_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a KohonenLearningMechanism, the unsupervised learning mechanism that updates connection weights for a KohonenMechanism (self-organizing map).'
        return _impl(args or {})
