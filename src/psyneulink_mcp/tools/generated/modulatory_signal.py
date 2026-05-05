"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'aadf149baa60f7993431b9a49ebd5017c55bba68b21dbdd89233598fda8518d1'
__pnl_qualname__ = 'psyneulink.ModulatorySignal'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_modulatory_signal'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — ModulatorySignal is an abstract base class and will raise an error if instantiated. Call it only to inspect or reference the class itself, or when you need to understand the shared interface of ControlSignal and GatingSignal. To create a modulation signal in practice, use the `control_signal` or `gating_signal` tools instead.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_allocation": {\n      "description": "Default template and initial value for the signal\'s variable (i.e., its allocation). Scalar numeric.",\n      "type": "number"\n    },\n    "function": {\n      "description": "TransferFunction used to convert allocation into the signal\'s output value. Defaults to Identity (value == allocation).",\n      "type": "string"\n    },\n    "modulates": {\n      "description": "List of Port or Mechanism specifications that this signal projects to and modulates. Each entry can be a Port name or Mechanism name.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "modulation": {\n      "description": "How the signal\'s value is applied to the modulated Port. MULTIPLICATIVE (default) scales the parameter; ADDITIVE offsets it; OVERRIDE replaces it; DISABLE removes modulation.",\n      "enum": [\n        "MULTIPLICATIVE",\n        "ADDITIVE",\n        "OVERRIDE",\n        "DISABLE"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the signal. Auto-named from target Mechanism/Port names if omitted.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nModulatorySignal is abstract and must NEVER be instantiated directly — doing so will cause an error. Always use a concrete subclass: ControlSignal (for ControlMechanism), GatingSignal (for GatingMechanism), or LearningSignal (for LearningMechanism). The `modulation` parameter defaults to MULTIPLICATIVE but inherits from the owner Mechanism if not specified. The `modulates` argument is an alias for `projections` in the underlying OutputPort constructor. Auto-naming uses projection targets: single target → "MechName[PortName] ClassName"; same-mechanism targets → "MechName[Port1, Port2] ClassName"; cross-mechanism targets → "OwnerName divergent ClassName".'
TOOL_PARAMETERS = { 'properties': { 'default_allocation': { 'description': 'Default template and initial '
                                                         "value for the signal's "
                                                         'variable (i.e., its '
                                                         'allocation). Scalar numeric.',
                                          'type': 'number'},
                  'function': { 'description': 'TransferFunction used to convert '
                                               "allocation into the signal's output "
                                               'value. Defaults to Identity (value == '
                                               'allocation).',
                                'type': 'string'},
                  'modulates': { 'description': 'List of Port or Mechanism '
                                                'specifications that this signal '
                                                'projects to and modulates. Each entry '
                                                'can be a Port name or Mechanism name.',
                                 'items': {'type': 'string'},
                                 'type': 'array'},
                  'modulation': { 'description': "How the signal's value is applied to "
                                                 'the modulated Port. MULTIPLICATIVE '
                                                 '(default) scales the parameter; '
                                                 'ADDITIVE offsets it; OVERRIDE '
                                                 'replaces it; DISABLE removes '
                                                 'modulation.',
                                  'enum': [ 'MULTIPLICATIVE',
                                            'ADDITIVE',
                                            'OVERRIDE',
                                            'DISABLE'],
                                  'type': 'string'},
                  'name': { 'description': 'Optional name for the signal. Auto-named '
                                           'from target Mechanism/Port names if '
                                           'omitted.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'ModulatorySignal is abstract and must NEVER be instantiated directly — doing so will cause an error. Always use a concrete subclass: ControlSignal (for ControlMechanism), GatingSignal (for GatingMechanism), or LearningSignal (for LearningMechanism). The `modulation` parameter defaults to MULTIPLICATIVE but inherits from the owner Mechanism if not specified. The `modulates` argument is an alias for `projections` in the underlying OutputPort constructor. Auto-naming uses projection targets: single target → "MechName[PortName] ClassName"; same-mechanism targets → "MechName[Port1, Port2] ClassName"; cross-mechanism targets → "OwnerName divergent ClassName".'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ModulatorySignal
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
    def create_modulatory_signal(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — ModulatorySignal is an abstract base class and will raise an error if instantiated.'
        return _impl(args or {})
