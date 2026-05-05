"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = '9767dcb39769316a528b0e66a087e14c5fca7ae1c58c98185d5d4aab2a0c5575'
__pnl_qualname__ = 'psyneulink.Composition.show_graph'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'show_graph'
TOOL_DESCRIPTION = 'Call this tool to visualize a Composition\'s graph structure — nodes, projections, nested compositions, controllers, and learning pathways. Returns a rendered graph in the specified format (PDF by default, or PNG/GIF/SVG/Jupyter). Use after assembling a Composition to inspect its topology before or after running it.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "active_items": {\n      "description": "List of node handle strings to highlight as currently active. Optional; used to visualize execution state mid-run.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "composition": {\n      "description": "Handle string returned by create_composition (or equivalent constructor). Identifies the live Composition instance whose graph will be rendered.",\n      "type": "string"\n    },\n    "output_fmt": {\n      "default": "pdf",\n      "description": "Output format for the rendered graph. \'pdf\' (default) opens in viewer; \'jupyter\' renders inline in a notebook; \'gv\' returns raw Graphviz source.",\n      "enum": [\n        "pdf",\n        "png",\n        "gif",\n        "svg",\n        "jupyter",\n        "gv"\n      ],\n      "type": "string"\n    },\n    "show_all": {\n      "default": false,\n      "description": "If true, show all nodes including those not currently active. Default false.",\n      "type": "boolean"\n    },\n    "show_cim": {\n      "default": false,\n      "description": "If true, show CompositionInterfaceMechanisms (input/output interface nodes). Default false.",\n      "type": "boolean"\n    },\n    "show_controller": {\n      "default": true,\n      "description": "If true, include the controller and its projections in the graph. Default true.",\n      "type": "boolean"\n    },\n    "show_dimensions": {\n      "default": false,\n      "description": "If true, annotate nodes and projections with their array dimensions. Default false.",\n      "type": "boolean"\n    },\n    "show_headers": {\n      "default": true,\n      "description": "If true, show header labels on nodes. Default true.",\n      "type": "boolean"\n    },\n    "show_learning": {\n      "default": false,\n      "description": "If true, include learning components (LearningMechanisms, LearningProjections) in the graph. Default false.",\n      "type": "boolean"\n    },\n    "show_nested": {\n      "default": "NESTED",\n      "description": "Controls rendering of nested Compositions. Pass \'NESTED\' (default) to show nested comps inline, or \'INSET\' to show them as collapsed boxes.",\n      "type": "string"\n    },\n    "show_nested_args": {\n      "default": "ALL",\n      "description": "Which arguments to display for nested Compositions. Pass \'ALL\' (default) to show all.",\n      "type": "string"\n    },\n    "show_node_structure": {\n      "default": false,\n      "description": "If true, expand each node to show its internal port/parameter structure. Default false.",\n      "type": "boolean"\n    },\n    "show_projection_labels": {\n      "default": false,\n      "description": "If true, label projection edges with their names. Default false.",\n      "type": "boolean"\n    },\n    "show_projections_not_in_composition": {\n      "default": false,\n      "description": "If true, also render projections that exist on nodes but are not members of this Composition. Default false.",\n      "type": "boolean"\n    },\n    "show_types": {\n      "default": false,\n      "description": "If true, display the PsyNeuLink class type of each node. Default false.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "composition"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `show_nested` and `show_nested_args` expect PsyNeuLink constant strings (\'NESTED\', \'ALL\', \'INSET\', etc.) — the runtime resolves bare class-name strings but these are not class names; pass the string literals exactly.\n- `output_fmt=\'pdf\'` silently opens a PDF viewer on the server machine; prefer \'png\' or \'gv\' in headless/agent contexts where no display is available.\n- Passing unrecognized kwargs raises a CompositionError — do not pass extra arguments.\n- This method is defined on plain Composition. AutodiffComposition has its own show_graph that additionally accepts a SHOW_PYTORCH flag; this tool explicitly rejects that flag with a CompositionError.\n- `context` is managed by the runtime and must not be passed.'
TOOL_PARAMETERS = { 'properties': { 'active_items': { 'description': 'List of node handle strings to '
                                                   'highlight as currently active. '
                                                   'Optional; used to visualize '
                                                   'execution state mid-run.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'composition': { 'description': 'Handle string returned by '
                                                  'create_composition (or equivalent '
                                                  'constructor). Identifies the live '
                                                  'Composition instance whose graph '
                                                  'will be rendered.',
                                   'type': 'string'},
                  'output_fmt': { 'default': 'pdf',
                                  'description': 'Output format for the rendered '
                                                 "graph. 'pdf' (default) opens in "
                                                 "viewer; 'jupyter' renders inline in "
                                                 "a notebook; 'gv' returns raw "
                                                 'Graphviz source.',
                                  'enum': ['pdf', 'png', 'gif', 'svg', 'jupyter', 'gv'],
                                  'type': 'string'},
                  'show_all': { 'default': False,
                                'description': 'If true, show all nodes including '
                                               'those not currently active. Default '
                                               'false.',
                                'type': 'boolean'},
                  'show_cim': { 'default': False,
                                'description': 'If true, show '
                                               'CompositionInterfaceMechanisms '
                                               '(input/output interface nodes). '
                                               'Default false.',
                                'type': 'boolean'},
                  'show_controller': { 'default': True,
                                       'description': 'If true, include the controller '
                                                      'and its projections in the '
                                                      'graph. Default true.',
                                       'type': 'boolean'},
                  'show_dimensions': { 'default': False,
                                       'description': 'If true, annotate nodes and '
                                                      'projections with their array '
                                                      'dimensions. Default false.',
                                       'type': 'boolean'},
                  'show_headers': { 'default': True,
                                    'description': 'If true, show header labels on '
                                                   'nodes. Default true.',
                                    'type': 'boolean'},
                  'show_learning': { 'default': False,
                                     'description': 'If true, include learning '
                                                    'components (LearningMechanisms, '
                                                    'LearningProjections) in the '
                                                    'graph. Default false.',
                                     'type': 'boolean'},
                  'show_nested': { 'default': 'NESTED',
                                   'description': 'Controls rendering of nested '
                                                  "Compositions. Pass 'NESTED' "
                                                  '(default) to show nested comps '
                                                  "inline, or 'INSET' to show them as "
                                                  'collapsed boxes.',
                                   'type': 'string'},
                  'show_nested_args': { 'default': 'ALL',
                                        'description': 'Which arguments to display for '
                                                       'nested Compositions. Pass '
                                                       "'ALL' (default) to show all.",
                                        'type': 'string'},
                  'show_node_structure': { 'default': False,
                                           'description': 'If true, expand each node '
                                                          'to show its internal '
                                                          'port/parameter structure. '
                                                          'Default false.',
                                           'type': 'boolean'},
                  'show_projection_labels': { 'default': False,
                                              'description': 'If true, label '
                                                             'projection edges with '
                                                             'their names. Default '
                                                             'false.',
                                              'type': 'boolean'},
                  'show_projections_not_in_composition': { 'default': False,
                                                           'description': 'If true, '
                                                                          'also render '
                                                                          'projections '
                                                                          'that exist '
                                                                          'on nodes '
                                                                          'but are not '
                                                                          'members of '
                                                                          'this '
                                                                          'Composition. '
                                                                          'Default '
                                                                          'false.',
                                                           'type': 'boolean'},
                  'show_types': { 'default': False,
                                  'description': 'If true, display the PsyNeuLink '
                                                 'class type of each node. Default '
                                                 'false.',
                                  'type': 'boolean'}},
  'required': ['composition'],
  'type': 'object'}
TOOL_NOTES = "- `show_nested` and `show_nested_args` expect PsyNeuLink constant strings ('NESTED', 'ALL', 'INSET', etc.) — the runtime resolves bare class-name strings but these are not class names; pass the string literals exactly.\n- `output_fmt='pdf'` silently opens a PDF viewer on the server machine; prefer 'png' or 'gv' in headless/agent contexts where no display is available.\n- Passing unrecognized kwargs raises a CompositionError — do not pass extra arguments.\n- This method is defined on plain Composition. AutodiffComposition has its own show_graph that additionally accepts a SHOW_PYTORCH flag; this tool explicitly rejects that flag with a CompositionError.\n- `context` is managed by the runtime and must not be passed."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='show_graph',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def show_graph(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to visualize a Composition's graph structure — nodes, projections, nested compositions, controllers, and learning pathways."
        return _impl(args or {})
