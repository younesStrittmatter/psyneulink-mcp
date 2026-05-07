"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e1fac85c4630b6ae2852fa07700431b619a6aa55eac9a133a8a8e5bbb8ff8e95'
__pnl_qualname__ = 'psyneulink.core.components.functions.stateful.integratorfunctions.DriftOnASphereIntegrator'
__pnl_kind__ = 'class'
__pnl_parents__ = ['IntegratorFunction',
 'StatefulFunction',
 'Function_Base',
 'Function',
 'ShellClass',
 'Component',
 'MDFSerializable']
__pnl_parent_sha256s__ = {'Component': 'b878afca9fca90ac1a952605ca8d39a37f25ebebf1411a7f545b9c48a3eaeec3',
 'Function': '49ff0535055d97328c0f76806a53021714e2f8577d138152b75b7e15fcaab2e3',
 'Function_Base': '9b4c0d2feb23147f7d25af3ae03decf546fdb1f2e8be53abb8d8168801d60afa',
 'IntegratorFunction': '8a17d1e7ef745b7ec20cf5925290acde573cbabda2806b3a7aa26ce0cc966916',
 'MDFSerializable': 'caad6059e8ef158be1269a23127f13da3733824c3585f9b4d6e3a63de82f65da',
 'ShellClass': 'adc23754ebeb0c55bdde1324622b33a509116703503508ee7e7de181a8afeee6',
 'StatefulFunction': 'b49d4a3b9b27486e488e3eb62eb3a9313fc20a2170b37eebb6b79b803fa7dedb'}
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_drift_on_a_sphere_integrator'
TOOL_DESCRIPTION = 'Build a `DriftOnASphereIntegrator` function for use inside a Mechanism (typically an IntegratorMechanism). Use this when you need a stateful integrator whose value is constrained to the unit sphere S^(dimension-1) — i.e., the previous_value is always a unit vector and updates are computed in the tangent space and mapped back via the exponential map (correct geometric Brownian motion on a sphere). Beyond its IntegratorFunction parent, it adds the `dimension` parameter and three input interpretations selected by `input_space` ("auto" | "tangent" | "target"): scalar drift along a parallel-transported persistent direction, length-(dimension-1) tangent displacement, or length-dimension target point on the sphere. Returns a function handle to attach to a mechanism\'s `function=` argument.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for runtime drift input. In tangent mode use length d-1; in target mode use length d. If omitted, defaults to zeros of length d-1 (or length d when input_space=\'target\'). NOTE: PNL validates that any array-valued parameter (rate, noise, offset) has the same length as default_variable, so set default_variable consistently with how you size those arrays.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "dimension": {\n      "default": 3,\n      "description": "Ambient dimension d of R^d; the state lives on S^(d-1). Must be >= 2.",\n      "minimum": 2,\n      "type": "integer"\n    },\n    "initializer": {\n      "description": "Starting point. Length d = Cartesian (normalized to unit length); length d-1 = hyperspherical angles converted to Cartesian. Must not be the zero vector. If omitted, defaults to e_0 = [1, 0, ..., 0].",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_space": {\n      "default": "auto",\n      "description": "How to interpret a vector `variable` at runtime. \'tangent\' = length d-1 displacement; \'target\' = length d point on the sphere (magnitude ignored); \'auto\' infers from length. A scalar `variable` always drives the persistent drift_dir regardless of this setting.",\n      "enum": [\n        "auto",\n        "tangent",\n        "target"\n      ],\n      "type": "string"\n    },\n    "noise": {\n      "anyOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ],\n      "default": 0,\n      "description": "Diffusion. Scalar = isotropic on the sphere; 1d array of length d-1 = anisotropic in tangent coordinates. Scaled by sqrt(time_step_size)."\n    },\n    "offset": {\n      "anyOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ],\n      "default": 0,\n      "description": "Additive drift term, projected into the tangent space. Prefer a scalar. If you pass an array its length MUST equal default_variable\'s length (PNL validates this \\u2014 passing length d-1 alongside a length-d default_variable, or vice versa, raises FunctionError)."\n    },\n    "rate": {\n      "anyOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ],\n      "default": 1,\n      "description": "Angular velocity scaling. Scalar, or 1d array matching default_variable length. In target mode, rate=1.0 with time_step_size=1.0 reaches the target in one step; 0<rate<1 moves partway."\n    },\n    "seed": {\n      "description": "Seed for the internal RandomState used for diffusion noise.",\n      "type": "integer"\n    },\n    "time_step_size": {\n      "default": 1,\n      "description": "Integration step dt. Drift contributes dt * drift_tangent; noise contributes sqrt(dt) * noise_tangent.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "dimension"\n  ],\n  "type": "object"\n}\n\nNotes:\nPNL parameter-length validation gotcha (root cause of the recent feedback issue): the parent `IntegratorFunction._validate_params` enforces that EVERY array-valued parameter (rate/noise/offset) has the same length as `default_variable`. This conflicts with the mathematical convention that offset/noise live in the tangent space (length d-1) while a target-mode default_variable has length d. Safe recipes: (a) keep offset/rate as scalars whenever possible; (b) if you pass an array offset, make its length exactly match default_variable; (c) for target mode (input_space=\'target\', default_variable length d), only scalar offset is reliable. Other things to know: previous_value is always re-normalized to unit length; in target mode the magnitude of `variable` is ignored (it is projected to the sphere); a scalar `variable` drives a persistent `drift_dir` that is parallel-transported each step; \'auto\' input_space emits a one-time RuntimeWarning when it interprets a length-d vector as a target — set input_space explicitly to silence it; `dimension` is read-only after construction and must be >= 2; antipodal target points pick an arbitrary tangent direction via Householder basis.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for runtime drift '
                                                       'input. In tangent mode use '
                                                       'length d-1; in target mode use '
                                                       'length d. If omitted, defaults '
                                                       'to zeros of length d-1 (or '
                                                       'length d when '
                                                       "input_space='target'). NOTE: "
                                                       'PNL validates that any '
                                                       'array-valued parameter (rate, '
                                                       'noise, offset) has the same '
                                                       'length as default_variable, so '
                                                       'set default_variable '
                                                       'consistently with how you size '
                                                       'those arrays.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'dimension': { 'default': 3,
                                 'description': 'Ambient dimension d of R^d; the state '
                                                'lives on S^(d-1). Must be >= 2.',
                                 'minimum': 2,
                                 'type': 'integer'},
                  'initializer': { 'description': 'Starting point. Length d = '
                                                  'Cartesian (normalized to unit '
                                                  'length); length d-1 = '
                                                  'hyperspherical angles converted to '
                                                  'Cartesian. Must not be the zero '
                                                  'vector. If omitted, defaults to e_0 '
                                                  '= [1, 0, ..., 0].',
                                   'items': {'type': 'number'},
                                   'type': 'array'},
                  'input_space': { 'default': 'auto',
                                   'description': 'How to interpret a vector '
                                                  "`variable` at runtime. 'tangent' = "
                                                  "length d-1 displacement; 'target' = "
                                                  'length d point on the sphere '
                                                  "(magnitude ignored); 'auto' infers "
                                                  'from length. A scalar `variable` '
                                                  'always drives the persistent '
                                                  'drift_dir regardless of this '
                                                  'setting.',
                                   'enum': ['auto', 'tangent', 'target'],
                                   'type': 'string'},
                  'noise': { 'anyOf': [ {'type': 'number'},
                                        {'items': {'type': 'number'}, 'type': 'array'}],
                             'default': 0,
                             'description': 'Diffusion. Scalar = isotropic on the '
                                            'sphere; 1d array of length d-1 = '
                                            'anisotropic in tangent coordinates. '
                                            'Scaled by sqrt(time_step_size).'},
                  'offset': { 'anyOf': [ {'type': 'number'},
                                         { 'items': {'type': 'number'},
                                           'type': 'array'}],
                              'default': 0,
                              'description': 'Additive drift term, projected into the '
                                             'tangent space. Prefer a scalar. If you '
                                             'pass an array its length MUST equal '
                                             "default_variable's length (PNL validates "
                                             'this — passing length d-1 alongside a '
                                             'length-d default_variable, or vice '
                                             'versa, raises FunctionError).'},
                  'rate': { 'anyOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}],
                            'default': 1,
                            'description': 'Angular velocity scaling. Scalar, or 1d '
                                           'array matching default_variable length. In '
                                           'target mode, rate=1.0 with '
                                           'time_step_size=1.0 reaches the target in '
                                           'one step; 0<rate<1 moves partway.'},
                  'seed': { 'description': 'Seed for the internal RandomState used for '
                                           'diffusion noise.',
                            'type': 'integer'},
                  'time_step_size': { 'default': 1,
                                      'description': 'Integration step dt. Drift '
                                                     'contributes dt * drift_tangent; '
                                                     'noise contributes sqrt(dt) * '
                                                     'noise_tangent.',
                                      'type': 'number'}},
  'required': ['dimension'],
  'type': 'object'}
