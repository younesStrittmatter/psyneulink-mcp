"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b619ed414bd77d1be37325a8323fb6db4ae6a9dac58e1a0133c0c0294a86daab'
__pnl_qualname__ = 'psyneulink.AutoNumber'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_auto_number'
TOOL_DESCRIPTION = 'AutoNumber is a base class for defining auto-numbered IntEnum subclasses where members are assigned integer values starting at 0. Do NOT call this tool to instantiate AutoNumber directly — it is a metaclass utility meant to be subclassed when defining a new enumeration type in Python code. The result would be an integer-valued enum member, but direct instantiation produces no useful modeling object.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nAutoNumber is a base class (IntEnum subclass), not a standalone callable. Instantiating it directly via this tool is almost certainly wrong — the class is designed to be subclassed in Python source (e.g., `class MyEnum(AutoNumber): A = ()`). The `__new__` method only has meaning as part of enum member construction machinery. If you need a specific PsyNeuLink enum value, look up the concrete enum class that inherits from AutoNumber rather than calling this tool.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'AutoNumber is a base class (IntEnum subclass), not a standalone callable. Instantiating it directly via this tool is almost certainly wrong — the class is designed to be subclassed in Python source (e.g., `class MyEnum(AutoNumber): A = ()`). The `__new__` method only has meaning as part of enum member construction machinery. If you need a specific PsyNeuLink enum value, look up the concrete enum class that inherits from AutoNumber rather than calling this tool.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.AutoNumber
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
    def create_auto_number(args: dict[str, Any] | None = None) -> Any:
        'AutoNumber is a base class for defining auto-numbered IntEnum subclasses where members are assigned integer values starting at 0.'
        return _impl(args or {})
