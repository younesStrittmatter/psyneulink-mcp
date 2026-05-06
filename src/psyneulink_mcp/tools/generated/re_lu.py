"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ef2513c6356f5fd7c5683a8c7f0b8d8da77dce5ca646e0792fda3657c48834bb'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.transferfunctions.ReLU'
__pnl_kind__ = 'class'
__pnl_parents__ = ['DeterministicTransferFunction',
 'TransferFunction',
 'Function_Base',
 'Function',
 'ShellClass',
 'Component',
 'MDFSerializable']
__pnl_parent_sha256s__ = {'Component': 'b878afca9fca90ac1a952605ca8d39a37f25ebebf1411a7f545b9c48a3eaeec3',
 'DeterministicTransferFunction': '1daf99136f1f0514df0e5a49c0ff7df2543035627b4c8652b2972001c6b3dc2d',
 'Function': '49ff0535055d97328c0f76806a53021714e2f8577d138152b75b7e15fcaab2e3',
 'Function_Base': '9b4c0d2feb23147f7d25af3ae03decf546fdb1f2e8be53abb8d8168801d60afa',
 'MDFSerializable': 'caad6059e8ef158be1269a23127f13da3733824c3585f9b4d6e3a63de82f65da',
 'ShellClass': 'adc23754ebeb0c55bdde1324622b33a509116703503508ee7e7de181a8afeee6',
 'TransferFunction': '0e6ecff88f6b55381f0295545a1697d4de9cc3cec153447b558945804ad26812'}
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_re_lu'
TOOL_DESCRIPTION = 'Construct a PsyNeuLink ReLU transfer function — a rectified linear (optionally leaky) activation that maps `x = gain * (variable - bias)` to `scale * max(x, leak * x) + offset`. Call this when you need a ReLU/Leaky-ReLU activation to attach to a TransferMechanism (or any component that accepts a TransferFunction); returns a Function handle, not a numeric value. Adds `gain`, `bias`, `leak`, `scale`, `offset` on top of the generic TransferFunction / DeterministicTransferFunction / Function_Base contract — see those parents for shape/owner/prefs semantics.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "default": 0,\n      "description": "Threshold subtracted from each element of variable before gain. Default 0.0.",\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template value/array shape to be transformed; defaults to the class default scalar.",\n      "items": {\n        "type": "number"\n      },\n      "type": [\n        "number",\n        "array"\n      ]\n    },\n    "gain": {\n      "default": 1,\n      "description": "Multiplier applied to (variable - bias). Default 1.0.",\n      "type": "number"\n    },\n    "leak": {\n      "default": 0,\n      "description": "Slope for the negative side (Leaky ReLU); 0.0 gives standard ReLU. Should be in [0, 1].",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the Function; auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Constant added to the final result after scale. Default 0.0.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplier applied to the rectified result before offset is added. Default 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nPass each parameter as a flat top-level keyword (e.g. `{"gain": 2.0, "bias": 0.1}`). Do NOT wrap them in an `args` / `kwargs` envelope — ReLU\'s constructor rejects an `args` keyword with `ComponentError: Illegal argument in constructor (type: ReLU): \'args\'` (see feedback issue #27). `params`, `owner`, and `prefs` are intentionally omitted; supply parameter overrides directly via the named arguments above. `leak` outside [0, 1] is not enforced by PNL but is mathematically nonstandard. The returned object is a Function instance; to actually compute values, hand it to a Mechanism or call it inside a Composition rather than expecting a numeric output here.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'default': 0,
                            'description': 'Threshold subtracted from each element of '
                                           'variable before gain. Default 0.0.',
                            'type': 'number'},
                  'default_variable': { 'description': 'Template value/array shape to '
                                                       'be transformed; defaults to '
                                                       'the class default scalar.',
                                        'items': {'type': 'number'},
                                        'type': ['number', 'array']},
                  'gain': { 'default': 1,
                            'description': 'Multiplier applied to (variable - bias). '
                                           'Default 1.0.',
                            'type': 'number'},
                  'leak': { 'default': 0,
                            'description': 'Slope for the negative side (Leaky ReLU); '
                                           '0.0 gives standard ReLU. Should be in [0, '
                                           '1].',
                            'maximum': 1,
                            'minimum': 0,
                            'type': 'number'},
                  'name': { 'description': 'Optional name for the Function; '
                                           'auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Constant added to the final result after '
                                             'scale. Default 0.0.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplier applied to the rectified '
                                            'result before offset is added. Default '
                                            '1.0.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Pass each parameter as a flat top-level keyword (e.g. `{"gain": 2.0, "bias": 0.1}`). Do NOT wrap them in an `args` / `kwargs` envelope — ReLU\'s constructor rejects an `args` keyword with `ComponentError: Illegal argument in constructor (type: ReLU): \'args\'` (see feedback issue #27). `params`, `owner`, and `prefs` are intentionally omitted; supply parameter overrides directly via the named arguments above. `leak` outside [0, 1] is not enforced by PNL but is mathematically nonstandard. The returned object is a Function instance; to actually compute values, hand it to a Mechanism or call it inside a Composition rather than expecting a numeric output here.'


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
        'Construct a PsyNeuLink ReLU transfer function — a rectified linear (optionally leaky) activation that maps `x = gain * (variable - bias)` to `scale * max(x, leak * x) + offset`.'
        return _impl(args or {})
