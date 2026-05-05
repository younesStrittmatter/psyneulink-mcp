"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '15e5f324ffdcdcd496a407bc349a9d5212bf9ff02b9d66e024e9f3d4062cf0b2'
__pnl_qualname__ = 'psyneulink.OrthogonalMatrix'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_orthogonal_matrix'
TOOL_DESCRIPTION = 'Call this tool when you need to create an orthogonal weight matrix initializer to pass as the `matrix` parameter of a `MappingProjection`. Use it when setting up recurrent or deep linear networks where preserving signal magnitude across layers matters — it returns a callable that, when invoked by MappingProjection with sender/receiver sizes, produces a scaled orthogonal matrix via QR decomposition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "gain": {\n      "default": 1,\n      "description": "Scalar multiplier applied to the orthogonal matrix. Defaults to 1.0 (no scaling). Use values > 1.0 to amplify, < 1.0 to attenuate signal magnitude.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis tool instantiates the OrthogonalMatrix callable — it does NOT immediately produce a matrix. The matrix is generated lazily when MappingProjection calls the object with its sender/receiver sizes. Each invocation produces a fresh random orthogonal matrix (non-deterministic unless you seed numpy). For non-square projections, the initializer internally uses a square matrix of size max(sender_size, receiver_size) and slices it, so orthogonality is preserved along the shorter dimension only. Pass the returned object as `matrix=OrthogonalMatrix(gain=...)` in MappingProjection, not as a raw array.'
TOOL_PARAMETERS = { 'properties': { 'gain': { 'default': 1,
                            'description': 'Scalar multiplier applied to the '
                                           'orthogonal matrix. Defaults to 1.0 (no '
                                           'scaling). Use values > 1.0 to amplify, < '
                                           '1.0 to attenuate signal magnitude.',
                            'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'This tool instantiates the OrthogonalMatrix callable — it does NOT immediately produce a matrix. The matrix is generated lazily when MappingProjection calls the object with its sender/receiver sizes. Each invocation produces a fresh random orthogonal matrix (non-deterministic unless you seed numpy). For non-square projections, the initializer internally uses a square matrix of size max(sender_size, receiver_size) and slices it, so orthogonality is preserved along the shorter dimension only. Pass the returned object as `matrix=OrthogonalMatrix(gain=...)` in MappingProjection, not as a raw array.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.OrthogonalMatrix
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
    def create_orthogonal_matrix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to create an orthogonal weight matrix initializer to pass as the `matrix` parameter of a `MappingProjection`.'
        return _impl(args or {})
