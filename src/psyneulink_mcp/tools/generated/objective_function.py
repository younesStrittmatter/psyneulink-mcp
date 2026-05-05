"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '3ea0d478634c848552554cbde082907dd033f2425d49da77691284ad124c76b7'
__pnl_qualname__ = 'psyneulink.ObjectiveFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_objective_function'
TOOL_DESCRIPTION = 'Call this tool to instantiate a PsyNeuLink ObjectiveFunction, the abstract base class for functions that evaluate and compare port values (e.g., for use in control or learning mechanisms). In practice, you should call a concrete subclass (such as Distance or Stability) rather than ObjectiveFunction directly, since this class is abstract and cannot be run on its own. Use it only when you need to reference the base type or inspect shared parameters.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "metric": {\n      "description": "The metric used to evaluate or compare port values (e.g., \'EUCLIDEAN\', \'COSINE\', \'CORRELATION\'). Defaults to None; concrete subclasses may override or require this.",\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "Whether to normalize the result of the metric computation. Defaults to False.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nObjectiveFunction is abstract — instantiating it directly will raise a TypeError or produce a non-functional object. Always use a concrete subclass (Distance, Stability, etc.) in practice. The `metric` parameter accepts PsyNeuLink metric keyword strings, not numeric values. The valid set of metric strings depends on the concrete subclass.'
TOOL_PARAMETERS = { 'properties': { 'metric': { 'description': 'The metric used to evaluate or compare '
                                             "port values (e.g., 'EUCLIDEAN', "
                                             "'COSINE', 'CORRELATION'). Defaults to "
                                             'None; concrete subclasses may override '
                                             'or require this.',
                              'type': 'string'},
                  'normalize': { 'default': False,
                                 'description': 'Whether to normalize the result of '
                                                'the metric computation. Defaults to '
                                                'False.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'ObjectiveFunction is abstract — instantiating it directly will raise a TypeError or produce a non-functional object. Always use a concrete subclass (Distance, Stability, etc.) in practice. The `metric` parameter accepts PsyNeuLink metric keyword strings, not numeric values. The valid set of metric strings depends on the concrete subclass.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ObjectiveFunction
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
    def create_objective_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a PsyNeuLink ObjectiveFunction, the abstract base class for functions that evaluate and compare port values (e.g., for use in control or learning mechanisms).'
        return _impl(args or {})
