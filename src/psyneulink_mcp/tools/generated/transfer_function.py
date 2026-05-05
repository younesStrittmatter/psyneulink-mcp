"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0e6ecff88f6b55381f0295545a1697d4de9cc3cec153447b558945804ad26812'
__pnl_qualname__ = 'psyneulink.TransferFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_transfer_function'
TOOL_DESCRIPTION = 'Call this tool only when you need a reference to the abstract TransferFunction base class itself — for example, to check isinstance membership or inspect shared class attributes like `range` and `default_range`. Do NOT call this to create a working transfer function; use a concrete subclass tool (Linear, Logistic, ReLU, Tanh, etc.) instead, as TransferFunction is abstract and cannot be instantiated directly.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nTransferFunction is an abstract base class and cannot be instantiated — calling it directly will raise a TypeError. Always use a concrete subclass (e.g., Linear, Logistic, ReLU, Tanh, SoftMax, Exponential, etc.). The `range` attribute is read-only and returns a tuple of (lower_bound, upper_bound), where None means unbounded; it is set by the subclass, not by the caller. All subclasses expose a `multiplicative_param` and an `additive_param` for modulatory control.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'TransferFunction is an abstract base class and cannot be instantiated — calling it directly will raise a TypeError. Always use a concrete subclass (e.g., Linear, Logistic, ReLU, Tanh, SoftMax, Exponential, etc.). The `range` attribute is read-only and returns a tuple of (lower_bound, upper_bound), where None means unbounded; it is set by the subclass, not by the caller. All subclasses expose a `multiplicative_param` and an `additive_param` for modulatory control.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.TransferFunction
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
    def create_transfer_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need a reference to the abstract TransferFunction base class itself — for example, to check isinstance membership or inspect shared class attributes like `range` and `default_range`.'
        return _impl(args or {})
