"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b5a2130e818cebf60e4ce4ec5e9d6b37acb276d9e6462bdd5cb9c8070895c893'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.recurrenttransfermechanism.MappingProjection'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_mapping_projection'
TOOL_DESCRIPTION = 'Call this tool to create a MappingProjection — a weighted connection that routes the output of one Mechanism to the input of another. Use it when you need a standalone projection object before adding it to a Composition, or when wiring two mechanisms with a specific matrix. Returns the created MappingProjection, which can then be passed to composition_add_projection or referenced by name.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "learnable": {\n      "default": true,\n      "description": "Whether the matrix can be modified by learning. Set to false to permanently lock the weights; once false, assigning a numeric learning_rate raises an error.",\n      "type": "boolean"\n    },\n    "learning_rate": {\n      "description": "Projection-specific learning rate. Only valid when learnable is true. If null or omitted, inherits from the Composition\'s learning_rate. Set to false (as boolean) to suppress learning even when learnable is true.",\n      "type": "number"\n    },\n    "matrix": {\n      "default": "AUTO_ASSIGN_MATRIX",\n      "description": "Matrix specification. Keyword strings: \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'HOLLOW_MATRIX\', \'RANDOM_CONNECTIVITY_MATRIX\', \'AUTO_ASSIGN_MATRIX\' (default \\u2014 uses IDENTITY when dimensions match, FULL_CONNECTIVITY otherwise). You may also pass a 2D array as a JSON array of arrays.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the projection. Auto-named as \'MappingProjection from <sender>[OutputPort] to <receiver>[InputPort]\' if omitted.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name of the destination Mechanism (uses its primary InputPort). Must be a plain mechanism name string \\u2014 do NOT use bracket-notation like \'mech[PORT_NAME]\'; that format is invalid and will raise an AssertionError. For mechanisms with multiple named InputPorts (e.g., EMComposition), use composition_add_projection instead.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name of the source Mechanism (uses its primary OutputPort). Must be a plain mechanism name string \\u2014 do NOT use dot-notation or bracket-notation like \'mech.output_ports[\\"PORT\\"]\' or \'mech[PORT]\'; those formats are invalid and will raise an AssertionError.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — sender/receiver are plain mechanism name strings only: strings like "mech[PORT_NAME]" (bracket notation) and "mech.output_ports[\'PORT_NAME\']" (dot notation) are NOT resolved and will raise AssertionError. Pass only the mechanism\'s name attribute (e.g., "my_mech").\n\nFor multi-port receivers (e.g., EMComposition which has one InputPort per memory field): MappingProjection cannot target a non-primary InputPort by name string. Use composition_add_projection or composition_add_linear_processing_pathway instead, which support explicit port-level targeting within a Composition.\n\nDuplicateProjectionError is raised if an identical projection (same sender → receiver pair) already exists. If you hit this error, the connection is already present — do not retry.\n\nMappingProjection instantiation with both sender and receiver triggers full initialization including matrix dimension validation. If sender output size ≠ receiver input size and matrix is IDENTITY_MATRIX or HOLLOW_MATRIX, a ProjectionError is raised (those matrices are not reshapable). FULL_CONNECTIVITY_MATRIX and AUTO_ASSIGN_MATRIX will be automatically reshaped.\n\nIf either sender or receiver is omitted, the projection enters deferred initialization and cannot be used until both are assigned via a Composition context.'
TOOL_PARAMETERS = { 'properties': { 'learnable': { 'default': True,
                                 'description': 'Whether the matrix can be modified by '
                                                'learning. Set to false to permanently '
                                                'lock the weights; once false, '
                                                'assigning a numeric learning_rate '
                                                'raises an error.',
                                 'type': 'boolean'},
                  'learning_rate': { 'description': 'Projection-specific learning '
                                                    'rate. Only valid when learnable '
                                                    'is true. If null or omitted, '
                                                    "inherits from the Composition's "
                                                    'learning_rate. Set to false (as '
                                                    'boolean) to suppress learning '
                                                    'even when learnable is true.',
                                     'type': 'number'},
                  'matrix': { 'default': 'AUTO_ASSIGN_MATRIX',
                              'description': 'Matrix specification. Keyword strings: '
                                             "'IDENTITY_MATRIX', "
                                             "'FULL_CONNECTIVITY_MATRIX', "
                                             "'HOLLOW_MATRIX', "
                                             "'RANDOM_CONNECTIVITY_MATRIX', "
                                             "'AUTO_ASSIGN_MATRIX' (default — uses "
                                             'IDENTITY when dimensions match, '
                                             'FULL_CONNECTIVITY otherwise). You may '
                                             'also pass a 2D array as a JSON array of '
                                             'arrays.',
                              'type': 'string'},
                  'name': { 'description': 'Optional name for the projection. '
                                           "Auto-named as 'MappingProjection from "
                                           '<sender>[OutputPort] to '
                                           "<receiver>[InputPort]' if omitted.",
                            'type': 'string'},
                  'receiver': { 'description': 'Name of the destination Mechanism '
                                               '(uses its primary InputPort). Must be '
                                               'a plain mechanism name string — do NOT '
                                               'use bracket-notation like '
                                               "'mech[PORT_NAME]'; that format is "
                                               'invalid and will raise an '
                                               'AssertionError. For mechanisms with '
                                               'multiple named InputPorts (e.g., '
                                               'EMComposition), use '
                                               'composition_add_projection instead.',
                                'type': 'string'},
                  'sender': { 'description': 'Name of the source Mechanism (uses its '
                                             'primary OutputPort). Must be a plain '
                                             'mechanism name string — do NOT use '
                                             'dot-notation or bracket-notation like '
                                             '\'mech.output_ports["PORT"]\' or '
                                             "'mech[PORT]'; those formats are invalid "
                                             'and will raise an AssertionError.',
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL — sender/receiver are plain mechanism name strings only: strings like "mech[PORT_NAME]" (bracket notation) and "mech.output_ports[\'PORT_NAME\']" (dot notation) are NOT resolved and will raise AssertionError. Pass only the mechanism\'s name attribute (e.g., "my_mech").\n\nFor multi-port receivers (e.g., EMComposition which has one InputPort per memory field): MappingProjection cannot target a non-primary InputPort by name string. Use composition_add_projection or composition_add_linear_processing_pathway instead, which support explicit port-level targeting within a Composition.\n\nDuplicateProjectionError is raised if an identical projection (same sender → receiver pair) already exists. If you hit this error, the connection is already present — do not retry.\n\nMappingProjection instantiation with both sender and receiver triggers full initialization including matrix dimension validation. If sender output size ≠ receiver input size and matrix is IDENTITY_MATRIX or HOLLOW_MATRIX, a ProjectionError is raised (those matrices are not reshapable). FULL_CONNECTIVITY_MATRIX and AUTO_ASSIGN_MATRIX will be automatically reshaped.\n\nIf either sender or receiver is omitted, the projection enters deferred initialization and cannot be used until both are assigned via a Composition context.'


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
        'Call this tool to create a MappingProjection — a weighted connection that routes the output of one Mechanism to the input of another.'
        return _impl(args or {})
