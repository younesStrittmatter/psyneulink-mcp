"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = '0dcd14d35661089943cfc4cb9a4f39bc0cafd2c823ca04eb04e690aaef8f1cbc'
__pnl_qualname__ = 'psyneulink.Composition.run'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'run'
TOOL_DESCRIPTION = 'Call this tool to execute a fully-wired Composition: feed inputs to its INPUT nodes, run all nodes for the specified number of trials, and get the OUTPUT node values back. Call this after building the Composition with `create_composition` and adding nodes/projections. Returns a 2D list where each inner list is the `output_values` for one OUTPUT Node, ordered as returned by `get_nodes_by_role(OUTPUT)`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clamp_input": {\n      "default": "SOFT_CLAMP",\n      "description": "How external inputs are applied to INPUT nodes across time steps within a trial. SOFT_CLAMP (default) adds the input to the node\'s output; HARD_CLAMP forces the node\'s output to equal the input; PULSE_CLAMP applies only on the first time step; NO_CLAMP does not apply the input after initialization.",\n      "enum": [\n        "SOFT_CLAMP",\n        "HARD_CLAMP",\n        "PULSE_CLAMP",\n        "NO_CLAMP"\n      ],\n      "type": "string"\n    },\n    "composition": {\n      "description": "Handle string for the Composition to run, as returned by create_composition.",\n      "type": "string"\n    },\n    "execution_mode": {\n      "default": "Python",\n      "description": "Execution backend. \'Python\' (default) uses the Python interpreter. LLVM/PTX variants use compiled modes for speed; if compilation fails, PNL falls back toward Python when the Fallback flag is set.",\n      "enum": [\n        "Python",\n        "LLVM",\n        "LLVMExec",\n        "LLVMRun",\n        "PTX",\n        "PTXExec",\n        "PTXRun"\n      ],\n      "type": "string"\n    },\n    "initialize_cycle_values": {\n      "additionalProperties": true,\n      "description": "Mapping of node handle strings to initial values for nodes in a cycle (NodeRole.CYCLE). Nodes not listed use their default values.",\n      "type": "object"\n    },\n    "inputs": {\n      "additionalProperties": true,\n      "description": "Mapping of INPUT node handle strings to lists of input values (one entry per trial). Keys are node name strings; values are lists (one element per trial, each element being the input array/value for that trial). If omitted, each INPUT node uses its default_variable for every trial.",\n      "type": "object"\n    },\n    "log": {\n      "default": false,\n      "description": "If true, sets log_condition to EXECUTION for all nodes and projections that do not already have a log condition set.",\n      "type": "boolean"\n    },\n    "num_trials": {\n      "description": "Number of trials to execute. Inferred from input list length if not specified. Use this to repeat the same inputs multiple times (pair with single-element input lists).",\n      "type": "integer"\n    },\n    "report_output": {\n      "default": "OFF",\n      "description": "Controls trial-by-trial output reporting. OFF suppresses output (default).",\n      "enum": [\n        "OFF",\n        "TERSE",\n        "FULL"\n      ],\n      "type": "string"\n    },\n    "report_params": {\n      "default": "OFF",\n      "description": "Controls whether parameter values are included in output reports.",\n      "enum": [\n        "OFF",\n        "TERSE",\n        "FULL"\n      ],\n      "type": "string"\n    },\n    "report_progress": {\n      "default": "OFF",\n      "description": "Controls real-time progress reporting during execution.",\n      "enum": [\n        "OFF",\n        "TERSE",\n        "FULL"\n      ],\n      "type": "string"\n    },\n    "reset_stateful_functions_to": {\n      "additionalProperties": true,\n      "description": "Mapping of node handle strings to seed values passed to each node\'s reset() method when its reset_stateful_function_when condition is met. If a node\'s condition is Never, it is reset once at run start.",\n      "type": "object"\n    },\n    "runtime_params": {\n      "additionalProperties": true,\n      "description": "Nested dict of temporary parameter overrides: {node_handle: {param_name: [value, condition_string]}}. Overrides apply only during this run when the condition is met.",\n      "type": "object"\n    },\n    "scheduling_mode": {\n      "description": "Sets the scheduling mode for this and all future runs. STANDARD is the default; EXACT_TIME uses absolute time conditions.",\n      "enum": [\n        "STANDARD",\n        "EXACT_TIME"\n      ],\n      "type": "string"\n    },\n    "skip_analyze_graph": {\n      "default": false,\n      "description": "If true, suppresses the _analyze_graph() call at run start. Only set true for repeated runs where graph structure has not changed, to save overhead.",\n      "type": "boolean"\n    },\n    "skip_initialization": {\n      "default": false,\n      "description": "If true, skips re-initialization from base_context at the start of the run. Rarely needed; leave false in most cases.",\n      "type": "boolean"\n    },\n    "termination_processing": {\n      "additionalProperties": true,\n      "description": "Dict mapping TimeScale strings to Condition objects that override the Composition\'s termination conditions for this run only. E.g. {\\"TRIAL\\": <Condition>}.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "composition"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `inputs` keys must be node name strings (not Python objects); the runtime resolves handles before dispatch. Values should be lists with one element per trial; a list of length 1 is reused for all trials when num_trials > 1.\n- Callable parameters (call_before_time_step, call_after_time_step, call_before_pass, call_after_pass, call_before_trial, call_after_trial) cannot be passed through the MCP tool interface and are omitted.\n- `animate` is omitted; it generates GIF files on disk and is not useful in an MCP context.\n- `scheduler` is omitted; the Composition uses its auto-generated scheduler by default.\n- The return value is the OUTPUT node values from the **last trial only**. To retrieve results across all trials, read `composition.results` via a separate tool after the run.\n- `num_trials` overrides the inferred count. If inputs lists have length 1 and num_trials is not set, only one trial runs.\n- `reset_stateful_functions_when` (a Condition or dict of Conditions) is omitted from the schema because Condition objects are not directly JSON-serializable; use reset_stateful_functions_to with nodes whose condition is Never to reset at run start.\n- `execution_mode` strings map to pnl.ExecutionMode enum members at dispatch; \'Python\' is safe universally; LLVM modes require a working LLVM/CUDA toolchain.'
TOOL_PARAMETERS = { 'properties': { 'clamp_input': { 'default': 'SOFT_CLAMP',
                                   'description': 'How external inputs are applied to '
                                                  'INPUT nodes across time steps '
                                                  'within a trial. SOFT_CLAMP '
                                                  '(default) adds the input to the '
                                                  "node's output; HARD_CLAMP forces "
                                                  "the node's output to equal the "
                                                  'input; PULSE_CLAMP applies only on '
                                                  'the first time step; NO_CLAMP does '
                                                  'not apply the input after '
                                                  'initialization.',
                                   'enum': [ 'SOFT_CLAMP',
                                             'HARD_CLAMP',
                                             'PULSE_CLAMP',
                                             'NO_CLAMP'],
                                   'type': 'string'},
                  'composition': { 'description': 'Handle string for the Composition '
                                                  'to run, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'execution_mode': { 'default': 'Python',
                                      'description': "Execution backend. 'Python' "
                                                     '(default) uses the Python '
                                                     'interpreter. LLVM/PTX variants '
                                                     'use compiled modes for speed; if '
                                                     'compilation fails, PNL falls '
                                                     'back toward Python when the '
                                                     'Fallback flag is set.',
                                      'enum': [ 'Python',
                                                'LLVM',
                                                'LLVMExec',
                                                'LLVMRun',
                                                'PTX',
                                                'PTXExec',
                                                'PTXRun'],
                                      'type': 'string'},
                  'initialize_cycle_values': { 'additionalProperties': True,
                                               'description': 'Mapping of node handle '
                                                              'strings to initial '
                                                              'values for nodes in a '
                                                              'cycle (NodeRole.CYCLE). '
                                                              'Nodes not listed use '
                                                              'their default values.',
                                               'type': 'object'},
                  'inputs': { 'additionalProperties': True,
                              'description': 'Mapping of INPUT node handle strings to '
                                             'lists of input values (one entry per '
                                             'trial). Keys are node name strings; '
                                             'values are lists (one element per trial, '
                                             'each element being the input array/value '
                                             'for that trial). If omitted, each INPUT '
                                             'node uses its default_variable for every '
                                             'trial.',
                              'type': 'object'},
                  'log': { 'default': False,
                           'description': 'If true, sets log_condition to EXECUTION '
                                          'for all nodes and projections that do not '
                                          'already have a log condition set.',
                           'type': 'boolean'},
                  'num_trials': { 'description': 'Number of trials to execute. '
                                                 'Inferred from input list length if '
                                                 'not specified. Use this to repeat '
                                                 'the same inputs multiple times (pair '
                                                 'with single-element input lists).',
                                  'type': 'integer'},
                  'report_output': { 'default': 'OFF',
                                     'description': 'Controls trial-by-trial output '
                                                    'reporting. OFF suppresses output '
                                                    '(default).',
                                     'enum': ['OFF', 'TERSE', 'FULL'],
                                     'type': 'string'},
                  'report_params': { 'default': 'OFF',
                                     'description': 'Controls whether parameter values '
                                                    'are included in output reports.',
                                     'enum': ['OFF', 'TERSE', 'FULL'],
                                     'type': 'string'},
                  'report_progress': { 'default': 'OFF',
                                       'description': 'Controls real-time progress '
                                                      'reporting during execution.',
                                       'enum': ['OFF', 'TERSE', 'FULL'],
                                       'type': 'string'},
                  'reset_stateful_functions_to': { 'additionalProperties': True,
                                                   'description': 'Mapping of node '
                                                                  'handle strings to '
                                                                  'seed values passed '
                                                                  "to each node's "
                                                                  'reset() method when '
                                                                  'its '
                                                                  'reset_stateful_function_when '
                                                                  'condition is met. '
                                                                  "If a node's "
                                                                  'condition is Never, '
                                                                  'it is reset once at '
                                                                  'run start.',
                                                   'type': 'object'},
                  'runtime_params': { 'additionalProperties': True,
                                      'description': 'Nested dict of temporary '
                                                     'parameter overrides: '
                                                     '{node_handle: {param_name: '
                                                     '[value, condition_string]}}. '
                                                     'Overrides apply only during this '
                                                     'run when the condition is met.',
                                      'type': 'object'},
                  'scheduling_mode': { 'description': 'Sets the scheduling mode for '
                                                      'this and all future runs. '
                                                      'STANDARD is the default; '
                                                      'EXACT_TIME uses absolute time '
                                                      'conditions.',
                                       'enum': ['STANDARD', 'EXACT_TIME'],
                                       'type': 'string'},
                  'skip_analyze_graph': { 'default': False,
                                          'description': 'If true, suppresses the '
                                                         '_analyze_graph() call at run '
                                                         'start. Only set true for '
                                                         'repeated runs where graph '
                                                         'structure has not changed, '
                                                         'to save overhead.',
                                          'type': 'boolean'},
                  'skip_initialization': { 'default': False,
                                           'description': 'If true, skips '
                                                          're-initialization from '
                                                          'base_context at the start '
                                                          'of the run. Rarely needed; '
                                                          'leave false in most cases.',
                                           'type': 'boolean'},
                  'termination_processing': { 'additionalProperties': True,
                                              'description': 'Dict mapping TimeScale '
                                                             'strings to Condition '
                                                             'objects that override '
                                                             "the Composition's "
                                                             'termination conditions '
                                                             'for this run only. E.g. '
                                                             '{"TRIAL": <Condition>}.',
                                              'type': 'object'}},
  'required': ['composition'],
  'type': 'object'}
