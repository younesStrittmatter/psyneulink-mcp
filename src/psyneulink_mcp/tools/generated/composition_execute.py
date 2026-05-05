"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = '6962e1c06258aa8492925bdd5637b663f528d843c27fb25dae4ff7e9a944a788'
__pnl_qualname__ = 'psyneulink.Composition.execute'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'execute'
TOOL_DESCRIPTION = 'Call this tool to execute exactly one trial of a Composition — pass inputs to its INPUT nodes, let the Scheduler coordinate node execution until termination conditions are met, and receive the output values. Use this instead of `run` when you need single-trial control (e.g., stepping through a simulation manually or embedding execution in a custom loop). Returns a numpy array of the Composition\'s output port values, excluding PROBE node outputs.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clamp_input": {\n      "default": "SOFT_CLAMP",\n      "description": "How to clamp inputs to INPUT nodes. One of \'SOFT_CLAMP\', \'HARD_CLAMP\', \'PULSE_CLAMP\', or \'NO_CLAMP\'.",\n      "type": "string"\n    },\n    "composition": {\n      "description": "Handle string for the Composition to execute, as returned by create_composition or analogous constructor tool.",\n      "type": "string"\n    },\n    "execution_mode": {\n      "default": "Python",\n      "description": "Whether to run in Python interpreter or a compiled mode. \'Python\' is the safe default; compiled modes require LLVM-JIT support and are not universally available.",\n      "enum": [\n        "Auto",\n        "LLVM",\n        "LLVMexec",\n        "Python"\n      ],\n      "type": "string"\n    },\n    "inputs": {\n      "additionalProperties": {},\n      "description": "Mapping from node handle strings (Mechanism or nested Composition) to their input values. Each value must match the node\'s default_variable shape. If omitted, each INPUT node uses its default_variable. Keys are node handle strings; values are arrays or lists.",\n      "type": "object"\n    },\n    "report_output": {\n      "default": "OFF",\n      "description": "Whether to print output values of the Composition and its nodes during execution.",\n      "enum": [\n        "OFF",\n        "TERSE",\n        "FULL"\n      ],\n      "type": "string"\n    },\n    "report_params": {\n      "default": "OFF",\n      "description": "Whether to print parameter values of the Composition and its nodes during execution.",\n      "enum": [\n        "OFF",\n        "TERSE",\n        "FULL"\n      ],\n      "type": "string"\n    },\n    "report_progress": {\n      "default": "OFF",\n      "description": "Whether to report execution progress.",\n      "enum": [\n        "OFF",\n        "TERSE",\n        "FULL"\n      ],\n      "type": "string"\n    },\n    "report_simulations": {\n      "default": "OFF",\n      "description": "Whether to report output/progress for controller simulations during this execution.",\n      "enum": [\n        "OFF",\n        "TERSE",\n        "FULL"\n      ],\n      "type": "string"\n    },\n    "report_to_devices": {\n      "description": "List of device strings specifying where reports are sent (e.g. [\'CONSOLE\']). Defaults to CONSOLE if reporting is enabled.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "runtime_params": {\n      "description": "Alternate parameter values applied only during this execution when specified Conditions are met. Structure: {node_handle: {param_name: [value, condition]}}.",\n      "type": "object"\n    },\n    "scheduler": {\n      "description": "Handle string for a custom Scheduler to use. If omitted, the Composition\'s automatically generated scheduler is used.",\n      "type": "string"\n    },\n    "skip_initialization": {\n      "default": false,\n      "description": "If true, skip re-initialization from base context. Use only when you know the context is already correctly initialized.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "composition"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `execute` runs exactly one trial. For multi-trial runs (with num_trials, reset logic, run-level controller execution, etc.) use `run` instead. Calling `execute` directly bypasses the AFTER-RUN controller execution that `run` handles.\n- The callable parameters from the Python signature (`call_before_time_step`, `call_after_time_step`, `call_before_pass`, `call_after_pass`) cannot be passed via MCP and are omitted from this schema.\n- `inputs` keys must be node handle strings, not raw PsyNeuLink objects. The runtime resolves them to live objects before dispatch.\n- Output excludes values from nodes with NodeRole.PROBE in the enclosing Composition.\n- `runtime_params` is an advanced feature; incorrect Condition types will raise errors. Omit unless you specifically need per-execution parameter overrides.\n- Compiled execution modes (`LLVM`, `LLVMexec`) require LLVM-JIT infrastructure and fall back to Python if unavailable. Stick to `"Python"` unless you have a specific performance need and know compilation is supported.\n- `termination_processing` (a scheduler TerminationConditions dict) and `reset_stateful_functions_to` (a per-node reset-value dict) appear in the Python signature but are undocumented; they are intentionally omitted here.'
TOOL_PARAMETERS = { 'properties': { 'clamp_input': { 'default': 'SOFT_CLAMP',
                                   'description': 'How to clamp inputs to INPUT nodes. '
                                                  "One of 'SOFT_CLAMP', 'HARD_CLAMP', "
                                                  "'PULSE_CLAMP', or 'NO_CLAMP'.",
                                   'type': 'string'},
                  'composition': { 'description': 'Handle string for the Composition '
                                                  'to execute, as returned by '
                                                  'create_composition or analogous '
                                                  'constructor tool.',
                                   'type': 'string'},
                  'execution_mode': { 'default': 'Python',
                                      'description': 'Whether to run in Python '
                                                     'interpreter or a compiled mode. '
                                                     "'Python' is the safe default; "
                                                     'compiled modes require LLVM-JIT '
                                                     'support and are not universally '
                                                     'available.',
                                      'enum': ['Auto', 'LLVM', 'LLVMexec', 'Python'],
                                      'type': 'string'},
                  'inputs': { 'additionalProperties': {},
                              'description': 'Mapping from node handle strings '
                                             '(Mechanism or nested Composition) to '
                                             'their input values. Each value must '
                                             "match the node's default_variable shape. "
                                             'If omitted, each INPUT node uses its '
                                             'default_variable. Keys are node handle '
                                             'strings; values are arrays or lists.',
                              'type': 'object'},
                  'report_output': { 'default': 'OFF',
                                     'description': 'Whether to print output values of '
                                                    'the Composition and its nodes '
                                                    'during execution.',
                                     'enum': ['OFF', 'TERSE', 'FULL'],
                                     'type': 'string'},
                  'report_params': { 'default': 'OFF',
                                     'description': 'Whether to print parameter values '
                                                    'of the Composition and its nodes '
                                                    'during execution.',
                                     'enum': ['OFF', 'TERSE', 'FULL'],
                                     'type': 'string'},
                  'report_progress': { 'default': 'OFF',
                                       'description': 'Whether to report execution '
                                                      'progress.',
                                       'enum': ['OFF', 'TERSE', 'FULL'],
                                       'type': 'string'},
                  'report_simulations': { 'default': 'OFF',
                                          'description': 'Whether to report '
                                                         'output/progress for '
                                                         'controller simulations '
                                                         'during this execution.',
                                          'enum': ['OFF', 'TERSE', 'FULL'],
                                          'type': 'string'},
                  'report_to_devices': { 'description': 'List of device strings '
                                                        'specifying where reports are '
                                                        "sent (e.g. ['CONSOLE']). "
                                                        'Defaults to CONSOLE if '
                                                        'reporting is enabled.',
                                         'items': {'type': 'string'},
                                         'type': 'array'},
                  'runtime_params': { 'description': 'Alternate parameter values '
                                                     'applied only during this '
                                                     'execution when specified '
                                                     'Conditions are met. Structure: '
                                                     '{node_handle: {param_name: '
                                                     '[value, condition]}}.',
                                      'type': 'object'},
                  'scheduler': { 'description': 'Handle string for a custom Scheduler '
                                                "to use. If omitted, the Composition's "
                                                'automatically generated scheduler is '
                                                'used.',
                                 'type': 'string'},
                  'skip_initialization': { 'default': False,
                                           'description': 'If true, skip '
                                                          're-initialization from base '
                                                          'context. Use only when you '
                                                          'know the context is already '
                                                          'correctly initialized.',
                                           'type': 'boolean'}},
  'required': ['composition'],
  'type': 'object'}
