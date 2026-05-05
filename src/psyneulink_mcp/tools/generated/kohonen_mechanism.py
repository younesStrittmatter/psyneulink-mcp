"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a07d94bafedbb8764c1e9046dd5e1e1ce0945a412f98352a2a0abc9ec8ba261f'
__pnl_qualname__ = 'psyneulink.KohonenMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_kohonen_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a KohonenMechanism — a self-organizing map (SOM) node that learns an unsupervised topographic representation of its input via Kohonen learning. Use it when building a Composition that needs competitive, unsupervised learning where nearby units should respond to similar inputs. The result is a KohonenMechanism instance with RESULT and INPUT_PATTERN output ports and an auto-created LearningMechanism if learning is enabled.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "Minimum and maximum values for output: [min, max].",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "default_variable": {\n      "description": "Default input value; determines input dimensionality.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "Whether to configure the mechanism for learning at construction time. Default True. If False, call configure_learning() later before learning can occur.",\n      "type": "boolean"\n    },\n    "function": {\n      "description": "Transfer function applied to input (e.g. \'Linear\', \'Logistic\'). Defaults to Linear inherited from TransferMechanism.",\n      "type": "string"\n    },\n    "input_shapes": {\n      "description": "Convenience alternative to default_variable: integer specifying the size of the input vector.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "description": "Rate of integration when integrator_mode is True (0-1).",\n      "type": "number"\n    },\n    "integrator_mode": {\n      "description": "If True, input is integrated over time before applying the transfer function.",\n      "type": "boolean"\n    },\n    "learned_projection": {\n      "description": "Specific MappingProjection to train. If omitted, defaults to the first afferent projection to the primary InputPort.",\n      "type": "string"\n    },\n    "learning_function": {\n      "description": "Learning function used to update the afferent MappingProjection matrix. Default is Kohonen(distance_function=GAUSSIAN). Pass as a string name or constructed LearningFunction.",\n      "type": "string"\n    },\n    "learning_rate": {\n      "description": "Learning rate for the Kohonen learning function. If None (default), uses the LearningMechanism system default.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Name for the mechanism; auto-generated if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Noise added to input before applying the transfer function.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- Learning setup requires an afferent MappingProjection to exist before the mechanism is added to a Composition; if enable_learning=True but no projection exists yet, learning configuration is deferred until one is added.\n- The docstring says default learning_rate is False but the signature default is None — treat None as "use system default".\n- Two output ports are always present: RESULT (transfer function output) and INPUT_PATTERN (raw input, fed to the LearningMechanism).\n- The docstring contains a typo: "GUASSIAN" in the learning_function description; the actual default is GAUSSIAN.\n- enable_learning=True at construction auto-creates a KohonenLearningMechanism, a LearningProjection, and two error MappingProjections — expect these extra components in the Composition graph.\n- learning_enabled can be toggled after construction; setting it to True without a configured LearningMechanism raises a warning and is silently ignored.\n- matrix attribute is shared with the learned_projection\'s parameter port — modifying it updates the projection weight matrix directly.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': 'Minimum and maximum values for output: '
                                           '[min, max].',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'default_variable': { 'description': 'Default input value; '
                                                       'determines input '
                                                       'dimensionality.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'enable_learning': { 'default': True,
                                       'description': 'Whether to configure the '
                                                      'mechanism for learning at '
                                                      'construction time. Default '
                                                      'True. If False, call '
                                                      'configure_learning() later '
                                                      'before learning can occur.',
                                       'type': 'boolean'},
                  'function': { 'description': 'Transfer function applied to input '
                                               "(e.g. 'Linear', 'Logistic'). Defaults "
                                               'to Linear inherited from '
                                               'TransferMechanism.',
                                'type': 'string'},
                  'input_shapes': { 'description': 'Convenience alternative to '
                                                   'default_variable: integer '
                                                   'specifying the size of the input '
                                                   'vector.',
                                    'type': 'integer'},
                  'integration_rate': { 'description': 'Rate of integration when '
                                                       'integrator_mode is True (0-1).',
                                        'type': 'number'},
                  'integrator_mode': { 'description': 'If True, input is integrated '
                                                      'over time before applying the '
                                                      'transfer function.',
                                       'type': 'boolean'},
                  'learned_projection': { 'description': 'Specific MappingProjection '
                                                         'to train. If omitted, '
                                                         'defaults to the first '
                                                         'afferent projection to the '
                                                         'primary InputPort.',
                                          'type': 'string'},
                  'learning_function': { 'description': 'Learning function used to '
                                                        'update the afferent '
                                                        'MappingProjection matrix. '
                                                        'Default is '
                                                        'Kohonen(distance_function=GAUSSIAN). '
                                                        'Pass as a string name or '
                                                        'constructed LearningFunction.',
                                         'type': 'string'},
                  'learning_rate': { 'description': 'Learning rate for the Kohonen '
                                                    'learning function. If None '
                                                    '(default), uses the '
                                                    'LearningMechanism system default.',
                                     'type': 'number'},
                  'name': { 'description': 'Name for the mechanism; auto-generated if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'description': 'Noise added to input before applying the '
                                            'transfer function.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- Learning setup requires an afferent MappingProjection to exist before the mechanism is added to a Composition; if enable_learning=True but no projection exists yet, learning configuration is deferred until one is added.\n- The docstring says default learning_rate is False but the signature default is None — treat None as "use system default".\n- Two output ports are always present: RESULT (transfer function output) and INPUT_PATTERN (raw input, fed to the LearningMechanism).\n- The docstring contains a typo: "GUASSIAN" in the learning_function description; the actual default is GAUSSIAN.\n- enable_learning=True at construction auto-creates a KohonenLearningMechanism, a LearningProjection, and two error MappingProjections — expect these extra components in the Composition graph.\n- learning_enabled can be toggled after construction; setting it to True without a configured LearningMechanism raises a warning and is silently ignored.\n- matrix attribute is shared with the learned_projection\'s parameter port — modifying it updates the projection weight matrix directly.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.KohonenMechanism
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
    def create_kohonen_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a KohonenMechanism — a self-organizing map (SOM) node that learns an unsupervised topographic representation of its input via Kohonen learning.'
        return _impl(args or {})
