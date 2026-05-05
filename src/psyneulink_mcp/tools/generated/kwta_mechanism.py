"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '1e6f83ce6b65546646d3c1a9781d2eba03e6aae0ffcf413f2ec429fa1d66fa97'
__pnl_qualname__ = 'psyneulink.KWTAMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_kwta_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a KWTAMechanism (k-winners-take-all) — a RecurrentTransferMechanism that shifts its input vector before activation so that exactly k elements land at or above a threshold. Use it when modeling competitive inhibition or sparse coding where a fixed number (or proportion) of units should win. Returns an instantiated KWTAMechanism object ready to be added to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "auto": {\n      "description": "Self-excitation weight on the recurrent matrix diagonal. Defaults to 5 (KWTAMechanism-specific default, overrides RecurrentTransferMechanism\'s default).",\n      "type": "number"\n    },\n    "average_based": {\n      "description": "If true, use the mean of top-k and bottom-(n-k) differences (weighted by ratio) to compute the offset, rather than boundary-point interpolation. Default false.",\n      "type": "boolean"\n    },\n    "clip": {\n      "description": "Hard [min, max] bounds applied to the output after the transfer function.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "function": {\n      "description": "Transfer function applied after KWTA scaling. Defaults to Logistic (not Linear as in base TransferMechanism). Pass a PsyNeuLink function name string or object.",\n      "type": "string"\n    },\n    "hetero": {\n      "description": "Cross-inhibition weight on the off-diagonal entries of the recurrent matrix. Defaults to 0.",\n      "type": "number"\n    },\n    "inhibition_only": {\n      "description": "If true (default), the computed offset is clamped to \\u2264 0 so inputs can only be shifted downward. Set to false to allow excitatory (positive) offsets.",\n      "type": "boolean"\n    },\n    "initial_value": {\n      "description": "Starting activation values used when integrator_mode is true.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Number of input elements (size of the input vector). Also determines the pool over which k-winners compete.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "description": "Rate of integration when integrator_mode is true. Value between 0 and 1.",\n      "type": "number"\n    },\n    "integrator_mode": {\n      "description": "If true, activations are integrated over time using integrator_function before the transfer function is applied.",\n      "type": "boolean"\n    },\n    "k_value": {\n      "description": "Target number or proportion of elements to be at or above threshold. A float in (0, 1) is treated as a proportion; a positive integer is a count; a negative integer means that many elements should be BELOW threshold. Default 0.5.",\n      "type": "number"\n    },\n    "matrix": {\n      "description": "Explicit recurrent weight matrix (2-D array). If provided, auto and hetero are ignored.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Name for this mechanism instance.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Noise added to the input. Can be a scalar or a distribution function.",\n      "type": "number"\n    },\n    "ratio": {\n      "description": "Interpolation weight (0\\u20131) between the k-th and (k+1)-th sorted differences when computing the shift offset. Default 0.5.",\n      "type": "number"\n    },\n    "threshold": {\n      "description": "Activation level that k elements should reach or exceed. The mechanism shifts inputs to meet this target. Default 0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n1. KWTA scaling is applied BEFORE noise and integration — the offset shift happens on the raw input vector, not the integrated state. This can produce unexpected results when integrator_mode=True.\n2. k_value validation: if k_value is a non-integer float it must be strictly between 0 and 1; |k_value| must not exceed input_shapes. Passing k_value > input size raises a KWTAError.\n3. ratio must be in [0, 1]; values outside this range raise a KWTAError.\n4. Default auto=5 and hetero=0 are KWTAMechanism-specific overrides set in __init__ when matrix=None — they differ from RecurrentTransferMechanism defaults. The comment in source notes "this value is bad" and may change.\n5. Default function is Logistic, not Linear (unlike base TransferMechanism/RecurrentTransferMechanism).\n6. inhibition_only=True (default) means if all k winners are already above threshold the offset is 0 — no upward correction is made even if fewer than k units are winning.\n7. When k == 0, the offset is derived from sorted_diffs[0] (the smallest difference); when k == n, from sorted_diffs[n-1]. Edge cases at exact boundaries are handled but may produce a warning if scaling overshoots.'
TOOL_PARAMETERS = { 'properties': { 'auto': { 'description': 'Self-excitation weight on the recurrent '
                                           'matrix diagonal. Defaults to 5 '
                                           '(KWTAMechanism-specific default, overrides '
                                           "RecurrentTransferMechanism's default).",
                            'type': 'number'},
                  'average_based': { 'description': 'If true, use the mean of top-k '
                                                    'and bottom-(n-k) differences '
                                                    '(weighted by ratio) to compute '
                                                    'the offset, rather than '
                                                    'boundary-point interpolation. '
                                                    'Default false.',
                                     'type': 'boolean'},
                  'clip': { 'description': 'Hard [min, max] bounds applied to the '
                                           'output after the transfer function.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'function': { 'description': 'Transfer function applied after KWTA '
                                               'scaling. Defaults to Logistic (not '
                                               'Linear as in base TransferMechanism). '
                                               'Pass a PsyNeuLink function name string '
                                               'or object.',
                                'type': 'string'},
                  'hetero': { 'description': 'Cross-inhibition weight on the '
                                             'off-diagonal entries of the recurrent '
                                             'matrix. Defaults to 0.',
                              'type': 'number'},
                  'inhibition_only': { 'description': 'If true (default), the computed '
                                                      'offset is clamped to ≤ 0 so '
                                                      'inputs can only be shifted '
                                                      'downward. Set to false to allow '
                                                      'excitatory (positive) offsets.',
                                       'type': 'boolean'},
                  'initial_value': { 'description': 'Starting activation values used '
                                                    'when integrator_mode is true.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Number of input elements (size of '
                                                   'the input vector). Also determines '
                                                   'the pool over which k-winners '
                                                   'compete.',
                                    'type': 'integer'},
                  'integration_rate': { 'description': 'Rate of integration when '
                                                       'integrator_mode is true. Value '
                                                       'between 0 and 1.',
                                        'type': 'number'},
                  'integrator_mode': { 'description': 'If true, activations are '
                                                      'integrated over time using '
                                                      'integrator_function before the '
                                                      'transfer function is applied.',
                                       'type': 'boolean'},
                  'k_value': { 'description': 'Target number or proportion of elements '
                                              'to be at or above threshold. A float in '
                                              '(0, 1) is treated as a proportion; a '
                                              'positive integer is a count; a negative '
                                              'integer means that many elements should '
                                              'be BELOW threshold. Default 0.5.',
                               'type': 'number'},
                  'matrix': { 'description': 'Explicit recurrent weight matrix (2-D '
                                             'array). If provided, auto and hetero are '
                                             'ignored.',
                              'items': {'items': {'type': 'number'}, 'type': 'array'},
                              'type': 'array'},
                  'name': { 'description': 'Name for this mechanism instance.',
                            'type': 'string'},
                  'noise': { 'description': 'Noise added to the input. Can be a scalar '
                                            'or a distribution function.',
                             'type': 'number'},
                  'ratio': { 'description': 'Interpolation weight (0–1) between the '
                                            'k-th and (k+1)-th sorted differences when '
                                            'computing the shift offset. Default 0.5.',
                             'type': 'number'},
                  'threshold': { 'description': 'Activation level that k elements '
                                                'should reach or exceed. The mechanism '
                                                'shifts inputs to meet this target. '
                                                'Default 0.',
                                 'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '1. KWTA scaling is applied BEFORE noise and integration — the offset shift happens on the raw input vector, not the integrated state. This can produce unexpected results when integrator_mode=True.\n2. k_value validation: if k_value is a non-integer float it must be strictly between 0 and 1; |k_value| must not exceed input_shapes. Passing k_value > input size raises a KWTAError.\n3. ratio must be in [0, 1]; values outside this range raise a KWTAError.\n4. Default auto=5 and hetero=0 are KWTAMechanism-specific overrides set in __init__ when matrix=None — they differ from RecurrentTransferMechanism defaults. The comment in source notes "this value is bad" and may change.\n5. Default function is Logistic, not Linear (unlike base TransferMechanism/RecurrentTransferMechanism).\n6. inhibition_only=True (default) means if all k winners are already above threshold the offset is 0 — no upward correction is made even if fewer than k units are winning.\n7. When k == 0, the offset is derived from sorted_diffs[0] (the smallest difference); when k == n, from sorted_diffs[n-1]. Edge cases at exact boundaries are handled but may produce a warning if scaling overshoots.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.KWTAMechanism
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
    def create_kwta_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a KWTAMechanism (k-winners-take-all) — a RecurrentTransferMechanism that shifts its input vector before activation so that exactly k elements land at or above a threshold.'
        return _impl(args or {})
