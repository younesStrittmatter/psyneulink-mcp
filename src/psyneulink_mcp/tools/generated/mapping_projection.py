"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd8c007bf89379bd13588392139b4772df8ab11d4616387b02906045f135ac087'
__pnl_qualname__ = 'psyneulink.MappingProjection'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_mapping_projection'
TOOL_DESCRIPTION = 'Call this tool to create a MappingProjection that transmits the output of one Mechanism\'s OutputPort to the InputPort of another (or the same) Mechanism. Use it when wiring two Mechanisms together in a Composition, optionally specifying a weight matrix and whether the connection can be modified by learning. Returns a MappingProjection object that can be passed to Composition.add_projection() or used inline in pathway specifications.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "learnable": {\n      "default": true,\n      "description": "Whether the matrix can be modified by a LearningMechanism. Set to false to permanently prevent learning on this projection.",\n      "type": "boolean"\n    },\n    "learning_rate": {\n      "description": "Projection-specific learning rate. Only valid when learnable is true. If null or omitted, inherits the Composition\'s learning_rate. Setting this when learnable=false raises an error.",\n      "type": "number"\n    },\n    "matrix": {\n      "description": "Weight matrix transforming sender output to receiver input. Can be a 2D array of numbers, or a keyword string: \'AUTO_ASSIGN_MATRIX\' (default \\u2014 identity if same size, full connectivity otherwise), \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'HOLLOW_MATRIX\'. Use a nested array for explicit weights.",\n      "oneOf": [\n        {\n          "enum": [\n            "AUTO_ASSIGN_MATRIX",\n            "IDENTITY_MATRIX",\n            "FULL_CONNECTIVITY_MATRIX",\n            "HOLLOW_MATRIX"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the projection. Auto-generated as \'MappingProjection from <sender>[OutputPort] to <receiver>[InputPort]\' if omitted.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name of the destination Mechanism or its InputPort. If omitted, assignment is deferred until the projection is placed in a Composition.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name of the source Mechanism or its OutputPort. If omitted, assignment is deferred until the projection is placed in a Composition.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- If both sender and receiver are omitted, the projection enters deferred initialization and must be fully specified when added to a Composition.\n- matrix defaults to AUTO_ASSIGN_MATRIX: identity matrix when sender and receiver sizes match, full connectivity matrix otherwise. Mismatched sizes with IDENTITY_MATRIX or HOLLOW_MATRIX raise a ProjectionError.\n- Passing learnable=false and a numeric learning_rate simultaneously raises a MappingError at construction time.\n- List inputs for matrix are automatically converted to np.ndarray internally.\n- The matrix ParameterPort uses an AccumulatorIntegrator function internally for learning; do not confuse this with the projection\'s main transform function (MatrixTransform).\n- learning_rate=True or learning_rate=None both resolve to the Composition\'s learning_rate at runtime; only a float/int pins a specific value.'
TOOL_PARAMETERS = { 'properties': { 'learnable': { 'default': True,
                                 'description': 'Whether the matrix can be modified by '
                                                'a LearningMechanism. Set to false to '
                                                'permanently prevent learning on this '
                                                'projection.',
                                 'type': 'boolean'},
                  'learning_rate': { 'description': 'Projection-specific learning '
                                                    'rate. Only valid when learnable '
                                                    'is true. If null or omitted, '
                                                    "inherits the Composition's "
                                                    'learning_rate. Setting this when '
                                                    'learnable=false raises an error.',
                                     'type': 'number'},
                  'matrix': { 'description': 'Weight matrix transforming sender output '
                                             'to receiver input. Can be a 2D array of '
                                             'numbers, or a keyword string: '
                                             "'AUTO_ASSIGN_MATRIX' (default — identity "
                                             'if same size, full connectivity '
                                             "otherwise), 'IDENTITY_MATRIX', "
                                             "'FULL_CONNECTIVITY_MATRIX', "
                                             "'HOLLOW_MATRIX'. Use a nested array for "
                                             'explicit weights.',
                              'oneOf': [ { 'enum': [ 'AUTO_ASSIGN_MATRIX',
                                                     'IDENTITY_MATRIX',
                                                     'FULL_CONNECTIVITY_MATRIX',
                                                     'HOLLOW_MATRIX'],
                                           'type': 'string'},
                                         { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'}]},
                  'name': { 'description': 'Optional name for the projection. '
                                           "Auto-generated as 'MappingProjection from "
                                           '<sender>[OutputPort] to '
                                           "<receiver>[InputPort]' if omitted.",
                            'type': 'string'},
                  'receiver': { 'description': 'Name of the destination Mechanism or '
                                               'its InputPort. If omitted, assignment '
                                               'is deferred until the projection is '
                                               'placed in a Composition.',
                                'type': 'string'},
                  'sender': { 'description': 'Name of the source Mechanism or its '
                                             'OutputPort. If omitted, assignment is '
                                             'deferred until the projection is placed '
                                             'in a Composition.',
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- If both sender and receiver are omitted, the projection enters deferred initialization and must be fully specified when added to a Composition.\n- matrix defaults to AUTO_ASSIGN_MATRIX: identity matrix when sender and receiver sizes match, full connectivity matrix otherwise. Mismatched sizes with IDENTITY_MATRIX or HOLLOW_MATRIX raise a ProjectionError.\n- Passing learnable=false and a numeric learning_rate simultaneously raises a MappingError at construction time.\n- List inputs for matrix are automatically converted to np.ndarray internally.\n- The matrix ParameterPort uses an AccumulatorIntegrator function internally for learning; do not confuse this with the projection's main transform function (MatrixTransform).\n- learning_rate=True or learning_rate=None both resolve to the Composition's learning_rate at runtime; only a float/int pins a specific value."


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
        "Call this tool to create a MappingProjection that transmits the output of one Mechanism's OutputPort to the InputPort of another (or the same) Mechanism."
        return _impl(args or {})
