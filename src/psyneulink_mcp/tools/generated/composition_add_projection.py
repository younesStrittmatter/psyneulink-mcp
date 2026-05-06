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
TOOL_DESCRIPTION = 'Wire one node to another inside an existing Composition by adding a Projection between a sender and a receiver. Call this after creating both endpoint handles (Mechanisms or nested Compositions) when you need explicit connectivity beyond what a pathway-based constructor provides; you do NOT need to pre-add the endpoints with add_node — the runtime ensures both are members of the composition before wiring. Returns nothing meaningful to the agent (the live Projection stays inside PNL); a successful call means the edge exists.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle of the Composition to add the projection into, as returned by a Composition-creating tool.",\n      "type": "string"\n    },\n    "default_matrix": {\n      "description": "Weight matrix used when auto-creating a default MappingProjection (ignored if `projection` is given). Either a 2-D numeric array shaped (sender_size, receiver_size), or a PNL matrix-keyword string: \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'HOLLOW_MATRIX\', \'RANDOM_CONNECTIVITY_MATRIX\', \'INVERSE_HOLLOW_MATRIX\', \'AUTO_ASSOCIATIVE_MATRIX\'. Pass this kwarg as `default_matrix` (NOT `matrix`); the helper also accepts the alias `matrix` and translates it.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "feedback": {\n      "default": false,\n      "description": "If True, force-mark this projection as a feedback edge that breaks cycles in the composition graph. Default False (PNL\'s normal cycle-detection rules apply).",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Optional human-readable name for the auto-created default Projection. Ignored when `projection` is supplied.",\n      "type": "string"\n    },\n    "projection": {\n      "description": "Optional handle of a pre-built Projection (e.g. a MappingProjection, ControlProjection, LearningProjection) to install. Omit to auto-create a default MappingProjection between sender and receiver.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Handle of the receiver Mechanism, nested Composition, or InputPort. The runtime resolves the string and adds it to the composition first. NOTE: if this resolves to a nested Composition with multiple INPUT nodes (e.g. an EMComposition with several QUERY fields), the projection is routed via the input_CIM to the FIRST INPUT node \\u2014 this tool has no parameter to pick a specific field/port. To target a specific field, pass the InputPort handle of the desired inner node directly as the receiver instead of the outer Composition handle.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Handle of the sender Mechanism, nested Composition, or OutputPort. The runtime resolves the string to the live PNL object and (defensively) adds it to the composition first.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "sender",\n    "receiver"\n  ],\n  "type": "object"\n}\n\nNotes:\n- The runtime helper defensively calls add_node for sender and receiver before wiring, so do not separately add_node first; a DuplicateProjectionError from PNL is treated as a no-op success, so retrying the same add_projection call is safe.\n- Use `default_matrix`, not `matrix`. PNL has a known parameter-port bug when `matrix` is passed directly to a free-standing MappingProjection; the helper avoids it by translating both names to PNL\'s `default_matrix` kwarg.\n- Matrix-keyword strings like \'IDENTITY_MATRIX\' must be uppercase and are case-sensitive; numeric arrays must be 2-D and dimensionally compatible with the sender\'s output and receiver\'s input sizes.\n- Nested-Composition receivers route through the input_CIM to the FIRST INPUT node found; there is no `receiver_port`/`target_field` argument here. For multi-input nested Compositions (e.g. EMComposition with several QUERY fields), pass the inner node\'s InputPort handle as `receiver` directly to disambiguate.\n- If a projection already exists between the same sender Port and receiver Port within the composition, the request is silently ignored and the existing edge is reused; if multiple exist outside the composition, the most recent one is adopted (a warning may be emitted).\n- ControlProjections and LearningProjections are accepted as `projection`, but ModulatoryProjection routing differs from MappingProjection — pass a fully constructed projection handle if you need non-default modulatory behavior.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle of the Composition to add '
                                                  'the projection into, as returned by '
                                                  'a Composition-creating tool.',
                                   'type': 'string'},
                  'default_matrix': { 'description': 'Weight matrix used when '
                                                     'auto-creating a default '
                                                     'MappingProjection (ignored if '
                                                     '`projection` is given). Either a '
                                                     '2-D numeric array shaped '
                                                     '(sender_size, receiver_size), or '
                                                     'a PNL matrix-keyword string: '
                                                     "'IDENTITY_MATRIX', "
                                                     "'FULL_CONNECTIVITY_MATRIX', "
                                                     "'HOLLOW_MATRIX', "
                                                     "'RANDOM_CONNECTIVITY_MATRIX', "
                                                     "'INVERSE_HOLLOW_MATRIX', "
                                                     "'AUTO_ASSOCIATIVE_MATRIX'. Pass "
                                                     'this kwarg as `default_matrix` '
                                                     '(NOT `matrix`); the helper also '
                                                     'accepts the alias `matrix` and '
                                                     'translates it.',
                                      'oneOf': [ {'type': 'string'},
                                                 { 'items': { 'items': { 'type': 'number'},
                                                              'type': 'array'},
                                                   'type': 'array'}]},
                  'feedback': { 'default': False,
                                'description': 'If True, force-mark this projection as '
                                               'a feedback edge that breaks cycles in '
                                               'the composition graph. Default False '
                                               "(PNL's normal cycle-detection rules "
                                               'apply).',
                                'type': 'boolean'},
                  'name': { 'description': 'Optional human-readable name for the '
                                           'auto-created default Projection. Ignored '
                                           'when `projection` is supplied.',
                            'type': 'string'},
                  'projection': { 'description': 'Optional handle of a pre-built '
                                                 'Projection (e.g. a '
                                                 'MappingProjection, '
                                                 'ControlProjection, '
                                                 'LearningProjection) to install. Omit '
                                                 'to auto-create a default '
                                                 'MappingProjection between sender and '
                                                 'receiver.',
                                  'type': 'string'},
                  'receiver': { 'description': 'Handle of the receiver Mechanism, '
                                               'nested Composition, or InputPort. The '
                                               'runtime resolves the string and adds '
                                               'it to the composition first. NOTE: if '
                                               'this resolves to a nested Composition '
                                               'with multiple INPUT nodes (e.g. an '
                                               'EMComposition with several QUERY '
                                               'fields), the projection is routed via '
                                               'the input_CIM to the FIRST INPUT node '
                                               '— this tool has no parameter to pick a '
                                               'specific field/port. To target a '
                                               'specific field, pass the InputPort '
                                               'handle of the desired inner node '
                                               'directly as the receiver instead of '
                                               'the outer Composition handle.',
                                'type': 'string'},
                  'sender': { 'description': 'Handle of the sender Mechanism, nested '
                                             'Composition, or OutputPort. The runtime '
                                             'resolves the string to the live PNL '
                                             'object and (defensively) adds it to the '
                                             'composition first.',
                              'type': 'string'}},
  'required': ['composition', 'sender', 'receiver'],
  'type': 'object'}
