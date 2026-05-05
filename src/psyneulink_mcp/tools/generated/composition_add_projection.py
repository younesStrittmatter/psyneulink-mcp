"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'c5041bab66b1c5fd5c2e1b3ac9db00b905bf0bb39f0ecfbb1f796e0426493f01'
__pnl_qualname__ = 'psyneulink.Composition.add_projection'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_projection'
TOOL_DESCRIPTION = 'Call this tool to connect two nodes in a Composition with a directed projection. Use it when you need to wire a sender (Mechanism, Composition, or OutputPort handle) to a receiver (Mechanism, Composition, or InputPort handle) — either by letting PsyNeuLink create a default MappingProjection, or by passing an existing projection handle or matrix spec. The runtime defensively pre-adds both sender and receiver to the composition before projecting, so you do NOT need to call add_node first. Calling this when the wiring already exists is safe — DuplicateProjectionError is silently treated as success.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "default_matrix": {\n      "description": "Matrix for the default MappingProjection when no projection is specified. Pass a 2-D numeric array (list-of-lists) or a PNL keyword string: \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'HOLLOW_MATRIX\', or \'RANDOM_CONNECTIVITY_MATRIX\'. Passing \'matrix\' is also accepted \\u2014 the runtime normalises it to default_matrix.",\n      "type": [\n        "array",\n        "string"\n      ]\n    },\n    "feedback": {\n      "default": false,\n      "description": "If true, forces the projection to be treated as a feedback projection that breaks a cycle. If false (default), PNL\'s own cycle-detection logic decides.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Optional name for a newly created projection.",\n      "type": "string"\n    },\n    "projection": {\n      "description": "Optional handle string for an already-instantiated Projection to add. Omit to create a default MappingProjection between sender and receiver.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Handle string for the receiving node: a Mechanism, nested Composition, or InputPort. Required unless projection already encodes a receiver.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Handle string for the sending node: a Mechanism, nested Composition, or OutputPort. Required unless projection already encodes a sender.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition"\n  ],\n  "type": "object"\n}\n\nNotes:\n- Either (sender + receiver) or projection must effectively be provided; passing none of them will raise an error inside PNL.\n- If both projection and sender/receiver are given, the sender/receiver on the projection must match — a mismatch raises CompositionError.\n- The PNL source parameter is `default_matrix`, not `matrix` or `default_projection_matrix` (the docstring has a copy-paste error listing `default_projection_matrix` twice). The runtime helper accepts both `matrix` and `default_matrix` and forwards as `default_matrix`.\n- Duplicate wiring (same sender→receiver already in the composition) is a no-op — the existing projection is returned silently; no exception propagates to the agent.\n- `is_learning_projection` and `allow_duplicates` are internal PNL parameters; do not pass them.\n- When sender or receiver is specified as a Mechanism (not a Port), any projection between *any* of its OutputPorts and the receiver\'s InputPorts counts as a duplicate. Pass explicit Port handles to allow multiple projections between the same Mechanism pair.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'default_matrix': { 'description': 'Matrix for the default '
                                                     'MappingProjection when no '
                                                     'projection is specified. Pass a '
                                                     '2-D numeric array '
                                                     '(list-of-lists) or a PNL keyword '
                                                     "string: 'IDENTITY_MATRIX', "
                                                     "'FULL_CONNECTIVITY_MATRIX', "
                                                     "'HOLLOW_MATRIX', or "
                                                     "'RANDOM_CONNECTIVITY_MATRIX'. "
                                                     "Passing 'matrix' is also "
                                                     'accepted — the runtime '
                                                     'normalises it to default_matrix.',
                                      'type': ['array', 'string']},
                  'feedback': { 'default': False,
                                'description': 'If true, forces the projection to be '
                                               'treated as a feedback projection that '
                                               'breaks a cycle. If false (default), '
                                               "PNL's own cycle-detection logic "
                                               'decides.',
                                'type': 'boolean'},
                  'name': { 'description': 'Optional name for a newly created '
                                           'projection.',
                            'type': 'string'},
                  'projection': { 'description': 'Optional handle string for an '
                                                 'already-instantiated Projection to '
                                                 'add. Omit to create a default '
                                                 'MappingProjection between sender and '
                                                 'receiver.',
                                  'type': 'string'},
                  'receiver': { 'description': 'Handle string for the receiving node: '
                                               'a Mechanism, nested Composition, or '
                                               'InputPort. Required unless projection '
                                               'already encodes a receiver.',
                                'type': 'string'},
                  'sender': { 'description': 'Handle string for the sending node: a '
                                             'Mechanism, nested Composition, or '
                                             'OutputPort. Required unless projection '
                                             'already encodes a sender.',
                              'type': 'string'}},
  'required': ['composition'],
  'type': 'object'}
TOOL_NOTES = "- Either (sender + receiver) or projection must effectively be provided; passing none of them will raise an error inside PNL.\n- If both projection and sender/receiver are given, the sender/receiver on the projection must match — a mismatch raises CompositionError.\n- The PNL source parameter is `default_matrix`, not `matrix` or `default_projection_matrix` (the docstring has a copy-paste error listing `default_projection_matrix` twice). The runtime helper accepts both `matrix` and `default_matrix` and forwards as `default_matrix`.\n- Duplicate wiring (same sender→receiver already in the composition) is a no-op — the existing projection is returned silently; no exception propagates to the agent.\n- `is_learning_projection` and `allow_duplicates` are internal PNL parameters; do not pass them.\n- When sender or receiver is specified as a Mechanism (not a Port), any projection between *any* of its OutputPorts and the receiver's InputPorts counts as a duplicate. Pass explicit Port handles to allow multiple projections between the same Mechanism pair."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_projection',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_projection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to connect two nodes in a Composition with a directed projection.'
        return _impl(args or {})
