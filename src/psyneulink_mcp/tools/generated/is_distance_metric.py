"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b9faeb6b9d2ba1f8921ef84b693bd902748d3ff096b4da1c10e961891fcac377'
__pnl_qualname__ = 'psyneulink.is_distance_metric'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_distance_metric'
TOOL_DESCRIPTION = 'Call this tool to validate whether a string is a recognized PsyNeuLink distance metric before passing it to any function that accepts a distance metric parameter (e.g., ObjectiveMechanism, DistanceFunction). Returns True if the value is a valid metric, False otherwise — use it as a guard check to avoid silent failures downstream.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "s": {\n      "description": "The candidate distance metric string to validate (e.g., \'EUCLIDEAN\', \'COSINE\', \'CROSS_ENTROPY\', \'MAX_ABS_DIFF\').",\n      "type": "string"\n    }\n  },\n  "required": [\n    "s"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function checks membership in the internal DISTANCE_METRICS set — a fixed collection of PsyNeuLink string constants. It returns False silently for unrecognized values and never raises. Use the PsyNeuLink distance metric constants (e.g., psyneulink.EUCLIDEAN, psyneulink.COSINE) rather than arbitrary strings to ensure a match.'
TOOL_PARAMETERS = { 'properties': { 's': { 'description': 'The candidate distance metric string to '
                                        "validate (e.g., 'EUCLIDEAN', 'COSINE', "
                                        "'CROSS_ENTROPY', 'MAX_ABS_DIFF').",
                         'type': 'string'}},
  'required': ['s'],
  'type': 'object'}
TOOL_NOTES = 'The function checks membership in the internal DISTANCE_METRICS set — a fixed collection of PsyNeuLink string constants. It returns False silently for unrecognized values and never raises. Use the PsyNeuLink distance metric constants (e.g., psyneulink.EUCLIDEAN, psyneulink.COSINE) rather than arbitrary strings to ensure a match.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_distance_metric
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
    def is_distance_metric(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to validate whether a string is a recognized PsyNeuLink distance metric before passing it to any function that accepts a distance metric parameter (e.g., ObjectiveMechanism, DistanceFunction).'
        return _impl(args or {})
