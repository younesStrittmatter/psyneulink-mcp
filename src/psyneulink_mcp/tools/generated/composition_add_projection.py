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
__pnl_parents__ = []
__pnl_parent_sha256s__ = {}
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_projection'
TOOL_DESCRIPTION = 'Wire a Projection (typically a MappingProjection) between two nodes already conceivable in a Composition: call this when you need to add an explicit connection that wasn\'t created by a pathway, override a default matrix, mark a connection as feedback (cycle-breaking), or attach a pre-built Projection instance. The runtime helper defensively adds `sender` and `receiver` to the composition first, so you do NOT need to call add_node beforehand. Returns the resulting Projection handle (or a no-op success marker if PNL flags the wiring as a duplicate, which the helper treats as a benign retry).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle of the Composition that should own the new Projection (returned by create_composition or the analogous constructor).",\n      "type": "string"\n    },\n    "default_matrix": {\n      "anyOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ],\n      "description": "Matrix used to build the default MappingProjection when `projection` is not given and no Projection already exists between sender and receiver. Pass either a 2-D numeric array (rows = sender output size, cols = receiver input size) OR one of PNL\'s matrix keyword strings: \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'HOLLOW_MATRIX\', \'RANDOM_CONNECTIVITY_MATRIX\', \'AUTO_ASSOCIATIVE_MATRIX\', \'INVERSE_HOLLOW_MATRIX\'. NOTE: the underlying PNL kwarg is `default_matrix`, not `matrix` \\u2014 passing `matrix` to a free-standing MappingProjection trips a parameter-port bug, so always specify the matrix here."\n    },\n    "feedback": {\n      "default": false,\n      "description": "If True, the Projection is always designated as a feedback Projection used to break cycles in the Composition\'s graph. If False (default), it is never designated as feedback even when it closes a loop. Use this to control cycle resolution explicitly.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Optional human-readable name for the new Projection.",\n      "type": "string"\n    },\n    "projection": {\n      "description": "Optional handle of an already-constructed Projection (e.g. a MappingProjection or ControlProjection). If omitted, a default MappingProjection is created between sender and receiver using `default_matrix`. If both this and sender/receiver are given, they must agree with the Projection\'s own sender/receiver.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Handle of the target node \\u2014 a Mechanism, a (nested) Composition, or an InputPort. Pass the OBJECT handle, not a port-name string and not a {\'mechanism\': ..., \'input_port\': ...} dict (both forms trip a PNL UnboundLocalError). To target a specific InputPort of a Mechanism, first obtain a handle to that InputPort via the Mechanism\'s input_ports and pass that handle here.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Handle of the source node \\u2014 a Mechanism, a (nested) Composition, or an OutputPort. Pass the OBJECT handle, not a port-name string.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "sender",\n    "receiver"\n  ],\n  "type": "object"\n}\n\nNotes:\nReceiver/sender forms that fail: passing an InputPort name as a bare string (e.g. \'FIELD_1_INPUT\' or \'EM[FIELD_1_INPUT]\') or as a dict {\'mechanism\': ..., \'input_port\': ...} causes PsyNeuLink to raise `UnboundLocalError: cannot access local variable \'receiver_ports\'`. Always pass an OBJECT handle — a Mechanism, a Composition, an InputPort, or an OutputPort. To target a specific port, fetch its handle via the Mechanism\'s input_ports/output_ports, then pass that handle.\n\nThe runtime helper auto-adds `sender` and `receiver` to the Composition before dispatching (PNL no-ops if either is already a node), so callers do not need to call add_node first; PNL\'s `CompositionError: ... not (yet) in it` should not occur. The helper also turns `DuplicateProjectionError` into a no-op success — re-issuing add_projection for an existing wiring is safe and idempotent.\n\nUse `default_matrix` (NOT `matrix`) for the matrix specification; the PNL kwarg name on the bound method is `default_matrix`, and the helper accepts either alias and forwards it as `default_matrix`. Matrix dimensions must be (sender_output_size × receiver_input_size); IDENTITY_MATRIX requires equal sizes. Returns the resulting Projection (or None when the helper short-circuits a duplicate); when more than one matching Projection already exists outside the Composition, PNL adopts the most recent one and emits a verbose warning. The `is_learning_projection`, `allow_duplicates`, and `context` parameters of the underlying method are managed by the runtime and intentionally not exposed.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle of the Composition that '
                                                  'should own the new Projection '
                                                  '(returned by create_composition or '
                                                  'the analogous constructor).',
                                   'type': 'string'},
                  'default_matrix': { 'anyOf': [ {'type': 'string'},
                                                 { 'items': { 'items': { 'type': 'number'},
                                                              'type': 'array'},
                                                   'type': 'array'}],
                                      'description': 'Matrix used to build the default '
                                                     'MappingProjection when '
                                                     '`projection` is not given and no '
                                                     'Projection already exists '
                                                     'between sender and receiver. '
                                                     'Pass either a 2-D numeric array '
                                                     '(rows = sender output size, cols '
                                                     '= receiver input size) OR one of '
                                                     "PNL's matrix keyword strings: "
                                                     "'IDENTITY_MATRIX', "
                                                     "'FULL_CONNECTIVITY_MATRIX', "
                                                     "'HOLLOW_MATRIX', "
                                                     "'RANDOM_CONNECTIVITY_MATRIX', "
                                                     "'AUTO_ASSOCIATIVE_MATRIX', "
                                                     "'INVERSE_HOLLOW_MATRIX'. NOTE: "
                                                     'the underlying PNL kwarg is '
                                                     '`default_matrix`, not `matrix` — '
                                                     'passing `matrix` to a '
                                                     'free-standing MappingProjection '
                                                     'trips a parameter-port bug, so '
                                                     'always specify the matrix here.'},
                  'feedback': { 'default': False,
                                'description': 'If True, the Projection is always '
                                               'designated as a feedback Projection '
                                               'used to break cycles in the '
                                               "Composition's graph. If False "
                                               '(default), it is never designated as '
                                               'feedback even when it closes a loop. '
                                               'Use this to control cycle resolution '
                                               'explicitly.',
                                'type': 'boolean'},
                  'name': { 'description': 'Optional human-readable name for the new '
                                           'Projection.',
                            'type': 'string'},
                  'projection': { 'description': 'Optional handle of an '
                                                 'already-constructed Projection (e.g. '
                                                 'a MappingProjection or '
                                                 'ControlProjection). If omitted, a '
                                                 'default MappingProjection is created '
                                                 'between sender and receiver using '
                                                 '`default_matrix`. If both this and '
                                                 'sender/receiver are given, they must '
                                                 "agree with the Projection's own "
                                                 'sender/receiver.',
                                  'type': 'string'},
                  'receiver': { 'description': 'Handle of the target node — a '
                                               'Mechanism, a (nested) Composition, or '
                                               'an InputPort. Pass the OBJECT handle, '
                                               'not a port-name string and not a '
                                               "{'mechanism': ..., 'input_port': ...} "
                                               'dict (both forms trip a PNL '
                                               'UnboundLocalError). To target a '
                                               'specific InputPort of a Mechanism, '
                                               'first obtain a handle to that '
                                               "InputPort via the Mechanism's "
                                               'input_ports and pass that handle here.',
                                'type': 'string'},
                  'sender': { 'description': 'Handle of the source node — a Mechanism, '
                                             'a (nested) Composition, or an '
                                             'OutputPort. Pass the OBJECT handle, not '
                                             'a port-name string.',
                              'type': 'string'}},
  'required': ['composition', 'sender', 'receiver'],
  'type': 'object'}
