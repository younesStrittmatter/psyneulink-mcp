"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '006375fea4294ba03570f29207cf8209b835af1ac232b07a58edabb7899a0ce2'
__pnl_qualname__ = 'psyneulink.BasePreferenceSet'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_base_preference_set'
TOOL_DESCRIPTION = 'Call this tool when you need to create a shared preference configuration for one or more PsyNeuLink components — controlling verbose output, parameter validation, execution reporting, logging, and runtime parameter modulation. Returns a `BasePreferenceSet` instance that can be passed as the `prefs` argument when constructing any PsyNeuLink Component, or assigned directly to a component\'s `prefs` attribute to override its class-level defaults.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "level": {\n      "description": "The default PreferenceLevel for this PreferenceSet. Determines how far up the class hierarchy to look when a preference is not set at the instance level. Defaults to \'COMPOSITION\'.",\n      "enum": [\n        "COMPOSITION",\n        "CATEGORY",\n        "TYPE",\n        "SUBTYPE",\n        "INSTANCE"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for this PreferenceSet. Used for display and identification only.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "Name of the PsyNeuLink Component class or instance that owns this PreferenceSet. Used to resolve appropriate class-level defaults. If omitted, defaults to DefaultProcessingMechanism. Rarely needed when constructing a shared PreferenceSet for later assignment.",\n      "type": "string"\n    },\n    "prefs": {\n      "additionalProperties": true,\n      "description": "Dict mapping PNL preference keyword constants to values, PreferenceSets, or PreferenceLevel strings. Valid keys: \'VERBOSE_PREF\', \'PARAM_VALIDATION_PREF\', \'REPORT_OUTPUT_PREF\', \'LOG_PREF\', \'DELIVERY_PREF\', \'RUNTIME_PARAM_MODULATION_PREF\', \'PREFERENCE_SET_NAME\'. Each value can be the raw setting (e.g., true/false) or a PreferenceLevel string (\'COMPOSITION\', \'CATEGORY\', \'TYPE\', \'SUBTYPE\', \'INSTANCE\').",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nPreference key strings must be PNL keyword constants (e.g., \'VERBOSE_PREF\', \'PARAM_VALIDATION_PREF\'), not Python attribute names like \'verbosePref\' — passing attribute-style names silently has no effect. REPORT_OUTPUT_PREF accepts bool or ReportOutput enum values; True maps internally to ReportOutput.TERSE and False to ReportOutput.OFF. A single BasePreferenceSet can be shared across multiple components; the effective owner is resolved dynamically at access time, so class-level preferences propagate correctly. Most agents do not need to instantiate this directly — PNL components carry their own classPreferences and accept a prefs dict on construction without requiring an explicit BasePreferenceSet wrapper.'
TOOL_PARAMETERS = { 'properties': { 'level': { 'description': 'The default PreferenceLevel for this '
                                            'PreferenceSet. Determines how far up the '
                                            'class hierarchy to look when a preference '
                                            'is not set at the instance level. '
                                            "Defaults to 'COMPOSITION'.",
                             'enum': [ 'COMPOSITION',
                                       'CATEGORY',
                                       'TYPE',
                                       'SUBTYPE',
                                       'INSTANCE'],
                             'type': 'string'},
                  'name': { 'description': 'Optional name for this PreferenceSet. Used '
                                           'for display and identification only.',
                            'type': 'string'},
                  'owner': { 'description': 'Name of the PsyNeuLink Component class or '
                                            'instance that owns this PreferenceSet. '
                                            'Used to resolve appropriate class-level '
                                            'defaults. If omitted, defaults to '
                                            'DefaultProcessingMechanism. Rarely needed '
                                            'when constructing a shared PreferenceSet '
                                            'for later assignment.',
                             'type': 'string'},
                  'prefs': { 'additionalProperties': True,
                             'description': 'Dict mapping PNL preference keyword '
                                            'constants to values, PreferenceSets, or '
                                            'PreferenceLevel strings. Valid keys: '
                                            "'VERBOSE_PREF', 'PARAM_VALIDATION_PREF', "
                                            "'REPORT_OUTPUT_PREF', 'LOG_PREF', "
                                            "'DELIVERY_PREF', "
                                            "'RUNTIME_PARAM_MODULATION_PREF', "
                                            "'PREFERENCE_SET_NAME'. Each value can be "
                                            'the raw setting (e.g., true/false) or a '
                                            "PreferenceLevel string ('COMPOSITION', "
                                            "'CATEGORY', 'TYPE', 'SUBTYPE', "
                                            "'INSTANCE').",
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Preference key strings must be PNL keyword constants (e.g., 'VERBOSE_PREF', 'PARAM_VALIDATION_PREF'), not Python attribute names like 'verbosePref' — passing attribute-style names silently has no effect. REPORT_OUTPUT_PREF accepts bool or ReportOutput enum values; True maps internally to ReportOutput.TERSE and False to ReportOutput.OFF. A single BasePreferenceSet can be shared across multiple components; the effective owner is resolved dynamically at access time, so class-level preferences propagate correctly. Most agents do not need to instantiate this directly — PNL components carry their own classPreferences and accept a prefs dict on construction without requiring an explicit BasePreferenceSet wrapper."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.BasePreferenceSet
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
    def create_base_preference_set(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to create a shared preference configuration for one or more PsyNeuLink components — controlling verbose output, parameter validation, execution reporting, logging, and runtime parameter modulation.'
        return _impl(args or {})
