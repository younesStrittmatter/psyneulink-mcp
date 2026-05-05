"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8de69ff3f688af1e7f547356b2f9236c560f8bccc95ff0ce29cd311ed83d30ab'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.optimizationfunctions.Number'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_number'
TOOL_DESCRIPTION = 'Call this tool only when you need to verify or assert that a value is of the abstract numeric base type in PsyNeuLink\'s optimization function context. This wraps Python\'s `numbers.Number` ABC — the root of the numeric tower — and produces an instance check rather than a usable numeric value. The result is an abstract class instance (cannot be used as a concrete number).\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n`numbers.Number` is an abstract base class with ABCMeta; it cannot be instantiated and has no constructor parameters. Its `__hash__` is explicitly set to None. Do not call this tool expecting a concrete numeric value — use specific PsyNeuLink numeric types or Python primitives (int, float) instead. The only practical use of `Number` is as a type-check target via `isinstance(x, Number)`, which does not require instantiation.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = '`numbers.Number` is an abstract base class with ABCMeta; it cannot be instantiated and has no constructor parameters. Its `__hash__` is explicitly set to None. Do not call this tool expecting a concrete numeric value — use specific PsyNeuLink numeric types or Python primitives (int, float) instead. The only practical use of `Number` is as a type-check target via `isinstance(x, Number)`, which does not require instantiation.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Number
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
    def create_number(args: dict[str, Any] | None = None) -> Any:
        "Call this tool only when you need to verify or assert that a value is of the abstract numeric base type in PsyNeuLink's optimization function context."
        return _impl(args or {})
