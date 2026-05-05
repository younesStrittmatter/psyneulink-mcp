"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e6814c4882325e730c8152949b4c82b805391b13b752617e9a2ffed8f9c19784'
__pnl_qualname__ = 'psyneulink.Report'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_report'
TOOL_DESCRIPTION = 'Use this tool to configure and activate a reporting context for a PsyNeuLink Composition execution — it controls whether trial-by-trial output, parameter values, progress bars, and simulation results are printed to the console or captured in memory. Call it before wrapping a Composition\'s `run` or `execute` call when you need visibility into execution (e.g., debugging, verifying outputs, monitoring simulations). The tool returns a singleton context object; all reporting options default to OFF, so specify at minimum `report_output` or `report_progress` to see any output.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "depth_indent_factor": {\n      "default": 2,\n      "description": "Number of spaces per nesting level used to indent output for nested Compositions and simulations when report_output=TERSE.",\n      "type": "integer"\n    },\n    "padding_indent": {\n      "default": 1,\n      "description": "Number of spaces to indent each nested rich Panel border relative to its enclosing Panel, when report_output=FULL.",\n      "type": "integer"\n    },\n    "padding_lines": {\n      "default": 1,\n      "description": "Number of blank lines below each rich Panel to separate it from the next, when report_output=FULL.",\n      "type": "integer"\n    },\n    "report_output": {\n      "default": "OFF",\n      "description": "Controls trial-by-trial output reporting. OFF suppresses all output. TERSE prints one line per node executed. FULL renders rich-formatted panels with input, output, and optionally parameters. USE_PREFS defers to each node\'s reportOutputPref setting.",\n      "enum": [\n        "OFF",\n        "TERSE",\n        "FULL",\n        "USE_PREFS"\n      ],\n      "type": "string"\n    },\n    "report_params": {\n      "default": "OFF",\n      "description": "Which parameter values to include in FULL output reports. Only relevant when report_output=FULL. MODULATED/CONTROLLED shows params being controlled; MONITORED shows params being monitored; LOGGED shows logged params; ALL shows all params.",\n      "enum": [\n        "OFF",\n        "USE_PREFS",\n        "MODULATED",\n        "CONTROLLED",\n        "MONITORED",\n        "LOGGED",\n        "ALL"\n      ],\n      "type": "string"\n    },\n    "report_progress": {\n      "default": "OFF",\n      "description": "Whether to show a rich progress bar indicating how many trials have completed out of the total during Composition execution.",\n      "enum": [\n        "OFF",\n        "ON"\n      ],\n      "type": "string"\n    },\n    "report_simulations": {\n      "default": "OFF",\n      "description": "Whether to include output and progress reporting for controller simulations (OptimizationControlMechanism). Only relevant when a Composition has a controller that runs simulations.",\n      "enum": [\n        "OFF",\n        "ON"\n      ],\n      "type": "string"\n    },\n    "report_to_devices": {\n      "default": [\n        "CONSOLE"\n      ],\n      "description": "Destinations for reporting output. CONSOLE prints to terminal. DIVERT captures output to rich_diverted_reports. RECORD captures plain-text to recorded_reports. Multiple destinations can be specified together.",\n      "items": {\n        "enum": [\n          "CONSOLE",\n          "DIVERT",\n          "RECORD",\n          "PNL_VIEW"\n        ],\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nReport is a singleton: once instantiated within an execution scope, all subsequent Report() calls in nested scopes return the same instance. The singleton is destroyed on __exit__ of the outermost context, so each top-level Composition run gets a fresh instance. The `caller` argument (a Composition or Mechanism) is required internally by the class but is supplied by the MCP host template — do not pass it. There is a discrepancy between the docstring (report_params default = USE_PREFS) and the actual __new__ signature (default = OFF); the effective default at runtime is OFF. Specifying only report_to_devices without enabling report_output or report_progress produces no visible output since _reporting_enabled will be False. DIVERT and RECORD devices capture output on the outermost Composition\'s rich_diverted_reports and recorded_reports attributes respectively — the agent must retrieve those attributes after execution to access the captured text. PNL_VIEW is listed but not yet implemented (triggers a warning).'
TOOL_PARAMETERS = { 'properties': { 'depth_indent_factor': { 'default': 2,
                                           'description': 'Number of spaces per '
                                                          'nesting level used to '
                                                          'indent output for nested '
                                                          'Compositions and '
                                                          'simulations when '
                                                          'report_output=TERSE.',
                                           'type': 'integer'},
                  'padding_indent': { 'default': 1,
                                      'description': 'Number of spaces to indent each '
                                                     'nested rich Panel border '
                                                     'relative to its enclosing Panel, '
                                                     'when report_output=FULL.',
                                      'type': 'integer'},
                  'padding_lines': { 'default': 1,
                                     'description': 'Number of blank lines below each '
                                                    'rich Panel to separate it from '
                                                    'the next, when '
                                                    'report_output=FULL.',
                                     'type': 'integer'},
                  'report_output': { 'default': 'OFF',
                                     'description': 'Controls trial-by-trial output '
                                                    'reporting. OFF suppresses all '
                                                    'output. TERSE prints one line per '
                                                    'node executed. FULL renders '
                                                    'rich-formatted panels with input, '
                                                    'output, and optionally '
                                                    'parameters. USE_PREFS defers to '
                                                    "each node's reportOutputPref "
                                                    'setting.',
                                     'enum': ['OFF', 'TERSE', 'FULL', 'USE_PREFS'],
                                     'type': 'string'},
                  'report_params': { 'default': 'OFF',
                                     'description': 'Which parameter values to include '
                                                    'in FULL output reports. Only '
                                                    'relevant when report_output=FULL. '
                                                    'MODULATED/CONTROLLED shows params '
                                                    'being controlled; MONITORED shows '
                                                    'params being monitored; LOGGED '
                                                    'shows logged params; ALL shows '
                                                    'all params.',
                                     'enum': [ 'OFF',
                                               'USE_PREFS',
                                               'MODULATED',
                                               'CONTROLLED',
                                               'MONITORED',
                                               'LOGGED',
                                               'ALL'],
                                     'type': 'string'},
                  'report_progress': { 'default': 'OFF',
                                       'description': 'Whether to show a rich progress '
                                                      'bar indicating how many trials '
                                                      'have completed out of the total '
                                                      'during Composition execution.',
                                       'enum': ['OFF', 'ON'],
                                       'type': 'string'},
                  'report_simulations': { 'default': 'OFF',
                                          'description': 'Whether to include output '
                                                         'and progress reporting for '
                                                         'controller simulations '
                                                         '(OptimizationControlMechanism). '
                                                         'Only relevant when a '
                                                         'Composition has a controller '
                                                         'that runs simulations.',
                                          'enum': ['OFF', 'ON'],
                                          'type': 'string'},
                  'report_to_devices': { 'default': ['CONSOLE'],
                                         'description': 'Destinations for reporting '
                                                        'output. CONSOLE prints to '
                                                        'terminal. DIVERT captures '
                                                        'output to '
                                                        'rich_diverted_reports. RECORD '
                                                        'captures plain-text to '
                                                        'recorded_reports. Multiple '
                                                        'destinations can be specified '
                                                        'together.',
                                         'items': { 'enum': [ 'CONSOLE',
                                                              'DIVERT',
                                                              'RECORD',
                                                              'PNL_VIEW'],
                                                    'type': 'string'},
                                         'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Report is a singleton: once instantiated within an execution scope, all subsequent Report() calls in nested scopes return the same instance. The singleton is destroyed on __exit__ of the outermost context, so each top-level Composition run gets a fresh instance. The `caller` argument (a Composition or Mechanism) is required internally by the class but is supplied by the MCP host template — do not pass it. There is a discrepancy between the docstring (report_params default = USE_PREFS) and the actual __new__ signature (default = OFF); the effective default at runtime is OFF. Specifying only report_to_devices without enabling report_output or report_progress produces no visible output since _reporting_enabled will be False. DIVERT and RECORD devices capture output on the outermost Composition's rich_diverted_reports and recorded_reports attributes respectively — the agent must retrieve those attributes after execution to access the captured text. PNL_VIEW is listed but not yet implemented (triggers a warning)."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Report
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
    def create_report(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to configure and activate a reporting context for a PsyNeuLink Composition execution — it controls whether trial-by-trial output, parameter values, progress bars, and simulation results are printed to the console or captured in memory.'
        return _impl(args or {})
