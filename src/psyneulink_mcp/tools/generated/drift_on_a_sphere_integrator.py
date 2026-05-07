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
TOOL_DESCRIPTION = 'Create a DriftOnASphereIntegrator function: an IntegratorFunction whose state is constrained to the unit sphere S^(dimension-1), updated via tangent-space drift+noise composed with the exponential map. Use this when you need geometric Brownian motion on a sphere (e.g., temporal context vectors in EGO/EM models) — distinct from flat-space integrators like DriftDiffusionIntegrator because previous_value is always a unit vector and rate/noise act as angular quantities. Returns a function handle to attach to a Mechanism (typically a ProcessingMechanism serving as a context generator).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the drift input. Length MUST be exactly dimension-1 (tangent-space template) OR exactly dimension (target-mode template). A scalar/length-1 array is NOT accepted when dimension>2 \\u2014 pass an array of zeros of the right length, or omit entirely (the constructor will pick the right shape based on input_space).",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "dimension": {\n      "default": 3,\n      "description": "Ambient dimension d of R^d. The sphere is S^(d-1). Most other shape rules are derived from this.",\n      "minimum": 2,\n      "type": "integer"\n    },\n    "initializer": {\n      "description": "Starting point on the sphere. MUST be 1D with length == dimension (Cartesian, will be normalized to unit length) OR length == dimension-1 (interpreted as hyperspherical angle coords). MUST NOT be the zero vector \\u2014 use e.g. [1, 0, 0, ...] or random nonzero values, never all zeros. If omitted, defaults to e_0 = [1, 0, ..., 0].",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_space": {\n      "default": "auto",\n      "description": "How runtime variable is interpreted: \'tangent\' (length d-1 displacement), \'target\' (length d point on sphere, geodesic step toward it), or \'auto\' (infer from variable length; emits a warning when length-d input is treated as target).",\n      "enum": [\n        "auto",\n        "tangent",\n        "target"\n      ],\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Scalar = isotropic diffusion. Array MUST have length dimension-1 (anisotropic tangent-coord diffusion).",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "offset": {\n      "default": 0,\n      "description": "Additive drift term, projected into tangent space. Keep this as a SCALAR \\u2014 passing an array triggers PNL\'s len>1 parameter-shape check against default_variable and almost always raises FunctionError.",\n      "type": "number"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Scales angular movement per unit time. In target-mode with rate=1.0 and time_step_size=1.0 the system reaches the target in one step.",\n      "type": "number"\n    },\n    "seed": {\n      "description": "Seeds the internal RNG.",\n      "type": "integer"\n    },\n    "time_step_size": {\n      "default": 1,\n      "description": "Integration time step dt.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "dimension"\n  ],\n  "type": "object"\n}\n\nNotes:\nShape rules (the source of nearly every error in feedback for this tool):\n- `initializer` length must be EXACTLY `dimension` (Cartesian) or `dimension-1` (hyperspherical). Passing length-1 with dimension=25 fails with "must be a list or 1d array of length 25".\n- `initializer` must NOT be the all-zeros vector — it gets normalized and zero-norm raises FunctionError. Use e.g. [1, 0, 0, ...] (the implicit default) or any nonzero pattern.\n- `default_variable` must be length `dimension-1` (tangent template) or `dimension` (target template). A scalar [0] with dimension=25 fails with "must be length 24 (tangent template) or 25 (target template). Got 1." If unsure, omit `default_variable` entirely.\n- `offset` should be a scalar. Array offsets pass through PNL\'s StatefulFunction len>1 shape check that requires equality with default_variable\'s length, which mismatches in target mode and raises "parameters with len>1 ... don\'t have the same length as its \'default_variable\'".\n- `noise` array must be length `dimension-1`, not `dimension`.\n- previous_value is always renormalized to a unit vector after each step, so passing an unnormalized initializer is fine — but a zero vector still errors.\n- For geometric Brownian motion at sub-step accuracy, prefer small `time_step_size`; rate and noise are angular (radians) not linear units.\n- `dimension` is read-only after construction; recreate the function to change it.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the drift input. '
                                                       'Length MUST be exactly '
                                                       'dimension-1 (tangent-space '
                                                       'template) OR exactly dimension '
                                                       '(target-mode template). A '
                                                       'scalar/length-1 array is NOT '
                                                       'accepted when dimension>2 — '
                                                       'pass an array of zeros of the '
                                                       'right length, or omit entirely '
                                                       '(the constructor will pick the '
                                                       'right shape based on '
                                                       'input_space).',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'dimension': { 'default': 3,
                                 'description': 'Ambient dimension d of R^d. The '
                                                'sphere is S^(d-1). Most other shape '
                                                'rules are derived from this.',
                                 'minimum': 2,
                                 'type': 'integer'},
                  'initializer': { 'description': 'Starting point on the sphere. MUST '
                                                  'be 1D with length == dimension '
                                                  '(Cartesian, will be normalized to '
                                                  'unit length) OR length == '
                                                  'dimension-1 (interpreted as '
                                                  'hyperspherical angle coords). MUST '
                                                  'NOT be the zero vector — use e.g. '
                                                  '[1, 0, 0, ...] or random nonzero '
                                                  'values, never all zeros. If '
                                                  'omitted, defaults to e_0 = [1, 0, '
                                                  '..., 0].',
                                   'items': {'type': 'number'},
                                   'type': 'array'},
                  'input_space': { 'default': 'auto',
                                   'description': 'How runtime variable is '
                                                  "interpreted: 'tangent' (length d-1 "
                                                  "displacement), 'target' (length d "
                                                  'point on sphere, geodesic step '
                                                  "toward it), or 'auto' (infer from "
                                                  'variable length; emits a warning '
                                                  'when length-d input is treated as '
                                                  'target).',
                                   'enum': ['auto', 'tangent', 'target'],
                                   'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Scalar = isotropic diffusion. Array MUST '
                                            'have length dimension-1 (anisotropic '
                                            'tangent-coord diffusion).',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'offset': { 'default': 0,
                              'description': 'Additive drift term, projected into '
                                             'tangent space. Keep this as a SCALAR — '
                                             "passing an array triggers PNL's len>1 "
                                             'parameter-shape check against '
                                             'default_variable and almost always '
                                             'raises FunctionError.',
                              'type': 'number'},
                  'rate': { 'default': 1,
                            'description': 'Scales angular movement per unit time. In '
                                           'target-mode with rate=1.0 and '
                                           'time_step_size=1.0 the system reaches the '
                                           'target in one step.',
                            'type': 'number'},
                  'seed': {'description': 'Seeds the internal RNG.', 'type': 'integer'},
                  'time_step_size': { 'default': 1,
                                      'description': 'Integration time step dt.',
                                      'type': 'number'}},
  'required': ['dimension'],
  'type': 'object'}
