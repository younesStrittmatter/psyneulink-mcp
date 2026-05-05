"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'dd8e4abdbc469153c8eca21637accc88b976e02260bc44e636d3daf5dd74e74f'
__pnl_qualname__ = 'psyneulink.Reinforcement'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_reinforcement'
TOOL_DESCRIPTION = 'Call this tool to instantiate a Reinforcement learning function for single-action reinforcement learning (e.g., Q-learning or TD-learning on a discrete action selection). Use it when you need a LearningFunction that updates only the weight corresponding to the chosen action/stimulus — the one non-zero element in the activation output — by scaling the error signal by the learning rate. The result is an error array of the same length as the activation output, with Δw = learning_rate × error_signal at the selected action index and zero elsewhere.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template 2d array with exactly 3 items: [activation_input (1d, unused), activation_output (1d, exactly one non-zero value representing the chosen action/stimulus), error_signal (1d with a single scalar element)]. Example: [[0], [0, 1, 0], [0.3]].",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "learning_rate": {\n      "description": "Scales the error signal to produce the weight change. Defaults to 0.05 if not specified here or via the owning LearningMechanism.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Name for this Reinforcement function instance.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter names, values override defaults.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The variable passed at call time (and default_variable) MUST have exactly 3 items — even though only items [1] and [2] are used. Passing 2 items raises a ComponentError.\n- activation_output (variable[1]) must have AT MOST one non-zero value. Multiple non-zero values raise a ComponentError; this often means the upstream SoftMax needs its output arg set to \'PROB\'.\n- error_signal (variable[2]) must be a 1d array with exactly one scalar element.\n- The function returns TWO copies of the same error array (both identical) — the first is a placeholder for the weight-change matrix that other LearningFunctions return. Callers should be aware they get a list of two arrays, not one.\n- Default learning_rate is 0.05; if None is passed the function falls back to this default silently.\n- activation_input (variable[0]) is completely ignored at runtime but must be present for API compatibility with other LearningFunctions.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template 2d array with exactly '
                                                       '3 items: [activation_input '
                                                       '(1d, unused), '
                                                       'activation_output (1d, exactly '
                                                       'one non-zero value '
                                                       'representing the chosen '
                                                       'action/stimulus), error_signal '
                                                       '(1d with a single scalar '
                                                       'element)]. Example: [[0], [0, '
                                                       '1, 0], [0.3]].',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'learning_rate': { 'description': 'Scales the error signal to '
                                                    'produce the weight change. '
                                                    'Defaults to 0.05 if not specified '
                                                    'here or via the owning '
                                                    'LearningMechanism.',
                                     'type': 'number'},
                  'name': { 'description': 'Name for this Reinforcement function '
                                           'instance.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter names, values override '
                                             'defaults.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- The variable passed at call time (and default_variable) MUST have exactly 3 items — even though only items [1] and [2] are used. Passing 2 items raises a ComponentError.\n- activation_output (variable[1]) must have AT MOST one non-zero value. Multiple non-zero values raise a ComponentError; this often means the upstream SoftMax needs its output arg set to 'PROB'.\n- error_signal (variable[2]) must be a 1d array with exactly one scalar element.\n- The function returns TWO copies of the same error array (both identical) — the first is a placeholder for the weight-change matrix that other LearningFunctions return. Callers should be aware they get a list of two arrays, not one.\n- Default learning_rate is 0.05; if None is passed the function falls back to this default silently.\n- activation_input (variable[0]) is completely ignored at runtime but must be present for API compatibility with other LearningFunctions."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Reinforcement
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
    def create_reinforcement(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a Reinforcement learning function for single-action reinforcement learning (e.g., Q-learning or TD-learning on a discrete action selection).'
        return _impl(args or {})
