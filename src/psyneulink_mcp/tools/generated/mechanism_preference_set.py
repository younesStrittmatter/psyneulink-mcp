"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4a3acc88f6bdcd823facf03d99d4bcbe6d2f79dbe15a35223290d02a285e2911'
__pnl_qualname__ = 'psyneulink.MechanismPreferenceSet'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_mechanism_preference_set'
TOOL_DESCRIPTION = 'Call this tool to create a MechanismPreferenceSet that configures mechanism-level behavioral preferences, particularly whether runtime parameter modulation is active. Use it when you need to attach or customize a preference set on a Mechanism, overriding defaults for output reporting, logging, verbosity, parameter validation, or runtime param modulation. Returns a MechanismPreferenceSet instance that can be assigned to a Mechanism\'s `prefs` attribute.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "level": {\n      "default": "COMPOSITION",\n      "description": "Overall PreferenceLevel for this preference set. Defaults to COMPOSITION.",\n      "enum": [\n        "INSTANCE",\n        "COMPOSITION",\n        "CATEGORY",\n        "ALL"\n      ],\n      "type": "string"\n    },\n    "log_pref": {\n      "description": "PreferenceEntry controlling logging behavior. Provide as {\\"setting\\": <LogCondition string e.g. \'OFF\', \'INITIALIZATION\', \'VALIDATION\', \'EXECUTION\', \'ALL_ASSIGNMENTS\'>, \\"level\\": <PreferenceLevel string>}.",\n      "properties": {\n        "level": {\n          "enum": [\n            "INSTANCE",\n            "COMPOSITION",\n            "CATEGORY",\n            "ALL"\n          ],\n          "type": "string"\n        },\n        "setting": {\n          "enum": [\n            "OFF",\n            "INITIALIZATION",\n            "VALIDATION",\n            "EXECUTION",\n            "ALL_ASSIGNMENTS"\n          ],\n          "type": "string"\n        }\n      },\n      "type": "object"\n    },\n    "name": {\n      "description": "Optional name for this preference set instance.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "Name or reference to the Mechanism that owns this preference set. Pass the mechanism\'s name string; the host resolves it.",\n      "type": "string"\n    },\n    "param_validation_pref": {\n      "description": "PreferenceEntry for whether parameters are validated during execution. Provide as {\\"setting\\": <bool>, \\"level\\": <PreferenceLevel string>}.",\n      "properties": {\n        "level": {\n          "enum": [\n            "INSTANCE",\n            "COMPOSITION",\n            "CATEGORY",\n            "ALL"\n          ],\n          "type": "string"\n        },\n        "setting": {\n          "type": "boolean"\n        }\n      },\n      "type": "object"\n    },\n    "reportOutput_pref": {\n      "description": "PreferenceEntry for whether the mechanism reports its output after execution. Provide as {\\"setting\\": <bool or ReportOutput enum string>, \\"level\\": <PreferenceLevel string>}.",\n      "properties": {\n        "level": {\n          "enum": [\n            "INSTANCE",\n            "COMPOSITION",\n            "CATEGORY",\n            "ALL"\n          ],\n          "type": "string"\n        },\n        "setting": {\n          "type": "boolean"\n        }\n      },\n      "type": "object"\n    },\n    "runtimeParamModulation_pref": {\n      "description": "PreferenceEntry controlling whether runtime parameters modulate the execute method. Provide as {\\"setting\\": <Modulation value or function>, \\"level\\": <PreferenceLevel string>}. Defaults to runtimeParamModulationPrefInstanceDefault.",\n      "properties": {\n        "level": {\n          "description": "PreferenceLevel at which this preference applies",\n          "enum": [\n            "INSTANCE",\n            "COMPOSITION",\n            "CATEGORY",\n            "ALL"\n          ],\n          "type": "string"\n        },\n        "setting": {\n          "description": "Modulation setting value (e.g. \'MULTIPLICATIVE\', \'ADDITIVE\', \'OVERRIDE\', \'DISABLE\')",\n          "type": "string"\n        }\n      },\n      "type": "object"\n    },\n    "verbose_pref": {\n      "description": "PreferenceEntry for verbose output during execution. Provide as {\\"setting\\": <bool>, \\"level\\": <PreferenceLevel string>}.",\n      "properties": {\n        "level": {\n          "enum": [\n            "INSTANCE",\n            "COMPOSITION",\n            "CATEGORY",\n            "ALL"\n          ],\n          "type": "string"\n        },\n        "setting": {\n          "type": "boolean"\n        }\n      },\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThere is a subtle bug in the source: inside the `kargs` branch the local variable is named `runtime_param_modulation_pref` (no leading `runtimeParam`), so if extra kwargs are supplied via `**kargs` the preference is read from `kargs[RUNTIME_PARAM_MODULATION_PREF]` into that local, but if no kargs are given the constructor parameter `runtimeParamModulation_pref` is used directly — behaviour is consistent for normal usage but could be surprising with unusual kwargs. All preference arguments are PNL `PreferenceEntry` namedtuples (setting, level); passing raw dicts may not work unless the host adapter converts them. The `level` parameter here sets the default lookup level for the *set*, not for individual preferences — each preference has its own level field in its `PreferenceEntry`. `owner` is typically set automatically when a Mechanism creates its own preference set; only supply it when constructing one manually to attach later.'
TOOL_PARAMETERS = { 'properties': { 'level': { 'default': 'COMPOSITION',
                             'description': 'Overall PreferenceLevel for this '
                                            'preference set. Defaults to COMPOSITION.',
                             'enum': ['INSTANCE', 'COMPOSITION', 'CATEGORY', 'ALL'],
                             'type': 'string'},
                  'log_pref': { 'description': 'PreferenceEntry controlling logging '
                                               'behavior. Provide as {"setting": '
                                               "<LogCondition string e.g. 'OFF', "
                                               "'INITIALIZATION', 'VALIDATION', "
                                               "'EXECUTION', 'ALL_ASSIGNMENTS'>, "
                                               '"level": <PreferenceLevel string>}.',
                                'properties': { 'level': { 'enum': [ 'INSTANCE',
                                                                     'COMPOSITION',
                                                                     'CATEGORY',
                                                                     'ALL'],
                                                           'type': 'string'},
                                                'setting': { 'enum': [ 'OFF',
                                                                       'INITIALIZATION',
                                                                       'VALIDATION',
                                                                       'EXECUTION',
                                                                       'ALL_ASSIGNMENTS'],
                                                             'type': 'string'}},
                                'type': 'object'},
                  'name': { 'description': 'Optional name for this preference set '
                                           'instance.',
                            'type': 'string'},
                  'owner': { 'description': 'Name or reference to the Mechanism that '
                                            'owns this preference set. Pass the '
                                            "mechanism's name string; the host "
                                            'resolves it.',
                             'type': 'string'},
                  'param_validation_pref': { 'description': 'PreferenceEntry for '
                                                            'whether parameters are '
                                                            'validated during '
                                                            'execution. Provide as '
                                                            '{"setting": <bool>, '
                                                            '"level": <PreferenceLevel '
                                                            'string>}.',
                                             'properties': { 'level': { 'enum': [ 'INSTANCE',
                                                                                  'COMPOSITION',
                                                                                  'CATEGORY',
                                                                                  'ALL'],
                                                                        'type': 'string'},
                                                             'setting': { 'type': 'boolean'}},
                                             'type': 'object'},
                  'reportOutput_pref': { 'description': 'PreferenceEntry for whether '
                                                        'the mechanism reports its '
                                                        'output after execution. '
                                                        'Provide as {"setting": <bool '
                                                        'or ReportOutput enum string>, '
                                                        '"level": <PreferenceLevel '
                                                        'string>}.',
                                         'properties': { 'level': { 'enum': [ 'INSTANCE',
                                                                              'COMPOSITION',
                                                                              'CATEGORY',
                                                                              'ALL'],
                                                                    'type': 'string'},
                                                         'setting': { 'type': 'boolean'}},
                                         'type': 'object'},
                  'runtimeParamModulation_pref': { 'description': 'PreferenceEntry '
                                                                  'controlling whether '
                                                                  'runtime parameters '
                                                                  'modulate the '
                                                                  'execute method. '
                                                                  'Provide as '
                                                                  '{"setting": '
                                                                  '<Modulation value '
                                                                  'or function>, '
                                                                  '"level": '
                                                                  '<PreferenceLevel '
                                                                  'string>}. Defaults '
                                                                  'to '
                                                                  'runtimeParamModulationPrefInstanceDefault.',
                                                   'properties': { 'level': { 'description': 'PreferenceLevel '
                                                                                             'at '
                                                                                             'which '
                                                                                             'this '
                                                                                             'preference '
                                                                                             'applies',
                                                                              'enum': [ 'INSTANCE',
                                                                                        'COMPOSITION',
                                                                                        'CATEGORY',
                                                                                        'ALL'],
                                                                              'type': 'string'},
                                                                   'setting': { 'description': 'Modulation '
                                                                                               'setting '
                                                                                               'value '
                                                                                               '(e.g. '
                                                                                               "'MULTIPLICATIVE', "
                                                                                               "'ADDITIVE', "
                                                                                               "'OVERRIDE', "
                                                                                               "'DISABLE')",
                                                                                'type': 'string'}},
                                                   'type': 'object'},
                  'verbose_pref': { 'description': 'PreferenceEntry for verbose output '
                                                   'during execution. Provide as '
                                                   '{"setting": <bool>, "level": '
                                                   '<PreferenceLevel string>}.',
                                    'properties': { 'level': { 'enum': [ 'INSTANCE',
                                                                         'COMPOSITION',
                                                                         'CATEGORY',
                                                                         'ALL'],
                                                               'type': 'string'},
                                                    'setting': {'type': 'boolean'}},
                                    'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'There is a subtle bug in the source: inside the `kargs` branch the local variable is named `runtime_param_modulation_pref` (no leading `runtimeParam`), so if extra kwargs are supplied via `**kargs` the preference is read from `kargs[RUNTIME_PARAM_MODULATION_PREF]` into that local, but if no kargs are given the constructor parameter `runtimeParamModulation_pref` is used directly — behaviour is consistent for normal usage but could be surprising with unusual kwargs. All preference arguments are PNL `PreferenceEntry` namedtuples (setting, level); passing raw dicts may not work unless the host adapter converts them. The `level` parameter here sets the default lookup level for the *set*, not for individual preferences — each preference has its own level field in its `PreferenceEntry`. `owner` is typically set automatically when a Mechanism creates its own preference set; only supply it when constructing one manually to attach later.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.MechanismPreferenceSet
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
    def create_mechanism_preference_set(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a MechanismPreferenceSet that configures mechanism-level behavioral preferences, particularly whether runtime parameter modulation is active.'
        return _impl(args or {})
