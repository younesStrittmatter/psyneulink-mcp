"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'de7ba1d8b39bb1daaed8d5f6763a0e3cad134dcf6840808b120324d4d0bf1f53'
__pnl_qualname__ = 'psyneulink.Composition.add_controller'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_controller'
TOOL_DESCRIPTION = 'Call this tool after creating both a Composition and a ControlMechanism (or OptimizationControlMechanism) to assign the ControlMechanism as the Composition\'s controller. This wires up control signals, control projections to parameter ports, and enables the controller for execution — including simulation-based optimization if the controller supports it. Returns no value; the Composition is mutated in place.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the Composition instance (returned by create_composition or equivalent constructor). The ControlMechanism will be assigned as its controller.",\n      "type": "string"\n    },\n    "controller": {\n      "description": "Handle string for a ControlMechanism (or subclass such as OptimizationControlMechanism) to assign as the Composition\'s controller. Must be a ControlMechanism instance \\u2014 other types raise CompositionError.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "controller"\n  ],\n  "type": "object"\n}\n\nNotes:\n- If the controller is already assigned to a different Composition, the assignment is silently ignored (a Python warning is emitted but no exception is raised).\n- If the controller is already this Composition\'s controller, the call is a no-op with a warning.\n- Assigning a new controller replaces any existing one (projections for the old controller are removed) with a warning.\n- Sets `enable_controller = True` on the Composition unconditionally upon successful assignment.\n- An OptimizationControlMechanism in DEFERRED_INIT state (e.g., constructed inline as the `controller` arg of the Composition) will have its initialization completed here using the Composition as its `agent_rep`.\n- If the controller\'s aux components reference Nodes/Projections not yet in the Composition, initialization is deferred (`_controller_initialization_status = DEFERRED_INIT`) and the method returns early without fully wiring the controller — add the missing nodes first and then call add_controller again.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the Composition '
                                                  'instance (returned by '
                                                  'create_composition or equivalent '
                                                  'constructor). The ControlMechanism '
                                                  'will be assigned as its controller.',
                                   'type': 'string'},
                  'controller': { 'description': 'Handle string for a ControlMechanism '
                                                 '(or subclass such as '
                                                 'OptimizationControlMechanism) to '
                                                 "assign as the Composition's "
                                                 'controller. Must be a '
                                                 'ControlMechanism instance — other '
                                                 'types raise CompositionError.',
                                  'type': 'string'}},
  'required': ['composition', 'controller'],
  'type': 'object'}
TOOL_NOTES = "- If the controller is already assigned to a different Composition, the assignment is silently ignored (a Python warning is emitted but no exception is raised).\n- If the controller is already this Composition's controller, the call is a no-op with a warning.\n- Assigning a new controller replaces any existing one (projections for the old controller are removed) with a warning.\n- Sets `enable_controller = True` on the Composition unconditionally upon successful assignment.\n- An OptimizationControlMechanism in DEFERRED_INIT state (e.g., constructed inline as the `controller` arg of the Composition) will have its initialization completed here using the Composition as its `agent_rep`.\n- If the controller's aux components reference Nodes/Projections not yet in the Composition, initialization is deferred (`_controller_initialization_status = DEFERRED_INIT`) and the method returns early without fully wiring the controller — add the missing nodes first and then call add_controller again."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_controller',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_controller(args: dict[str, Any] | None = None) -> Any:
        "Call this tool after creating both a Composition and a ControlMechanism (or OptimizationControlMechanism) to assign the ControlMechanism as the Composition's controller."
        return _impl(args or {})
