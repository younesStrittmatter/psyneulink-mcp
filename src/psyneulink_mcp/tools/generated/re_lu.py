"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ef2513c6356f5fd7c5683a8c7f0b8d8da77dce5ca646e0792fda3657c48834bb'
__pnl_qualname__ = 'psyneulink.ReLU'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_re_lu'
TOOL_DESCRIPTION = 'Call this tool to create a ReLU (Rectified Linear Unit) transfer function for use as the function parameter of a PsyNeuLink mechanism (e.g., TransferMechanism). Use it when you need a standard or leaky ReLU activation: output is scale * max(gain*(input-bias), leak*gain*(input-bias)) + offset. Returns a ReLU Function object, not a numeric result.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "default": 0,\n      "description": "Value subtracted from input before applying gain; acts as a threshold shift.",\n      "type": "number"\n    },\n    "gain": {\n      "default": 1,\n      "description": "Multiplier applied to (variable - bias). Acts as the slope for positive inputs.",\n      "type": "number"\n    },\n    "leak": {\n      "default": 0,\n      "description": "Scaling factor (0 to 1) applied when (variable - bias) <= 0. Set >0 for leaky ReLU; 0 gives standard ReLU.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the ReLU Function instance.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Constant added to the final result after scale is applied.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplier applied to the rectified result before adding offset.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nleak must be between 0 and 1; values outside this range are not automatically clamped but produce non-standard behavior. The computation is scale * max(gain*(var-bias), leak*gain*(var-bias)) + offset — note that offset is added after scale, so it is NOT scaled. default_variable is a template for input shape, not a runtime value; omit it unless you need to constrain input dimensionality. This tool returns a Function object to assign to a mechanism\'s function parameter, not a direct numeric output.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'default': 0,
                            'description': 'Value subtracted from input before '
                                           'applying gain; acts as a threshold shift.',
                            'type': 'number'},
                  'gain': { 'default': 1,
                            'description': 'Multiplier applied to (variable - bias). '
                                           'Acts as the slope for positive inputs.',
                            'type': 'number'},
                  'leak': { 'default': 0,
                            'description': 'Scaling factor (0 to 1) applied when '
                                           '(variable - bias) <= 0. Set >0 for leaky '
                                           'ReLU; 0 gives standard ReLU.',
                            'type': 'number'},
                  'name': { 'description': 'Optional name for the ReLU Function '
                                           'instance.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Constant added to the final result after '
                                             'scale is applied.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplier applied to the rectified '
                                            'result before adding offset.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "leak must be between 0 and 1; values outside this range are not automatically clamped but produce non-standard behavior. The computation is scale * max(gain*(var-bias), leak*gain*(var-bias)) + offset — note that offset is added after scale, so it is NOT scaled. default_variable is a template for input shape, not a runtime value; omit it unless you need to constrain input dimensionality. This tool returns a Function object to assign to a mechanism's function parameter, not a direct numeric output."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ReLU
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
    def create_re_lu(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a ReLU (Rectified Linear Unit) transfer function for use as the function parameter of a PsyNeuLink mechanism (e.g., TransferMechanism).'
        return _impl(args or {})
