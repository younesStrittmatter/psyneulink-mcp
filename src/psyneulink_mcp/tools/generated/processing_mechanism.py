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
TOOL_DESCRIPTION = 'Create a generic ProcessingMechanism — the default-purpose Mechanism for transforming inputs into outputs inside a Composition. Reach for this when no specialized subclass (TransferMechanism, IntegratorMechanism, etc.) applies and you just need a node that runs a function on its input. Returns an opaque handle to register with `add_node` / pathway helpers; the handle\'s value after execution is the function\'s output. Beyond the generic Mechanism contract (see INHERITS FROM), this class adds a richer `standard_output_ports` set (MEAN, MEDIAN, STANDARD_DEVIATION, VARIANCE, MAX_VAL, MAX_ABS_VAL, MAX_ONE_HOT, MAX_ABS_ONE_HOT, MAX_INDICATOR, MAX_ABS_INDICATOR, PROB) computed over the first item of the mechanism\'s value, selectable by name in `output_ports`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template/initial input. Use a 2D list (list of input-port arrays) for multi-port mechanisms or a 1D list for a single port. Determines the shape the function must accept. Mutually informative with input_shapes \\u2014 supply one or the other, not both.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "type": "number"\n        }\n      ]\n    },\n    "function": {\n      "description": "Function applied to the mechanism\'s variable each timestep. Accepts a function-handle string returned by another tool (e.g. a Linear, Logistic, DriftOnASphereIntegrator handle). If omitted, PNL uses the class default (Linear). The function\'s expected input shape must match default_variable / input_shapes \\u2014 see notes."\n    },\n    "input_ports": {\n      "description": "Optional list of InputPort specifications. Each entry can be a string name, an int (size), a dict spec (e.g. {NAME, INPUT_SHAPES, PROJECTIONS}), or a handle to another Mechanism/OutputPort to project from. Length must match the outer dimension of default_variable / input_shapes.",\n      "items": {},\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Shorthand for the size of each InputPort. An int creates one InputPort of that length; a list of ints creates one InputPort per entry with the given length. Use this instead of default_variable when you don\'t need specific initial values.",\n      "oneOf": [\n        {\n          "minimum": 1,\n          "type": "integer"\n        },\n        {\n          "items": {\n            "minimum": 1,\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Human-readable name for the mechanism; used in logs, in Composition graph displays, and as the key when other components reference this one.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Optional list of OutputPort specifications. Strings may name standard output ports \\u2014 for ProcessingMechanism these include MEAN, MEDIAN, STANDARD_DEVIATION, VARIANCE, MAX_VAL, MAX_ABS_VAL, MAX_ONE_HOT, MAX_ABS_ONE_HOT, MAX_INDICATOR, MAX_ABS_INDICATOR, PROB \\u2014 in addition to those inherited from Mechanism. Dict specs allow custom names/variables. If function is a TransferFunction and there are multiple input ports, ports are auto-mirrored 1:1 unless overridden.",\n      "items": {},\n      "type": "array"\n    },\n    "params": {\n      "description": "Optional dict of parameter overrides applied at construction. Prefer top-level kwargs when they exist.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- Function/input shape must agree. The recent feedback case passed a DriftOnASphereIntegrator handle with `default_variable=[[0]*24]`, which crashed in `matmul` because that integrator interprets its `dimension` parameter as N+1 of the input vector — so a 24-d input requires `dimension=25` on the integrator, not `dimension=24`. When wiring stateful integrator functions (DriftOnASphereIntegrator, OrnsteinUhlenbeck, etc.) through this mechanism, make sure the function was built for the exact input shape you give the mechanism here; if you change `default_variable`/`input_shapes`, rebuild the function handle with matching dimensions.\\n- Pass either `default_variable` or `input_shapes`, not both — they specify the same thing in different ways and PNL will warn or error on conflict.\\n- `default_variable` is 2D in the general case (one row per InputPort). A bare 1D list is auto-promoted to a single InputPort.\\n- `output_ports` strings are matched case-sensitively against PNL\'s standard names. Unknown strings are treated as new OutputPort names with default behavior, not an error — typos won\'t surface until execution.\\n- When `function` is a TransferFunction and there are multiple InputPorts, the mechanism auto-creates one OutputPort per InputPort (named to match) unless you supply `output_ports` explicitly. Supplying fewer `output_ports` than InputPorts triggers a partial-fill behavior in `_instantiate_output_ports` that may surprise you — supply one per InputPort if you care about the mapping.\\n- Returns a handle, not a numeric result. To execute, add the handle to a Composition and run that.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template/initial input. Use a '
                                                       '2D list (list of input-port '
                                                       'arrays) for multi-port '
                                                       'mechanisms or a 1D list for a '
                                                       'single port. Determines the '
                                                       'shape the function must '
                                                       'accept. Mutually informative '
                                                       'with input_shapes — supply one '
                                                       'or the other, not both.',
                                        'oneOf': [ { 'items': {'type': 'number'},
                                                     'type': 'array'},
                                                   { 'items': { 'items': { 'type': 'number'},
                                                                'type': 'array'},
                                                     'type': 'array'},
                                                   {'type': 'number'}]},
                  'function': { 'description': "Function applied to the mechanism's "
                                               'variable each timestep. Accepts a '
                                               'function-handle string returned by '
                                               'another tool (e.g. a Linear, Logistic, '
                                               'DriftOnASphereIntegrator handle). If '
                                               'omitted, PNL uses the class default '
                                               "(Linear). The function's expected "
                                               'input shape must match '
                                               'default_variable / input_shapes — see '
                                               'notes.'},
                  'input_ports': { 'description': 'Optional list of InputPort '
                                                  'specifications. Each entry can be a '
                                                  'string name, an int (size), a dict '
                                                  'spec (e.g. {NAME, INPUT_SHAPES, '
                                                  'PROJECTIONS}), or a handle to '
                                                  'another Mechanism/OutputPort to '
                                                  'project from. Length must match the '
                                                  'outer dimension of default_variable '
                                                  '/ input_shapes.',
                                   'items': {},
                                   'type': 'array'},
                  'input_shapes': { 'description': 'Shorthand for the size of each '
                                                   'InputPort. An int creates one '
                                                   'InputPort of that length; a list '
                                                   'of ints creates one InputPort per '
                                                   'entry with the given length. Use '
                                                   'this instead of default_variable '
                                                   "when you don't need specific "
                                                   'initial values.',
                                    'oneOf': [ {'minimum': 1, 'type': 'integer'},
                                               { 'items': { 'minimum': 1,
                                                            'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Human-readable name for the mechanism; '
                                           'used in logs, in Composition graph '
                                           'displays, and as the key when other '
                                           'components reference this one.',
                            'type': 'string'},
                  'output_ports': { 'description': 'Optional list of OutputPort '
                                                   'specifications. Strings may name '
                                                   'standard output ports — for '
                                                   'ProcessingMechanism these include '
                                                   'MEAN, MEDIAN, STANDARD_DEVIATION, '
                                                   'VARIANCE, MAX_VAL, MAX_ABS_VAL, '
                                                   'MAX_ONE_HOT, MAX_ABS_ONE_HOT, '
                                                   'MAX_INDICATOR, MAX_ABS_INDICATOR, '
                                                   'PROB — in addition to those '
                                                   'inherited from Mechanism. Dict '
                                                   'specs allow custom '
                                                   'names/variables. If function is a '
                                                   'TransferFunction and there are '
                                                   'multiple input ports, ports are '
                                                   'auto-mirrored 1:1 unless '
                                                   'overridden.',
                                    'items': {},
                                    'type': 'array'},
                  'params': { 'description': 'Optional dict of parameter overrides '
                                             'applied at construction. Prefer '
                                             'top-level kwargs when they exist.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- Function/input shape must agree. The recent feedback case passed a DriftOnASphereIntegrator handle with `default_variable=[[0]*24]`, which crashed in `matmul` because that integrator interprets its `dimension` parameter as N+1 of the input vector — so a 24-d input requires `dimension=25` on the integrator, not `dimension=24`. When wiring stateful integrator functions (DriftOnASphereIntegrator, OrnsteinUhlenbeck, etc.) through this mechanism, make sure the function was built for the exact input shape you give the mechanism here; if you change `default_variable`/`input_shapes`, rebuild the function handle with matching dimensions.\\n- Pass either `default_variable` or `input_shapes`, not both — they specify the same thing in different ways and PNL will warn or error on conflict.\\n- `default_variable` is 2D in the general case (one row per InputPort). A bare 1D list is auto-promoted to a single InputPort.\\n- `output_ports` strings are matched case-sensitively against PNL's standard names. Unknown strings are treated as new OutputPort names with default behavior, not an error — typos won't surface until execution.\\n- When `function` is a TransferFunction and there are multiple InputPorts, the mechanism auto-creates one OutputPort per InputPort (named to match) unless you supply `output_ports` explicitly. Supplying fewer `output_ports` than InputPorts triggers a partial-fill behavior in `_instantiate_output_ports` that may surprise you — supply one per InputPort if you care about the mapping.\\n- Returns a handle, not a numeric result. To execute, add the handle to a Composition and run that."


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
        'Create a generic ProcessingMechanism — the default-purpose Mechanism for transforming inputs into outputs inside a Composition.'
        return _impl(args or {})
