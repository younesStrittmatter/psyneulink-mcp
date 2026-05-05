"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '67b044181eb054ef98fc334eb753c44520b52a77bed42fb782bd6a7eb5856b74'
__pnl_qualname__ = 'psyneulink.Condition'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_condition'
TOOL_DESCRIPTION = 'Use this tool only when no named Condition subclass (AfterNCalls, Always, EveryNCalls, AtPass, etc.) fits your scheduling need and you must supply a custom Python callable as the condition test. Returns a Condition object that wraps the callable; pass it to a Scheduler or as a node condition in a Composition to gate execution. Prefer the specific named-condition tools — call this base tool only when the logic cannot be expressed as one of them.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "args": {\n      "description": "Positional arguments forwarded to func each time the condition is evaluated. JSON-serializable values only.",\n      "items": {},\n      "type": "array"\n    },\n    "func": {\n      "description": "Fully-qualified name or importable expression of the Python callable to evaluate (e.g. \'mymodule.my_condition_fn\'). The callable must be resolvable in the server\'s Python environment. It receives *args and **kwargs at evaluation time and must return a truthy value when the condition is satisfied.",\n      "type": "string"\n    },\n    "kwargs": {\n      "additionalProperties": true,\n      "description": "Keyword arguments forwarded to func each time the condition is evaluated. JSON-serializable values only.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "func"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe base Condition class is rarely what you want. PsyNeuLink ships dozens of named subclasses (AfterNCalls, Always, Never, EveryNCalls, AtPass, AfterPass, WhenFinished, etc.) — each has its own generated MCP tool with a stricter schema. Use those first. This tool is the fallback for logic that truly cannot be expressed by any named subclass. The func string must resolve to a Python callable in the server process; passing a lambda string or arbitrary expression will fail. args and kwargs are passed through directly to func on every is_satisfied() call, not just at construction time, so avoid mutable defaults. Condition is also the base for MDF serialisation (as_mdf_model); if you need MDF export, only named subclasses serialise cleanly — a custom func may fall back to dill-serialising the callable.'
TOOL_PARAMETERS = { 'properties': { 'args': { 'description': 'Positional arguments forwarded to func '
                                           'each time the condition is evaluated. '
                                           'JSON-serializable values only.',
                            'items': {},
                            'type': 'array'},
                  'func': { 'description': 'Fully-qualified name or importable '
                                           'expression of the Python callable to '
                                           'evaluate (e.g. '
                                           "'mymodule.my_condition_fn'). The callable "
                                           "must be resolvable in the server's Python "
                                           'environment. It receives *args and '
                                           '**kwargs at evaluation time and must '
                                           'return a truthy value when the condition '
                                           'is satisfied.',
                            'type': 'string'},
                  'kwargs': { 'additionalProperties': True,
                              'description': 'Keyword arguments forwarded to func each '
                                             'time the condition is evaluated. '
                                             'JSON-serializable values only.',
                              'type': 'object'}},
  'required': ['func'],
  'type': 'object'}
TOOL_NOTES = 'The base Condition class is rarely what you want. PsyNeuLink ships dozens of named subclasses (AfterNCalls, Always, Never, EveryNCalls, AtPass, AfterPass, WhenFinished, etc.) — each has its own generated MCP tool with a stricter schema. Use those first. This tool is the fallback for logic that truly cannot be expressed by any named subclass. The func string must resolve to a Python callable in the server process; passing a lambda string or arbitrary expression will fail. args and kwargs are passed through directly to func on every is_satisfied() call, not just at construction time, so avoid mutable defaults. Condition is also the base for MDF serialisation (as_mdf_model); if you need MDF export, only named subclasses serialise cleanly — a custom func may fall back to dill-serialising the callable.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Condition
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
    def create_condition(args: dict[str, Any] | None = None) -> Any:
        'Use this tool only when no named Condition subclass (AfterNCalls, Always, EveryNCalls, AtPass, etc.) fits your scheduling need and you must supply a custom Python callable as the condition test.'
        return _impl(args or {})
