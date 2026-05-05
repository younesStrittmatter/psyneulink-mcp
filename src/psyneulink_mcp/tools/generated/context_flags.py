"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '76624d5e0afb78fa401681a7d4c95c00f7ad16bd4854d4bc89aea8a2b3eddd3d'
__pnl_qualname__ = 'psyneulink.ContextFlags'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_context_flags'
TOOL_DESCRIPTION = 'Call this tool to decode or construct a PsyNeuLink ContextFlags bitmask from an integer value. Use it when you need to inspect which initialization, execution-phase, source, or run-mode flags are active in a context integer returned by another tool, or when building a flags value to pass to tools that accept a `context` argument.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Integer bitmask to decode into named ContextFlags. Combine individual flag values with bitwise OR (|) to represent multiple active flags. Pass 0 for UNSET. Named members and their values: UNSET=0, DEFERRED_INIT=1, INITIALIZING=2, VALIDATING=4, INITIALIZED=8, RESET=16, UNINITIALIZED=32, PREPARING=64, PROCESSING=128, LEARNING=256, CONTROL=512, DISPLAYING=1024, IDLE=2048, COMMAND_LINE=4096, CONSTRUCTOR=8192, METHOD=16384, COMPOSITION=32768, SHOW_GRAPH=65536, NONE=131072, DEFAULT_MODE=262144, LEARNING_MODE=524288, SIMULATION_MODE=1048576.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nContextFlags is an IntFlag enum, not a class you instantiate to create new objects — calling ContextFlags(n) returns the flag combination whose bits match n. Composite masks (INITIALIZATION_MASK, EXECUTION_PHASE_MASK, SOURCE_MASK, RUN_MODE_MASK, ALL_FLAGS, EXECUTING) are not standalone members; they are bitwise OR combinations of members. Agents should not pass mask values as targets; use them only to filter. Individual flag integer values depend on enum.auto() insertion order — do not hard-code them; prefer accessing members by attribute (ContextFlags.PROCESSING) in Python code rather than raw integers where possible. The tool is read/lookup only; it does not mutate any Component state.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Integer bitmask to decode into named '
                                            'ContextFlags. Combine individual flag '
                                            'values with bitwise OR (|) to represent '
                                            'multiple active flags. Pass 0 for UNSET. '
                                            'Named members and their values: UNSET=0, '
                                            'DEFERRED_INIT=1, INITIALIZING=2, '
                                            'VALIDATING=4, INITIALIZED=8, RESET=16, '
                                            'UNINITIALIZED=32, PREPARING=64, '
                                            'PROCESSING=128, LEARNING=256, '
                                            'CONTROL=512, DISPLAYING=1024, IDLE=2048, '
                                            'COMMAND_LINE=4096, CONSTRUCTOR=8192, '
                                            'METHOD=16384, COMPOSITION=32768, '
                                            'SHOW_GRAPH=65536, NONE=131072, '
                                            'DEFAULT_MODE=262144, '
                                            'LEARNING_MODE=524288, '
                                            'SIMULATION_MODE=1048576.',
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'ContextFlags is an IntFlag enum, not a class you instantiate to create new objects — calling ContextFlags(n) returns the flag combination whose bits match n. Composite masks (INITIALIZATION_MASK, EXECUTION_PHASE_MASK, SOURCE_MASK, RUN_MODE_MASK, ALL_FLAGS, EXECUTING) are not standalone members; they are bitwise OR combinations of members. Agents should not pass mask values as targets; use them only to filter. Individual flag integer values depend on enum.auto() insertion order — do not hard-code them; prefer accessing members by attribute (ContextFlags.PROCESSING) in Python code rather than raw integers where possible. The tool is read/lookup only; it does not mutate any Component state.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ContextFlags
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
    def create_context_flags(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to decode or construct a PsyNeuLink ContextFlags bitmask from an integer value.'
        return _impl(args or {})
