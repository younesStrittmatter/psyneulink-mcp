"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a225176588f1fed1656b5209966392e511904fd049dea4beb144a367123f12ac'
__pnl_qualname__ = 'psyneulink.MatrixKeywords'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_matrix_keywords'
TOOL_DESCRIPTION = 'Call this tool to discover the valid matrix keyword constants accepted by PsyNeuLink projections and functions (e.g., the `matrix` parameter of MappingProjection). It returns a MatrixKeywords instance whose attributes — IDENTITY_MATRIX, HOLLOW_MATRIX, FULL_CONNECTIVITY_MATRIX, ZEROS_MATRIX, RANDOM_CONNECTIVITY_MATRIX, AUTO_ASSIGN_MATRIX, DEFAULT_MATRIX — are the string values you pass elsewhere. Use it when you need to enumerate or validate matrix keyword options before constructing a projection or weight function.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMatrixKeywords takes no constructor arguments — it is a namespace/enum container, not a configurable class. The instance attributes are the actual string constants (e.g., IDENTITY_MATRIX = "IdentityMatrix") that PsyNeuLink components accept as matrix= values. Square-matrix keywords (IDENTITY_MATRIX, HOLLOW_MATRIX, INVERSE_HOLLOW_MATRIX) require sender and receiver to have the same length; rectangular keywords (FULL_CONNECTIVITY_MATRIX, ZEROS_MATRIX, RANDOM_CONNECTIVITY_MATRIX) do not. AUTO_ASSIGN_MATRIX selects IDENTITY_MATRIX when lengths match, FULL_CONNECTIVITY_MATRIX otherwise. DEFAULT_MATRIX currently resolves to IDENTITY_MATRIX. INVERSE_HOLLOW_MATRIX appears in the source but is undocumented in the docstring.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'MatrixKeywords takes no constructor arguments — it is a namespace/enum container, not a configurable class. The instance attributes are the actual string constants (e.g., IDENTITY_MATRIX = "IdentityMatrix") that PsyNeuLink components accept as matrix= values. Square-matrix keywords (IDENTITY_MATRIX, HOLLOW_MATRIX, INVERSE_HOLLOW_MATRIX) require sender and receiver to have the same length; rectangular keywords (FULL_CONNECTIVITY_MATRIX, ZEROS_MATRIX, RANDOM_CONNECTIVITY_MATRIX) do not. AUTO_ASSIGN_MATRIX selects IDENTITY_MATRIX when lengths match, FULL_CONNECTIVITY_MATRIX otherwise. DEFAULT_MATRIX currently resolves to IDENTITY_MATRIX. INVERSE_HOLLOW_MATRIX appears in the source but is undocumented in the docstring.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.MatrixKeywords
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
    def create_matrix_keywords(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to discover the valid matrix keyword constants accepted by PsyNeuLink projections and functions (e.g., the `matrix` parameter of MappingProjection).'
        return _impl(args or {})
