"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7081f1eeb1933720e671dd08ceb3cec5cad8b6c6d65c93db3bceb89a4a51959a'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.processing.processingmechanism.SoftMax'
__pnl_kind__ = 'class'
__pnl_parents__ = ['TransferFunction',
 'Function_Base',
 'Function',
 'ShellClass',
 'Component',
 'MDFSerializable']
__pnl_parent_sha256s__ = {'Component': 'b878afca9fca90ac1a952605ca8d39a37f25ebebf1411a7f545b9c48a3eaeec3',
 'Function': '49ff0535055d97328c0f76806a53021714e2f8577d138152b75b7e15fcaab2e3',
 'Function_Base': '9b4c0d2feb23147f7d25af3ae03decf546fdb1f2e8be53abb8d8168801d60afa',
 'MDFSerializable': 'caad6059e8ef158be1269a23127f13da3733824c3585f9b4d6e3a63de82f65da',
 'ShellClass': 'adc23754ebeb0c55bdde1324622b33a509116703503508ee7e7de181a8afeee6',
 'TransferFunction': '0e6ecff88f6b55381f0295545a1697d4de9cc3cec153447b558945804ad26812'}
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_soft_max'
TOOL_DESCRIPTION = 'Constructs a `psyneulink.SoftMax` transfer function — typically passed as the `function=` of a ProcessingMechanism, or as a selection/retrieval function inside memory mechanisms (ContentAddressableMemory, EpisodicMemoryMechanism). Beyond the shape-preserving transform contract from TransferFunction, this adds inverse-temperature `gain` (or *ADAPTIVE* gain that auto-tunes to the entropy/length of the input — useful for one-hot or sparse vectors), `mask_threshold` for ignoring small entries, and `output` modes that turn the softmax into argmax/max-indicator/probabilistic-sample selectors. Returns an opaque function handle the agent then attaches to a Mechanism.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "adapt_base": {\n      "description": "base parameter for adapt_gain (only used when gain=\'ADAPTIVE\'). Default 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_entropy_weighting": {\n      "description": "entropy_weighting parameter for adapt_gain (only used when gain=\'ADAPTIVE\'). Default 0.1 in docstring (0.95 in current Parameters).",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "adapt_scale": {\n      "description": "scale parameter for adapt_gain (only used when gain=\'ADAPTIVE\'). Default 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "1d array template for the value to be transformed; sets the expected input length.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "gain": {\n      "description": "Inverse temperature: scalar > 0 sharpens the distribution. Pass the string \'ADAPTIVE\' to have gain auto-tuned from variable entropy/length (mask_threshold is then ignored).",\n      "oneOf": [\n        {\n          "exclusiveMinimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "mask_threshold": {\n      "description": "If set, elements of (gain*variable) with |value| <= threshold are masked to -inf before softmax. Only honored when gain is a scalar; ignored when gain=\'ADAPTIVE\'.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional Function name.",\n      "type": "string"\n    },\n    "output": {\n      "description": "Selection mode applied AFTER softmax. OMIT this argument to get the default full softmax distribution \\u2014 do NOT pass \'ALL\' (see notes). \'arg_max\'/\'arg_max_indicator\': 1 at the argmax index, 0 elsewhere. \'MAX_VAL\'/\'MAX_INDICATOR\': max softmax value (or 1) at the argmax index, 0 elsewhere. \'PROB\'/\'PROB_INDICATOR\': probabilistically sample one index using the softmax distribution.",\n      "enum": [\n        "arg_max",\n        "arg_max_indicator",\n        "MAX_VAL",\n        "MAX_INDICATOR",\n        "PROB",\n        "PROB_INDICATOR"\n      ],\n      "type": "string"\n    },\n    "per_item": {\n      "description": "For 2d variable: if true (default), softmax is applied to each row independently; if false, applied to the full flattened variable.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — `output=\'ALL\'` is broken (issue #34): SoftMax tests `if output not in {None, ALL}:` against the PNL keyword constant, but the user-facing string \'ALL\' does not match it, so the call falls through to `OneHot(mode=\'ALL\')`, which beartype rejects (OneHot only accepts lowercase \'arg_max\' / \'PROB\' / \'MAX_VAL\' / etc.). To get the default full-softmax-distribution behavior, simply omit the `output` argument. For non-default selection, use the enum values listed: \'arg_max\', \'arg_max_indicator\', \'MAX_VAL\', \'MAX_INDICATOR\', \'PROB\', \'PROB_INDICATOR\'. Other gotchas: gain must be > 0 when scalar; mask_threshold is silently ignored under ADAPTIVE gain; if variable is all zeros the result is all zeros (no normalization); derivative is undefined (raises) when output=\'PROB\'; ADAPTIVE gain is finicky and may need adapt_scale/adapt_base/adapt_entropy_weighting tuning per variable length. This is a Function — pass the returned handle as `function=` to a Mechanism, do not call it standalone in a Composition.'
TOOL_PARAMETERS = { 'properties': { 'adapt_base': { 'description': 'base parameter for adapt_gain (only '
                                                 "used when gain='ADAPTIVE'). Default "
                                                 '1.0.',
                                  'exclusiveMinimum': 0,
                                  'type': 'number'},
                  'adapt_entropy_weighting': { 'description': 'entropy_weighting '
                                                              'parameter for '
                                                              'adapt_gain (only used '
                                                              "when gain='ADAPTIVE'). "
                                                              'Default 0.1 in '
                                                              'docstring (0.95 in '
                                                              'current Parameters).',
                                               'exclusiveMinimum': 0,
                                               'type': 'number'},
                  'adapt_scale': { 'description': 'scale parameter for adapt_gain '
                                                  "(only used when gain='ADAPTIVE'). "
                                                  'Default 1.0.',
                                   'exclusiveMinimum': 0,
                                   'type': 'number'},
                  'default_variable': { 'description': '1d array template for the '
                                                       'value to be transformed; sets '
                                                       'the expected input length.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'gain': { 'description': 'Inverse temperature: scalar > 0 sharpens '
                                           'the distribution. Pass the string '
                                           "'ADAPTIVE' to have gain auto-tuned from "
                                           'variable entropy/length (mask_threshold is '
                                           'then ignored).',
                            'oneOf': [ {'exclusiveMinimum': 0, 'type': 'number'},
                                       {'enum': ['ADAPTIVE'], 'type': 'string'}]},
                  'mask_threshold': { 'description': 'If set, elements of '
                                                     '(gain*variable) with |value| <= '
                                                     'threshold are masked to -inf '
                                                     'before softmax. Only honored '
                                                     'when gain is a scalar; ignored '
                                                     "when gain='ADAPTIVE'.",
                                      'exclusiveMinimum': 0,
                                      'type': 'number'},
                  'name': {'description': 'Optional Function name.', 'type': 'string'},
                  'output': { 'description': 'Selection mode applied AFTER softmax. '
                                             'OMIT this argument to get the default '
                                             'full softmax distribution — do NOT pass '
                                             "'ALL' (see notes). "
                                             "'arg_max'/'arg_max_indicator': 1 at the "
                                             'argmax index, 0 elsewhere. '
                                             "'MAX_VAL'/'MAX_INDICATOR': max softmax "
                                             'value (or 1) at the argmax index, 0 '
                                             "elsewhere. 'PROB'/'PROB_INDICATOR': "
                                             'probabilistically sample one index using '
                                             'the softmax distribution.',
                              'enum': [ 'arg_max',
                                        'arg_max_indicator',
                                        'MAX_VAL',
                                        'MAX_INDICATOR',
                                        'PROB',
                                        'PROB_INDICATOR'],
                              'type': 'string'},
                  'per_item': { 'description': 'For 2d variable: if true (default), '
                                               'softmax is applied to each row '
                                               'independently; if false, applied to '
                                               'the full flattened variable.',
                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL — `output='ALL'` is broken (issue #34): SoftMax tests `if output not in {None, ALL}:` against the PNL keyword constant, but the user-facing string 'ALL' does not match it, so the call falls through to `OneHot(mode='ALL')`, which beartype rejects (OneHot only accepts lowercase 'arg_max' / 'PROB' / 'MAX_VAL' / etc.). To get the default full-softmax-distribution behavior, simply omit the `output` argument. For non-default selection, use the enum values listed: 'arg_max', 'arg_max_indicator', 'MAX_VAL', 'MAX_INDICATOR', 'PROB', 'PROB_INDICATOR'. Other gotchas: gain must be > 0 when scalar; mask_threshold is silently ignored under ADAPTIVE gain; if variable is all zeros the result is all zeros (no normalization); derivative is undefined (raises) when output='PROB'; ADAPTIVE gain is finicky and may need adapt_scale/adapt_base/adapt_entropy_weighting tuning per variable length. This is a Function — pass the returned handle as `function=` to a Mechanism, do not call it standalone in a Composition."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.SoftMax
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
    def create_soft_max(args: dict[str, Any] | None = None) -> Any:
        'Constructs a `psyneulink.SoftMax` transfer function — typically passed as the `function=` of a ProcessingMechanism, or as a selection/retrieval function inside memory mechanisms (ContentAddressableMemory, EpisodicMemoryMechanism).'
        return _impl(args or {})
