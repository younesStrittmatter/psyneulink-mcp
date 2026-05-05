"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '179fd63cd00d054c281e674756a5fb3718001a59d927d5a771b3d2dac52912d0'
__pnl_qualname__ = 'psyneulink.OneHot'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_one_hot'
TOOL_DESCRIPTION = 'Use this tool to create a PsyNeuLink OneHot selection function that transforms an input array by zeroing all elements except those at extremal (max or min) positions. Call it when you need a winner-take-all, argmax/argmin, or probabilistic selection function — for example, as the function of a TransferMechanism to implement competition or soft selection. Returns a OneHot instance whose `.function()` produces an array of the same length as input with non-extreme values set to zero.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "abs_val": {\n      "default": false,\n      "description": "If true, selection is based on absolute values of elements (but output retains original signed values unless indicator=true). Only effective when mode is \'DETERMINISTIC\'.",\n      "type": "boolean"\n    },\n    "default_variable": {\n      "description": "Template array for the input to be transformed. For PROB or PROB_INDICATOR mode, must be a 2-element list: [[values], [probabilities]] where probabilities sum to 1. For all other modes, a 1d array of numbers suffices.",\n      "items": {},\n      "type": "array"\n    },\n    "direction": {\n      "default": "MAX",\n      "description": "Whether to select the maximum (\'MAX\') or minimum (\'MIN\') value(s). Only effective when mode is \'DETERMINISTIC\'; ignored (and must not be set) for legacy mode keywords.",\n      "enum": [\n        "MAX",\n        "MIN"\n      ],\n      "type": "string"\n    },\n    "indicator": {\n      "default": false,\n      "description": "If true, the selected element(s) are replaced with 1 rather than their actual value. Only effective when mode is \'DETERMINISTIC\'.",\n      "type": "boolean"\n    },\n    "mode": {\n      "default": "DETERMINISTIC",\n      "description": "Selection strategy. Use \'DETERMINISTIC\' (default) to control behavior via direction/abs_val/indicator/tie args. Use \'PROB\' or \'PROB_INDICATOR\' for probabilistic selection (requires 2d variable). Legacy shortcuts (e.g. \'ARG_MAX\', \'MAX_VAL\', \'MIN_INDICATOR\') are preset combinations \\u2014 do NOT also set direction/abs_val/indicator when using them.",\n      "enum": [\n        "DETERMINISTIC",\n        "PROB",\n        "PROB_INDICATOR",\n        "ARG_MAX",\n        "ARG_MAX_ABS",\n        "ARG_MAX_INDICATOR",\n        "ARG_MAX_ABS_INDICATOR",\n        "ARG_MIN",\n        "ARG_MIN_ABS",\n        "ARG_MIN_INDICATOR",\n        "ARG_MIN_ABS_INDICATOR",\n        "MAX_VAL",\n        "MAX_ABS_VAL",\n        "MAX_INDICATOR",\n        "MAX_ABS_INDICATOR",\n        "MIN_VAL",\n        "MIN_ABS_VAL",\n        "MIN_INDICATOR",\n        "MIN_ABS_INDICATOR"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for this function instance.",\n      "type": "string"\n    },\n    "seed": {\n      "description": "Random seed for reproducible behavior when tie=\'RANDOM\' or mode is \'PROB\'/\'PROB_INDICATOR\'.",\n      "type": "integer"\n    },\n    "tie": {\n      "default": "ALL",\n      "description": "How to handle ties (multiple elements sharing the extreme value). \'ALL\': keep all tied elements; \'FIRST\': keep only the lowest-index tied element; \'LAST\': keep only the highest-index tied element; \'RANDOM\': randomly pick one tied element. Applies in DETERMINISTIC mode and to MAX_VAL/MIN_VAL/etc. legacy modes.",\n      "enum": [\n        "ALL",\n        "FIRST",\n        "LAST",\n        "RANDOM"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n1. The true runtime default for mode is \'DETERMINISTIC\' (set in Parameters class), not \'ARG_MAX\' as the docstring header implies — the header is misleading.\n2. When mode is \'PROB\' or \'PROB_INDICATOR\', default_variable MUST be a 2d array [[values], [probabilities]] where probabilities are in [0,1] and sum to 1; passing a 1d array will raise FunctionError.\n3. When mode is any legacy keyword (anything except \'DETERMINISTIC\', \'PROB\', \'PROB_INDICATOR\'), direction/abs_val/indicator must NOT be specified — doing so raises FunctionError even if values match the legacy mode\'s preset.\n4. The legacy ARG_* shortcuts hard-code tie=FIRST; the MAX_*/MIN_* shortcuts use the tie parameter (defaulting to ALL). Use DETERMINISTIC + explicit args for full control.\n5. With indicator=True and abs_val=True, the output is 1 at the selected position(s), not the absolute value — the abs_val flag only affects which element is chosen, not the output value when indicator=True.'
TOOL_PARAMETERS = { 'properties': { 'abs_val': { 'default': False,
                               'description': 'If true, selection is based on absolute '
                                              'values of elements (but output retains '
                                              'original signed values unless '
                                              'indicator=true). Only effective when '
                                              "mode is 'DETERMINISTIC'.",
                               'type': 'boolean'},
                  'default_variable': { 'description': 'Template array for the input '
                                                       'to be transformed. For PROB or '
                                                       'PROB_INDICATOR mode, must be a '
                                                       '2-element list: [[values], '
                                                       '[probabilities]] where '
                                                       'probabilities sum to 1. For '
                                                       'all other modes, a 1d array of '
                                                       'numbers suffices.',
                                        'items': {},
                                        'type': 'array'},
                  'direction': { 'default': 'MAX',
                                 'description': "Whether to select the maximum ('MAX') "
                                                "or minimum ('MIN') value(s). Only "
                                                'effective when mode is '
                                                "'DETERMINISTIC'; ignored (and must "
                                                'not be set) for legacy mode keywords.',
                                 'enum': ['MAX', 'MIN'],
                                 'type': 'string'},
                  'indicator': { 'default': False,
                                 'description': 'If true, the selected element(s) are '
                                                'replaced with 1 rather than their '
                                                'actual value. Only effective when '
                                                "mode is 'DETERMINISTIC'.",
                                 'type': 'boolean'},
                  'mode': { 'default': 'DETERMINISTIC',
                            'description': "Selection strategy. Use 'DETERMINISTIC' "
                                           '(default) to control behavior via '
                                           'direction/abs_val/indicator/tie args. Use '
                                           "'PROB' or 'PROB_INDICATOR' for "
                                           'probabilistic selection (requires 2d '
                                           'variable). Legacy shortcuts (e.g. '
                                           "'ARG_MAX', 'MAX_VAL', 'MIN_INDICATOR') are "
                                           'preset combinations — do NOT also set '
                                           'direction/abs_val/indicator when using '
                                           'them.',
                            'enum': [ 'DETERMINISTIC',
                                      'PROB',
                                      'PROB_INDICATOR',
                                      'ARG_MAX',
                                      'ARG_MAX_ABS',
                                      'ARG_MAX_INDICATOR',
                                      'ARG_MAX_ABS_INDICATOR',
                                      'ARG_MIN',
                                      'ARG_MIN_ABS',
                                      'ARG_MIN_INDICATOR',
                                      'ARG_MIN_ABS_INDICATOR',
                                      'MAX_VAL',
                                      'MAX_ABS_VAL',
                                      'MAX_INDICATOR',
                                      'MAX_ABS_INDICATOR',
                                      'MIN_VAL',
                                      'MIN_ABS_VAL',
                                      'MIN_INDICATOR',
                                      'MIN_ABS_INDICATOR'],
                            'type': 'string'},
                  'name': { 'description': 'Optional name for this function instance.',
                            'type': 'string'},
                  'seed': { 'description': 'Random seed for reproducible behavior when '
                                           "tie='RANDOM' or mode is "
                                           "'PROB'/'PROB_INDICATOR'.",
                            'type': 'integer'},
                  'tie': { 'default': 'ALL',
                           'description': 'How to handle ties (multiple elements '
                                          "sharing the extreme value). 'ALL': keep all "
                                          "tied elements; 'FIRST': keep only the "
                                          "lowest-index tied element; 'LAST': keep "
                                          'only the highest-index tied element; '
                                          "'RANDOM': randomly pick one tied element. "
                                          'Applies in DETERMINISTIC mode and to '
                                          'MAX_VAL/MIN_VAL/etc. legacy modes.',
                           'enum': ['ALL', 'FIRST', 'LAST', 'RANDOM'],
                           'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "1. The true runtime default for mode is 'DETERMINISTIC' (set in Parameters class), not 'ARG_MAX' as the docstring header implies — the header is misleading.\n2. When mode is 'PROB' or 'PROB_INDICATOR', default_variable MUST be a 2d array [[values], [probabilities]] where probabilities are in [0,1] and sum to 1; passing a 1d array will raise FunctionError.\n3. When mode is any legacy keyword (anything except 'DETERMINISTIC', 'PROB', 'PROB_INDICATOR'), direction/abs_val/indicator must NOT be specified — doing so raises FunctionError even if values match the legacy mode's preset.\n4. The legacy ARG_* shortcuts hard-code tie=FIRST; the MAX_*/MIN_* shortcuts use the tie parameter (defaulting to ALL). Use DETERMINISTIC + explicit args for full control.\n5. With indicator=True and abs_val=True, the output is 1 at the selected position(s), not the absolute value — the abs_val flag only affects which element is chosen, not the output value when indicator=True."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.OneHot
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
    def create_one_hot(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a PsyNeuLink OneHot selection function that transforms an input array by zeroing all elements except those at extremal (max or min) positions.'
        return _impl(args or {})
