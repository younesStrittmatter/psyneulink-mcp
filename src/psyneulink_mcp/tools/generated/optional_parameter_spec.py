"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'bc870ff24d43bbb349e50744f524527f419e0e6dadf5225ec0bedc1d2e7567ca'
__pnl_qualname__ = 'psyneulink.optional_parameter_spec'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'optional_parameter_spec'
TOOL_DESCRIPTION = 'Call this tool when you need to validate that a value is either None or a legal PsyNeuLink parameter specification before passing it to a component that requires an optional parameter. Returns true if the value is None or passes the parameter_spec check, false otherwise — use the result to gate downstream calls or report schema mismatches.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "param": {\n      "description": "The value to validate. Pass null to confirm None is acceptable, or pass a candidate parameter specification (number, array, string, or object) to check if it is a legal PsyNeuLink parameter spec.",\n      "oneOf": [\n        {\n          "type": "null"\n        },\n        {\n          "type": "number"\n        },\n        {\n          "type": "string"\n        },\n        {\n          "type": "boolean"\n        },\n        {\n          "type": "array"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    }\n  },\n  "required": [\n    "param"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe check `if not param` short-circuits for any falsy value (None, 0, empty list, empty string, False) — all return True without calling parameter_spec. This means passing 0 or [] will return True even though they may not be meaningful parameter specs. Only use this tool to validate non-falsy candidate values when strict parameter_spec checking is needed; for falsy inputs the result is vacuously True.'
TOOL_PARAMETERS = { 'properties': { 'param': { 'description': 'The value to validate. Pass null to '
                                            'confirm None is acceptable, or pass a '
                                            'candidate parameter specification '
                                            '(number, array, string, or object) to '
                                            'check if it is a legal PsyNeuLink '
                                            'parameter spec.',
                             'oneOf': [ {'type': 'null'},
                                        {'type': 'number'},
                                        {'type': 'string'},
                                        {'type': 'boolean'},
                                        {'type': 'array'},
                                        {'type': 'object'}]}},
  'required': ['param'],
  'type': 'object'}
TOOL_NOTES = 'The check `if not param` short-circuits for any falsy value (None, 0, empty list, empty string, False) — all return True without calling parameter_spec. This means passing 0 or [] will return True even though they may not be meaningful parameter specs. Only use this tool to validate non-falsy candidate values when strict parameter_spec checking is needed; for falsy inputs the result is vacuously True.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.optional_parameter_spec
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
    def optional_parameter_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to validate that a value is either None or a legal PsyNeuLink parameter specification before passing it to a component that requires an optional parameter.'
        return _impl(args or {})
