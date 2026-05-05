"""Integration tests: real PNL through the curated composition tools.

These actually build and run a small PsyNeuLink composition via the
public tool surface, so they exercise (a) the handles registry, (b) the
remaining curated composition tools, and (c) the assumption that PNL
accepts default MappingProjections between two TransferMechanisms.

Three of the originally-curated tools (``add_node``,
``add_linear_pathway``, ``add_projection``) moved to the generated
layer; their tests now live in ``test_composition_method_tools.py``.

Marked ``integration`` because they import psyneulink (slow). Run with
``pytest -m integration`` or as part of the full suite.
"""

from __future__ import annotations

from typing import Any

import pytest

from psyneulink_mcp import feedback, handles
from psyneulink_mcp.tools.curated import composition as curated_composition

pytestmark = pytest.mark.integration


@pytest.fixture(autouse=True)
def _isolate_feedback_log(monkeypatch, tmp_path):
    """Stop captured-tool errors from these tests from polluting the dev's
    real feedback/pending/issues.jsonl."""
    monkeypatch.setenv(
        feedback.ENV_FEEDBACK_PATH, str(tmp_path / "issues.jsonl")
    )


class FakeMCP:
    """Capture registered tools so we can call them as plain functions."""

    def __init__(self) -> None:
        self.tools: dict[str, Any] = {}

    def tool(self, **_kwargs: Any):
        def decorator(fn):
            self.tools[fn.__name__] = fn
            return fn

        return decorator


@pytest.fixture
def tools():
    handles.clear_handles()
    mcp = FakeMCP()
    curated_composition.register(mcp)
    yield mcp.tools
    handles.clear_handles()


def _make_transfer(name: str, default_variable=None):
    import psyneulink as pnl

    kwargs: dict[str, Any] = {"name": name}
    if default_variable is not None:
        kwargs["default_variable"] = default_variable
    obj = pnl.TransferMechanism(**kwargs)
    return handles.register_handle(obj)["handle"]


def _make_composition(name: str = "comp"):
    import psyneulink as pnl

    return handles.register_handle(pnl.Composition(name=name))["handle"]


def _name_of(handle: str) -> str:
    """Resolve a handle and return the underlying object's PNL-assigned name.

    PNL maintains its own global name registry, so the *requested* name
    can be modified (``a`` → ``a-1``) when a second test creates a
    mechanism with the same string. Tests that assert on node names
    must read the actual assigned name back, not the requested one.
    """
    return handles.resolve_handle(handle).name


def test_run_composition_returns_per_node_output(tools):
    """``run_composition`` produces a JSON-serialisable result + per-node output.

    Wires a 3-node feed-forward chain via the *generated* method tool
    (the migrated path) so this also smoke-tests that ``run_composition``
    still pairs correctly with the new layer split.
    """
    import psyneulink as pnl

    from psyneulink_mcp.tools.generated import (
        composition_add_linear_processing_pathway as gen_pathway,
    )

    h_in = _make_transfer("rc_in")
    h_hidden = _make_transfer("rc_hidden")
    h_out = _make_transfer("rc_out")
    h_comp = _make_composition(name="rc_comp")

    gen_pathway._impl(
        {"composition": h_comp, "pathway": [h_in, h_hidden, h_out]}
    )

    result = tools["run_composition"](
        composition=h_comp, inputs={h_in: [[1.0]]}
    )
    assert result["composition"] == h_comp
    assert _name_of(h_in) in result["output_values"]
    assert _name_of(h_out) in result["output_values"]
    # ``Composition.run`` returns an ``ndarray`` — the curated tool
    # is responsible for coercing that to a JSON-friendly shape.
    assert not isinstance(result["result"], pnl.Composition)


def test_list_and_describe(tools):
    h = _make_transfer("solo")
    rows = tools["list_handles"]()
    assert any(r["handle"] == h for r in rows)
    desc = tools["describe_handle"](handle=h)
    assert desc["name"] == _name_of(h)
    assert desc["type"] == "TransferMechanism"
