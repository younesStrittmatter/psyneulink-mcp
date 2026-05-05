"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4c4e2d4902fd6f8255a834c8fc9944766856760ab658825f309773fa3b0bf1a9'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.modulatory.learning.learningmechanism.LearningTiming'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_learning_timing'
TOOL_DESCRIPTION = 'Call this tool to obtain a `LearningTiming` enum member that specifies when a LearningMechanism executes within a Composition\'s run cycle. Use it when constructing or configuring a LearningMechanism and you need to pass a `learning_timing` value: choose `EXECUTION_PHASE` (value 0) to run learning immediately after the target Mechanism executes, or `LEARNING_PHASE` (value 1) to defer learning to a separate learning phase.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Integer value selecting the enum member: 0 = EXECUTION_PHASE (learn right after the learned Mechanism runs), 1 = LEARNING_PHASE (learn during the Composition\'s dedicated learning phase).",\n      "enum": [\n        0,\n        1\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is an Enum class; the only valid call forms are `LearningTiming(0)` and `LearningTiming(1)`. Keyword argument passing is not supported by Python\'s Enum machinery — the host template must unpack the `value` field as a positional argument, not `**kwargs`. In practice, agents rarely need to call this tool directly; instead, pass the string literal `"EXECUTION_PHASE"` or `"LEARNING_PHASE"` where a `learning_timing` parameter is accepted and PsyNeuLink will coerce it. Use this tool only if you need an actual enum instance.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Integer value selecting the enum member: '
                                            '0 = EXECUTION_PHASE (learn right after '
                                            'the learned Mechanism runs), 1 = '
                                            'LEARNING_PHASE (learn during the '
                                            "Composition's dedicated learning phase).",
                             'enum': [0, 1],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'This is an Enum class; the only valid call forms are `LearningTiming(0)` and `LearningTiming(1)`. Keyword argument passing is not supported by Python\'s Enum machinery — the host template must unpack the `value` field as a positional argument, not `**kwargs`. In practice, agents rarely need to call this tool directly; instead, pass the string literal `"EXECUTION_PHASE"` or `"LEARNING_PHASE"` where a `learning_timing` parameter is accepted and PsyNeuLink will coerce it. Use this tool only if you need an actual enum instance.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LearningTiming
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
    def create_learning_timing(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to obtain a `LearningTiming` enum member that specifies when a LearningMechanism executes within a Composition's run cycle."
        return _impl(args or {})
