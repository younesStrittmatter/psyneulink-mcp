"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '52dc0455236fb87a2a4bb2c54767b32bce2cc68fb71896f0c641d356950e2f96'
__pnl_qualname__ = 'psyneulink.Identity'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_identity'
TOOL_DESCRIPTION = 'Use this tool to create a PsyNeuLink Identity transfer function — a pass-through that returns its input unchanged. Call it when assigning a Mechanism\'s function and you want no transformation applied (e.g., a relay node, a buffer, or to explicitly suppress any default nonlinearity). The result is an Identity instance ready to be passed as the `function` argument to a Mechanism or Projection.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the value the function will receive and return. Accepts a scalar or a list representing an array. Determines the shape of the function\'s variable.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this Identity instance. If omitted, FunctionRegistry assigns a default name.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary. Values here override constructor arguments. Rarely needed for Identity since it has no tunable parameters.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nIdentity has no learnable or tunable parameters — it is a strict pass-through. `owner` and `prefs` are omitted from the schema because they accept live PsyNeuLink Component/PreferenceSet objects that cannot be expressed as JSON; the framework typically sets `owner` automatically when the function is assigned to a Mechanism. `default_variable` shapes the function\'s port but does not filter or truncate input at runtime — Identity always returns whatever variable it receives verbatim.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the value the '
                                                       'function will receive and '
                                                       'return. Accepts a scalar or a '
                                                       'list representing an array. '
                                                       'Determines the shape of the '
                                                       "function's variable.",
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'name': { 'description': 'Name for this Identity instance. If '
                                           'omitted, FunctionRegistry assigns a '
                                           'default name.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary. Values '
                                             'here override constructor arguments. '
                                             'Rarely needed for Identity since it has '
                                             'no tunable parameters.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Identity has no learnable or tunable parameters — it is a strict pass-through. `owner` and `prefs` are omitted from the schema because they accept live PsyNeuLink Component/PreferenceSet objects that cannot be expressed as JSON; the framework typically sets `owner` automatically when the function is assigned to a Mechanism. `default_variable` shapes the function's port but does not filter or truncate input at runtime — Identity always returns whatever variable it receives verbatim."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Identity
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
    def create_identity(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a PsyNeuLink Identity transfer function — a pass-through that returns its input unchanged.'
        return _impl(args or {})
