"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'dfe35aa28c6336d5e8f33aa743164f840aca153be35e4f5a8089509929428014'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.processing.processingmechanism.ProcessingMechanism'
__pnl_kind__ = 'class'
__pnl_parents__ = ['ProcessingMechanism_Base',
 'Mechanism_Base',
 'Mechanism',
 'ShellClass',
 'Component',
 'MDFSerializable']
__pnl_parent_sha256s__ = {'Component': 'b878afca9fca90ac1a952605ca8d39a37f25ebebf1411a7f545b9c48a3eaeec3',
 'MDFSerializable': 'caad6059e8ef158be1269a23127f13da3733824c3585f9b4d6e3a63de82f65da',
 'Mechanism': 'ed9f10960d87126524669ea7084cb8128621de90ddb7306c8c9bde15f524d28d',
 'Mechanism_Base': '91d72ef88b0cb638b5895df2f04ed7f449ce951198c10e44c22558b699e8bf21',
 'ProcessingMechanism_Base': '471c65452d591ff8e0270afdeb8e535a0f97b3b23673c7bc21e9c32a6524cf80',
 'ShellClass': 'adc23754ebeb0c55bdde1324622b33a509116703503508ee7e7de181a8afeee6'}
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_processing_mechanism'
TOOL_DESCRIPTION = 'Use this when you need a generic single-step processor that applies a `function` to its input and emits the result — the simplest concrete `Mechanism`. Beyond what `Mechanism_Base` provides, it adds stat-based standard OutputPorts (MEAN, MEDIAN, STANDARD_DEVIATION, VARIANCE, MAX_VAL, MAX_ABS_VAL, MAX_ONE_HOT, MAX_ABS_ONE_HOT, MAX_INDICATOR, MAX_ABS_INDICATOR, PROB) selectable via `output_ports`, and — when given multiple InputPorts together with a `TransferFunction` — auto-creates one OutputPort per InputPort named after it. Returns a node handle suitable for `add_node` / pathway wiring in a `Composition`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input. Scalar, 1D list (single InputPort), or 2D list (one row per InputPort). Sets the mechanism\'s variable shape and \\u2014 implicitly \\u2014 the shape its `function` must accept. Mutually constrains `input_shapes`; provide one or the other, not both contradictorily.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "function": {\n      "description": "Function applied to the input. A handle from a `create_*_function` tool, a function class name string, or omitted to default to Linear (identity). For stateful functions (e.g. DriftOnASphere, Integrator variants), the function\'s internal dimensionality is fixed at function-creation time and MUST match this mechanism\'s variable shape.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    },\n    "input_ports": {\n      "description": "InputPort specs. Strings (port names), ints (sizes), dicts (full specs with NAME/INPUT_SHAPES/PROJECTIONS/etc.), or references to other Mechanisms/OutputPorts that will project in. Length determines the number of InputPorts.",\n      "items": {\n        "oneOf": [\n          {\n            "type": "string"\n          },\n          {\n            "type": "integer"\n          },\n          {\n            "type": "object"\n          }\n        ]\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Shorthand for `default_variable` shape when initial values don\'t matter: int (single InputPort of that length) or list of ints (one InputPort per entry).",\n      "oneOf": [\n        {\n          "minimum": 1,\n          "type": "integer"\n        },\n        {\n          "items": {\n            "minimum": 1,\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Identifier for the mechanism; used in logs, Composition graph, and as the prefix for auto-named OutputPorts.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "OutputPort specs. Use the standard names listed in the description (e.g. \\"MEAN\\", \\"MAX_INDICATOR\\") to expose computed summaries, or dicts/strings to define custom ones. If omitted with multiple InputPorts + a TransferFunction, one OutputPort is auto-created per InputPort.",\n      "items": {\n        "oneOf": [\n          {\n            "type": "string"\n          },\n          {\n            "type": "object"\n          }\n        ]\n      },\n      "type": "array"\n    },\n    "params": {\n      "description": "Dict of parameter overrides applied at construction. Rarely needed \\u2014 prefer passing the parameter as a top-level kwarg.",\n      "type": "object"\n    },\n    "prefs": {\n      "description": "PreferenceSet overrides (logging, reporting). Usually omitted.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nFunction/variable shape coupling is the #1 source of runtime errors here (recent feedback: a `DriftOnASphere` function configured for dimension 1 was attached to a mechanism with `default_variable` of length 24, producing a `matmul: size 1 is different from 24` ValueError deep inside the function). A pre-built function carries its own shape (set when you created it via its `create_*` tool — e.g. its `initializer`/`dimension`/`default_variable`), and that shape must match this mechanism\'s `default_variable` / `input_shapes`. If you\'re choosing the dimensionality here, either (a) build the function with matching shape first, or (b) leave `function` unset and let it default to Linear, which adapts.\n\nOther gotchas:\n- If both `default_variable` and `input_shapes` are given they must agree.\n- With multiple InputPorts AND a `TransferFunction`, OutputPorts are auto-instantiated one-per-InputPort and named after the corresponding InputPort — passing fewer `output_ports` than InputPorts triggers per-port name/variable filling, not truncation.\n- Standard OutputPort statistics (MEAN, VARIANCE, MAX_*, PROB, etc.) are computed over the elements of axis-0 of the mechanism\'s `value` — i.e. the first InputPort\'s output, not all of them.\n- `PROB` samples stochastically (softmax) — not deterministic across runs unless you seed.\n- The error from a shape mismatch surfaces from the function\'s `_function`, not from this constructor — read the traceback\'s bottom frame to identify which function and which dimension is wrong.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input. '
                                                       'Scalar, 1D list (single '
                                                       'InputPort), or 2D list (one '
                                                       'row per InputPort). Sets the '
                                                       "mechanism's variable shape and "
                                                       '— implicitly — the shape its '
                                                       '`function` must accept. '
                                                       'Mutually constrains '
                                                       '`input_shapes`; provide one or '
                                                       'the other, not both '
                                                       'contradictorily.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'},
                                                   { 'items': { 'items': { 'type': 'number'},
                                                                'type': 'array'},
                                                     'type': 'array'}]},
                  'function': { 'description': 'Function applied to the input. A '
                                               'handle from a `create_*_function` '
                                               'tool, a function class name string, or '
                                               'omitted to default to Linear '
                                               '(identity). For stateful functions '
                                               '(e.g. DriftOnASphere, Integrator '
                                               "variants), the function's internal "
                                               'dimensionality is fixed at '
                                               'function-creation time and MUST match '
                                               "this mechanism's variable shape.",
                                'oneOf': [{'type': 'string'}, {'type': 'object'}]},
                  'input_ports': { 'description': 'InputPort specs. Strings (port '
                                                  'names), ints (sizes), dicts (full '
                                                  'specs with '
                                                  'NAME/INPUT_SHAPES/PROJECTIONS/etc.), '
                                                  'or references to other '
                                                  'Mechanisms/OutputPorts that will '
                                                  'project in. Length determines the '
                                                  'number of InputPorts.',
                                   'items': { 'oneOf': [ {'type': 'string'},
                                                         {'type': 'integer'},
                                                         {'type': 'object'}]},
                                   'type': 'array'},
                  'input_shapes': { 'description': 'Shorthand for `default_variable` '
                                                   "shape when initial values don't "
                                                   'matter: int (single InputPort of '
                                                   'that length) or list of ints (one '
                                                   'InputPort per entry).',
                                    'oneOf': [ {'minimum': 1, 'type': 'integer'},
                                               { 'items': { 'minimum': 1,
                                                            'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Identifier for the mechanism; used in '
                                           'logs, Composition graph, and as the prefix '
                                           'for auto-named OutputPorts.',
                            'type': 'string'},
                  'output_ports': { 'description': 'OutputPort specs. Use the standard '
                                                   'names listed in the description '
                                                   '(e.g. "MEAN", "MAX_INDICATOR") to '
                                                   'expose computed summaries, or '
                                                   'dicts/strings to define custom '
                                                   'ones. If omitted with multiple '
                                                   'InputPorts + a TransferFunction, '
                                                   'one OutputPort is auto-created per '
                                                   'InputPort.',
                                    'items': { 'oneOf': [ {'type': 'string'},
                                                          {'type': 'object'}]},
                                    'type': 'array'},
                  'params': { 'description': 'Dict of parameter overrides applied at '
                                             'construction. Rarely needed — prefer '
                                             'passing the parameter as a top-level '
                                             'kwarg.',
                              'type': 'object'},
                  'prefs': { 'description': 'PreferenceSet overrides (logging, '
                                            'reporting). Usually omitted.',
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Function/variable shape coupling is the #1 source of runtime errors here (recent feedback: a `DriftOnASphere` function configured for dimension 1 was attached to a mechanism with `default_variable` of length 24, producing a `matmul: size 1 is different from 24` ValueError deep inside the function). A pre-built function carries its own shape (set when you created it via its `create_*` tool — e.g. its `initializer`/`dimension`/`default_variable`), and that shape must match this mechanism's `default_variable` / `input_shapes`. If you're choosing the dimensionality here, either (a) build the function with matching shape first, or (b) leave `function` unset and let it default to Linear, which adapts.\n\nOther gotchas:\n- If both `default_variable` and `input_shapes` are given they must agree.\n- With multiple InputPorts AND a `TransferFunction`, OutputPorts are auto-instantiated one-per-InputPort and named after the corresponding InputPort — passing fewer `output_ports` than InputPorts triggers per-port name/variable filling, not truncation.\n- Standard OutputPort statistics (MEAN, VARIANCE, MAX_*, PROB, etc.) are computed over the elements of axis-0 of the mechanism's `value` — i.e. the first InputPort's output, not all of them.\n- `PROB` samples stochastically (softmax) — not deterministic across runs unless you seed.\n- The error from a shape mismatch surfaces from the function's `_function`, not from this constructor — read the traceback's bottom frame to identify which function and which dimension is wrong."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ProcessingMechanism
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
    def create_processing_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Use this when you need a generic single-step processor that applies a `function` to its input and emits the result — the simplest concrete `Mechanism`.'
        return _impl(args or {})
