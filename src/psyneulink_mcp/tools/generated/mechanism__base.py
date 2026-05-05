"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '91d72ef88b0cb638b5895df2f04ed7f449ce951198c10e44c22558b699e8bf21'
__pnl_qualname__ = 'psyneulink.Mechanism_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_mechanism__base'
TOOL_DESCRIPTION = 'Call this tool to understand the shared constructor interface for all PsyNeuLink Mechanism subclasses — do NOT call it directly to create a mechanism, as Mechanism_Base is abstract. Use it as a reference when the desired subclass tool is unavailable, or to understand common parameters (default_variable, input_shapes, input_ports, function, output_ports) that every Mechanism accepts. The result would be a configured Mechanism instance if instantiated via a concrete subclass.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the Mechanism\'s input; sets the shape of its InputPorts and function variable. Provide a number for a scalar input, a 1D list/array for a vector, or a 2D list/array to define multiple InputPorts (one per row). Subclass default is [[0]] if omitted.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "function": {\n      "description": "The computation function applied to the Mechanism\'s variable. Can be a PsyNeuLink Function instance/class (e.g., Linear, Logistic) or a UserDefinedFunction. Defaults to Linear. Its output shape determines the primary OutputPort shape.",\n      "type": "string"\n    },\n    "input_labels": {\n      "description": "Dict mapping string labels to numeric input values, enabling symbolic inputs. Entries are label:value pairs, or sub-dicts keyed by InputPort name/index for multi-port labeling.",\n      "type": "object"\n    },\n    "input_ports": {\n      "description": "Specification for one or more InputPorts. Can be a port name string, a list of names/dicts/specs, or a dict. If omitted, a single InputPort is created from default_variable. Number of ports must match the first axis of default_variable if both are specified.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "type": "array"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    },\n    "input_shapes": {\n      "description": "Alternative to default_variable: specify input size as an integer (single InputPort of that length) or a list of ints/tuples (one per InputPort). Ignored if default_variable is also provided and they are compatible; raises an error if they conflict.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for the Mechanism. If omitted, a default is assigned by MechanismRegistry using the subclass name plus an index suffix for duplicates.",\n      "type": "string"\n    },\n    "output_labels": {\n      "description": "Dict mapping string labels to numeric output values for reporting. Same structure as input_labels but applied to OutputPorts.",\n      "type": "object"\n    },\n    "output_ports": {\n      "description": "Specification for one or more OutputPorts. Can be a name string, a list of names/dicts, or a standard output port name (e.g., \'RESULT\', \'OWNER_VALUE\'). If omitted, a single OutputPort is created from the first item of the Mechanism\'s value.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "type": "array"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    },\n    "prefs": {\n      "description": "PreferenceSet or specification dict for the Mechanism\'s preferences (e.g., verbosity, logging). Rarely needed; omit to use class defaults.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMechanism_Base is abstract and cannot be instantiated directly — always use a concrete subclass (TransferMechanism, LCAMechanism, DDM, etc.). The variable is always stored internally as a 2D numpy array; scalars become [[value]]. Specifying both default_variable and input_shapes is allowed only if they describe the same shape, otherwise a MechanismError is raised. The function parameter here is typed as string for JSON Schema compatibility, but at the Python level it should be a PsyNeuLink Function instance or class — pass the name of the function (e.g., "Linear", "Logistic") and expect the generated template to resolve it. Standard output port names that can be passed in output_ports: "RESULT" (axis-0 slice of value), "OWNER_VALUE" / "MECHANISM_VALUE" (full value array). ParameterPorts cannot be added or removed after construction. Removing InputPorts after construction changes variable shape and may break the function.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': "Template for the Mechanism's "
                                                       'input; sets the shape of its '
                                                       'InputPorts and function '
                                                       'variable. Provide a number for '
                                                       'a scalar input, a 1D '
                                                       'list/array for a vector, or a '
                                                       '2D list/array to define '
                                                       'multiple InputPorts (one per '
                                                       'row). Subclass default is '
                                                       '[[0]] if omitted.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'},
                                                   { 'items': { 'items': { 'type': 'number'},
                                                                'type': 'array'},
                                                     'type': 'array'}]},
                  'function': { 'description': 'The computation function applied to '
                                               "the Mechanism's variable. Can be a "
                                               'PsyNeuLink Function instance/class '
                                               '(e.g., Linear, Logistic) or a '
                                               'UserDefinedFunction. Defaults to '
                                               'Linear. Its output shape determines '
                                               'the primary OutputPort shape.',
                                'type': 'string'},
                  'input_labels': { 'description': 'Dict mapping string labels to '
                                                   'numeric input values, enabling '
                                                   'symbolic inputs. Entries are '
                                                   'label:value pairs, or sub-dicts '
                                                   'keyed by InputPort name/index for '
                                                   'multi-port labeling.',
                                    'type': 'object'},
                  'input_ports': { 'description': 'Specification for one or more '
                                                  'InputPorts. Can be a port name '
                                                  'string, a list of '
                                                  'names/dicts/specs, or a dict. If '
                                                  'omitted, a single InputPort is '
                                                  'created from default_variable. '
                                                  'Number of ports must match the '
                                                  'first axis of default_variable if '
                                                  'both are specified.',
                                   'oneOf': [ {'type': 'string'},
                                              {'type': 'array'},
                                              {'type': 'object'}]},
                  'input_shapes': { 'description': 'Alternative to default_variable: '
                                                   'specify input size as an integer '
                                                   '(single InputPort of that length) '
                                                   'or a list of ints/tuples (one per '
                                                   'InputPort). Ignored if '
                                                   'default_variable is also provided '
                                                   'and they are compatible; raises an '
                                                   'error if they conflict.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Name for the Mechanism. If omitted, a '
                                           'default is assigned by MechanismRegistry '
                                           'using the subclass name plus an index '
                                           'suffix for duplicates.',
                            'type': 'string'},
                  'output_labels': { 'description': 'Dict mapping string labels to '
                                                    'numeric output values for '
                                                    'reporting. Same structure as '
                                                    'input_labels but applied to '
                                                    'OutputPorts.',
                                     'type': 'object'},
                  'output_ports': { 'description': 'Specification for one or more '
                                                   'OutputPorts. Can be a name string, '
                                                   'a list of names/dicts, or a '
                                                   'standard output port name (e.g., '
                                                   "'RESULT', 'OWNER_VALUE'). If "
                                                   'omitted, a single OutputPort is '
                                                   'created from the first item of the '
                                                   "Mechanism's value.",
                                    'oneOf': [ {'type': 'string'},
                                               {'type': 'array'},
                                               {'type': 'object'}]},
                  'prefs': { 'description': 'PreferenceSet or specification dict for '
                                            "the Mechanism's preferences (e.g., "
                                            'verbosity, logging). Rarely needed; omit '
                                            'to use class defaults.',
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Mechanism_Base is abstract and cannot be instantiated directly — always use a concrete subclass (TransferMechanism, LCAMechanism, DDM, etc.). The variable is always stored internally as a 2D numpy array; scalars become [[value]]. Specifying both default_variable and input_shapes is allowed only if they describe the same shape, otherwise a MechanismError is raised. The function parameter here is typed as string for JSON Schema compatibility, but at the Python level it should be a PsyNeuLink Function instance or class — pass the name of the function (e.g., "Linear", "Logistic") and expect the generated template to resolve it. Standard output port names that can be passed in output_ports: "RESULT" (axis-0 slice of value), "OWNER_VALUE" / "MECHANISM_VALUE" (full value array). ParameterPorts cannot be added or removed after construction. Removing InputPorts after construction changes variable shape and may break the function.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Mechanism_Base
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
    def create_mechanism__base(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to understand the shared constructor interface for all PsyNeuLink Mechanism subclasses — do NOT call it directly to create a mechanism, as Mechanism_Base is abstract.'
        return _impl(args or {})
