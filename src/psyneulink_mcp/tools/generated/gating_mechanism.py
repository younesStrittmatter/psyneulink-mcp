"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6e48010b08a4d945840b21abb577fdcf7ee5c325b0ac7f181a393e17ea8ed27e'
__pnl_qualname__ = 'psyneulink.GatingMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gating_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a GatingMechanism that multiplicatively (or additively) modulates the value of one or more InputPorts or OutputPorts of other mechanisms in a Composition. Use it when you need dynamic gain control — e.g., gating sensory inputs on/off, scaling activity of specific ports based on context, or implementing attention-like modulation. Returns a GatingMechanism object whose `gating_allocation` (array of scalars) is broadcast to all connected GatingSignals.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_allocation": {\n      "description": "Default allocation value(s) for GatingSignals that don\'t specify their own; one scalar per gating signal. Defaults to [0.5] for each signal if omitted.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "function": {\n      "description": "PsyNeuLink TransferFunction that maps variable \\u2192 gating_allocation. Defaults to Linear(slope=1, intercept=0), i.e., identity pass-through.",\n      "type": "object"\n    },\n    "gate": {\n      "description": "List of ports/mechanisms to gate. Each item can be an InputPort, OutputPort, Mechanism (primary InputPort used), a (port_name, Mechanism) tuple, or a GatingSignal spec dict. Length must match default_allocation if that is specified.",\n      "items": {},\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Shape of the default_allocation as int or list of ints (e.g., 2 \\u2192 [0, 0]). Ignored if default_allocation is also provided.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "modulation": {\n      "default": "MULTIPLICATIVE",\n      "description": "Default modulation type applied by all GatingSignals unless individually overridden. \'MULTIPLICATIVE\' (default) scales port value; \'ADDITIVE\' shifts it.",\n      "enum": [\n        "MULTIPLICATIVE",\n        "ADDITIVE",\n        "OVERRIDE",\n        "DISABLE"\n      ],\n      "type": "string"\n    },\n    "monitor_for_gating": {\n      "description": "OutputPorts or Mechanisms whose activity the GatingMechanism monitors to compute its gating_allocation (used with an ObjectiveMechanism or directly). Pass Mechanism to use its primary OutputPort.",\n      "items": {},\n      "type": "array"\n    },\n    "name": {\n      "description": "Name for the GatingMechanism; auto-assigned from registry if omitted.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Optional parameter dictionary to override constructor arguments or set function parameters.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `default_allocation` appears twice in the docstring signature — this is a PNL docstring bug; there is only one `default_allocation` parameter and it maps to `default_variable` internally.\n- The length of `gate` and `default_allocation` must match; mismatches raise a runtime error.\n- If neither `gate` nor `default_allocation` is specified, the mechanism is created with a single GatingSignal with allocation 0.5 — gates must be added later via `add_ports` or as part of a Composition.\n- `gating_signals` is an alias for `gate` (backward compat); use `gate` in new code.\n- `default_gating_allocation` kwarg is deprecated and raises GatingMechanismError — always use `default_allocation`.\n- Passing a bare Mechanism to `gate` uses its primary InputPort, not its OutputPort; this differs from `monitor_for_gating` where a bare Mechanism uses its primary OutputPort.\n- The `function` parameter accepts a PsyNeuLink function object, not a plain Python callable.'
TOOL_PARAMETERS = { 'properties': { 'default_allocation': { 'description': 'Default allocation value(s) '
                                                         "for GatingSignals that don't "
                                                         'specify their own; one '
                                                         'scalar per gating signal. '
                                                         'Defaults to [0.5] for each '
                                                         'signal if omitted.',
                                          'items': {'type': 'number'},
                                          'type': 'array'},
                  'function': { 'description': 'PsyNeuLink TransferFunction that maps '
                                               'variable → gating_allocation. Defaults '
                                               'to Linear(slope=1, intercept=0), i.e., '
                                               'identity pass-through.',
                                'type': 'object'},
                  'gate': { 'description': 'List of ports/mechanisms to gate. Each '
                                           'item can be an InputPort, OutputPort, '
                                           'Mechanism (primary InputPort used), a '
                                           '(port_name, Mechanism) tuple, or a '
                                           'GatingSignal spec dict. Length must match '
                                           'default_allocation if that is specified.',
                            'items': {},
                            'type': 'array'},
                  'input_shapes': { 'description': 'Shape of the default_allocation as '
                                                   'int or list of ints (e.g., 2 → [0, '
                                                   '0]). Ignored if default_allocation '
                                                   'is also provided.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'}]},
                  'modulation': { 'default': 'MULTIPLICATIVE',
                                  'description': 'Default modulation type applied by '
                                                 'all GatingSignals unless '
                                                 'individually overridden. '
                                                 "'MULTIPLICATIVE' (default) scales "
                                                 "port value; 'ADDITIVE' shifts it.",
                                  'enum': [ 'MULTIPLICATIVE',
                                            'ADDITIVE',
                                            'OVERRIDE',
                                            'DISABLE'],
                                  'type': 'string'},
                  'monitor_for_gating': { 'description': 'OutputPorts or Mechanisms '
                                                         'whose activity the '
                                                         'GatingMechanism monitors to '
                                                         'compute its '
                                                         'gating_allocation (used with '
                                                         'an ObjectiveMechanism or '
                                                         'directly). Pass Mechanism to '
                                                         'use its primary OutputPort.',
                                          'items': {},
                                          'type': 'array'},
                  'name': { 'description': 'Name for the GatingMechanism; '
                                           'auto-assigned from registry if omitted.',
                            'type': 'string'},
                  'params': { 'description': 'Optional parameter dictionary to '
                                             'override constructor arguments or set '
                                             'function parameters.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `default_allocation` appears twice in the docstring signature — this is a PNL docstring bug; there is only one `default_allocation` parameter and it maps to `default_variable` internally.\n- The length of `gate` and `default_allocation` must match; mismatches raise a runtime error.\n- If neither `gate` nor `default_allocation` is specified, the mechanism is created with a single GatingSignal with allocation 0.5 — gates must be added later via `add_ports` or as part of a Composition.\n- `gating_signals` is an alias for `gate` (backward compat); use `gate` in new code.\n- `default_gating_allocation` kwarg is deprecated and raises GatingMechanismError — always use `default_allocation`.\n- Passing a bare Mechanism to `gate` uses its primary InputPort, not its OutputPort; this differs from `monitor_for_gating` where a bare Mechanism uses its primary OutputPort.\n- The `function` parameter accepts a PsyNeuLink function object, not a plain Python callable.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.GatingMechanism
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
    def create_gating_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a GatingMechanism that multiplicatively (or additively) modulates the value of one or more InputPorts or OutputPorts of other mechanisms in a Composition.'
        return _impl(args or {})
