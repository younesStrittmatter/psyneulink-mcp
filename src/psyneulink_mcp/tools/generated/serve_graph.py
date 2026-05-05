"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '540fc22362a2e51f4a06337f9b46c152a86e2583937072c0a873663129cc3174'
__pnl_qualname__ = 'psyneulink.ServeGraph'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_serve_graph'
TOOL_DESCRIPTION = 'Call this tool only when you need to interact with a running PsyNeuLink gRPC graph server at the lowest level — e.g., to load scripts, run compositions, or query graph structure via raw RPC calls. `ServeGraph` is a gRPC client stub class with static methods for each RPC endpoint; instantiating it yields no useful object — use the static methods directly (e.g., `ServeGraph.LoadScript`, `ServeGraph.RunComposition`). Do not call this tool for ordinary PsyNeuLink modeling; it is only relevant when a PsyNeuLink gRPC server process is already running.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis class is auto-generated gRPC boilerplate (`graph_pb2_grpc`). All methods are static and operate as unary-unary, unary-stream, or stream-unary RPC calls — none are instance methods, so instantiating `ServeGraph()` itself provides no functionality. Agents should call the static methods directly with a `request` protobuf message and a `target` host:port string, not via the MCP tool wrapper. Exposing this as an MCP tool is only useful for advanced introspection; routine PsyNeuLink modeling tasks should use higher-level tools (Composition, TransferMechanism, etc.).'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'This class is auto-generated gRPC boilerplate (`graph_pb2_grpc`). All methods are static and operate as unary-unary, unary-stream, or stream-unary RPC calls — none are instance methods, so instantiating `ServeGraph()` itself provides no functionality. Agents should call the static methods directly with a `request` protobuf message and a `target` host:port string, not via the MCP tool wrapper. Exposing this as an MCP tool is only useful for advanced introspection; routine PsyNeuLink modeling tasks should use higher-level tools (Composition, TransferMechanism, etc.).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ServeGraph
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
    def create_serve_graph(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to interact with a running PsyNeuLink gRPC graph server at the lowest level — e.g., to load scripts, run compositions, or query graph structure via raw RPC calls.'
        return _impl(args or {})
