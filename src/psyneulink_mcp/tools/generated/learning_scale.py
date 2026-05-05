"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0080ac1932a392268ea935ebfe98a84438bac2e9345b33e4e51eaf4088d51046'
__pnl_qualname__ = 'psyneulink.LearningScale'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_learning_scale'
TOOL_DESCRIPTION = 'Call this tool when you need to retrieve a LearningScale enum value to pass to learning-related parameters of a Composition (e.g., to specify at what granularity callbacks or weight updates occur during Composition.learn()). Returns a LearningScale enum member corresponding to the requested scale (OPTIMIZATION_STEP, MINIBATCH, EPOCH, RUN, or TRIAL).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Which learning scale to retrieve. OPTIMIZATION_STEP: a single gradient step within a minibatch. MINIBATCH: one subset of the training set (one gradient update). EPOCH: a full pass through the training set. RUN: the full execution of Composition.learn() across all epochs. TRIAL: equivalent to MINIBATCH only when minibatch_size=1.",\n      "enum": [\n        "OPTIMIZATION_STEP",\n        "TRIAL",\n        "MINIBATCH",\n        "EPOCH",\n        "RUN"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nTRIAL is only safe when Composition.minibatch_size=1; using TRIAL with minibatch_size>1 raises a warning and can produce unanticipated results — prefer MINIBATCH in that case. The number of gradient steps per EPOCH depends on both mini_batch_size and optimizations_per_minibatch Composition parameters.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Which learning scale to retrieve. '
                                            'OPTIMIZATION_STEP: a single gradient step '
                                            'within a minibatch. MINIBATCH: one subset '
                                            'of the training set (one gradient '
                                            'update). EPOCH: a full pass through the '
                                            'training set. RUN: the full execution of '
                                            'Composition.learn() across all epochs. '
                                            'TRIAL: equivalent to MINIBATCH only when '
                                            'minibatch_size=1.',
                             'enum': [ 'OPTIMIZATION_STEP',
                                       'TRIAL',
                                       'MINIBATCH',
                                       'EPOCH',
                                       'RUN'],
                             'type': 'string'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'TRIAL is only safe when Composition.minibatch_size=1; using TRIAL with minibatch_size>1 raises a warning and can produce unanticipated results — prefer MINIBATCH in that case. The number of gradient steps per EPOCH depends on both mini_batch_size and optimizations_per_minibatch Composition parameters.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LearningScale
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
    def create_learning_scale(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to retrieve a LearningScale enum value to pass to learning-related parameters of a Composition (e.g., to specify at what granularity callbacks or weight updates occur during Composition.learn()).'
        return _impl(args or {})