TOOL_NOTES = 'Shape rules (the source of nearly every error in feedback for this tool):\n- `initializer` length must be EXACTLY `dimension` (Cartesian) or `dimension-1` (hyperspherical). Passing length-1 with dimension=25 fails with "must be a list or 1d array of length 25".\n- `initializer` must NOT be the all-zeros vector — it gets normalized and zero-norm raises FunctionError. Use e.g. [1, 0, 0, ...] (the implicit default) or any nonzero pattern.\n- `default_variable` must be length `dimension-1` (tangent template) or `dimension` (target template). A scalar [0] with dimension=25 fails with "must be length 24 (tangent template) or 25 (target template). Got 1." If unsure, omit `default_variable` entirely.\n- `offset` should be a scalar. Array offsets pass through PNL\'s StatefulFunction len>1 shape check that requires equality with default_variable\'s length, which mismatches in target mode and raises "parameters with len>1 ... don\'t have the same length as its \'default_variable\'".\n- `noise` array must be length `dimension-1`, not `dimension`.\n- previous_value is always renormalized to a unit vector after each step, so passing an unnormalized initializer is fine — but a zero vector still errors.\n- For geometric Brownian motion at sub-step accuracy, prefer small `time_step_size`; rate and noise are angular (radians) not linear units.\n- `dimension` is read-only after construction; recreate the function to change it.'


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
        'Create a DriftOnASphereIntegrator function: an IntegratorFunction whose state is constrained to the unit sphere S^(dimension-1), updated via tangent-space drift+noise composed with the exponential map.'
        return _impl(args or {})
