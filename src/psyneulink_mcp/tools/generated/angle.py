"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '25eb5e0001fd19375e3a75e664b469ad245bfca2d3ab1107dc0158bfe044dfbe'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.transferfunctions.Angle'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_angle'
TOOL_DESCRIPTION = 'Do NOT call this tool — `Angle` is deprecated and will be removed in a future release. Use `hyperspherical_to_cartesian` (the `HypersphericalToCartesian` tool) instead. If you encounter existing code or a saved model that references `Angle`, you can instantiate it here for backward compatibility only; it behaves identically to `HypersphericalToCartesian`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Input array of hyperspherical coordinates (angles). Passed directly to HypersphericalToCartesian.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "owner": {\n      "additionalProperties": true,\n      "description": "PsyNeuLink Component that owns this function. Usually set automatically when the function is assigned to a mechanism.",\n      "type": "object"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional dict of parameter overrides. Use sparingly; prefer named arguments.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDEPRECATED — emits a DeprecationWarning at instantiation time. Prefer `HypersphericalToCartesian` for all new code. The `prefs` argument is intentionally omitted from the schema since it requires a PsyNeuLink `ValidPrefSet` object that cannot be expressed in JSON Schema; leave it unset and the class defaults apply. This class used a non-standard hyperspherical parameterization in older versions; the current implementation simply delegates to `HypersphericalToCartesian`, so behavior is now identical.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Input array of hyperspherical '
                                                       'coordinates (angles). Passed '
                                                       'directly to '
                                                       'HypersphericalToCartesian.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'owner': { 'additionalProperties': True,
                             'description': 'PsyNeuLink Component that owns this '
                                            'function. Usually set automatically when '
                                            'the function is assigned to a mechanism.',
                             'type': 'object'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional dict of parameter overrides. '
                                             'Use sparingly; prefer named arguments.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'DEPRECATED — emits a DeprecationWarning at instantiation time. Prefer `HypersphericalToCartesian` for all new code. The `prefs` argument is intentionally omitted from the schema since it requires a PsyNeuLink `ValidPrefSet` object that cannot be expressed in JSON Schema; leave it unset and the class defaults apply. This class used a non-standard hyperspherical parameterization in older versions; the current implementation simply delegates to `HypersphericalToCartesian`, so behavior is now identical.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Angle
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
    def create_angle(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool — `Angle` is deprecated and will be removed in a future release.'
        return _impl(args or {})
