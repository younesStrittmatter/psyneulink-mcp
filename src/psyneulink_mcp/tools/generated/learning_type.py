"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9d976db4f304a94469a61817604e731a2b104674b6fe1856445b31259b380f4d'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.modulatory.learning.learningmechanism.LearningType'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_learning_type'
TOOL_DESCRIPTION = 'Call this tool when you need to obtain a LearningType enum member to pass as the `learning_type` argument of a LearningMechanism. Returns either LearningType.UNSUPERVISED (requires an incoming ERROR_SIGNAL Projection) or LearningType.SUPERVISED (no ERROR_SIGNAL InputPort). Use this to make the learning modality explicit rather than relying on defaults.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Integer value of the enum member: 0 for UNSUPERVISED (requires ERROR_SIGNAL InputPort), 1 for SUPERVISED (no ERROR_SIGNAL InputPort).",\n      "enum": [\n        0,\n        1\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe docstring attribute descriptions appear inverted relative to everyday ML terminology: in PsyNeuLink, UNSUPERVISED implements and *requires* a Projection to an ERROR_SIGNAL InputPort, while SUPERVISED does *not* implement one. Verify the intended learning rule before choosing a value. You can also reference the members directly as `LearningType.UNSUPERVISED` or `LearningType.SUPERVISED` in any PsyNeuLink context without calling this tool.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Integer value of the enum member: 0 for '
                                            'UNSUPERVISED (requires ERROR_SIGNAL '
                                            'InputPort), 1 for SUPERVISED (no '
                                            'ERROR_SIGNAL InputPort).',
                             'enum': [0, 1],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'The docstring attribute descriptions appear inverted relative to everyday ML terminology: in PsyNeuLink, UNSUPERVISED implements and *requires* a Projection to an ERROR_SIGNAL InputPort, while SUPERVISED does *not* implement one. Verify the intended learning rule before choosing a value. You can also reference the members directly as `LearningType.UNSUPERVISED` or `LearningType.SUPERVISED` in any PsyNeuLink context without calling this tool.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LearningType
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
    def create_learning_type(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to obtain a LearningType enum member to pass as the `learning_type` argument of a LearningMechanism.'
        return _impl(args or {})
