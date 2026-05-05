"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '47469b63d3ea861656a64b6af19f38b34922b3d8823d50f168bcb7dc44db920a'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.learningfunctions.scalar_distance'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'scalar_distance'
TOOL_DESCRIPTION = 'Call this tool to apply a scalar transformation to a numeric value using one of four functional forms: Gaussian (normal PDF), Linear, Exponential, or Sinusoid. Use it when a learning rule or distance metric requires converting a raw scalar into a transformed output according to a named measure type. Returns a single float.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "measure": {\n      "description": "The transformation type to apply. GAUSSIAN returns the normal PDF; LINEAR returns scale*value+offset; EXPONENTIAL returns exp(scale*value+offset); SINUSOID returns a sinusoidal function with scale as frequency and offset as phase.",\n      "enum": [\n        "GAUSSIAN",\n        "LINEAR",\n        "EXPONENTIAL",\n        "SINUSOID"\n      ],\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Offset/shift. For GAUSSIAN: mean. For SINUSOID: phase. For LINEAR/EXPONENTIAL: additive offset.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Scaling factor. For GAUSSIAN: standard deviation. For SINUSOID: frequency. For LINEAR/EXPONENTIAL: multiplicative scale.",\n      "type": "number"\n    },\n    "value": {\n      "description": "The scalar input to transform.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "measure",\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nFor GAUSSIAN, arguments are passed as normpdf(value, offset, scale) — so offset is the mean and scale is the standard deviation, which is the reverse of the typical (mean, std) mental model. If measure does not match any of the four supported strings, the function returns None silently — pass only the enum values listed. scale and offset have different semantic roles depending on measure; do not assume they always mean multiply and add.'
TOOL_PARAMETERS = { 'properties': { 'measure': { 'description': 'The transformation type to apply. '
                                              'GAUSSIAN returns the normal PDF; LINEAR '
                                              'returns scale*value+offset; EXPONENTIAL '
                                              'returns exp(scale*value+offset); '
                                              'SINUSOID returns a sinusoidal function '
                                              'with scale as frequency and offset as '
                                              'phase.',
                               'enum': [ 'GAUSSIAN',
                                         'LINEAR',
                                         'EXPONENTIAL',
                                         'SINUSOID'],
                               'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Offset/shift. For GAUSSIAN: mean. For '
                                             'SINUSOID: phase. For LINEAR/EXPONENTIAL: '
                                             'additive offset.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Scaling factor. For GAUSSIAN: standard '
                                            'deviation. For SINUSOID: frequency. For '
                                            'LINEAR/EXPONENTIAL: multiplicative scale.',
                             'type': 'number'},
                  'value': { 'description': 'The scalar input to transform.',
                             'type': 'number'}},
  'required': ['measure', 'value'],
  'type': 'object'}
TOOL_NOTES = 'For GAUSSIAN, arguments are passed as normpdf(value, offset, scale) — so offset is the mean and scale is the standard deviation, which is the reverse of the typical (mean, std) mental model. If measure does not match any of the four supported strings, the function returns None silently — pass only the enum values listed. scale and offset have different semantic roles depending on measure; do not assume they always mean multiply and add.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.scalar_distance
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
    def scalar_distance(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to apply a scalar transformation to a numeric value using one of four functional forms: Gaussian (normal PDF), Linear, Exponential, or Sinusoid.'
        return _impl(args or {})
