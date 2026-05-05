"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b1b5ff07db0516f69244850a37e2bc6041435aca52d410ec1ae574e5e9bf881e'
__pnl_qualname__ = 'psyneulink.KaimingMatrix'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_kaiming_matrix'
TOOL_DESCRIPTION = 'Call this tool to create a Kaiming (He) weight matrix initializer when setting up a MappingProjection that feeds into ReLU or ReLU-like activations in a deep network. Pass the returned initializer as the `matrix` parameter of a MappingProjection — the actual matrix dimensions are inferred automatically from the connected mechanisms at build time.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "distribution": {\n      "default": "normal",\n      "description": "Sampling distribution for matrix elements. \'normal\' uses a zero-mean Gaussian; \'uniform\' uses a symmetric uniform range. Both are scaled by the same std derived from gain/fan.",\n      "enum": [\n        "normal",\n        "uniform"\n      ],\n      "type": "string"\n    },\n    "fan": {\n      "default": "in",\n      "description": "Fan value for variance scaling. \'in\' uses sender_size (standard He init); \'out\' uses receiver_size; a numeric value uses that number directly as the fan.",\n      "oneOf": [\n        {\n          "enum": [\n            "in",\n            "out"\n          ],\n          "type": "string"\n        },\n        {\n          "type": "number"\n        }\n      ]\n    },\n    "gain": {\n      "default": 2,\n      "description": "Scaling factor for initialization variance. Default 2.0 is calibrated for ReLU. Use 1.0 for linear activations or tanh.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis tool returns a KaimingMatrix initializer object, not a matrix array — it is intended to be passed directly as the `matrix` argument of a MappingProjection, where PsyNeuLink will call it with the actual sender_size and receiver_size at network construction time. The agent should never need to supply sender_size/receiver_size here. Default gain=2.0 matches the standard He (2015) recommendation for ReLU; override for other activations. When fan is a raw number it bypasses any connection-size relationship entirely.'
TOOL_PARAMETERS = { 'properties': { 'distribution': { 'default': 'normal',
                                    'description': 'Sampling distribution for matrix '
                                                   "elements. 'normal' uses a "
                                                   "zero-mean Gaussian; 'uniform' uses "
                                                   'a symmetric uniform range. Both '
                                                   'are scaled by the same std derived '
                                                   'from gain/fan.',
                                    'enum': ['normal', 'uniform'],
                                    'type': 'string'},
                  'fan': { 'default': 'in',
                           'description': "Fan value for variance scaling. 'in' uses "
                                          "sender_size (standard He init); 'out' uses "
                                          'receiver_size; a numeric value uses that '
                                          'number directly as the fan.',
                           'oneOf': [ {'enum': ['in', 'out'], 'type': 'string'},
                                      {'type': 'number'}]},
                  'gain': { 'default': 2,
                            'description': 'Scaling factor for initialization '
                                           'variance. Default 2.0 is calibrated for '
                                           'ReLU. Use 1.0 for linear activations or '
                                           'tanh.',
                            'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'This tool returns a KaimingMatrix initializer object, not a matrix array — it is intended to be passed directly as the `matrix` argument of a MappingProjection, where PsyNeuLink will call it with the actual sender_size and receiver_size at network construction time. The agent should never need to supply sender_size/receiver_size here. Default gain=2.0 matches the standard He (2015) recommendation for ReLU; override for other activations. When fan is a raw number it bypasses any connection-size relationship entirely.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.KaimingMatrix
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
    def create_kaiming_matrix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Kaiming (He) weight matrix initializer when setting up a MappingProjection that feeds into ReLU or ReLU-like activations in a deep network.'
        return _impl(args or {})