TOOL_NOTES = "- `inputs` keys must be node name strings (not Python objects); the runtime resolves handles before dispatch. Values should be lists with one element per trial; a list of length 1 is reused for all trials when num_trials > 1.\n- Callable parameters (call_before_time_step, call_after_time_step, call_before_pass, call_after_pass, call_before_trial, call_after_trial) cannot be passed through the MCP tool interface and are omitted.\n- `animate` is omitted; it generates GIF files on disk and is not useful in an MCP context.\n- `scheduler` is omitted; the Composition uses its auto-generated scheduler by default.\n- The return value is the OUTPUT node values from the **last trial only**. To retrieve results across all trials, read `composition.results` via a separate tool after the run.\n- `num_trials` overrides the inferred count. If inputs lists have length 1 and num_trials is not set, only one trial runs.\n- `reset_stateful_functions_when` (a Condition or dict of Conditions) is omitted from the schema because Condition objects are not directly JSON-serializable; use reset_stateful_functions_to with nodes whose condition is Never to reset at run start.\n- `execution_mode` strings map to pnl.ExecutionMode enum members at dispatch; 'Python' is safe universally; LLVM modes require a working LLVM/CUDA toolchain."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='run',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def run(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to execute a fully-wired Composition: feed inputs to its INPUT nodes, run all nodes for the specified number of trials, and get the OUTPUT node values back.'
        return _impl(args or {})
