"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'df665d692dca9e7ce9b37a8cd72acf131887017da565bc35b875bb66d9480b7d'
__pnl_qualname__ = 'psyneulink.CompositionFunctionApproximator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_composition_function_approximator'
TOOL_DESCRIPTION = 'Use this tool when you need to instantiate a `CompositionFunctionApproximator` to serve as the `agent_rep` of an `OptimizationControlMechanism`. This is an abstract base class — call it only when implementing a custom subclass that overrides `adapt` and `prediction_parameters`; for standard use, prefer a concrete subclass such as `RegressionCFA`. The result is a `Composition`-derived object that wraps a learnable function predicting `net_outcome` from state feature values and control allocations.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "description": "Name or reference to the LearningFunction, function, or method that will be parameterized by `adapt` and called by `evaluate` to predict net_outcome. Passed through to the parent Composition as part of param_defaults.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional string identifier for the CompositionFunctionApproximator instance.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis is an abstract base class: calling `adapt(...)` or accessing `prediction_parameters` on a direct instance raises `CompositionFunctionApproximatorError`. You must subclass and implement both. `evaluate` is implemented and calls `self.function(feature_values, control_allocation)` — the num_estimates and num_trials_per_estimate arguments are accepted but not yet used (marked FIX in source). All keyword arguments beyond `name` are forwarded to the parent `Composition.__init__` via `**param_defaults`, so any valid `Composition` constructor argument is also accepted. `runs_simulations` is always `False` for this class.'
TOOL_PARAMETERS = { 'properties': { 'function': { 'description': 'Name or reference to the '
                                               'LearningFunction, function, or method '
                                               'that will be parameterized by `adapt` '
                                               'and called by `evaluate` to predict '
                                               'net_outcome. Passed through to the '
                                               'parent Composition as part of '
                                               'param_defaults.',
                                'type': 'string'},
                  'name': { 'description': 'Optional string identifier for the '
                                           'CompositionFunctionApproximator instance.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'This is an abstract base class: calling `adapt(...)` or accessing `prediction_parameters` on a direct instance raises `CompositionFunctionApproximatorError`. You must subclass and implement both. `evaluate` is implemented and calls `self.function(feature_values, control_allocation)` — the num_estimates and num_trials_per_estimate arguments are accepted but not yet used (marked FIX in source). All keyword arguments beyond `name` are forwarded to the parent `Composition.__init__` via `**param_defaults`, so any valid `Composition` constructor argument is also accepted. `runs_simulations` is always `False` for this class.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.CompositionFunctionApproximator
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
    def create_composition_function_approximator(args: dict[str, Any] | None = None) -> Any:
        'Use this tool when you need to instantiate a `CompositionFunctionApproximator` to serve as the `agent_rep` of an `OptimizationControlMechanism`.'
        return _impl(args or {})
