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
TOOL_DESCRIPTION = 'Call this tool to wire two nodes (Mechanisms or Compositions) in a Composition with a projection — either by letting PNL create a default MappingProjection between sender and receiver, or by supplying an explicit projection handle. The tool auto-adds sender and receiver to the composition before creating the projection, so `add_node` calls are not required first. Retrying an identical call is safe: duplicate projections are silently treated as success and the existing projection is returned.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "default_matrix": {\n      "description": "Matrix to use when creating a default MappingProjection. Only applied when no explicit projection is specified and none already exists between sender and receiver. Keyword strings and the \'matrix\' alias are both accepted by the runtime.",\n      "oneOf": [\n        {\n          "description": "PNL matrix keyword. Use FULL_CONNECTIVITY_MATRIX when sender and receiver have different sizes; IDENTITY_MATRIX requires equal sizes.",\n          "enum": [\n            "IDENTITY_MATRIX",\n            "FULL_CONNECTIVITY_MATRIX",\n            "HOLLOW_MATRIX",\n            "RANDOM_CONNECTIVITY_MATRIX"\n          ],\n          "type": "string"\n        },\n        {\n          "description": "Explicit 2-D numeric matrix (rows = sender output size, cols = receiver input size).",\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "feedback": {\n      "default": false,\n      "description": "If true, designates the projection as a feedback projection, breaking cycles in the graph. If false, the projection is never treated as feedback even if PNL would default to that.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Optional name for the new projection.",\n      "type": "string"\n    },\n    "projection": {\n      "description": "Optional handle string for a pre-existing Projection object to add. Omit to create a default MappingProjection between sender and receiver.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Handle string for the receiver: a Mechanism, Composition, or InputPort handle. Required when no explicit projection handle is given.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Handle string for the sender: a Mechanism, Composition, or OutputPort handle. Required when no explicit projection handle is given.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition"\n  ],\n  "type": "object"\n}\n\nNotes:\nIDENTITY_MATRIX requires sender output size == receiver input size exactly; passing it across mechanisms with different sizes raises FunctionError (confirmed in recent failures: sender=25, receiver=20). Use FULL_CONNECTIVITY_MATRIX for cross-size connections or omit default_matrix to let PNL choose. The runtime accepts either `default_matrix` or the legacy `matrix` kwarg name and translates both to PNL\'s `default_matrix`. DuplicateProjectionError is silently swallowed as a no-op — the call returns the existing projection. Both sender and receiver are defensively added to the composition before projection creation, so CompositionError "not (yet) in it" will not occur. If both sender and receiver are omitted, the projection handle must already encode its endpoints.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'default_matrix': { 'description': 'Matrix to use when creating a '
                                                     'default MappingProjection. Only '
                                                     'applied when no explicit '
                                                     'projection is specified and none '
                                                     'already exists between sender '
                                                     'and receiver. Keyword strings '
                                                     "and the 'matrix' alias are both "
                                                     'accepted by the runtime.',
                                      'oneOf': [ { 'description': 'PNL matrix keyword. '
                                                                  'Use '
                                                                  'FULL_CONNECTIVITY_MATRIX '
                                                                  'when sender and '
                                                                  'receiver have '
                                                                  'different sizes; '
                                                                  'IDENTITY_MATRIX '
                                                                  'requires equal '
                                                                  'sizes.',
                                                   'enum': [ 'IDENTITY_MATRIX',
                                                             'FULL_CONNECTIVITY_MATRIX',
                                                             'HOLLOW_MATRIX',
                                                             'RANDOM_CONNECTIVITY_MATRIX'],
                                                   'type': 'string'},
                                                 { 'description': 'Explicit 2-D '
                                                                  'numeric matrix '
                                                                  '(rows = sender '
                                                                  'output size, cols = '
                                                                  'receiver input '
                                                                  'size).',
                                                   'items': { 'items': { 'type': 'number'},
                                                              'type': 'array'},
                                                   'type': 'array'}]},
                  'feedback': { 'default': False,
                                'description': 'If true, designates the projection as '
                                               'a feedback projection, breaking cycles '
                                               'in the graph. If false, the projection '
                                               'is never treated as feedback even if '
                                               'PNL would default to that.',
                                'type': 'boolean'},
                  'name': { 'description': 'Optional name for the new projection.',
                            'type': 'string'},
                  'projection': { 'description': 'Optional handle string for a '
                                                 'pre-existing Projection object to '
                                                 'add. Omit to create a default '
                                                 'MappingProjection between sender and '
                                                 'receiver.',
                                  'type': 'string'},
                  'receiver': { 'description': 'Handle string for the receiver: a '
                                               'Mechanism, Composition, or InputPort '
                                               'handle. Required when no explicit '
                                               'projection handle is given.',
                                'type': 'string'},
                  'sender': { 'description': 'Handle string for the sender: a '
                                             'Mechanism, Composition, or OutputPort '
                                             'handle. Required when no explicit '
                                             'projection handle is given.',
                              'type': 'string'}},
  'required': ['composition'],
  'type': 'object'}
TOOL_NOTES = 'IDENTITY_MATRIX requires sender output size == receiver input size exactly; passing it across mechanisms with different sizes raises FunctionError (confirmed in recent failures: sender=25, receiver=20). Use FULL_CONNECTIVITY_MATRIX for cross-size connections or omit default_matrix to let PNL choose. The runtime accepts either `default_matrix` or the legacy `matrix` kwarg name and translates both to PNL\'s `default_matrix`. DuplicateProjectionError is silently swallowed as a no-op — the call returns the existing projection. Both sender and receiver are defensively added to the composition before projection creation, so CompositionError "not (yet) in it" will not occur. If both sender and receiver are omitted, the projection handle must already encode its endpoints.'


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
        'Call this tool to wire two nodes (Mechanisms or Compositions) in a Composition with a projection — either by letting PNL create a default MappingProjection between sender and receiver, or by supplying an explicit projection handle.'
        return _impl(args or {})