TOOL_NOTES = '- `execute` runs exactly one trial. For multi-trial runs (with num_trials, reset logic, run-level controller execution, etc.) use `run` instead. Calling `execute` directly bypasses the AFTER-RUN controller execution that `run` handles.\n- The callable parameters from the Python signature (`call_before_time_step`, `call_after_time_step`, `call_before_pass`, `call_after_pass`) cannot be passed via MCP and are omitted from this schema.\n- `inputs` keys must be node handle strings, not raw PsyNeuLink objects. The runtime resolves them to live objects before dispatch.\n- Output excludes values from nodes with NodeRole.PROBE in the enclosing Composition.\n- `runtime_params` is an advanced feature; incorrect Condition types will raise errors. Omit unless you specifically need per-execution parameter overrides.\n- Compiled execution modes (`LLVM`, `LLVMexec`) require LLVM-JIT infrastructure and fall back to Python if unavailable. Stick to `"Python"` unless you have a specific performance need and know compilation is supported.\n- `termination_processing` (a scheduler TerminationConditions dict) and `reset_stateful_functions_to` (a per-node reset-value dict) appear in the Python signature but are undocumented; they are intentionally omitted here.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='execute',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def execute(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to execute exactly one trial of a Composition — pass inputs to its INPUT nodes, let the Scheduler coordinate node execution until termination conditions are met, and receive the output values.'
        return _impl(args or {})
