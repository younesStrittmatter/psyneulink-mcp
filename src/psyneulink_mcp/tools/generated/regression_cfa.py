"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '651dff42de3d66e5e07d765c11090def59cbd0fffb0496392655e17c2b252929'
__pnl_qualname__ = 'psyneulink.RegressionCFA'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_regression_cfa'
TOOL_DESCRIPTION = 'Call this tool to create a RegressionCFA instance when you need a regression-based function approximator to serve as the `agent_rep` of an `OptimizationControlMechanism`. It learns to predict `net_outcome` from state feature values and control allocations using updateable regression weights. Returns a RegressionCFA object to pass as `agent_rep` to `OptimizationControlMechanism`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Optional name for the RegressionCFA instance.",\n      "type": "string"\n    },\n    "prediction_terms": {\n      "description": "List of PV enum member names to include as predictors in the regression vector. \'F\'=state features, \'C\'=control allocations, \'COST\'=control costs, \'FC\'=feature\\u00d7control interactions, \'FF\'=feature\\u00d7feature, \'CC\'=control\\u00d7control, \'FFC\'/\'FCC\'/\'FFCC\'=higher-order interactions. Defaults to [\'F\', \'C\', \'COST\'] if omitted or null.",\n      "items": {\n        "enum": [\n          "F",\n          "C",\n          "FF",\n          "CC",\n          "FC",\n          "FFC",\n          "FCC",\n          "FFCC",\n          "COST"\n        ],\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "update_weights": {\n      "description": "Name of the LearningFunction used to update regression_weights each trial (e.g. \'BayesGLM\'). Must accept a 2d array whose first item matches the prediction_vector length and second item is a scalar net_outcome. Defaults to BayesGLM if omitted.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `prediction_terms` values are passed as strings (PV enum member names); the tool layer converts them to PV enum members internally.\n- Including \'FF\', \'FFC\', or \'FFCC\' requires at least 2 state features at runtime; including \'CC\', \'FCC\', or \'FFCC\' requires at least 2 control signals — these constraints are checked at `initialize()` time, not at construction.\n- The object is not usable until `initialize()` is called, which happens automatically when it is assigned as `agent_rep` of an OptimizationControlMechanism.\n- `update_weights` defaults to BayesGLM; pass the string name of any compatible LearningFunction (e.g. \'RidgeRegression\').\n- Omitting `prediction_terms` (or passing null) silently applies the default [F, C, COST], not [F, C, FC, COST] as the docstring example header suggests — the actual code default is [PV.F, PV.C, PV.COST].'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Optional name for the RegressionCFA '
                                           'instance.',
                            'type': 'string'},
                  'prediction_terms': { 'description': 'List of PV enum member names '
                                                       'to include as predictors in '
                                                       'the regression vector. '
                                                       "'F'=state features, "
                                                       "'C'=control allocations, "
                                                       "'COST'=control costs, "
                                                       "'FC'=feature×control "
                                                       'interactions, '
                                                       "'FF'=feature×feature, "
                                                       "'CC'=control×control, "
                                                       "'FFC'/'FCC'/'FFCC'=higher-order "
                                                       'interactions. Defaults to '
                                                       "['F', 'C', 'COST'] if omitted "
                                                       'or null.',
                                        'items': { 'enum': [ 'F',
                                                             'C',
                                                             'FF',
                                                             'CC',
                                                             'FC',
                                                             'FFC',
                                                             'FCC',
                                                             'FFCC',
                                                             'COST'],
                                                   'type': 'string'},
                                        'type': 'array'},
                  'update_weights': { 'description': 'Name of the LearningFunction '
                                                     'used to update '
                                                     'regression_weights each trial '
                                                     "(e.g. 'BayesGLM'). Must accept a "
                                                     '2d array whose first item '
                                                     'matches the prediction_vector '
                                                     'length and second item is a '
                                                     'scalar net_outcome. Defaults to '
                                                     'BayesGLM if omitted.',
                                      'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- `prediction_terms` values are passed as strings (PV enum member names); the tool layer converts them to PV enum members internally.\n- Including 'FF', 'FFC', or 'FFCC' requires at least 2 state features at runtime; including 'CC', 'FCC', or 'FFCC' requires at least 2 control signals — these constraints are checked at `initialize()` time, not at construction.\n- The object is not usable until `initialize()` is called, which happens automatically when it is assigned as `agent_rep` of an OptimizationControlMechanism.\n- `update_weights` defaults to BayesGLM; pass the string name of any compatible LearningFunction (e.g. 'RidgeRegression').\n- Omitting `prediction_terms` (or passing null) silently applies the default [F, C, COST], not [F, C, FC, COST] as the docstring example header suggests — the actual code default is [PV.F, PV.C, PV.COST]."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.RegressionCFA
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
    def create_regression_cfa(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a RegressionCFA instance when you need a regression-based function approximator to serve as the `agent_rep` of an `OptimizationControlMechanism`.'
        return _impl(args or {})
