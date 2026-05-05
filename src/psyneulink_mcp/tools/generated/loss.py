"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '15543353fadcba378aa97120dd90a7e68e3c00d77d13436d3aae101731261a75'
__pnl_qualname__ = 'psyneulink.Loss'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_loss'
TOOL_DESCRIPTION = 'Call this tool when you need to specify a loss function for learning in an AutodiffComposition or when constructing a learning pathway in a Composition. Use it to resolve the correct Loss enum member (e.g., Loss.MSE, Loss.CROSS_ENTROPY) to pass as the loss_spec argument to AutodiffComposition or learning pathway methods.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "member": {\n      "description": "Name of the Loss enum member to retrieve. L0/SUM: sum of absolute errors; L1: mean absolute error; SSE: sum of squared errors; MSE: mean squared errors; CROSS_ENTROPY: cross entropy; BINARY_CROSS_ENTROPY: binary cross entropy; KL_DIV: Kullback-Leibler divergence; NLL: negative log likelihood; POISSON_NLL: Poisson NLL.",\n      "enum": [\n        "L0",\n        "L1",\n        "SSE",\n        "MSE",\n        "CROSS_ENTROPY",\n        "BINARY_CROSS_ENTROPY",\n        "KL_DIV",\n        "NLL",\n        "POISSON_NLL",\n        "SUM"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "member"\n  ],\n  "type": "object"\n}\n\nNotes:\nSUM is an alias for L0 — they resolve to the same enum member. L1 (mean absolute error) is present in the source but was intentionally omitted from the public docstring; it exists but may be undocumented/experimental. BINARY_CROSS_ENTROPY appears in the source but is also absent from the docstring. Loss enum members map to PyTorch loss functions when the AutodiffComposition runs in ExecutionMode.PyTorch; behavior in native PNL execution mode may differ. Pass the returned enum member (not its string name) as the loss_spec argument to AutodiffComposition or learning pathway methods.'
TOOL_PARAMETERS = { 'properties': { 'member': { 'description': 'Name of the Loss enum member to '
                                             'retrieve. L0/SUM: sum of absolute '
                                             'errors; L1: mean absolute error; SSE: '
                                             'sum of squared errors; MSE: mean squared '
                                             'errors; CROSS_ENTROPY: cross entropy; '
                                             'BINARY_CROSS_ENTROPY: binary cross '
                                             'entropy; KL_DIV: Kullback-Leibler '
                                             'divergence; NLL: negative log '
                                             'likelihood; POISSON_NLL: Poisson NLL.',
                              'enum': [ 'L0',
                                        'L1',
                                        'SSE',
                                        'MSE',
                                        'CROSS_ENTROPY',
                                        'BINARY_CROSS_ENTROPY',
                                        'KL_DIV',
                                        'NLL',
                                        'POISSON_NLL',
                                        'SUM'],
                              'type': 'string'}},
  'required': ['member'],
  'type': 'object'}
TOOL_NOTES = 'SUM is an alias for L0 — they resolve to the same enum member. L1 (mean absolute error) is present in the source but was intentionally omitted from the public docstring; it exists but may be undocumented/experimental. BINARY_CROSS_ENTROPY appears in the source but is also absent from the docstring. Loss enum members map to PyTorch loss functions when the AutodiffComposition runs in ExecutionMode.PyTorch; behavior in native PNL execution mode may differ. Pass the returned enum member (not its string name) as the loss_spec argument to AutodiffComposition or learning pathway methods.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Loss
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
    def create_loss(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to specify a loss function for learning in an AutodiffComposition or when constructing a learning pathway in a Composition.'
        return _impl(args or {})