TOOL_NOTES = "- The runtime helper defensively calls add_node for sender and receiver before wiring, so do not separately add_node first; a DuplicateProjectionError from PNL is treated as a no-op success, so retrying the same add_projection call is safe.\n- Use `default_matrix`, not `matrix`. PNL has a known parameter-port bug when `matrix` is passed directly to a free-standing MappingProjection; the helper avoids it by translating both names to PNL's `default_matrix` kwarg.\n- Matrix-keyword strings like 'IDENTITY_MATRIX' must be uppercase and are case-sensitive; numeric arrays must be 2-D and dimensionally compatible with the sender's output and receiver's input sizes.\n- Nested-Composition receivers route through the input_CIM to the FIRST INPUT node found; there is no `receiver_port`/`target_field` argument here. For multi-input nested Compositions (e.g. EMComposition with several QUERY fields), pass the inner node's InputPort handle as `receiver` directly to disambiguate.\n- If a projection already exists between the same sender Port and receiver Port within the composition, the request is silently ignored and the existing edge is reused; if multiple exist outside the composition, the most recent one is adopted (a warning may be emitted).\n- ControlProjections and LearningProjections are accepted as `projection`, but ModulatoryProjection routing differs from MappingProjection — pass a fully constructed projection handle if you need non-default modulatory behavior."


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
        'Wire one node to another inside an existing Composition by adding a Projection between a sender and a receiver.'
        return _impl(args or {})
