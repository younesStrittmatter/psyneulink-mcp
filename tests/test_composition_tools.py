"""Integration tests: real PNL through the curated composition tools.

These actually build and run a small PsyNeuLink composition via the
public tool surface, so they exercise (a) the handles registry, (b) the
curated composition tools, and (c) the assumption that PNL accepts
default MappingProjections between two TransferMechanisms.

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
    real feedback/pending/issues.jsonl. ``test_add_linear_pathway_rejects_empty``
    deliberately raises through ``captured_tool``."""
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


def test_add_node_appears_in_node_list(tools):
    h_comp = _make_composition()
    h_node = _make_transfer("a")
    out = tools["add_node"](composition=h_comp, node=h_node)
    assert out["composition"] == h_comp
    assert out["added"] == h_node
    assert _name_of(h_node) in out["nodes"]


def test_add_linear_pathway_runs_end_to_end(tools):
    h_in = _make_transfer("in_node")
    h_hidden = _make_transfer("hidden")
    h_out = _make_transfer("out_node")
    h_comp = _make_composition()

    pathway = tools["add_linear_pathway"](
        composition=h_comp, nodes=[h_in, h_hidden, h_out]
    )
    assert pathway["pathway"] == [h_in, h_hidden, h_out]
    for h in (h_in, h_hidden, h_out):
        assert _name_of(h) in pathway["nodes"]

    result = tools["run_composition"](
        composition=h_comp, inputs={h_in: [[1.0]]}
    )
    assert result["composition"] == h_comp
    assert _name_of(h_in) in result["output_values"]
    assert _name_of(h_out) in result["output_values"]


def test_add_linear_pathway_rejects_empty(tools):
    h_comp = _make_composition()
    with pytest.raises(ValueError):
        tools["add_linear_pathway"](composition=h_comp, nodes=[])


def test_add_projection_with_explicit_matrix(tools):
    """Smoke: add_projection accepts a literal matrix and the composition runs.

    We deliberately don't pin the numerical output here — exact values
    depend on which nodes PNL classifies as INPUT vs INTERNAL when
    they're added with bare ``add_node``, and the MVP only needs to
    prove the surface (projection added, run produces output for both
    nodes) works.
    """
    h_a = _make_transfer("a")
    h_b = _make_transfer("b")
    h_comp = _make_composition()
    tools["add_node"](composition=h_comp, node=h_a)
    tools["add_node"](composition=h_comp, node=h_b)

    out = tools["add_projection"](
        composition=h_comp,
        sender=h_a,
        receiver=h_b,
        matrix=[[2.0]],
    )
    assert out == {"composition": h_comp, "from": h_a, "to": h_b}

    run = tools["run_composition"](
        composition=h_comp, inputs={h_a: [[3.0]]}
    )
    assert _name_of(h_a) in run["output_values"]
    assert _name_of(h_b) in run["output_values"]


def test_list_and_describe(tools):
    h = _make_transfer("solo")
    rows = tools["list_handles"]()
    assert any(r["handle"] == h for r in rows)
    desc = tools["describe_handle"](handle=h)
    assert desc["name"] == _name_of(h)
    assert desc["type"] == "TransferMechanism"
