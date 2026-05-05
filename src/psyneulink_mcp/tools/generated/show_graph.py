"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c4cc44b09853a6172f20994f5a324e9ad9116c9c3472848e7bb713e2dd7f80dc'
__pnl_qualname__ = 'psyneulink.ShowGraph'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_show_graph'
TOOL_DESCRIPTION = 'Call this tool to configure the visual styling defaults for PsyNeuLink Composition graph displays — node shapes, colors, and line widths. Use it when you want to customize how a Composition\'s graph looks before calling show_graph() on the Composition object. The tool instantiates a ShowGraph object whose properties control rendering aesthetics; actual graph output is produced by calling show_graph() on the Composition (which delegates to its attached ShowGraph instance).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "active_color": {\n      "default": "BOLD",\n      "description": "How to highlight active_items in a show_graph call. Use \'BOLD\' to thicken the border, or any GraphViz color name to recolor.",\n      "type": "string"\n    },\n    "active_thicker_by": {\n      "default": 2,\n      "description": "Amount added to default_width for items listed in active_items.",\n      "type": "integer"\n    },\n    "agent_rep_shape": {\n      "default": "egg",\n      "description": "GraphViz shape for the agent_rep of an OptimizationControlMechanism.",\n      "type": "string"\n    },\n    "bold_width": {\n      "default": 3,\n      "description": "Stroke width for INPUT and OUTPUT node outlines.",\n      "type": "integer"\n    },\n    "cim_shape": {\n      "default": "rectangle",\n      "description": "GraphViz shape for CompositionInterfaceMechanism (CIM) nodes.",\n      "type": "string"\n    },\n    "composition_color": {\n      "default": "pink",\n      "description": "Color for nested Composition nodes displayed as collapsed boxes.",\n      "type": "string"\n    },\n    "composition_shape": {\n      "default": "rectangle",\n      "description": "GraphViz shape for nested Composition nodes when show_nested is False or nesting exceeds the specified level.",\n      "type": "string"\n    },\n    "control_color": {\n      "default": "blue",\n      "description": "Color for ControlMechanisms (other than the Composition controller) and ControlProjections.",\n      "type": "string"\n    },\n    "control_projection_arrow": {\n      "default": "box",\n      "description": "GraphViz arrowhead style for the head of ControlProjection edges.",\n      "type": "string"\n    },\n    "controller_color": {\n      "default": "purple",\n      "description": "Color for the Composition\'s controller and its projections.",\n      "type": "string"\n    },\n    "controller_shape": {\n      "default": "doubleoctagon",\n      "description": "GraphViz shape for a Composition\'s controller node.",\n      "type": "string"\n    },\n    "cycle_shape": {\n      "default": "doublecircle",\n      "description": "GraphViz shape for nodes with NodeRole CYCLE.",\n      "type": "string"\n    },\n    "default_node_color": {\n      "default": "black",\n      "description": "Color for nodes not assigned any other role-based color. Must be a GraphViz-recognized color name.",\n      "type": "string"\n    },\n    "default_projection_arrow": {\n      "default": "normal",\n      "description": "GraphViz arrowhead style for MappingProjection edges.",\n      "type": "string"\n    },\n    "default_width": {\n      "default": 1,\n      "description": "Stroke width (in GraphViz pen units) for node outlines and projection arrow bodies.",\n      "type": "integer"\n    },\n    "direction": {\n      "default": "BT",\n      "description": "Orientation of the graph flow (input -> output). \'BT\'=bottom-to-top, \'TB\'=top-to-bottom, \'LR\'=left-to-right, \'RL\'=right-to-left.",\n      "enum": [\n        "BT",\n        "TB",\n        "LR",\n        "RL"\n      ],\n      "type": "string"\n    },\n    "feedback_shape": {\n      "default": "octagon",\n      "description": "GraphViz shape for nodes with NodeRole FEEDBACK_SENDER.",\n      "type": "string"\n    },\n    "inactive_projection_color": {\n      "default": "red",\n      "description": "Color for Projections not active in the current Composition, shown when show_projections_not_in_composition is True.",\n      "type": "string"\n    },\n    "input_and_output_color": {\n      "default": "brown",\n      "description": "Color for nodes that are both INPUT and OUTPUT.",\n      "type": "string"\n    },\n    "input_color": {\n      "default": "green",\n      "description": "Color for INPUT nodes.",\n      "type": "string"\n    },\n    "learning_color": {\n      "default": "orange",\n      "description": "Color for learning components (LearningMechanisms, LearningProjections).",\n      "type": "string"\n    },\n    "learning_projection_shape": {\n      "default": "diamond",\n      "description": "GraphViz shape for LearningProjection nodes.",\n      "type": "string"\n    },\n    "mechanism_shape": {\n      "default": "oval",\n      "description": "GraphViz shape for ordinary Mechanism nodes (those without a special NodeRole).",\n      "type": "string"\n    },\n    "output_color": {\n      "default": "red",\n      "description": "Color for OUTPUT nodes.",\n      "type": "string"\n    },\n    "probe_color": {\n      "default": "pink",\n      "description": "Color for PROBE nodes.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The `composition` argument is required by the constructor but is injected internally by PsyNeuLink when it assigns a ShowGraph to a Composition — do not pass it.\n- This tool configures styling *defaults* only. Content-control arguments (show_nested, show_controller, show_learning, show_node_structure, output_fmt, active_items, etc.) belong in the separate show_graph() call on the Composition object.\n- Docstring says feedback_shape default is \'septagon\', but the actual source default is \'octagon\' — use \'octagon\' unless you want septagon explicitly.\n- Docstring says cim_shape default is \'square\', but source defaults to \'rectangle\' — use \'rectangle\' to match runtime behavior.\n- active_color accepts the special string \'BOLD\' (a PsyNeuLink keyword) or any GraphViz color name. \'BOLD\' thickens the border rather than changing color.\n- Rendering requires both the graphviz Python package and the graphviz system binary. If the system binary is missing, show_graph raises ShowGraphError with an installation message.\n- All shape strings must be valid GraphViz node shape names (e.g. \'oval\', \'rectangle\', \'doublecircle\'); invalid values will cause GraphViz errors at render time, not at instantiation.\n- Width parameters are integers representing GraphViz penwidth units, not pixels.'
TOOL_PARAMETERS = { 'properties': { 'active_color': { 'default': 'BOLD',
                                    'description': 'How to highlight active_items in a '
                                                   "show_graph call. Use 'BOLD' to "
                                                   'thicken the border, or any '
                                                   'GraphViz color name to recolor.',
                                    'type': 'string'},
                  'active_thicker_by': { 'default': 2,
                                         'description': 'Amount added to default_width '
                                                        'for items listed in '
                                                        'active_items.',
                                         'type': 'integer'},
                  'agent_rep_shape': { 'default': 'egg',
                                       'description': 'GraphViz shape for the '
                                                      'agent_rep of an '
                                                      'OptimizationControlMechanism.',
                                       'type': 'string'},
                  'bold_width': { 'default': 3,
                                  'description': 'Stroke width for INPUT and OUTPUT '
                                                 'node outlines.',
                                  'type': 'integer'},
                  'cim_shape': { 'default': 'rectangle',
                                 'description': 'GraphViz shape for '
                                                'CompositionInterfaceMechanism (CIM) '
                                                'nodes.',
                                 'type': 'string'},
                  'composition_color': { 'default': 'pink',
                                         'description': 'Color for nested Composition '
                                                        'nodes displayed as collapsed '
                                                        'boxes.',
                                         'type': 'string'},
                  'composition_shape': { 'default': 'rectangle',
                                         'description': 'GraphViz shape for nested '
                                                        'Composition nodes when '
                                                        'show_nested is False or '
                                                        'nesting exceeds the specified '
                                                        'level.',
                                         'type': 'string'},
                  'control_color': { 'default': 'blue',
                                     'description': 'Color for ControlMechanisms '
                                                    '(other than the Composition '
                                                    'controller) and '
                                                    'ControlProjections.',
                                     'type': 'string'},
                  'control_projection_arrow': { 'default': 'box',
                                                'description': 'GraphViz arrowhead '
                                                               'style for the head of '
                                                               'ControlProjection '
                                                               'edges.',
                                                'type': 'string'},
                  'controller_color': { 'default': 'purple',
                                        'description': "Color for the Composition's "
                                                       'controller and its '
                                                       'projections.',
                                        'type': 'string'},
                  'controller_shape': { 'default': 'doubleoctagon',
                                        'description': 'GraphViz shape for a '
                                                       "Composition's controller node.",
                                        'type': 'string'},
                  'cycle_shape': { 'default': 'doublecircle',
                                   'description': 'GraphViz shape for nodes with '
                                                  'NodeRole CYCLE.',
                                   'type': 'string'},
                  'default_node_color': { 'default': 'black',
                                          'description': 'Color for nodes not assigned '
                                                         'any other role-based color. '
                                                         'Must be a '
                                                         'GraphViz-recognized color '
                                                         'name.',
                                          'type': 'string'},
                  'default_projection_arrow': { 'default': 'normal',
                                                'description': 'GraphViz arrowhead '
                                                               'style for '
                                                               'MappingProjection '
                                                               'edges.',
                                                'type': 'string'},
                  'default_width': { 'default': 1,
                                     'description': 'Stroke width (in GraphViz pen '
                                                    'units) for node outlines and '
                                                    'projection arrow bodies.',
                                     'type': 'integer'},
                  'direction': { 'default': 'BT',
                                 'description': 'Orientation of the graph flow (input '
                                                "-> output). 'BT'=bottom-to-top, "
                                                "'TB'=top-to-bottom, "
                                                "'LR'=left-to-right, "
                                                "'RL'=right-to-left.",
                                 'enum': ['BT', 'TB', 'LR', 'RL'],
                                 'type': 'string'},
                  'feedback_shape': { 'default': 'octagon',
                                      'description': 'GraphViz shape for nodes with '
                                                     'NodeRole FEEDBACK_SENDER.',
                                      'type': 'string'},
                  'inactive_projection_color': { 'default': 'red',
                                                 'description': 'Color for Projections '
                                                                'not active in the '
                                                                'current Composition, '
                                                                'shown when '
                                                                'show_projections_not_in_composition '
                                                                'is True.',
                                                 'type': 'string'},
                  'input_and_output_color': { 'default': 'brown',
                                              'description': 'Color for nodes that are '
                                                             'both INPUT and OUTPUT.',
                                              'type': 'string'},
                  'input_color': { 'default': 'green',
                                   'description': 'Color for INPUT nodes.',
                                   'type': 'string'},
                  'learning_color': { 'default': 'orange',
                                      'description': 'Color for learning components '
                                                     '(LearningMechanisms, '
                                                     'LearningProjections).',
                                      'type': 'string'},
                  'learning_projection_shape': { 'default': 'diamond',
                                                 'description': 'GraphViz shape for '
                                                                'LearningProjection '
                                                                'nodes.',
                                                 'type': 'string'},
                  'mechanism_shape': { 'default': 'oval',
                                       'description': 'GraphViz shape for ordinary '
                                                      'Mechanism nodes (those without '
                                                      'a special NodeRole).',
                                       'type': 'string'},
                  'output_color': { 'default': 'red',
                                    'description': 'Color for OUTPUT nodes.',
                                    'type': 'string'},
                  'probe_color': { 'default': 'pink',
                                   'description': 'Color for PROBE nodes.',
                                   'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- The `composition` argument is required by the constructor but is injected internally by PsyNeuLink when it assigns a ShowGraph to a Composition — do not pass it.\n- This tool configures styling *defaults* only. Content-control arguments (show_nested, show_controller, show_learning, show_node_structure, output_fmt, active_items, etc.) belong in the separate show_graph() call on the Composition object.\n- Docstring says feedback_shape default is 'septagon', but the actual source default is 'octagon' — use 'octagon' unless you want septagon explicitly.\n- Docstring says cim_shape default is 'square', but source defaults to 'rectangle' — use 'rectangle' to match runtime behavior.\n- active_color accepts the special string 'BOLD' (a PsyNeuLink keyword) or any GraphViz color name. 'BOLD' thickens the border rather than changing color.\n- Rendering requires both the graphviz Python package and the graphviz system binary. If the system binary is missing, show_graph raises ShowGraphError with an installation message.\n- All shape strings must be valid GraphViz node shape names (e.g. 'oval', 'rectangle', 'doublecircle'); invalid values will cause GraphViz errors at render time, not at instantiation.\n- Width parameters are integers representing GraphViz penwidth units, not pixels."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ShowGraph
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
    def create_show_graph(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to configure the visual styling defaults for PsyNeuLink Composition graph displays — node shapes, colors, and line widths.'
        return _impl(args or {})
