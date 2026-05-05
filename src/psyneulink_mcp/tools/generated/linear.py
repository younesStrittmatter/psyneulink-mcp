"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '98a322b7bad6dbebd82235eb389ad02207232c77e75965068ae21b25a6cd8553'
__pnl_qualname__ = 'psyneulink.Linear'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_linear'
TOOL_DESCRIPTION = 'Call this tool to create a `psyneulink.Linear` transfer function that applies `scale * (slope * variable + intercept) + offset` element-wise to its input. Use it when assigning a linear activation function to a TransferMechanism or any PsyNeuLink component that accepts a `function` argument. Returns a configured `Linear` instance ready for assignment.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "intercept": {\n      "default": 0,\n      "description": "Value added to slope*variable before scale is applied.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for this Linear function instance.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Value added after scale is applied; shifts the output up or down.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplier applied to the entire (slope*variable + intercept) result before adding offset.",\n      "type": "number"\n    },\n    "slope": {\n      "default": 1,\n      "description": "Multiplicative factor applied to the variable before adding intercept.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nWith all defaults (slope=1, intercept=0, scale=1, offset=0) this implements the identity function and PNL may silently replace it with an `Identity` function during compilation — if you need a true Linear instance to persist (e.g., to modulate slope at runtime), set at least one parameter to a non-identity value. `scale` and `offset` are NOT equivalent to `slope` and `intercept`: the former pair is applied after the latter, so `scale=2, slope=1` differs from `scale=1, slope=2` when `intercept != 0`. The `default_variable`, `params`, `owner`, and `prefs` arguments are managed by the host template and should not be passed by the agent.'
TOOL_PARAMETERS = { 'properties': { 'intercept': { 'default': 0,
                                 'description': 'Value added to slope*variable before '
                                                'scale is applied.',
                                 'type': 'number'},
                  'name': { 'description': 'Optional name for this Linear function '
                                           'instance.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Value added after scale is applied; '
                                             'shifts the output up or down.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplier applied to the entire '
                                            '(slope*variable + intercept) result '
                                            'before adding offset.',
                             'type': 'number'},
                  'slope': { 'default': 1,
                             'description': 'Multiplicative factor applied to the '
                                            'variable before adding intercept.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'With all defaults (slope=1, intercept=0, scale=1, offset=0) this implements the identity function and PNL may silently replace it with an `Identity` function during compilation — if you need a true Linear instance to persist (e.g., to modulate slope at runtime), set at least one parameter to a non-identity value. `scale` and `offset` are NOT equivalent to `slope` and `intercept`: the former pair is applied after the latter, so `scale=2, slope=1` differs from `scale=1, slope=2` when `intercept != 0`. The `default_variable`, `params`, `owner`, and `prefs` arguments are managed by the host template and should not be passed by the agent.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Linear
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
    def create_linear(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a `psyneulink.Linear` transfer function that applies `scale * (slope * variable + intercept) + offset` element-wise to its input.'
        return _impl(args or {})