TOOL_NOTES = "PNL parameter-length validation gotcha (root cause of the recent feedback issue): the parent `IntegratorFunction._validate_params` enforces that EVERY array-valued parameter (rate/noise/offset) has the same length as `default_variable`. This conflicts with the mathematical convention that offset/noise live in the tangent space (length d-1) while a target-mode default_variable has length d. Safe recipes: (a) keep offset/rate as scalars whenever possible; (b) if you pass an array offset, make its length exactly match default_variable; (c) for target mode (input_space='target', default_variable length d), only scalar offset is reliable. Other things to know: previous_value is always re-normalized to unit length; in target mode the magnitude of `variable` is ignored (it is projected to the sphere); a scalar `variable` drives a persistent `drift_dir` that is parallel-transported each step; 'auto' input_space emits a one-time RuntimeWarning when it interprets a length-d vector as a target — set input_space explicitly to silence it; `dimension` is read-only after construction and must be >= 2; antipodal target points pick an arbitrary tangent direction via Householder basis."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DriftOnASphereIntegrator
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
    def create_drift_on_a_sphere_integrator(args: dict[str, Any] | None = None) -> Any:
        'Build a `DriftOnASphereIntegrator` function for use inside a Mechanism (typically an IntegratorMechanism).'
        return _impl(args or {})
