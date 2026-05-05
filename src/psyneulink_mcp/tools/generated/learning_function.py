"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8c83ea25310b97195970c54ae75e7234d7e82220c7b03691a8be4abc93c33adc'
__pnl_qualname__ = 'psyneulink.LearningFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_learning_function'
TOOL_DESCRIPTION = 'Call this tool only when you need to inspect or reference the abstract LearningFunction base class itself — not to instantiate it. LearningFunction is the abstract superclass for all PsyNeuLink learning functions (Hebbian, BackPropagation, TDLearning, etc.); it cannot be instantiated directly and will raise an error if you try. Use concrete subclass tools (e.g., Hebbian, BackPropagation) to actually create a learning function.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "default": [\n        0,\n        0,\n        0\n      ],\n      "description": "Template for the function\'s input. Most LearningFunctions expect a 3-element array: [activation_input, activation_output, error_output]. Exact layout depends on the concrete subclass.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "learning_rate": {\n      "default": 0.05,\n      "description": "Scalar multiplier applied to the learning update. Defaults to 0.05. Can be overridden at the LearningMechanism or Composition level at runtime.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nLearningFunction is abstract — instantiating it directly raises an error. Always use a concrete subclass (Hebbian, BackPropagation, Reinforcement, TDLearning, etc.). The learning_rate here is the function-level default; it is overridden by learning_rate set on the LearningMechanism, Composition, or passed to Composition.learn() at runtime — in that priority order. The variable is read-only after construction; pass the shape you need via default_variable at construction time.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'default': [0, 0, 0],
                                        'description': "Template for the function's "
                                                       'input. Most LearningFunctions '
                                                       'expect a 3-element array: '
                                                       '[activation_input, '
                                                       'activation_output, '
                                                       'error_output]. Exact layout '
                                                       'depends on the concrete '
                                                       'subclass.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'learning_rate': { 'default': 0.05,
                                     'description': 'Scalar multiplier applied to the '
                                                    'learning update. Defaults to '
                                                    '0.05. Can be overridden at the '
                                                    'LearningMechanism or Composition '
                                                    'level at runtime.',
                                     'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'LearningFunction is abstract — instantiating it directly raises an error. Always use a concrete subclass (Hebbian, BackPropagation, Reinforcement, TDLearning, etc.). The learning_rate here is the function-level default; it is overridden by learning_rate set on the LearningMechanism, Composition, or passed to Composition.learn() at runtime — in that priority order. The variable is read-only after construction; pass the shape you need via default_variable at construction time.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LearningFunction
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
    def create_learning_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to inspect or reference the abstract LearningFunction base class itself — not to instantiate it.'
        return _impl(args or {})
