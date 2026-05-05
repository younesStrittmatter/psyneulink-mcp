"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '457de0be710fe537bcc6be153a5cac78e63d3a94f85e416b280097ec82b746bf'
__pnl_qualname__ = 'psyneulink.CostFunctions'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_cost_functions'
TOOL_DESCRIPTION = 'Call this tool when you need a CostFunctions flag value to pass to TransferWithCosts methods (enable_costs, disable_costs, toggle_cost, assign_costs). Returns a CostFunctions Flag enum member controlling which cost components (intensity, adjustment, duration) contribute to the aggregate cost. To combine multiple cost functions, sum their integer values (e.g., INTENSITY|DURATION = 5).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "default": 0,\n      "description": "Integer value of the desired flag combination. Named members: NONE=0, INTENSITY=1, ADJUSTMENT=2, DURATION=4, ALL=7, DEFAULTS=0. Sum values to combine flags (e.g., INTENSITY|ADJUSTMENT=3, INTENSITY|DURATION=5, ALL=7).",\n      "maximum": 7,\n      "minimum": 0,\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCostFunctions is a Python Flag enum, not a regular class — it is constructed with a single positional integer argument, not keyword arguments. The host template unpacking **kwargs will not work directly; the value parameter should be passed positionally. Named members: NONE=0 (no cost computed), INTENSITY=1 (cost from current intensity), ADJUSTMENT=2 (cost from change in intensity), DURATION=4 (cost from accumulated integral), ALL=7 (all three active), DEFAULTS=0 (same as NONE). DEFAULTS and NONE are both 0 and behave identically. The docstring contains a typo attributing INTENSITY behavior to "duration_cost_fct" — the correct function for INTENSITY is intensity_cost_fct.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'default': 0,
                             'description': 'Integer value of the desired flag '
                                            'combination. Named members: NONE=0, '
                                            'INTENSITY=1, ADJUSTMENT=2, DURATION=4, '
                                            'ALL=7, DEFAULTS=0. Sum values to combine '
                                            'flags (e.g., INTENSITY|ADJUSTMENT=3, '
                                            'INTENSITY|DURATION=5, ALL=7).',
                             'maximum': 7,
                             'minimum': 0,
                             'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CostFunctions is a Python Flag enum, not a regular class — it is constructed with a single positional integer argument, not keyword arguments. The host template unpacking **kwargs will not work directly; the value parameter should be passed positionally. Named members: NONE=0 (no cost computed), INTENSITY=1 (cost from current intensity), ADJUSTMENT=2 (cost from change in intensity), DURATION=4 (cost from accumulated integral), ALL=7 (all three active), DEFAULTS=0 (same as NONE). DEFAULTS and NONE are both 0 and behave identically. The docstring contains a typo attributing INTENSITY behavior to "duration_cost_fct" — the correct function for INTENSITY is intensity_cost_fct.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.CostFunctions
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
    def create_cost_functions(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need a CostFunctions flag value to pass to TransferWithCosts methods (enable_costs, disable_costs, toggle_cost, assign_costs).'
        return _impl(args or {})
