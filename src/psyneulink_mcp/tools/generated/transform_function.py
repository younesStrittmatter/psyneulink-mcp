"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '32345693b7088b35bd3dd777c9c0eadc8759e15ce3582efdda91885efeb0f925'
__pnl_qualname__ = 'psyneulink.TransformFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_transform_function'
TOOL_DESCRIPTION = 'Call this tool only when you need to instantiate TransformFunction directly as an abstract base — in practice, prefer a concrete subclass (Linear, Logistic, etc.) that inherits from it. TransformFunction is the root class for all PsyNeuLink functions that combine multiple inputs into a result of the same shape, and it exposes the multiplicative_param/additive_param contract required by ModulatoryProjections and GatingProjections.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Initial value that sets the shape and default for the function\'s input variable. Defaults to [0].",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nTransformFunction is an abstract base class; instantiating it directly will not produce a callable function — it has no _function implementation. Always use a concrete subclass (e.g. Linear, Logistic, SoftMax) unless you are subclassing it yourself. The variable parameter is read-only after construction; pass the desired shape via default_variable at instantiation time.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Initial value that sets the '
                                                       'shape and default for the '
                                                       "function's input variable. "
                                                       'Defaults to [0].',
                                        'items': {'type': 'number'},
                                        'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'TransformFunction is an abstract base class; instantiating it directly will not produce a callable function — it has no _function implementation. Always use a concrete subclass (e.g. Linear, Logistic, SoftMax) unless you are subclassing it yourself. The variable parameter is read-only after construction; pass the desired shape via default_variable at instantiation time.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.TransformFunction
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
    def create_transform_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to instantiate TransformFunction directly as an abstract base — in practice, prefer a concrete subclass (Linear, Logistic, etc.) that inherits from it.'
        return _impl(args or {})
