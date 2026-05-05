"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4beed91310e5ca99132dd0543147ee7600b7331bbd4f5cb8c4bba354b1656be4'
__pnl_qualname__ = 'psyneulink.ArgumentTherapy'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_argument_therapy'
TOOL_DESCRIPTION = 'Call this tool to instantiate a stochastic boolean-response function that mimics a therapist either agreeing or disagreeing with a boolean assertion. Use it when you need a probabilistic flip/confirm function for a mechanism — it returns True or False with a bias controlled by `propensity` and `pertinacity`. This is a demonstration/example Function; prefer domain-specific Functions for real modeling tasks.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Name for this Function instance. Auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "pertinacity": {\n      "default": 10,\n      "description": "Therapeutic consistency, 0\\u201310. Higher values make the response more reliably match the propensity; lower values introduce more randomness.",\n      "maximum": 10,\n      "minimum": 0,\n      "type": "number"\n    },\n    "propensity": {\n      "default": "CONTRARIAN",\n      "description": "Therapeutic manner. OBSEQUIOUS tends to agree with the input; CONTRARIAN tends to disagree. Consistency of the tendency is set by pertinacity.",\n      "enum": [\n        "OBSEQUIOUS",\n        "CONTRARIAN"\n      ],\n      "type": "string"\n    },\n    "variable": {\n      "description": "The boolean assertion to which the function responds. Required at call time; not needed at construction if setting up a Mechanism.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nOutput is stochastic: the function draws a random integer in [-10, 10) each call, so the same inputs can produce different outputs across calls. `pertinacity` must be strictly in [0, 10] — values outside this range raise a FunctionError at validation time. Pass `propensity` as the string "OBSEQUIOUS" or "CONTRARIAN", not as an integer; the host template resolves these to the `ArgumentTherapy.Manner` enum. At `pertinacity=10` with CONTRARIAN, output is almost always False; at `pertinacity=0` with OBSEQUIOUS, output is almost always False too — the asymmetry comes from the half-open random range (-10 inclusive, 10 exclusive). This is an example/demo class in PNL, not intended for production neuroscience models.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Name for this Function instance. '
                                           'Auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'pertinacity': { 'default': 10,
                                   'description': 'Therapeutic consistency, 0–10. '
                                                  'Higher values make the response '
                                                  'more reliably match the propensity; '
                                                  'lower values introduce more '
                                                  'randomness.',
                                   'maximum': 10,
                                   'minimum': 0,
                                   'type': 'number'},
                  'propensity': { 'default': 'CONTRARIAN',
                                  'description': 'Therapeutic manner. OBSEQUIOUS tends '
                                                 'to agree with the input; CONTRARIAN '
                                                 'tends to disagree. Consistency of '
                                                 'the tendency is set by pertinacity.',
                                  'enum': ['OBSEQUIOUS', 'CONTRARIAN'],
                                  'type': 'string'},
                  'variable': { 'description': 'The boolean assertion to which the '
                                               'function responds. Required at call '
                                               'time; not needed at construction if '
                                               'setting up a Mechanism.',
                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Output is stochastic: the function draws a random integer in [-10, 10) each call, so the same inputs can produce different outputs across calls. `pertinacity` must be strictly in [0, 10] — values outside this range raise a FunctionError at validation time. Pass `propensity` as the string "OBSEQUIOUS" or "CONTRARIAN", not as an integer; the host template resolves these to the `ArgumentTherapy.Manner` enum. At `pertinacity=10` with CONTRARIAN, output is almost always False; at `pertinacity=0` with OBSEQUIOUS, output is almost always False too — the asymmetry comes from the half-open random range (-10 inclusive, 10 exclusive). This is an example/demo class in PNL, not intended for production neuroscience models.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ArgumentTherapy
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
    def create_argument_therapy(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a stochastic boolean-response function that mimics a therapist either agreeing or disagreeing with a boolean assertion.'
        return _impl(args or {})
