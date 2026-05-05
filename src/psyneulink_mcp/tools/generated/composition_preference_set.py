"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c4209d08591ed0d092332d480d2c964d58fe2a5ae3989f890dbb2d8fc8f20b19'
__pnl_qualname__ = 'psyneulink.CompositionPreferenceSet'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_composition_preference_set'
TOOL_DESCRIPTION = 'Call this tool to create a CompositionPreferenceSet — a preference configuration object that controls Composition-specific behavior, particularly whether simulation runtime parameters are recorded and used to update the execute method\'s parameters. Pass it to a Composition\'s `prefs` argument when you need to customize simulation recording behavior beyond the default.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "record_simulation_pref": {\n      "description": "Whether to record simulation runtime parameters and use them to update the execute method\'s parameters. Defaults to the system-level recordSimulation preference default if omitted.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe `record_simulation_pref` argument accepts either a plain boolean or a PreferenceEntry (a tuple of `(setting, PreferenceLevel)`). Passing a boolean uses the instance-level default; passing a PreferenceEntry lets you specify inheritance level (e.g., SYSTEM, CATEGORY, TYPE, INSTANCE). The constructor also accepts arbitrary `**kargs` forwarded to `BasePreferenceSet`, including standard preference keys like `verbosePref`, `paramValidationPref`, `reportOutputPref`, `logPref`, and `deliverLogValueToMechanism`. If `record_simulation_pref` is passed both as a positional argument and inside `kargs`, the `kargs` value takes precedence.'
TOOL_PARAMETERS = { 'properties': { 'record_simulation_pref': { 'description': 'Whether to record '
                                                             'simulation runtime '
                                                             'parameters and use them '
                                                             'to update the execute '
                                                             "method's parameters. "
                                                             'Defaults to the '
                                                             'system-level '
                                                             'recordSimulation '
                                                             'preference default if '
                                                             'omitted.',
                                              'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The `record_simulation_pref` argument accepts either a plain boolean or a PreferenceEntry (a tuple of `(setting, PreferenceLevel)`). Passing a boolean uses the instance-level default; passing a PreferenceEntry lets you specify inheritance level (e.g., SYSTEM, CATEGORY, TYPE, INSTANCE). The constructor also accepts arbitrary `**kargs` forwarded to `BasePreferenceSet`, including standard preference keys like `verbosePref`, `paramValidationPref`, `reportOutputPref`, `logPref`, and `deliverLogValueToMechanism`. If `record_simulation_pref` is passed both as a positional argument and inside `kargs`, the `kargs` value takes precedence.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.CompositionPreferenceSet
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
    def create_composition_preference_set(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to create a CompositionPreferenceSet — a preference configuration object that controls Composition-specific behavior, particularly whether simulation runtime parameters are recorded and used to update the execute method's parameters."
        return _impl(args or {})
