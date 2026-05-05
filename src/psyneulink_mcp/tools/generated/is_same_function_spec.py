"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0bf7536a90a756a62ba54d7288758fe74b394dfa051baf58fa5d1d44fba01f80'
__pnl_qualname__ = 'psyneulink.is_same_function_spec'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_same_function_spec'
TOOL_DESCRIPTION = 'Call this tool when you need to check whether two PsyNeuLink Function specifications refer to the same Function class — for example, before deciding whether to replace or reuse a component\'s function. Returns True only when both arguments resolve to the same PsyNeuLink Function subclass; returns False if either argument is a plain Python callable (not a PNL Function), even if they are identical objects.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "fct_spec_1": {\n      "description": "Name of the first PsyNeuLink Function class to compare (e.g. \'Linear\', \'Logistic\', \'ReLU\'). Must be a valid PsyNeuLink Function subclass name.",\n      "type": "string"\n    },\n    "fct_spec_2": {\n      "description": "Name of the second PsyNeuLink Function class to compare (e.g. \'Linear\', \'Logistic\', \'ReLU\'). Must be a valid PsyNeuLink Function subclass name.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "fct_spec_1",\n    "fct_spec_2"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns False whenever either argument is not a PsyNeuLink Function class or instance — non-PNL callables (plain Python functions, lambdas, methods) always yield False even when both arguments are identical. Comparison is by class identity (type equality), so an instance and its own class are treated as the same spec, but two different subclasses are not equal even if functionally similar.'
TOOL_PARAMETERS = { 'properties': { 'fct_spec_1': { 'description': 'Name of the first PsyNeuLink '
                                                 'Function class to compare (e.g. '
                                                 "'Linear', 'Logistic', 'ReLU'). Must "
                                                 'be a valid PsyNeuLink Function '
                                                 'subclass name.',
                                  'type': 'string'},
                  'fct_spec_2': { 'description': 'Name of the second PsyNeuLink '
                                                 'Function class to compare (e.g. '
                                                 "'Linear', 'Logistic', 'ReLU'). Must "
                                                 'be a valid PsyNeuLink Function '
                                                 'subclass name.',
                                  'type': 'string'}},
  'required': ['fct_spec_1', 'fct_spec_2'],
  'type': 'object'}
TOOL_NOTES = 'Returns False whenever either argument is not a PsyNeuLink Function class or instance — non-PNL callables (plain Python functions, lambdas, methods) always yield False even when both arguments are identical. Comparison is by class identity (type equality), so an instance and its own class are treated as the same spec, but two different subclasses are not equal even if functionally similar.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_same_function_spec
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
    def is_same_function_spec(args: dict[str, Any] | None = None) -> Any:
        "Call this tool when you need to check whether two PsyNeuLink Function specifications refer to the same Function class — for example, before deciding whether to replace or reuse a component's function."
        return _impl(args or {})
