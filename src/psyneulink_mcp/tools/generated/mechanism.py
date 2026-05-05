"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ed9f10960d87126524669ea7084cb8128621de90ddb7306c8c9bde15f524d28d'
__pnl_qualname__ = 'psyneulink.Mechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_mechanism'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — Mechanism is an abstract base class that cannot be instantiated. Use a concrete Mechanism subclass tool instead (e.g., TransferMechanism, IntegratorMechanism, LCAMechanism). This tool exists only as a reference for the shared constructor signature common to all Mechanism subclasses.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input to the Mechanism\'s function; also used as the default input when none is provided at execution. Typically a 2D array or list of arrays.",\n      "type": "array"\n    },\n    "function": {\n      "description": "Name or specification of the Function to use; overrides the subclass default. Most agents should omit this and let the subclass pick its default function.",\n      "type": "string"\n    },\n    "input_shapes": {\n      "description": "Specifies the shape of default_variable as zero-filled arrays; ignored if default_variable is also provided (they are checked for compatibility).",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "integer"\n              },\n              {\n                "items": {\n                  "type": "integer"\n                },\n                "type": "array"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for the Mechanism instance; auto-assigned from the subclass registry if omitted.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Parameter dictionary overriding constructor argument values; keys are PNL parameter keywords.",\n      "type": "object"\n    },\n    "prefs": {\n      "additionalProperties": true,\n      "description": "PreferenceSet or specification dict controlling logging, reporting, and other preferences.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMechanism is abstract — calling it directly raises an error. Always use a concrete subclass. The `function` parameter is listed here for completeness but is almost never specified by agents; subclasses provide sensible defaults. `param_defaults` in the source signature is an internal alias and should not be passed by agents (use `params` instead). `default_variable` and `input_shapes` are mutually exclusive in effect: if both are given, compatibility is checked and a mismatch raises an error.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input to the '
                                                       "Mechanism's function; also "
                                                       'used as the default input when '
                                                       'none is provided at execution. '
                                                       'Typically a 2D array or list '
                                                       'of arrays.',
                                        'type': 'array'},
                  'function': { 'description': 'Name or specification of the Function '
                                               'to use; overrides the subclass '
                                               'default. Most agents should omit this '
                                               'and let the subclass pick its default '
                                               'function.',
                                'type': 'string'},
                  'input_shapes': { 'description': 'Specifies the shape of '
                                                   'default_variable as zero-filled '
                                                   'arrays; ignored if '
                                                   'default_variable is also provided '
                                                   '(they are checked for '
                                                   'compatibility).',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': { 'oneOf': [ { 'type': 'integer'},
                                                                       { 'items': { 'type': 'integer'},
                                                                         'type': 'array'}]},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Name for the Mechanism instance; '
                                           'auto-assigned from the subclass registry '
                                           'if omitted.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Parameter dictionary overriding '
                                             'constructor argument values; keys are '
                                             'PNL parameter keywords.',
                              'type': 'object'},
                  'prefs': { 'additionalProperties': True,
                             'description': 'PreferenceSet or specification dict '
                                            'controlling logging, reporting, and other '
                                            'preferences.',
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Mechanism is abstract — calling it directly raises an error. Always use a concrete subclass. The `function` parameter is listed here for completeness but is almost never specified by agents; subclasses provide sensible defaults. `param_defaults` in the source signature is an internal alias and should not be passed by agents (use `params` instead). `default_variable` and `input_shapes` are mutually exclusive in effect: if both are given, compatibility is checked and a mismatch raises an error.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Mechanism
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
    def create_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — Mechanism is an abstract base class that cannot be instantiated.'
        return _impl(args or {})
