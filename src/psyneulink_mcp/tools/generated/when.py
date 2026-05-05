"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '67b044181eb054ef98fc334eb753c44520b52a77bed42fb782bd6a7eb5856b74'
__pnl_qualname__ = 'psyneulink.When'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_when'
TOOL_DESCRIPTION = 'Call this tool to attach a custom predicate-based scheduling condition to a PsyNeuLink node — use it when no built-in condition (AfterNPasses, EveryNCalls, etc.) expresses the logic you need. The tool instantiates a `When` (Condition) object that the Scheduler evaluates each trial; the node executes only when `func(*args, **kwargs)` returns truthy.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "args": {\n      "default": [],\n      "description": "Positional arguments forwarded to func at each evaluation. Typically empty for lambdas that close over the scheduler/owner.",\n      "items": {},\n      "type": "array"\n    },\n    "func": {\n      "description": "Python expression string for the predicate callable (e.g. \'lambda owner, scheduler: owner.value[0][0] > 0.5\'). Evaluated at instantiation; must be a zero-side-effect callable that returns a bool-like value.",\n      "type": "string"\n    },\n    "kwargs": {\n      "additionalProperties": true,\n      "default": {},\n      "description": "Keyword arguments forwarded to func at each evaluation.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "func"\n  ],\n  "type": "object"\n}\n\nNotes:\nPrefer built-in condition tools (AfterNPasses, EveryNCalls, AtRunStart, etc.) over When whenever possible — they are safer and MDF-serializable. When is for custom logic only. The func string is eval\'d by the host template; it must be a valid Python lambda or callable expression. The callable receives no implicit arguments unless you wire them through args/kwargs — inspect what Scheduler passes at eval time if you need owner or trial-count references. Condition objects are not re-evaluated until the Scheduler ticks, so avoid closures over rapidly-mutating external state.'
TOOL_PARAMETERS = { 'properties': { 'args': { 'default': [],
                            'description': 'Positional arguments forwarded to func at '
                                           'each evaluation. Typically empty for '
                                           'lambdas that close over the '
                                           'scheduler/owner.',
                            'items': {},
                            'type': 'array'},
                  'func': { 'description': 'Python expression string for the predicate '
                                           "callable (e.g. 'lambda owner, scheduler: "
                                           "owner.value[0][0] > 0.5'). Evaluated at "
                                           'instantiation; must be a zero-side-effect '
                                           'callable that returns a bool-like value.',
                            'type': 'string'},
                  'kwargs': { 'additionalProperties': True,
                              'default': {},
                              'description': 'Keyword arguments forwarded to func at '
                                             'each evaluation.',
                              'type': 'object'}},
  'required': ['func'],
  'type': 'object'}
TOOL_NOTES = "Prefer built-in condition tools (AfterNPasses, EveryNCalls, AtRunStart, etc.) over When whenever possible — they are safer and MDF-serializable. When is for custom logic only. The func string is eval'd by the host template; it must be a valid Python lambda or callable expression. The callable receives no implicit arguments unless you wire them through args/kwargs — inspect what Scheduler passes at eval time if you need owner or trial-count references. Condition objects are not re-evaluated until the Scheduler ticks, so avoid closures over rapidly-mutating external state."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.When
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
    def create_when(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to attach a custom predicate-based scheduling condition to a PsyNeuLink node — use it when no built-in condition (AfterNPasses, EveryNCalls, etc.) expresses the logic you need.'
        return _impl(args or {})
