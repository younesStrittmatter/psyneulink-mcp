"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9a41d90576dc8bdaf23ffb8f21d29a8a921c07ec1713d806e0742a4ba0356889'
__pnl_qualname__ = 'psyneulink.LearningSignal'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_learning_signal'
TOOL_DESCRIPTION = 'Call this tool when you need to create a LearningSignal that will be owned by a LearningMechanism and used to modify the `matrix` parameter of one or more MappingProjections during learning. Returns a LearningSignal instance whose `learning_signal` value (output of its function) is sent via LearningProjections to modulate target MappingProjection weights.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "description": "Name or specification of the TransferFunction used to compute the learning_signal from the LearningMechanism\'s output. Default is Linear (identity), which passes the error signal through unchanged.",\n      "type": "string"\n    },\n    "modulates": {\n      "description": "List of LearningProjection or MappingProjection specifications that this LearningSignal should modulate. Determines which weight matrices are updated.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "modulation": {\n      "description": "How the learning_signal value modifies the MappingProjection matrix. Default is MULTIPLICATIVE. Use ADDITIVE to add the delta directly to weights.",\n      "enum": [\n        "MULTIPLICATIVE",\n        "ADDITIVE",\n        "OVERRIDE",\n        "DISABLE"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the LearningSignal. Defaults to \'LearningSignal\' for the first instance on an owner.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "The LearningMechanism to which this LearningSignal belongs. Usually assigned automatically when adding learning to a composition; pass explicitly only when constructing standalone.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional dict of additional parameter overrides passed to the Port constructor.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `learning_rate` is explicitly commented out in both the docstring and source as TBI — do not pass it; it will be ignored or raise an error.\n- The docstring says the default modulation is ADDITIVE, but the class signature default is MULTIPLICATIVE. The source is authoritative: use MULTIPLICATIVE unless you specifically want additive weight updates.\n- LearningSignal is almost always created implicitly when you enable learning on a Composition (e.g., `add_backpropagation_learning_pathway`); construct one explicitly only when customizing a LearningMechanism directly.\n- `value` and `learning_signal` are aliases for the same attribute (the function output).'
TOOL_PARAMETERS = { 'properties': { 'function': { 'description': 'Name or specification of the '
                                               'TransferFunction used to compute the '
                                               'learning_signal from the '
                                               "LearningMechanism's output. Default is "
                                               'Linear (identity), which passes the '
                                               'error signal through unchanged.',
                                'type': 'string'},
                  'modulates': { 'description': 'List of LearningProjection or '
                                                'MappingProjection specifications that '
                                                'this LearningSignal should modulate. '
                                                'Determines which weight matrices are '
                                                'updated.',
                                 'items': {'type': 'string'},
                                 'type': 'array'},
                  'modulation': { 'description': 'How the learning_signal value '
                                                 'modifies the MappingProjection '
                                                 'matrix. Default is MULTIPLICATIVE. '
                                                 'Use ADDITIVE to add the delta '
                                                 'directly to weights.',
                                  'enum': [ 'MULTIPLICATIVE',
                                            'ADDITIVE',
                                            'OVERRIDE',
                                            'DISABLE'],
                                  'type': 'string'},
                  'name': { 'description': 'Optional name for the LearningSignal. '
                                           "Defaults to 'LearningSignal' for the first "
                                           'instance on an owner.',
                            'type': 'string'},
                  'owner': { 'description': 'The LearningMechanism to which this '
                                            'LearningSignal belongs. Usually assigned '
                                            'automatically when adding learning to a '
                                            'composition; pass explicitly only when '
                                            'constructing standalone.',
                             'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional dict of additional parameter '
                                             'overrides passed to the Port '
                                             'constructor.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `learning_rate` is explicitly commented out in both the docstring and source as TBI — do not pass it; it will be ignored or raise an error.\n- The docstring says the default modulation is ADDITIVE, but the class signature default is MULTIPLICATIVE. The source is authoritative: use MULTIPLICATIVE unless you specifically want additive weight updates.\n- LearningSignal is almost always created implicitly when you enable learning on a Composition (e.g., `add_backpropagation_learning_pathway`); construct one explicitly only when customizing a LearningMechanism directly.\n- `value` and `learning_signal` are aliases for the same attribute (the function output).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LearningSignal
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
    def create_learning_signal(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to create a LearningSignal that will be owned by a LearningMechanism and used to modify the `matrix` parameter of one or more MappingProjections during learning.'
        return _impl(args or {})
