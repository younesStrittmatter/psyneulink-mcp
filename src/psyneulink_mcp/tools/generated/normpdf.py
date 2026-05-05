"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f8c2b19bc8566d4b0f5b1abe184edca0b297f4f70c8d93ab67867356ca790f87'
__pnl_qualname__ = 'psyneulink.normpdf'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'normpdf'
TOOL_DESCRIPTION = 'Call this tool to evaluate the normal (Gaussian) probability density function at a specific value. Use it when you need the PDF height at point x for a distribution with a given mean and standard deviation — for example, to score how likely an observed value is under a Gaussian prior, or to weight inputs by their proximity to a center. Returns a single non-negative float (the density value, not a probability mass).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "mu": {\n      "default": 0,\n      "description": "Mean (center) of the distribution. Defaults to 0.",\n      "type": "number"\n    },\n    "sigma": {\n      "default": 1,\n      "description": "Standard deviation of the distribution. Must be non-zero; the function uses abs(sigma) internally. Defaults to 1.",\n      "type": "number"\n    },\n    "x": {\n      "description": "The point at which to evaluate the normal PDF.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nsigma is passed through abs() internally, so a negative value silently behaves the same as its positive counterpart — pass a positive value to avoid confusion. The return value is a probability *density*, not a cumulative probability; it can exceed 1 for narrow distributions (small sigma). No validation is performed on inputs.'
TOOL_PARAMETERS = { 'properties': { 'mu': { 'default': 0,
                          'description': 'Mean (center) of the distribution. Defaults '
                                         'to 0.',
                          'type': 'number'},
                  'sigma': { 'default': 1,
                             'description': 'Standard deviation of the distribution. '
                                            'Must be non-zero; the function uses '
                                            'abs(sigma) internally. Defaults to 1.',
                             'type': 'number'},
                  'x': { 'description': 'The point at which to evaluate the normal '
                                        'PDF.',
                         'type': 'number'}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = 'sigma is passed through abs() internally, so a negative value silently behaves the same as its positive counterpart — pass a positive value to avoid confusion. The return value is a probability *density*, not a cumulative probability; it can exceed 1 for narrow distributions (small sigma). No validation is performed on inputs.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.normpdf
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
    def normpdf(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to evaluate the normal (Gaussian) probability density function at a specific value.'
        return _impl(args or {})
