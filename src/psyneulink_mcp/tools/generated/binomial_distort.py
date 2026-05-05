"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '2e1edfb5df671be2f2a3db4b9f7dcdc3c0b8441a1781dd60f73395a6cdaf8a43'
__pnl_qualname__ = 'psyneulink.BinomialDistort'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_binomial_distort'
TOOL_DESCRIPTION = 'Use this tool to create a BinomialDistort transfer function that randomly zeros elements of an array with probability p. Call it when you need stochastic dropout-style noise on a signal — e.g., to model unreliable transmission or add binomial noise to a Mechanism\'s output. The result is a BinomialDistort instance ready to be assigned as a Mechanism\'s function.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template array or scalar defining the shape of the input. Each element will be independently zeroed with probability p.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the function instance. If omitted, a default is assigned by FunctionRegistry.",\n      "type": "string"\n    },\n    "p": {\n      "default": 0.5,\n      "description": "Probability [0, 1] with which each element is replaced with zero. Default is 0.5. Higher p means more zeroing (more noise/dropout).",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "seed": {\n      "description": "Integer seed for the internal numpy RandomState. Set for reproducibility; omit for non-deterministic behavior.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThere is a discrepancy between the class signature header (p=0.05) and the Parameters class definition (p=Parameter(0.5, ...)). The actual runtime default is 0.5 (from Parameters), not 0.05 — use 0.5 as the canonical default. The zeroing rule is: element is set to 0 when rand[0,1] > p, otherwise it is kept — so p=0 means no elements are zeroed (identity), and p=1 means all elements are zeroed. Derivative is not implemented; calling derivative() raises FunctionError. The function requires variable to have a len(), so it cannot accept a bare scalar at call time even if a scalar is passed as default_variable.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template array or scalar '
                                                       'defining the shape of the '
                                                       'input. Each element will be '
                                                       'independently zeroed with '
                                                       'probability p.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'name': { 'description': 'Optional name for the function instance. '
                                           'If omitted, a default is assigned by '
                                           'FunctionRegistry.',
                            'type': 'string'},
                  'p': { 'default': 0.5,
                         'description': 'Probability [0, 1] with which each element is '
                                        'replaced with zero. Default is 0.5. Higher p '
                                        'means more zeroing (more noise/dropout).',
                         'maximum': 1,
                         'minimum': 0,
                         'type': 'number'},
                  'seed': { 'description': 'Integer seed for the internal numpy '
                                           'RandomState. Set for reproducibility; omit '
                                           'for non-deterministic behavior.',
                            'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'There is a discrepancy between the class signature header (p=0.05) and the Parameters class definition (p=Parameter(0.5, ...)). The actual runtime default is 0.5 (from Parameters), not 0.05 — use 0.5 as the canonical default. The zeroing rule is: element is set to 0 when rand[0,1] > p, otherwise it is kept — so p=0 means no elements are zeroed (identity), and p=1 means all elements are zeroed. Derivative is not implemented; calling derivative() raises FunctionError. The function requires variable to have a len(), so it cannot accept a bare scalar at call time even if a scalar is passed as default_variable.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.BinomialDistort
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
    def create_binomial_distort(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a BinomialDistort transfer function that randomly zeros elements of an array with probability p.'
        return _impl(args or {})
