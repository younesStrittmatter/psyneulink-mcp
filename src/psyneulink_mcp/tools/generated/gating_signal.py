"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f7557a2847ba427d4f8c7ac1ad17276c131cb62679bd73b310ea82ac2a3fdfea'
__pnl_qualname__ = 'psyneulink.GatingSignal'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gating_signal'
TOOL_DESCRIPTION = 'Call this tool when configuring a GatingMechanism to modulate the activity of InputPort(s) or OutputPort(s) in a composition. Use it to create a GatingSignal that defines what ports to gate and how (via function and modulation mode). Returns a GatingSignal instance that, once attached to a GatingMechanism, sends GatingProjections to scale or override the value of the specified ports.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_allocation": {\n      "default": 0.5,\n      "description": "Template and default value for the allocation parameter (the input to the gating function). Defaults to 0.5.",\n      "type": "number"\n    },\n    "function": {\n      "default": "Linear",\n      "description": "Name or specification of the TransferFunction used to convert the owner GatingMechanism\'s value into the GatingSignal\'s intensity. Defaults to Linear (identity pass-through).",\n      "type": "string"\n    },\n    "gate": {\n      "description": "List of Projection specifications identifying the InputPort(s) and/or OutputPort(s) this GatingSignal should modulate. Each element is a port name or projection spec string.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "modulation": {\n      "description": "How the GatingSignal\'s value modifies the target port\'s value. Common options: \'multiplicative\', \'additive\', \'override\'. If omitted, uses the GatingMechanism\'s default modulation.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the GatingSignal instance.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nGatingSignal is a specialized ControlSignal with no cost functions — do not pass cost-related arguments (intensity_cost_function, adjustment_cost_function, etc.) that ControlSignal accepts. The deprecated `modulates` keyword is silently remapped to `gate`; prefer `gate`. Cannot specify both `gate` and `projections` simultaneously. Default allocation is 0.5 (numpy array [0.5] internally). The `intensity` attribute is an alias for `value`, and `gating_signal` is also the same value. GatingSignal is normally created implicitly by specifying gating in a GatingMechanism rather than instantiated directly.'
TOOL_PARAMETERS = { 'properties': { 'default_allocation': { 'default': 0.5,
                                          'description': 'Template and default value '
                                                         'for the allocation parameter '
                                                         '(the input to the gating '
                                                         'function). Defaults to 0.5.',
                                          'type': 'number'},
                  'function': { 'default': 'Linear',
                                'description': 'Name or specification of the '
                                               'TransferFunction used to convert the '
                                               "owner GatingMechanism's value into the "
                                               "GatingSignal's intensity. Defaults to "
                                               'Linear (identity pass-through).',
                                'type': 'string'},
                  'gate': { 'description': 'List of Projection specifications '
                                           'identifying the InputPort(s) and/or '
                                           'OutputPort(s) this GatingSignal should '
                                           'modulate. Each element is a port name or '
                                           'projection spec string.',
                            'items': {'type': 'string'},
                            'type': 'array'},
                  'modulation': { 'description': "How the GatingSignal's value "
                                                 "modifies the target port's value. "
                                                 "Common options: 'multiplicative', "
                                                 "'additive', 'override'. If omitted, "
                                                 "uses the GatingMechanism's default "
                                                 'modulation.',
                                  'type': 'string'},
                  'name': { 'description': 'Optional name for the GatingSignal '
                                           'instance.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'GatingSignal is a specialized ControlSignal with no cost functions — do not pass cost-related arguments (intensity_cost_function, adjustment_cost_function, etc.) that ControlSignal accepts. The deprecated `modulates` keyword is silently remapped to `gate`; prefer `gate`. Cannot specify both `gate` and `projections` simultaneously. Default allocation is 0.5 (numpy array [0.5] internally). The `intensity` attribute is an alias for `value`, and `gating_signal` is also the same value. GatingSignal is normally created implicitly by specifying gating in a GatingMechanism rather than instantiated directly.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.GatingSignal
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
    def create_gating_signal(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when configuring a GatingMechanism to modulate the activity of InputPort(s) or OutputPort(s) in a composition.'
        return _impl(args or {})
