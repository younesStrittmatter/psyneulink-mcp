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
TOOL_DESCRIPTION = 'Construct a PsyNeuLink ReLU transfer function — a rectified-linear (optionally leaky) DeterministicTransferFunction. Call this when you need the function object itself to assign as the `function=` of a TransferMechanism (or any compatible component), not when you want to evaluate a numeric ReLU on data. Beyond what TransferFunction/DeterministicTransferFunction provide, this class adds three signature parameters specific to ReLU: `gain` (multiplier on `variable - bias`), `bias` (threshold subtracted from variable), and `leak` (slope for the negative side; `0.0` = standard ReLU, values in (0,1] = Leaky ReLU). The post-transform `scale` and `offset` are inherited from DeterministicTransferFunction. Returns a ReLU Function instance (formula: `scale * max(gain*(variable-bias), leak*gain*(variable-bias)) + offset`).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "description": "Threshold subtracted from each element of variable; the rectifier hinge sits at variable == bias. Default 0.0.",\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template for the value to be transformed; a scalar or array shape that fixes the function\'s input shape. Optional.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "gain": {\n      "description": "Multiplier applied to (variable - bias) before the max/leak step. Default 1.0.",\n      "type": "number"\n    },\n    "leak": {\n      "description": "Slope on the negative side of the hinge. 0.0 gives a standard ReLU; values in (0, 1] give a Leaky ReLU. Default 0.0.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the Function instance; FunctionRegistry assigns a default if omitted.",\n      "type": "string"\n    },\n    "offset": {\n      "description": "Constant added after scale is applied. Default 0.0.",\n      "type": "number"\n    },\n    "scale": {\n      "description": "Multiplier applied to the rectified value before offset is added. Default 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nPass parameters as flat top-level keyword arguments (e.g. {"gain": 2.0, "leak": 0.1}). Do NOT wrap them under an "args" or "kwargs" key — ReLU\'s constructor rejects an unknown `args` argument with `ComponentError: Illegal argument in constructor (type: ReLU): \'args\'` (this exact error has been observed in feedback). The tool returns a ReLU Function object, not a numeric output; to evaluate it, attach it to a Mechanism or call it as a callable. `leak` is conventionally between 0 and 1 — values outside that range are accepted by the constructor but are not standard Leaky ReLU. `gain` and `bias` are also exposed as the MULTIPLICATIVE_PARAM and ADDITIVE_PARAM aliases respectively, which matters if the function is being modulated by a ControlSignal.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'description': 'Threshold subtracted from each element of '
                                           'variable; the rectifier hinge sits at '
                                           'variable == bias. Default 0.0.',
                            'type': 'number'},
                  'default_variable': { 'description': 'Template for the value to be '
                                                       'transformed; a scalar or array '
                                                       'shape that fixes the '
                                                       "function's input shape. "
                                                       'Optional.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'},
                                                   { 'items': { 'items': { 'type': 'number'},
                                                                'type': 'array'},
                                                     'type': 'array'}]},
                  'gain': { 'description': 'Multiplier applied to (variable - bias) '
                                           'before the max/leak step. Default 1.0.',
                            'type': 'number'},
                  'leak': { 'description': 'Slope on the negative side of the hinge. '
                                           '0.0 gives a standard ReLU; values in (0, '
                                           '1] give a Leaky ReLU. Default 0.0.',
                            'type': 'number'},
                  'name': { 'description': 'Optional name for the Function instance; '
                                           'FunctionRegistry assigns a default if '
                                           'omitted.',
                            'type': 'string'},
                  'offset': { 'description': 'Constant added after scale is applied. '
                                             'Default 0.0.',
                              'type': 'number'},
                  'scale': { 'description': 'Multiplier applied to the rectified value '
                                            'before offset is added. Default 1.0.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Pass parameters as flat top-level keyword arguments (e.g. {"gain": 2.0, "leak": 0.1}). Do NOT wrap them under an "args" or "kwargs" key — ReLU\'s constructor rejects an unknown `args` argument with `ComponentError: Illegal argument in constructor (type: ReLU): \'args\'` (this exact error has been observed in feedback). The tool returns a ReLU Function object, not a numeric output; to evaluate it, attach it to a Mechanism or call it as a callable. `leak` is conventionally between 0 and 1 — values outside that range are accepted by the constructor but are not standard Leaky ReLU. `gain` and `bias` are also exposed as the MULTIPLICATIVE_PARAM and ADDITIVE_PARAM aliases respectively, which matters if the function is being modulated by a ControlSignal.'


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
        'Construct a PsyNeuLink ReLU transfer function — a rectified-linear (optionally leaky) DeterministicTransferFunction.'
        return _impl(args or {})
