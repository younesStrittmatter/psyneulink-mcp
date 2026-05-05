"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e4096d08651bbe567fb214a81db5d51a8048ce310bf7e137173cebd4ec2c0ff5'
__pnl_qualname__ = 'psyneulink.parameter_spec'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'parameter_spec'
TOOL_DESCRIPTION = 'Call this tool to validate that a candidate value is a legal PsyNeuLink parameter specification before passing it to a PNL component or function. Returns `true` if the value qualifies (numbers, arrays, lists, tuples, dicts, recognized keyword strings, or Component/Projection class names), `false` otherwise. Use it as a pre-flight check when you are unsure whether a user-supplied or computed value is PNL-compatible.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "numeric_only": {\n      "default": false,\n      "description": "If true, additionally requires that the param is numeric (a number or numeric array). Defaults to false (None) when omitted.",\n      "type": "boolean"\n    },\n    "param": {\n      "description": "The candidate value to validate. Pass a number, array, list, tuple, dict, or a string that names a PNL keyword (MODULATORY_SPEC_KEYWORDS or parameter_keywords) or a Component/Projection class name. Arbitrary strings that are not PNL keywords will return false.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "string"\n        },\n        {\n          "type": "array"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    }\n  },\n  "required": [\n    "param"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `numeric_only=None` (the Python default) behaves identically to `False`; only pass `true` when you specifically need to reject non-numeric specs such as keyword strings or dicts.\n- Functions and live Projection/Component instances are valid PNL parameter specs in Python but cannot be serialized through MCP JSON; only their JSON-representable equivalents (numbers, arrays, lists, dicts, keyword strings) are practically testable via this tool.\n- A string is matched against PNL\'s internal MODULATORY_SPEC_KEYWORDS and parameter_keywords sets — arbitrary strings are not accepted as valid specs.\n- The tool is primarily a typecheck utility; most modeling workflows won\'t need it unless implementing custom validation before constructing PNL components.'
TOOL_PARAMETERS = { 'properties': { 'numeric_only': { 'default': False,
                                    'description': 'If true, additionally requires '
                                                   'that the param is numeric (a '
                                                   'number or numeric array). Defaults '
                                                   'to false (None) when omitted.',
                                    'type': 'boolean'},
                  'param': { 'description': 'The candidate value to validate. Pass a '
                                            'number, array, list, tuple, dict, or a '
                                            'string that names a PNL keyword '
                                            '(MODULATORY_SPEC_KEYWORDS or '
                                            'parameter_keywords) or a '
                                            'Component/Projection class name. '
                                            'Arbitrary strings that are not PNL '
                                            'keywords will return false.',
                             'oneOf': [ {'type': 'number'},
                                        {'type': 'string'},
                                        {'type': 'array'},
                                        {'type': 'object'}]}},
  'required': ['param'],
  'type': 'object'}
TOOL_NOTES = "- `numeric_only=None` (the Python default) behaves identically to `False`; only pass `true` when you specifically need to reject non-numeric specs such as keyword strings or dicts.\n- Functions and live Projection/Component instances are valid PNL parameter specs in Python but cannot be serialized through MCP JSON; only their JSON-representable equivalents (numbers, arrays, lists, dicts, keyword strings) are practically testable via this tool.\n- A string is matched against PNL's internal MODULATORY_SPEC_KEYWORDS and parameter_keywords sets — arbitrary strings are not accepted as valid specs.\n- The tool is primarily a typecheck utility; most modeling workflows won't need it unless implementing custom validation before constructing PNL components."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.parameter_spec
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
    def parameter_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to validate that a candidate value is a legal PsyNeuLink parameter specification before passing it to a PNL component or function.'
        return _impl(args or {})
