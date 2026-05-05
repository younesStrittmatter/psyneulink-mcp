"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b5a2130e818cebf60e4ce4ec5e9d6b37acb276d9e6462bdd5cb9c8070895c893'
__pnl_qualname__ = 'psyneulink.MappingProjection'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_mapping_projection'
TOOL_DESCRIPTION = 'Call this tool to create a MappingProjection — a weighted connection that transmits the output of one Mechanism (or OutputPort) to the input of another (or InputPort). Use it when you need to wire two Mechanisms together explicitly, control the weight matrix between them, or enable/disable learning on a specific connection. Returns a MappingProjection object that can be passed to Composition.add_projection() or used inline when constructing pathways.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "learnable": {\n      "default": true,\n      "description": "Whether the matrix can be modified by a LearningMechanism. Setting to false permanently prevents learning on this projection; assigning a numeric learning_rate when learnable=false raises an error.",\n      "type": "boolean"\n    },\n    "learning_rate": {\n      "description": "Projection-specific learning rate. Numeric value overrides Composition-level rate; false disables learning even when learnable=true; true or null inherits the Composition\'s learning_rate. Only valid when learnable=true.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "boolean"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "matrix": {\n      "description": "Weight matrix transforming sender output into receiver input. Accepts a 2D list/array of numbers, or a keyword string: \'AUTO_ASSIGN_MATRIX\' (default \\u2014 auto-selects identity or full connectivity), \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'HOLLOW_MATRIX\', or \'RANDOM_CONNECTIVITY_MATRIX\'. Shape must be [sender_size x receiver_size].",\n      "oneOf": [\n        {\n          "enum": [\n            "AUTO_ASSIGN_MATRIX",\n            "IDENTITY_MATRIX",\n            "FULL_CONNECTIVITY_MATRIX",\n            "HOLLOW_MATRIX",\n            "RANDOM_CONNECTIVITY_MATRIX"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the projection. Defaults to \'MappingProjection from <sender>[OutputPort] to <receiver>[InputPort]\'.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name of the destination Mechanism or InputPort. If a Mechanism name is given, its primary InputPort is used. Can be omitted for deferred initialization.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name of the source Mechanism or OutputPort. If a Mechanism name is given, its primary OutputPort is used. Can be omitted if the projection will be assigned in context (deferred initialization).",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- If sender or receiver is omitted, the MappingProjection enters deferred initialization and must be fully specified before the Composition runs.\n- When matrix is omitted or set to \'AUTO_ASSIGN_MATRIX\', PNL selects IDENTITY_MATRIX if sender and receiver sizes match, otherwise FULL_CONNECTIVITY_MATRIX.\n- If a numeric matrix is supplied whose output length doesn\'t match the receiver InputPort width, PNL raises ProjectionError — dimensions must be [sender_output_size x receiver_input_size].\n- Assigning a numeric learning_rate when learnable=False raises a MappingError at construction time.\n- The matrix parameter is also the learning target: a LearningProjection modifies it in place when learning is active.\n- weight and exponent are inherited pathway parameters accepted by the constructor but not commonly needed; omit them unless you specifically need to scale/exponentiate the projection\'s output before it reaches the receiver.'
TOOL_PARAMETERS = { 'properties': { 'learnable': { 'default': True,
                                 'description': 'Whether the matrix can be modified by '
                                                'a LearningMechanism. Setting to false '
                                                'permanently prevents learning on this '
                                                'projection; assigning a numeric '
                                                'learning_rate when learnable=false '
                                                'raises an error.',
                                 'type': 'boolean'},
                  'learning_rate': { 'description': 'Projection-specific learning '
                                                    'rate. Numeric value overrides '
                                                    'Composition-level rate; false '
                                                    'disables learning even when '
                                                    'learnable=true; true or null '
                                                    "inherits the Composition's "
                                                    'learning_rate. Only valid when '
                                                    'learnable=true.',
                                     'oneOf': [ {'type': 'number'},
                                                {'type': 'boolean'},
                                                {'type': 'null'}]},
                  'matrix': { 'description': 'Weight matrix transforming sender output '
                                             'into receiver input. Accepts a 2D '
                                             'list/array of numbers, or a keyword '
                                             "string: 'AUTO_ASSIGN_MATRIX' (default — "
                                             'auto-selects identity or full '
                                             "connectivity), 'IDENTITY_MATRIX', "
                                             "'FULL_CONNECTIVITY_MATRIX', "
                                             "'HOLLOW_MATRIX', or "
                                             "'RANDOM_CONNECTIVITY_MATRIX'. Shape must "
                                             'be [sender_size x receiver_size].',
                              'oneOf': [ { 'enum': [ 'AUTO_ASSIGN_MATRIX',
                                                     'IDENTITY_MATRIX',
                                                     'FULL_CONNECTIVITY_MATRIX',
                                                     'HOLLOW_MATRIX',
                                                     'RANDOM_CONNECTIVITY_MATRIX'],
                                           'type': 'string'},
                                         { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'}]},
                  'name': { 'description': 'Optional name for the projection. Defaults '
                                           "to 'MappingProjection from "
                                           '<sender>[OutputPort] to '
                                           "<receiver>[InputPort]'.",
                            'type': 'string'},
                  'receiver': { 'description': 'Name of the destination Mechanism or '
                                               'InputPort. If a Mechanism name is '
                                               'given, its primary InputPort is used. '
                                               'Can be omitted for deferred '
                                               'initialization.',
                                'type': 'string'},
                  'sender': { 'description': 'Name of the source Mechanism or '
                                             'OutputPort. If a Mechanism name is '
                                             'given, its primary OutputPort is used. '
                                             'Can be omitted if the projection will be '
                                             'assigned in context (deferred '
                                             'initialization).',
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- If sender or receiver is omitted, the MappingProjection enters deferred initialization and must be fully specified before the Composition runs.\n- When matrix is omitted or set to 'AUTO_ASSIGN_MATRIX', PNL selects IDENTITY_MATRIX if sender and receiver sizes match, otherwise FULL_CONNECTIVITY_MATRIX.\n- If a numeric matrix is supplied whose output length doesn't match the receiver InputPort width, PNL raises ProjectionError — dimensions must be [sender_output_size x receiver_input_size].\n- Assigning a numeric learning_rate when learnable=False raises a MappingError at construction time.\n- The matrix parameter is also the learning target: a LearningProjection modifies it in place when learning is active.\n- weight and exponent are inherited pathway parameters accepted by the constructor but not commonly needed; omit them unless you specifically need to scale/exponentiate the projection's output before it reaches the receiver."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.MappingProjection
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
    def create_mapping_projection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a MappingProjection — a weighted connection that transmits the output of one Mechanism (or OutputPort) to the input of another (or InputPort).'
        return _impl(args or {})
