"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'fe2c671ee055638a7ef43f927a672800fb38148840b483fe333951a891b333f6'
__pnl_qualname__ = 'psyneulink.CompositionRunner'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_composition_runner'
TOOL_DESCRIPTION = 'Use this tool to instantiate a CompositionRunner that wraps a PsyNeuLink Composition for minibatch gradient-descent training. Call it when you need to train an AutodiffComposition (or a backprop-enabled Composition) across multiple epochs with configurable minibatch size, early stopping, and execution mode; the returned instance exposes run_learning() to execute the training loop and return the final trial\'s output array.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "compostion": {\n      "description": "Name or reference of the PsyNeuLink Composition (typically an AutodiffComposition) to wrap. Note: the parameter is intentionally spelled \'compostion\' (missing \'i\') in the PNL source \\u2014 use this exact spelling.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "compostion"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe constructor parameter is misspelled as `compostion` (not `composition`) in the PNL source — pass it under that exact key or the call will fail with an unexpected-keyword-argument error. CompositionRunner is primarily designed for AutodiffComposition; for plain Composition it computes loss by summing ObjectiveMechanism (comparator) values from _terminal_backprop_sequences, which may not exist on all Compositions. The main public method after instantiation is run_learning(inputs, targets, epochs, minibatch_size, learning_rate, patience, execution_mode, …); the constructor itself does no computation. In PyTorch execution_mode, synch_with_pnl_options and retain_in_pnl_options must be provided to run_learning to control weight synchronization cadence (OPTIMIZATION_STEP / TRIAL / MINIBATCH / EPOCH). Early stopping (patience/min_delta) is silently disabled in compiled (LLVM) execution modes.'
TOOL_PARAMETERS = { 'properties': { 'compostion': { 'description': 'Name or reference of the PsyNeuLink '
                                                 'Composition (typically an '
                                                 'AutodiffComposition) to wrap. Note: '
                                                 'the parameter is intentionally '
                                                 "spelled 'compostion' (missing 'i') "
                                                 'in the PNL source — use this exact '
                                                 'spelling.',
                                  'type': 'string'}},
  'required': ['compostion'],
  'type': 'object'}
TOOL_NOTES = 'The constructor parameter is misspelled as `compostion` (not `composition`) in the PNL source — pass it under that exact key or the call will fail with an unexpected-keyword-argument error. CompositionRunner is primarily designed for AutodiffComposition; for plain Composition it computes loss by summing ObjectiveMechanism (comparator) values from _terminal_backprop_sequences, which may not exist on all Compositions. The main public method after instantiation is run_learning(inputs, targets, epochs, minibatch_size, learning_rate, patience, execution_mode, …); the constructor itself does no computation. In PyTorch execution_mode, synch_with_pnl_options and retain_in_pnl_options must be provided to run_learning to control weight synchronization cadence (OPTIMIZATION_STEP / TRIAL / MINIBATCH / EPOCH). Early stopping (patience/min_delta) is silently disabled in compiled (LLVM) execution modes.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.CompositionRunner
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
    def create_composition_runner(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to instantiate a CompositionRunner that wraps a PsyNeuLink Composition for minibatch gradient-descent training.'
        return _impl(args or {})
