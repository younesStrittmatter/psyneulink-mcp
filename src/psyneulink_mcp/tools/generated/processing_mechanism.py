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
TOOL_DESCRIPTION = 'Create a generic ProcessingMechanism — the default, function-agnostic Mechanism for feedforward processing nodes (input layers, transform stages, simple output layers) inside a Composition. Use this when you want a Mechanism whose only job is to apply a Function to its input and emit the result; pick a more specialized subclass (TransferMechanism, IntegratorMechanism, RecurrentTransferMechanism, etc.) only when you need their specific extras (integration mode, lateral connectivity, …). Beyond what `Mechanism_Base`/`Component` already document, ProcessingMechanism just adds an extended `standard_output_ports` set (MEAN, MEDIAN, STANDARD_DEVIATION, VARIANCE, MAX_VAL, MAX_ABS_VAL, MAX_ONE_HOT, MAX_ABS_ONE_HOT, MAX_INDICATOR, MAX_ABS_INDICATOR, PROB) that you can name in `output_ports`. Returns a Mechanism handle to use as a node when wiring a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input value, given as a 2D list-of-lists (one inner list per InputPort). Determines the number and length of input ports. Use either this OR input_shapes, not both. Example: [[0, 0, 0]] = one InputPort of length 3.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "function": {\n      "description": "Name of the PNL Function class to apply to the input, e.g. \'Linear\', \'Logistic\', \'SoftMax\', \'Exponential\', \'ReLU\'. Must be a real PNL Function class name \\u2014 opaque handles or made-up identifiers will fail or be silently misinterpreted. Function output shape must match default_variable / input_shapes. Defaults to Linear (identity) if omitted.",\n      "type": "string"\n    },\n    "function_params": {\n      "additionalProperties": true,\n      "description": "Keyword arguments forwarded to the Function constructor (e.g. {\'slope\': 2.0, \'intercept\': 1.0} for Linear, {\'gain\': 1.0, \'bias\': 0.0, \'x_0\': 0.0} for Logistic). Optional.",\n      "type": "object"\n    },\n    "input_ports": {\n      "description": "Explicit InputPort specifications. Each entry can be a string name, a dict spec, or a reference to another Port/Mechanism. Usually omitted \\u2014 default_variable / input_shapes is enough.",\n      "items": {},\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Shorthand for default_variable. An int gives one InputPort of that length; a list of ints gives multiple InputPorts of those lengths. Example: 3 = one InputPort of length 3; [3, 2] = two InputPorts of lengths 3 and 2.",\n      "oneOf": [\n        {\n          "minimum": 1,\n          "type": "integer"\n        },\n        {\n          "items": {\n            "minimum": 1,\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Human-readable name for the mechanism. Used in logs and graph plots; should be unique within a Composition.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "OutputPort specifications. Strings may name standard output ports: \'RESULT\' (default), plus the ProcessingMechanism extras \'MEAN\', \'MEDIAN\', \'STANDARD_DEVIATION\', \'VARIANCE\', \'MAX_VAL\', \'MAX_ABS_VAL\', \'MAX_ONE_HOT\', \'MAX_ABS_ONE_HOT\', \'MAX_INDICATOR\', \'MAX_ABS_INDICATOR\', \'PROB\'. Dict specs allow custom OutputPorts.",\n      "items": {},\n      "type": "array"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Dict of additional parameter overrides applied at construction. Rarely needed \\u2014 prefer top-level kwargs.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "name"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `function` must be a PsyNeuLink Function class name (string like \'Linear\', \'Logistic\'), not an arbitrary handle/identifier. Recent feedback shows agents passing opaque strings like \'h_ab495ac919ec\' — these are not resolvable and lead to dimension-mismatch errors deep inside the chosen function.\n- The function\'s expected variable shape MUST match `default_variable` / `input_shapes`. Stateful integrator functions in particular (DriftOnASphereIntegrator, OrnsteinUhlenbeckIntegrator, …) have constraints tying their internal state shape to `default_variable` — passing a 24-element default_variable with a function whose noise/state was sized for length 1 (or vice-versa) raises `ValueError: matmul: ... size 1 is different from 24` at construction time. Configure the function\'s own dimensional kwargs so they match before passing it in.\n- Provide either `default_variable` or `input_shapes`, not both — they\'re redundant and conflicting values raise.\n- `default_variable` is 2D (list of InputPort templates). A 1D list is auto-promoted to one InputPort but being explicit avoids surprises.\n- If `len(default_variable) > 1` AND the function is a TransferFunction, ProcessingMechanism auto-creates one OutputPort per InputPort, each named after its InputPort. Override by passing `output_ports` explicitly.\n- The returned object is a Mechanism instance (not yet in any Composition); add it to a Composition before running.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input value, '
                                                       'given as a 2D list-of-lists '
                                                       '(one inner list per '
                                                       'InputPort). Determines the '
                                                       'number and length of input '
                                                       'ports. Use either this OR '
                                                       'input_shapes, not both. '
                                                       'Example: [[0, 0, 0]] = one '
                                                       'InputPort of length 3.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'function': { 'description': 'Name of the PNL Function class to '
                                               "apply to the input, e.g. 'Linear', "
                                               "'Logistic', 'SoftMax', 'Exponential', "
                                               "'ReLU'. Must be a real PNL Function "
                                               'class name — opaque handles or made-up '
                                               'identifiers will fail or be silently '
                                               'misinterpreted. Function output shape '
                                               'must match default_variable / '
                                               'input_shapes. Defaults to Linear '
                                               '(identity) if omitted.',
                                'type': 'string'},
                  'function_params': { 'additionalProperties': True,
                                       'description': 'Keyword arguments forwarded to '
                                                      'the Function constructor (e.g. '
                                                      "{'slope': 2.0, 'intercept': "
                                                      "1.0} for Linear, {'gain': 1.0, "
                                                      "'bias': 0.0, 'x_0': 0.0} for "
                                                      'Logistic). Optional.',
                                       'type': 'object'},
                  'input_ports': { 'description': 'Explicit InputPort specifications. '
                                                  'Each entry can be a string name, a '
                                                  'dict spec, or a reference to '
                                                  'another Port/Mechanism. Usually '
                                                  'omitted — default_variable / '
                                                  'input_shapes is enough.',
                                   'items': {},
                                   'type': 'array'},
                  'input_shapes': { 'description': 'Shorthand for default_variable. An '
                                                   'int gives one InputPort of that '
                                                   'length; a list of ints gives '
                                                   'multiple InputPorts of those '
                                                   'lengths. Example: 3 = one '
                                                   'InputPort of length 3; [3, 2] = '
                                                   'two InputPorts of lengths 3 and 2.',
                                    'oneOf': [ {'minimum': 1, 'type': 'integer'},
                                               { 'items': { 'minimum': 1,
                                                            'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Human-readable name for the mechanism. '
                                           'Used in logs and graph plots; should be '
                                           'unique within a Composition.',
                            'type': 'string'},
                  'output_ports': { 'description': 'OutputPort specifications. Strings '
                                                   'may name standard output ports: '
                                                   "'RESULT' (default), plus the "
                                                   "ProcessingMechanism extras 'MEAN', "
                                                   "'MEDIAN', 'STANDARD_DEVIATION', "
                                                   "'VARIANCE', 'MAX_VAL', "
                                                   "'MAX_ABS_VAL', 'MAX_ONE_HOT', "
                                                   "'MAX_ABS_ONE_HOT', "
                                                   "'MAX_INDICATOR', "
                                                   "'MAX_ABS_INDICATOR', 'PROB'. Dict "
                                                   'specs allow custom OutputPorts.',
                                    'items': {},
                                    'type': 'array'},
                  'params': { 'additionalProperties': True,
                              'description': 'Dict of additional parameter overrides '
                                             'applied at construction. Rarely needed — '
                                             'prefer top-level kwargs.',
                              'type': 'object'}},
  'required': ['name'],
  'type': 'object'}
TOOL_NOTES = "- `function` must be a PsyNeuLink Function class name (string like 'Linear', 'Logistic'), not an arbitrary handle/identifier. Recent feedback shows agents passing opaque strings like 'h_ab495ac919ec' — these are not resolvable and lead to dimension-mismatch errors deep inside the chosen function.\n- The function's expected variable shape MUST match `default_variable` / `input_shapes`. Stateful integrator functions in particular (DriftOnASphereIntegrator, OrnsteinUhlenbeckIntegrator, …) have constraints tying their internal state shape to `default_variable` — passing a 24-element default_variable with a function whose noise/state was sized for length 1 (or vice-versa) raises `ValueError: matmul: ... size 1 is different from 24` at construction time. Configure the function's own dimensional kwargs so they match before passing it in.\n- Provide either `default_variable` or `input_shapes`, not both — they're redundant and conflicting values raise.\n- `default_variable` is 2D (list of InputPort templates). A 1D list is auto-promoted to one InputPort but being explicit avoids surprises.\n- If `len(default_variable) > 1` AND the function is a TransferFunction, ProcessingMechanism auto-creates one OutputPort per InputPort, each named after its InputPort. Override by passing `output_ports` explicitly.\n- The returned object is a Mechanism instance (not yet in any Composition); add it to a Composition before running."


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
        'Create a generic ProcessingMechanism — the default, function-agnostic Mechanism for feedforward processing nodes (input layers, transform stages, simple output layers) inside a Composition.'
        return _impl(args or {})
