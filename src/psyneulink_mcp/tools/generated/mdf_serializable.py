"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'caad6059e8ef158be1269a23127f13da3733824c3585f9b4d6e3a63de82f65da'
__pnl_qualname__ = 'psyneulink.MDFSerializable'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_mdf_serializable'
TOOL_DESCRIPTION = 'Call this tool only when you need a bare MDFSerializable instance to access MDF (ModECI Model Description Format) serialization capabilities — specifically the `json_summary` or `yaml_summary` properties that export an object\'s structure in MDF-compliant JSON or YAML. In practice, you will rarely instantiate MDFSerializable directly; it is a mixin base class that PsyNeuLink components (Mechanisms, Compositions, etc.) already inherit from — use those specific component tools instead.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMDFSerializable is a mixin with no constructor parameters of its own. Its useful interface (`json_summary`, `yaml_summary`) depends on the concrete subclass implementing `as_mdf_model()` — calling it on a bare MDFSerializable instance will raise AttributeError because `as_mdf_model` is not defined on the base. Almost all real use comes from instantiating a concrete PsyNeuLink component that inherits this mixin.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'MDFSerializable is a mixin with no constructor parameters of its own. Its useful interface (`json_summary`, `yaml_summary`) depends on the concrete subclass implementing `as_mdf_model()` — calling it on a bare MDFSerializable instance will raise AttributeError because `as_mdf_model` is not defined on the base. Almost all real use comes from instantiating a concrete PsyNeuLink component that inherits this mixin.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.MDFSerializable
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
    def create_mdf_serializable(args: dict[str, Any] | None = None) -> Any:
        "Call this tool only when you need a bare MDFSerializable instance to access MDF (ModECI Model Description Format) serialization capabilities — specifically the `json_summary` or `yaml_summary` properties that export an object's structure in MDF-compliant JSON or YAML."
        return _impl(args or {})
