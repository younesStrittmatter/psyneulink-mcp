"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b84cdcfde346ace63f478cb7a2223e2ef99d484d39e8611accdbab15d113edbc'
__pnl_qualname__ = 'psyneulink.PV'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pv'
TOOL_DESCRIPTION = 'Call this tool to obtain a PV (PredictionVector term) enum member when configuring a RegressionCFA composition\'s prediction vector terms. Use it to select which feature/control-signal interaction terms (main effects, pairwise interactions, higher-order interactions, or cost) to include in `prediction_terms`. Returns the PV enum member corresponding to the given integer value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Integer value of the desired PV enum member. 0=F (main effect of state features), 1=C (main effect of control signal values), 2=FF (feature\\u00d7feature interactions), 3=CC (control\\u00d7control interactions), 4=FC (feature\\u00d7control interactions), 5=FFC (feature-interaction\\u00d7control), 6=FCC (feature\\u00d7control-interaction), 7=FFCC (feature-interaction\\u00d7control-interaction), 8=COST (main effect of control signal costs).",\n      "enum": [\n        0,\n        1,\n        2,\n        3,\n        4,\n        5,\n        6,\n        7,\n        8\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nPV is an Enum; calling `PV(value)` with an integer returns the corresponding member (e.g., `PV(0)` → `PV.F`). Enum members are typically passed as a list to the `prediction_terms` argument of RegressionCFA — e.g., `prediction_terms=[PV.F, PV.C, PV.COST]`. The underlying integers are stable (F=0 through COST=8). The class was originally an AutoNumberEnum and may be reverted in future versions, but the integer assignments are currently fixed in source. Do not confuse `PV` (PredictionVector terms) with PsyNeuLink\'s `pv` (parameter value) shorthand used elsewhere.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Integer value of the desired PV enum '
                                            'member. 0=F (main effect of state '
                                            'features), 1=C (main effect of control '
                                            'signal values), 2=FF (feature×feature '
                                            'interactions), 3=CC (control×control '
                                            'interactions), 4=FC (feature×control '
                                            'interactions), 5=FFC '
                                            '(feature-interaction×control), 6=FCC '
                                            '(feature×control-interaction), 7=FFCC '
                                            '(feature-interaction×control-interaction), '
                                            '8=COST (main effect of control signal '
                                            'costs).',
                             'enum': [0, 1, 2, 3, 4, 5, 6, 7, 8],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = "PV is an Enum; calling `PV(value)` with an integer returns the corresponding member (e.g., `PV(0)` → `PV.F`). Enum members are typically passed as a list to the `prediction_terms` argument of RegressionCFA — e.g., `prediction_terms=[PV.F, PV.C, PV.COST]`. The underlying integers are stable (F=0 through COST=8). The class was originally an AutoNumberEnum and may be reverted in future versions, but the integer assignments are currently fixed in source. Do not confuse `PV` (PredictionVector terms) with PsyNeuLink's `pv` (parameter value) shorthand used elsewhere."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PV
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
    def create_pv(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to obtain a PV (PredictionVector term) enum member when configuring a RegressionCFA composition's prediction vector terms."
        return _impl(args or {})
