"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7d59326d08f38fcb04bcceea6985b50ef4cdcd97ca58d321484a420169b3f281'
__pnl_qualname__ = 'psyneulink.PreferenceSet'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_preference_set'
TOOL_DESCRIPTION = 'Call this tool only when you need to inspect or understand PsyNeuLink\'s preference management infrastructure — for example, to introspect the preference hierarchy or serve as a base reference when working with concrete PreferenceSet subclasses (e.g., ComponentPreferenceSet, MechanismPreferenceSet). Do NOT call this tool to instantiate a PreferenceSet directly; PreferenceSet is abstract and will raise an error if instantiated without a concrete subclass that defines `defaultPreferencesDict` and `baseClass`. Use concrete subclass tools instead when configuring component preferences.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "level": {\n      "default": "COMPOSITION",\n      "description": "PreferenceLevel at which to report settings. One of: \'SYSTEM\', \'CATEGORY\', \'TYPE\', \'INSTANCE\', \'COMPOSITION\'. Determines which level of the class hierarchy is queried when a preference setting is requested. Defaults to COMPOSITION.",\n      "enum": [\n        "SYSTEM",\n        "CATEGORY",\n        "TYPE",\n        "INSTANCE",\n        "COMPOSITION"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for this PreferenceSet instance. If omitted, the name is auto-generated as \'<SubclassName>DefaultsFor<OwnerClassName>\'.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "Name of the PsyNeuLink Component class or object instance that will own this PreferenceSet. Must be a class or instance within the baseClass hierarchy defined by the concrete subclass.",\n      "type": "string"\n    },\n    "prefs": {\n      "additionalProperties": true,\n      "description": "Specification dict for preferences. Keys must be keyPath strings for preference attributes (e.g., \'kpReportOutput\', \'kpLog\', \'kpVerbose\', \'kpParamValidation\'). Values can be a PreferenceEntry (setting, level) tuple, a valid setting value, or a PreferenceLevel string. Any preferences not specified here are filled from the subclass defaultPreferencesDict.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "owner"\n  ],\n  "type": "object"\n}\n\nNotes:\nPreferenceSet is an abstract class and cannot be instantiated directly — calling psyneulink.PreferenceSet(...) will raise a TypeError or PreferenceSetError unless called from a concrete subclass that defines both `defaultPreferencesDict` (dict of default PreferenceEntry values) and `baseClass` (the root class of the hierarchy). The `level` parameter default in the docstring says PreferenceLevel.SYSTEM but the actual source code defaults to PreferenceLevel.COMPOSITION — use COMPOSITION as the real default. The `context` parameter from the signature is accepted but has no documented effect in current usage and can be omitted. Preference attribute names on subclass instances MUST contain the substring \'_pref\' to be recognized by show() and related methods. The `prefs` dict keys are keyPath strings like \'kpLog\', not arbitrary strings; invalid keys are silently ignored or cause a KeyError depending on the condition path taken during init.'
TOOL_PARAMETERS = { 'properties': { 'level': { 'default': 'COMPOSITION',
                             'description': 'PreferenceLevel at which to report '
                                            "settings. One of: 'SYSTEM', 'CATEGORY', "
                                            "'TYPE', 'INSTANCE', 'COMPOSITION'. "
                                            'Determines which level of the class '
                                            'hierarchy is queried when a preference '
                                            'setting is requested. Defaults to '
                                            'COMPOSITION.',
                             'enum': [ 'SYSTEM',
                                       'CATEGORY',
                                       'TYPE',
                                       'INSTANCE',
                                       'COMPOSITION'],
                             'type': 'string'},
                  'name': { 'description': 'Name for this PreferenceSet instance. If '
                                           'omitted, the name is auto-generated as '
                                           "'<SubclassName>DefaultsFor<OwnerClassName>'.",
                            'type': 'string'},
                  'owner': { 'description': 'Name of the PsyNeuLink Component class or '
                                            'object instance that will own this '
                                            'PreferenceSet. Must be a class or '
                                            'instance within the baseClass hierarchy '
                                            'defined by the concrete subclass.',
                             'type': 'string'},
                  'prefs': { 'additionalProperties': True,
                             'description': 'Specification dict for preferences. Keys '
                                            'must be keyPath strings for preference '
                                            "attributes (e.g., 'kpReportOutput', "
                                            "'kpLog', 'kpVerbose', "
                                            "'kpParamValidation'). Values can be a "
                                            'PreferenceEntry (setting, level) tuple, a '
                                            'valid setting value, or a PreferenceLevel '
                                            'string. Any preferences not specified '
                                            'here are filled from the subclass '
                                            'defaultPreferencesDict.',
                             'type': 'object'}},
  'required': ['owner'],
  'type': 'object'}
TOOL_NOTES = "PreferenceSet is an abstract class and cannot be instantiated directly — calling psyneulink.PreferenceSet(...) will raise a TypeError or PreferenceSetError unless called from a concrete subclass that defines both `defaultPreferencesDict` (dict of default PreferenceEntry values) and `baseClass` (the root class of the hierarchy). The `level` parameter default in the docstring says PreferenceLevel.SYSTEM but the actual source code defaults to PreferenceLevel.COMPOSITION — use COMPOSITION as the real default. The `context` parameter from the signature is accepted but has no documented effect in current usage and can be omitted. Preference attribute names on subclass instances MUST contain the substring '_pref' to be recognized by show() and related methods. The `prefs` dict keys are keyPath strings like 'kpLog', not arbitrary strings; invalid keys are silently ignored or cause a KeyError depending on the condition path taken during init."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PreferenceSet
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
    def create_preference_set(args: dict[str, Any] | None = None) -> Any:
        "Call this tool only when you need to inspect or understand PsyNeuLink's preference management infrastructure — for example, to introspect the preference hierarchy or serve as a base reference when working with concrete PreferenceSet subclasses (e.g., ComponentPreferenceSet, MechanismPreferenceSet)."
        return _impl(args or {})
