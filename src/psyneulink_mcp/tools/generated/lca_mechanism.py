"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a7616f78670f80e2f98d0ff7c781e2c3edb417162c1f59e88ef1751bcfc1a04d'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.lcamechanism.LCAMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_lca_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a Leaky Competitive Accumulator (LCA) mechanism — a recurrent network where units accumulate evidence over time with mutual lateral inhibition and optional self-excitation. Use it when building decision-making or response-selection models where competing units race toward a stopping threshold via a LeakyCompetingIntegrator. Returns an LCAMechanism handle to add to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "[min, max] bounds to clip activations after each step.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "competition": {\n      "description": "Magnitude of lateral inhibition (positive number). Sets negative off-diagonal weights in the recurrent matrix. Passing a negative value produces excitatory lateral connections and triggers a runtime warning. Default: 1.0.",\n      "type": "number"\n    },\n    "function": {\n      "description": "Transfer function applied after integration. Default: \'Logistic\'.",\n      "type": "string"\n    },\n    "initial_value": {\n      "description": "Initial activation values per unit. Length must match input_shapes.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Number of competing units. Must be >= 2 when threshold_criterion is \'max_vs_next\' or \'max_vs_avg\'.",\n      "type": "integer"\n    },\n    "leak": {\n      "description": "Decay rate for LeakyCompetingIntegrator \\u2014 scales how much prior state carries over each step. Default: 0.5.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Name for the mechanism instance.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Noise added at each integration step. Default: 0.",\n      "type": "number"\n    },\n    "output_ports": {\n      "description": "Output ports to include. LCA-specific extras: \'MAX_VS_NEXT\' and \'MAX_VS_AVG\'. Must be listed explicitly; they are not included by default.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "self_excitation": {\n      "description": "Diagonal (self-feedback) weight in the recurrent matrix. Alias for \'auto\'. Default: 0.0.",\n      "type": "number"\n    },\n    "threshold": {\n      "description": "Numeric value at which is_finished becomes True, halting execution. Must be paired with threshold_criterion. Omit for no early stopping.",\n      "type": "number"\n    },\n    "threshold_criterion": {\n      "description": "Stopping criterion: \'value\' = max unit activation >= threshold; \'max_vs_next\' = gap between top-2 units >= threshold; \'max_vs_avg\' = winner minus mean of others >= threshold; \'CONVERGENCE\' = max abs change between steps <= threshold. Requires threshold to also be set.",\n      "enum": [\n        "value",\n        "max_vs_next",\n        "max_vs_avg",\n        "CONVERGENCE"\n      ],\n      "type": "string"\n    },\n    "time_step_size": {\n      "description": "Integration time-step for LeakyCompetingIntegrator; also scales noise. Default: 0.1.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nROOT CAUSE OF ISSUE #3 FIXED: PNL threshold_criterion constants are lowercase strings — pass "value", "max_vs_next", "max_vs_avg", or "CONVERGENCE" (CONVERGENCE is the only uppercase one). The previous spec incorrectly listed "VALUE", "MAX_VS_NEXT", "MAX_VS_AVG" in uppercase; those strings do not match PNL\'s internal constants and silently fall through to an error-handler path that itself has a PNL bug (uses self.__name__ instead of self.__class__.__name__), producing a confusing AttributeError instead of a clear ValueError.\n\nintegrator_mode defaults to True for LCAMechanism (unlike the base TransferMechanism), so accumulation over time steps is always on.\n\nDo not set both competition and hetero; they are coupled (hetero = -competition). Do not set both self_excitation and the internal \'auto\' alias — they must agree.\n\nIf a matrix kwarg is passed directly, self_excitation and competition are silently ignored. Prefer self_excitation/competition for LCA models.\n\nthreshold_criterion with \'max_vs_next\' or \'max_vs_avg\' requires input_shapes >= 2.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': '[min, max] bounds to clip activations '
                                           'after each step.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'competition': { 'description': 'Magnitude of lateral inhibition '
                                                  '(positive number). Sets negative '
                                                  'off-diagonal weights in the '
                                                  'recurrent matrix. Passing a '
                                                  'negative value produces excitatory '
                                                  'lateral connections and triggers a '
                                                  'runtime warning. Default: 1.0.',
                                   'type': 'number'},
                  'function': { 'description': 'Transfer function applied after '
                                               "integration. Default: 'Logistic'.",
                                'type': 'string'},
                  'initial_value': { 'description': 'Initial activation values per '
                                                    'unit. Length must match '
                                                    'input_shapes.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Number of competing units. Must be '
                                                   '>= 2 when threshold_criterion is '
                                                   "'max_vs_next' or 'max_vs_avg'.",
                                    'type': 'integer'},
                  'leak': { 'description': 'Decay rate for LeakyCompetingIntegrator — '
                                           'scales how much prior state carries over '
                                           'each step. Default: 0.5.',
                            'type': 'number'},
                  'name': { 'description': 'Name for the mechanism instance.',
                            'type': 'string'},
                  'noise': { 'description': 'Noise added at each integration step. '
                                            'Default: 0.',
                             'type': 'number'},
                  'output_ports': { 'description': 'Output ports to include. '
                                                   "LCA-specific extras: 'MAX_VS_NEXT' "
                                                   "and 'MAX_VS_AVG'. Must be listed "
                                                   'explicitly; they are not included '
                                                   'by default.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'self_excitation': { 'description': 'Diagonal (self-feedback) weight '
                                                      'in the recurrent matrix. Alias '
                                                      "for 'auto'. Default: 0.0.",
                                       'type': 'number'},
                  'threshold': { 'description': 'Numeric value at which is_finished '
                                                'becomes True, halting execution. Must '
                                                'be paired with threshold_criterion. '
                                                'Omit for no early stopping.',
                                 'type': 'number'},
                  'threshold_criterion': { 'description': "Stopping criterion: 'value' "
                                                          '= max unit activation >= '
                                                          "threshold; 'max_vs_next' = "
                                                          'gap between top-2 units >= '
                                                          "threshold; 'max_vs_avg' = "
                                                          'winner minus mean of others '
                                                          ">= threshold; 'CONVERGENCE' "
                                                          '= max abs change between '
                                                          'steps <= threshold. '
                                                          'Requires threshold to also '
                                                          'be set.',
                                           'enum': [ 'value',
                                                     'max_vs_next',
                                                     'max_vs_avg',
                                                     'CONVERGENCE'],
                                           'type': 'string'},
                  'time_step_size': { 'description': 'Integration time-step for '
                                                     'LeakyCompetingIntegrator; also '
                                                     'scales noise. Default: 0.1.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'ROOT CAUSE OF ISSUE #3 FIXED: PNL threshold_criterion constants are lowercase strings — pass "value", "max_vs_next", "max_vs_avg", or "CONVERGENCE" (CONVERGENCE is the only uppercase one). The previous spec incorrectly listed "VALUE", "MAX_VS_NEXT", "MAX_VS_AVG" in uppercase; those strings do not match PNL\'s internal constants and silently fall through to an error-handler path that itself has a PNL bug (uses self.__name__ instead of self.__class__.__name__), producing a confusing AttributeError instead of a clear ValueError.\n\nintegrator_mode defaults to True for LCAMechanism (unlike the base TransferMechanism), so accumulation over time steps is always on.\n\nDo not set both competition and hetero; they are coupled (hetero = -competition). Do not set both self_excitation and the internal \'auto\' alias — they must agree.\n\nIf a matrix kwarg is passed directly, self_excitation and competition are silently ignored. Prefer self_excitation/competition for LCA models.\n\nthreshold_criterion with \'max_vs_next\' or \'max_vs_avg\' requires input_shapes >= 2.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LCAMechanism
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
    def create_lca_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Leaky Competitive Accumulator (LCA) mechanism — a recurrent network where units accumulate evidence over time with mutual lateral inhibition and optional self-excitation.'
        return _impl(args or {})
