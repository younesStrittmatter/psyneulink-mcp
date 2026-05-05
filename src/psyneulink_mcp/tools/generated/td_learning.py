"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7dd33424d7002d1662d78a0fe553f88462bdfd8b6d4efb3a6dcd3d6ad0dd0425'
__pnl_qualname__ = 'psyneulink.TDLearning'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_td_learning'
TOOL_DESCRIPTION = 'Call this tool to create a TDLearning function instance, which implements temporal difference (TD) learning as a variant of reinforcement learning. Use it when building a LearningMechanism that requires TD-style credit assignment across a sequence of states rather than single-step reward prediction. The result is a TDLearning function object that can be passed as the `function` argument to a LearningMechanism.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "A list of exactly three arrays: [activation_input, activation_output, error_signal]. Must have exactly 3 elements; omit to let PsyNeuLink infer from the owning mechanism.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "maxItems": 3,\n      "minItems": 3,\n      "type": "array"\n    },\n    "learning_rate": {\n      "default": 0.05,\n      "description": "Fraction of the prediction error used to update weights on each trial. Defaults to 0.05.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nTDLearning delegates entirely to the Reinforcement superclass; the only behavioral difference is that `default_variable` must contain exactly 3 sub-arrays (activation_input, activation_output, error_signal) — passing any other number raises a ComponentError. The `params`, `owner`, and `prefs` arguments are advanced PsyNeuLink internals; omit them unless you have a specific need. The default learning_rate is 0.05 (from the docstring, not the class body). Despite the temporal-difference name, the underlying update rule is the same single-step delta rule as Reinforcement — true multi-step TD requires the surrounding Composition/LearningMechanism wiring to supply appropriate error signals.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'A list of exactly three '
                                                       'arrays: [activation_input, '
                                                       'activation_output, '
                                                       'error_signal]. Must have '
                                                       'exactly 3 elements; omit to '
                                                       'let PsyNeuLink infer from the '
                                                       'owning mechanism.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'maxItems': 3,
                                        'minItems': 3,
                                        'type': 'array'},
                  'learning_rate': { 'default': 0.05,
                                     'description': 'Fraction of the prediction error '
                                                    'used to update weights on each '
                                                    'trial. Defaults to 0.05.',
                                     'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'TDLearning delegates entirely to the Reinforcement superclass; the only behavioral difference is that `default_variable` must contain exactly 3 sub-arrays (activation_input, activation_output, error_signal) — passing any other number raises a ComponentError. The `params`, `owner`, and `prefs` arguments are advanced PsyNeuLink internals; omit them unless you have a specific need. The default learning_rate is 0.05 (from the docstring, not the class body). Despite the temporal-difference name, the underlying update rule is the same single-step delta rule as Reinforcement — true multi-step TD requires the surrounding Composition/LearningMechanism wiring to supply appropriate error signals.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.TDLearning
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
    def create_td_learning(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a TDLearning function instance, which implements temporal difference (TD) learning as a variant of reinforcement learning.'
        return _impl(args or {})