TOOL_NOTES = "Receiver/sender forms that fail: passing an InputPort name as a bare string (e.g. 'FIELD_1_INPUT' or 'EM[FIELD_1_INPUT]') or as a dict {'mechanism': ..., 'input_port': ...} causes PsyNeuLink to raise `UnboundLocalError: cannot access local variable 'receiver_ports'`. Always pass an OBJECT handle — a Mechanism, a Composition, an InputPort, or an OutputPort. To target a specific port, fetch its handle via the Mechanism's input_ports/output_ports, then pass that handle.\n\nThe runtime helper auto-adds `sender` and `receiver` to the Composition before dispatching (PNL no-ops if either is already a node), so callers do not need to call add_node first; PNL's `CompositionError: ... not (yet) in it` should not occur. The helper also turns `DuplicateProjectionError` into a no-op success — re-issuing add_projection for an existing wiring is safe and idempotent.\n\nUse `default_matrix` (NOT `matrix`) for the matrix specification; the PNL kwarg name on the bound method is `default_matrix`, and the helper accepts either alias and forwards it as `default_matrix`. Matrix dimensions must be (sender_output_size × receiver_input_size); IDENTITY_MATRIX requires equal sizes. Returns the resulting Projection (or None when the helper short-circuits a duplicate); when more than one matching Projection already exists outside the Composition, PNL adopts the most recent one and emits a verbose warning. The `is_learning_projection`, `allow_duplicates`, and `context` parameters of the underlying method are managed by the runtime and intentionally not exposed."


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
        "Wire a Projection (typically a MappingProjection) between two nodes already conceivable in a Composition: call this when you need to add an explicit connection that wasn't created by a pathway, override a default matrix, mark a connection as feedback (cycle-breaking), or attach a pre-built Projection instance."
        return _impl(args or {})
