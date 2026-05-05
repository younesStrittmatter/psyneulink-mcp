"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = '739ba641ab0cfb7050b2c2ae4ed22e66063d97875435936b554acc4bead7b71f'
__pnl_qualname__ = 'psyneulink.Composition.learn'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'learn'
TOOL_DESCRIPTION = 'Call this tool to train a Composition that has learning pathways configured — i.e., run it in learning mode so enabled MappingProjection weights are updated. Pass labeled input/target dicts keyed by mechanism handle strings and control training with epochs, learning_rate, and early-stopping options. Returns a list of output values from the last trial of the final epoch; full epoch results are stored in the composition\'s `learning_results` attribute.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the Composition instance returned by create_composition (or equivalent constructor). Must already have at least one learning pathway added before calling learn.",\n      "type": "string"\n    },\n    "epochs": {\n      "default": 1,\n      "description": "Number of full passes through the input set (training epochs).",\n      "type": "integer"\n    },\n    "inputs": {\n      "additionalProperties": true,\n      "description": "Dict mapping input-node handle strings to lists of input arrays, one per trial. Alternatively, a dict with keys \'inputs\', \'targets\', and \'epochs\' to bundle all training specification in one argument.",\n      "type": "object"\n    },\n    "learning_rate": {\n      "description": "Per-call learning rate override. Applies only to MappingProjections without individually specified rates, and only for this call. Overrides the Composition-level default.",\n      "type": "number"\n    },\n    "min_delta": {\n      "default": 0,\n      "description": "Minimum loss reduction required for an epoch to be considered \'good\'. Used with patience for early stopping.",\n      "type": "number"\n    },\n    "minibatch_size": {\n      "description": "Number of trials per gradient-update step. Defaults to the Composition\'s minibatch_size parameter (typically 1).",\n      "type": "integer"\n    },\n    "num_trials": {\n      "description": "Exact number of trials to run per epoch. If greater than the number of provided inputs, inputs are repeated. Omit to infer from input length.",\n      "type": "integer"\n    },\n    "optimizations_per_minibatch": {\n      "description": "Number of forward+backward pass cycles per minibatch. Values > 1 implement multi-step optimization (e.g., backprop-to-activation). Only meaningful for AutodiffComposition.",\n      "type": "integer"\n    },\n    "patience": {\n      "description": "Early-stopping threshold: maximum number of consecutive \'bad\' epochs (epochs that do not reduce loss by at least min_delta) before training stops. Omit to disable early stopping.",\n      "type": "integer"\n    },\n    "randomize_minibatches": {\n      "default": false,\n      "description": "Whether to shuffle the trial order within each epoch before forming minibatches.",\n      "type": "boolean"\n    },\n    "report_output": {\n      "description": "Controls per-trial output reporting. Pass as string e.g. \'ReportOutput.FULL\'. Defaults to OFF.",\n      "type": "string"\n    },\n    "report_progress": {\n      "description": "Controls real-time progress reporting. Pass as string e.g. \'ReportProgress.TQDM\'. Defaults to OFF.",\n      "type": "string"\n    },\n    "targets": {\n      "additionalProperties": true,\n      "description": "Dict mapping output-node (or TARGET_MECHANISM) handle strings to lists of target arrays, one per trial. Keys can be the final output node or the dedicated target mechanism of each learning pathway. Omit only when targets are embedded inside the \'inputs\' dict.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "composition",\n    "inputs"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `inputs` keys must be mechanism handle strings (same strings used when adding nodes), not Python object references.\n- `targets` keys can be either the final output-node handle OR the TARGET_MECHANISM handle for each learning pathway; use `get_target_nodes` (via the composition_get_target_nodes tool if available) to enumerate valid target keys.\n- Non-Python execution modes (PyTorch, LLVM) are only supported on AutodiffComposition; calling with a plain Composition always uses Python mode regardless.\n- `call_before_minibatch` and `call_after_minibatch` (Python callables) and `execute_in_additional_optimizations` (complex node→parameter mapping) cannot be expressed in a JSON schema and are not exposed here; use the Python API directly for those.\n- If the Composition has no learning components, learn() will run but emit a warning and no weight updates will occur.\n- The return value is the output list from the **last trial** only; access `composition.learning_results` for all epochs.\n- `learning_rate` as a dict (per-projection mapping) is NOT supported for plain Composition — only for AutodiffComposition; pass a scalar float here.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the Composition '
                                                  'instance returned by '
                                                  'create_composition (or equivalent '
                                                  'constructor). Must already have at '
                                                  'least one learning pathway added '
                                                  'before calling learn.',
                                   'type': 'string'},
                  'epochs': { 'default': 1,
                              'description': 'Number of full passes through the input '
                                             'set (training epochs).',
                              'type': 'integer'},
                  'inputs': { 'additionalProperties': True,
                              'description': 'Dict mapping input-node handle strings '
                                             'to lists of input arrays, one per trial. '
                                             'Alternatively, a dict with keys '
                                             "'inputs', 'targets', and 'epochs' to "
                                             'bundle all training specification in one '
                                             'argument.',
                              'type': 'object'},
                  'learning_rate': { 'description': 'Per-call learning rate override. '
                                                    'Applies only to '
                                                    'MappingProjections without '
                                                    'individually specified rates, and '
                                                    'only for this call. Overrides the '
                                                    'Composition-level default.',
                                     'type': 'number'},
                  'min_delta': { 'default': 0,
                                 'description': 'Minimum loss reduction required for '
                                                "an epoch to be considered 'good'. "
                                                'Used with patience for early '
                                                'stopping.',
                                 'type': 'number'},
                  'minibatch_size': { 'description': 'Number of trials per '
                                                     'gradient-update step. Defaults '
                                                     "to the Composition's "
                                                     'minibatch_size parameter '
                                                     '(typically 1).',
                                      'type': 'integer'},
                  'num_trials': { 'description': 'Exact number of trials to run per '
                                                 'epoch. If greater than the number of '
                                                 'provided inputs, inputs are '
                                                 'repeated. Omit to infer from input '
                                                 'length.',
                                  'type': 'integer'},
                  'optimizations_per_minibatch': { 'description': 'Number of '
                                                                  'forward+backward '
                                                                  'pass cycles per '
                                                                  'minibatch. Values > '
                                                                  '1 implement '
                                                                  'multi-step '
                                                                  'optimization (e.g., '
                                                                  'backprop-to-activation). '
                                                                  'Only meaningful for '
                                                                  'AutodiffComposition.',
                                                   'type': 'integer'},
                  'patience': { 'description': 'Early-stopping threshold: maximum '
                                               "number of consecutive 'bad' epochs "
                                               '(epochs that do not reduce loss by at '
                                               'least min_delta) before training '
                                               'stops. Omit to disable early stopping.',
                                'type': 'integer'},
                  'randomize_minibatches': { 'default': False,
                                             'description': 'Whether to shuffle the '
                                                            'trial order within each '
                                                            'epoch before forming '
                                                            'minibatches.',
                                             'type': 'boolean'},
                  'report_output': { 'description': 'Controls per-trial output '
                                                    'reporting. Pass as string e.g. '
                                                    "'ReportOutput.FULL'. Defaults to "
                                                    'OFF.',
                                     'type': 'string'},
                  'report_progress': { 'description': 'Controls real-time progress '
                                                      'reporting. Pass as string e.g. '
                                                      "'ReportProgress.TQDM'. Defaults "
                                                      'to OFF.',
                                       'type': 'string'},
                  'targets': { 'additionalProperties': True,
                               'description': 'Dict mapping output-node (or '
                                              'TARGET_MECHANISM) handle strings to '
                                              'lists of target arrays, one per trial. '
                                              'Keys can be the final output node or '
                                              'the dedicated target mechanism of each '
                                              'learning pathway. Omit only when '
                                              'targets are embedded inside the '
                                              "'inputs' dict.",
                               'type': 'object'}},
  'required': ['composition', 'inputs'],
  'type': 'object'}
TOOL_NOTES = '- `inputs` keys must be mechanism handle strings (same strings used when adding nodes), not Python object references.\n- `targets` keys can be either the final output-node handle OR the TARGET_MECHANISM handle for each learning pathway; use `get_target_nodes` (via the composition_get_target_nodes tool if available) to enumerate valid target keys.\n- Non-Python execution modes (PyTorch, LLVM) are only supported on AutodiffComposition; calling with a plain Composition always uses Python mode regardless.\n- `call_before_minibatch` and `call_after_minibatch` (Python callables) and `execute_in_additional_optimizations` (complex node→parameter mapping) cannot be expressed in a JSON schema and are not exposed here; use the Python API directly for those.\n- If the Composition has no learning components, learn() will run but emit a warning and no weight updates will occur.\n- The return value is the output list from the **last trial** only; access `composition.learning_results` for all epochs.\n- `learning_rate` as a dict (per-projection mapping) is NOT supported for plain Composition — only for AutodiffComposition; pass a scalar float here.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='learn',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def learn(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to train a Composition that has learning pathways configured — i.e., run it in learning mode so enabled MappingProjection weights are updated.'
        return _impl(args or {})
