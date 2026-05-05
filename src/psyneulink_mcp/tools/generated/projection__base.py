"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'fce394c4df2c00bce7b22eb27a7116cda1a29d312a53900a71b21de49f835f42'
__pnl_qualname__ = 'psyneulink.Projection_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_projection__base'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — Projection_Base is an abstract base class that raises an error on direct instantiation. Call it only as a reference when you need to understand shared Projection attributes/parameters; for actual projection creation, use MappingProjection, ControlProjection, or GatingProjection instead. If you encounter a Projection_Base instance already attached to a Composition, its sender/receiver/function/weight/exponent attributes describe the data-flow edge.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "exclude_in_autodiff": {\n      "default": false,\n      "description": "If true, excludes this Projection from AutodiffComposition gradient calculations.",\n      "type": "boolean"\n    },\n    "exponent": {\n      "description": "Scalar exponent applied to this Projection\'s output value before weight multiplication and before combining with other Projections at the receiver Port.",\n      "type": "number"\n    },\n    "feedback": {\n      "description": "Whether to force this Projection to be treated as a feedback edge in a Composition cycle. True forces feedback assignment; False precludes it; omit to let the Composition decide.",\n      "type": "boolean"\n    },\n    "function": {\n      "default": "MatrixTransform",\n      "description": "TransferFunction used to convert the sender Port value to the receiver Port variable. Defaults to MatrixTransform.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for this Projection. If not specified, a default name is assigned by the subclass. Duplicate names are disambiguated with an indexed suffix.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name of the InputPort or Mechanism that is the destination of this Projection\'s output. If a Mechanism name is given, its primary InputPort is used. May be omitted for deferred initialization.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name of the OutputPort or Mechanism that is the source of this Projection\'s input. If a Mechanism name is given, its primary OutputPort is used. May be omitted for deferred initialization.",\n      "type": "string"\n    },\n    "weight": {\n      "description": "Scalar multiplier applied to this Projection\'s output value after exponentiation, before combining with other Projections at the receiver Port.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nProjection_Base is decorated with @abc.abstractmethod on __init__ — instantiating it directly will fail. Always use a concrete subclass (MappingProjection, ControlProjection, GatingProjection, LearningProjection, ModulatoryProjection). The `feedback` parameter accepts True, False, or the string keyword "FEEDBACK"; None (default) delegates the decision to the Composition. When sender or receiver is a Mechanism (not a Port), PNL silently redirects to the primary OutputPort or InputPort respectively — if a Mechanism has multiple InputPorts, assignment goes to the first one with a verbose warning. weight and exponent default to None (not 1/0), meaning they have no effect unless explicitly set. Duplicate Projections between the same sender and receiver raise DuplicateProjectionError rather than silently succeeding.'
TOOL_PARAMETERS = { 'properties': { 'exclude_in_autodiff': { 'default': False,
                                           'description': 'If true, excludes this '
                                                          'Projection from '
                                                          'AutodiffComposition '
                                                          'gradient calculations.',
                                           'type': 'boolean'},
                  'exponent': { 'description': 'Scalar exponent applied to this '
                                               "Projection's output value before "
                                               'weight multiplication and before '
                                               'combining with other Projections at '
                                               'the receiver Port.',
                                'type': 'number'},
                  'feedback': { 'description': 'Whether to force this Projection to be '
                                               'treated as a feedback edge in a '
                                               'Composition cycle. True forces '
                                               'feedback assignment; False precludes '
                                               'it; omit to let the Composition '
                                               'decide.',
                                'type': 'boolean'},
                  'function': { 'default': 'MatrixTransform',
                                'description': 'TransferFunction used to convert the '
                                               'sender Port value to the receiver Port '
                                               'variable. Defaults to MatrixTransform.',
                                'type': 'string'},
                  'name': { 'description': 'Name for this Projection. If not '
                                           'specified, a default name is assigned by '
                                           'the subclass. Duplicate names are '
                                           'disambiguated with an indexed suffix.',
                            'type': 'string'},
                  'receiver': { 'description': 'Name of the InputPort or Mechanism '
                                               'that is the destination of this '
                                               "Projection's output. If a Mechanism "
                                               'name is given, its primary InputPort '
                                               'is used. May be omitted for deferred '
                                               'initialization.',
                                'type': 'string'},
                  'sender': { 'description': 'Name of the OutputPort or Mechanism that '
                                             "is the source of this Projection's "
                                             'input. If a Mechanism name is given, its '
                                             'primary OutputPort is used. May be '
                                             'omitted for deferred initialization.',
                              'type': 'string'},
                  'weight': { 'description': 'Scalar multiplier applied to this '
                                             "Projection's output value after "
                                             'exponentiation, before combining with '
                                             'other Projections at the receiver Port.',
                              'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Projection_Base is decorated with @abc.abstractmethod on __init__ — instantiating it directly will fail. Always use a concrete subclass (MappingProjection, ControlProjection, GatingProjection, LearningProjection, ModulatoryProjection). The `feedback` parameter accepts True, False, or the string keyword "FEEDBACK"; None (default) delegates the decision to the Composition. When sender or receiver is a Mechanism (not a Port), PNL silently redirects to the primary OutputPort or InputPort respectively — if a Mechanism has multiple InputPorts, assignment goes to the first one with a verbose warning. weight and exponent default to None (not 1/0), meaning they have no effect unless explicitly set. Duplicate Projections between the same sender and receiver raise DuplicateProjectionError rather than silently succeeding.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Projection_Base
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
    def create_projection__base(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — Projection_Base is an abstract base class that raises an error on direct instantiation.'
        return _impl(args or {})
