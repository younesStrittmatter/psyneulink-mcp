"""Tests for the curated visualization tools and the composition revision counter.

Three layers of coverage live here:

* **Unit tests for the revision counter** in ``handles.py`` — pure dict
  mechanics, no PNL or graphviz needed.
* **FakeMCP register test** — confirms the tool names land where the
  server expects them, also no PNL needed.
* **Integration tests** (``pytest -m integration``) that build a real
  ``pnl.Composition`` through the curated tools, exercising both the
  bump-on-mutation wiring and the actual graphviz pipe. The PNG / SVG
  cases are skipped on machines without the ``dot`` system binary; the
  ``"dot"`` text-source case still runs because it never invokes ``dot``.
"""

from __future__ import annotations

import base64
import shutil
from typing import Any

import pytest

from psyneulink_mcp import feedback, handles
from psyneulink_mcp.tools.curated import composition as curated_composition
from psyneulink_mcp.tools.curated import visualization as curated_visualization
from psyneulink_mcp.tools.generated import (
    composition_add_linear_processing_pathway as gen_pathway,
)
from psyneulink_mcp.tools.generated import composition_add_node as gen_add_node
from psyneulink_mcp.tools.generated import (
    composition_add_projection as gen_add_projection,
)

_HAS_DOT = shutil.which("dot") is not None
_NEEDS_DOT = pytest.mark.skipif(
    not _HAS_DOT,
    reason="graphviz `dot` binary not installed; PNG / SVG rendering needs it",
)


# --------------------------------------------------------------------------- #
# Shared fixtures                                                             #
# --------------------------------------------------------------------------- #


class FakeMCP:
    """Capture registered tools so we can call them as plain functions.

    Mirrors the FakeMCP pattern in ``test_composition_tools.py``.
    """

    def __init__(self) -> None:
        self.tools: dict[str, Any] = {}

    def tool(self, **_kwargs: Any):
        def decorator(fn):
            self.tools[fn.__name__] = fn
            return fn

        return decorator


@pytest.fixture(autouse=True)
def _isolate_feedback_log(monkeypatch, tmp_path):
    """Stop captured-tool errors raised here from polluting the dev's real
    ``feedback/pending/issues.jsonl``. Several tests deliberately raise
    through ``captured_tool`` (unknown handle, wrong type, bad fmt)."""
    monkeypatch.setenv(
        feedback.ENV_FEEDBACK_PATH, str(tmp_path / "issues.jsonl")
    )


@pytest.fixture
def viz_only_tools():
    """Visualization tools registered in isolation (no PNL needed)."""
    handles.clear_handles()
    mcp = FakeMCP()
    curated_visualization.register(mcp)
    yield mcp.tools
    handles.clear_handles()


@pytest.fixture
def all_curated_tools():
    """Both composition + visualization tools registered together.

    Used by the integration tests that build a real composition through
    the same surface the agent uses, then ask the visualization tools to
    inspect / render it. Also registers the *generated* method tools that
    used to be curated (``add_node``, ``add_projection``,
    ``add_linear_processing_pathway``) so the integration tests below can
    drive a full pipeline through one tool dict.
    """
    handles.clear_handles()
    mcp = FakeMCP()
    curated_composition.register(mcp)
    curated_visualization.register(mcp)
    gen_add_node.register(mcp)
    gen_add_projection.register(mcp)
    gen_pathway.register(mcp)
    yield mcp.tools
    handles.clear_handles()


# --------------------------------------------------------------------------- #
# Revision counter — pure unit tests                                          #
# --------------------------------------------------------------------------- #


class _Dummy:
    """A non-PNL stand-in for handle-registry tests."""

    def __init__(self, name: str = "dummy") -> None:
        self.name = name


def test_get_revision_starts_at_zero_for_unbumped_handles():
    handles.clear_handles()
    h = handles.register_handle(_Dummy("c"))["handle"]
    assert handles.get_revision(h) == 0


def test_get_revision_zero_for_unknown_handle():
    handles.clear_handles()
    # Never been registered — still safe to ask, returns 0.
    assert handles.get_revision("h_deadbeefcafe") == 0


def test_bump_revision_increments():
    handles.clear_handles()
    h = handles.register_handle(_Dummy("c"))["handle"]
    assert handles.bump_revision(h) == 1
    assert handles.bump_revision(h) == 2
    assert handles.get_revision(h) == 2


def test_bump_revision_no_op_for_unknown_handle():
    handles.clear_handles()
    before = dict(handles._COMPOSITION_REVISION)
    assert handles.bump_revision("h_deadbeefcafe") == 0
    assert before == handles._COMPOSITION_REVISION
    assert handles.get_revision("h_deadbeefcafe") == 0


def test_clear_handles_clears_revisions():
    handles.clear_handles()
    h = handles.register_handle(_Dummy("c"))["handle"]
    handles.bump_revision(h)
    handles.bump_revision(h)
    assert handles.get_revision(h) == 2
    handles.clear_handles()
    # A stale handle string from before the clear: revision should be 0.
    assert handles.get_revision(h) == 0
    assert not handles._COMPOSITION_REVISION


# --------------------------------------------------------------------------- #
# FakeMCP wiring — unit                                                       #
# --------------------------------------------------------------------------- #


def test_visualization_tools_register_with_fake_mcp(viz_only_tools):
    assert "render_composition_graph" in viz_only_tools
    assert "get_composition_revision" in viz_only_tools


# --------------------------------------------------------------------------- #
# Integration tests                                                           #
# --------------------------------------------------------------------------- #


@pytest.fixture
def _pnl():
    return pytest.importorskip("psyneulink")


@pytest.fixture
def _gv():
    return pytest.importorskip("graphviz")


def _make_transfer(_pnl, name: str) -> str:
    return handles.register_handle(_pnl.TransferMechanism(name=name))["handle"]


def _make_composition(_pnl, name: str = "comp") -> str:
    return handles.register_handle(_pnl.Composition(name=name))["handle"]


# ---- bump-on-mutation integration ----------------------------------------- #


@pytest.mark.integration
def test_add_node_bumps_composition_revision(all_curated_tools, _pnl):
    h_comp = _make_composition(_pnl)
    h_a = _make_transfer(_pnl, "a")
    h_b = _make_transfer(_pnl, "b")

    assert handles.get_revision(h_comp) == 0
    all_curated_tools["add_node"]({"composition": h_comp, "node": h_a})
    assert handles.get_revision(h_comp) == 1
    all_curated_tools["add_node"]({"composition": h_comp, "node": h_b})
    assert handles.get_revision(h_comp) == 2


@pytest.mark.integration
def test_add_linear_processing_pathway_bumps_composition_revision(
    all_curated_tools, _pnl
):
    h_comp = _make_composition(_pnl)
    h_in = _make_transfer(_pnl, "in_node")
    h_out = _make_transfer(_pnl, "out_node")

    assert handles.get_revision(h_comp) == 0
    all_curated_tools["add_linear_processing_pathway"](
        {"composition": h_comp, "pathway": [h_in, h_out]}
    )
    assert handles.get_revision(h_comp) == 1


@pytest.mark.integration
def test_add_projection_bumps_composition_revision(all_curated_tools, _pnl):
    h_comp = _make_composition(_pnl)
    h_a = _make_transfer(_pnl, "a")
    h_b = _make_transfer(_pnl, "b")
    all_curated_tools["add_node"]({"composition": h_comp, "node": h_a})
    all_curated_tools["add_node"]({"composition": h_comp, "node": h_b})

    rev_before = handles.get_revision(h_comp)
    all_curated_tools["add_projection"](
        {
            "composition": h_comp,
            "sender": h_a,
            "receiver": h_b,
            "matrix": [[2.0]],
        }
    )
    assert handles.get_revision(h_comp) == rev_before + 1


@pytest.mark.integration
def test_run_composition_does_not_bump_revision(all_curated_tools, _pnl):
    h_comp = _make_composition(_pnl)
    h_in = _make_transfer(_pnl, "in_node")
    h_out = _make_transfer(_pnl, "out_node")
    all_curated_tools["add_linear_processing_pathway"](
        {"composition": h_comp, "pathway": [h_in, h_out]}
    )

    rev_before = handles.get_revision(h_comp)
    all_curated_tools["run_composition"](
        composition=h_comp, inputs={h_in: [[1.0]]}
    )
    assert handles.get_revision(h_comp) == rev_before


# ---- get_composition_revision tool ---------------------------------------- #


@pytest.mark.integration
def test_get_composition_revision_reports_current_count(
    all_curated_tools, _pnl
):
    h_comp = _make_composition(_pnl)
    h_a = _make_transfer(_pnl, "a")

    out0 = all_curated_tools["get_composition_revision"](composition=h_comp)
    assert out0 == {"composition": h_comp, "revision": 0}

    all_curated_tools["add_node"]({"composition": h_comp, "node": h_a})
    out1 = all_curated_tools["get_composition_revision"](composition=h_comp)
    assert out1 == {"composition": h_comp, "revision": 1}


@pytest.mark.integration
def test_get_composition_revision_rejects_non_composition(
    all_curated_tools, _pnl
):
    h_mech = _make_transfer(_pnl, "solo")
    with pytest.raises(ValueError, match="not a Composition handle"):
        all_curated_tools["get_composition_revision"](composition=h_mech)


# ---- render_composition_graph: format paths ------------------------------- #


@_NEEDS_DOT
@pytest.mark.integration
def test_render_composition_graph_png_returns_data_url(
    all_curated_tools, _pnl, _gv
):
    h_comp = _make_composition(_pnl)
    h_a = _make_transfer(_pnl, "png_a")
    all_curated_tools["add_node"]({"composition": h_comp, "node": h_a})

    out = all_curated_tools["render_composition_graph"](
        composition=h_comp, fmt="png"
    )
    assert out["composition"] == h_comp
    assert out["format"] == "png"
    assert out["mime"] == "image/png"
    assert out["data_url"].startswith("data:image/png;base64,")
    assert out["n_nodes"] >= 1
    # Revision was bumped by add_node and is reported back.
    assert out["revision"] == 1
    # The bytes are valid base64 of a non-trivial PNG (PNG magic bytes).
    raw = base64.b64decode(out["data_url"].split(",", 1)[1])
    assert raw.startswith(b"\x89PNG\r\n\x1a\n")


@_NEEDS_DOT
@pytest.mark.integration
def test_render_composition_graph_svg_returns_xml_data_url(
    all_curated_tools, _pnl, _gv
):
    h_comp = _make_composition(_pnl)
    h_a = _make_transfer(_pnl, "svg_a")
    all_curated_tools["add_node"]({"composition": h_comp, "node": h_a})

    out = all_curated_tools["render_composition_graph"](
        composition=h_comp, fmt="svg"
    )
    assert out["mime"] == "image/svg+xml"
    assert out["data_url"].startswith("data:image/svg+xml;base64,")
    raw = base64.b64decode(out["data_url"].split(",", 1)[1]).decode("utf-8")
    assert "<svg" in raw


@pytest.mark.integration
def test_render_composition_graph_dot_returns_dot_source(
    all_curated_tools, _pnl, _gv
):
    """The ``dot`` text format never invokes the ``dot`` binary, so this
    runs even on machines without graphviz installed."""
    h_comp = _make_composition(_pnl)
    h_a = _make_transfer(_pnl, "dot_a")
    all_curated_tools["add_node"]({"composition": h_comp, "node": h_a})

    out = all_curated_tools["render_composition_graph"](
        composition=h_comp, fmt="dot"
    )
    assert out["mime"] == "text/vnd.graphviz"
    assert out["data_url"].startswith("data:text/vnd.graphviz;base64,")
    decoded = base64.b64decode(out["data_url"].split(",", 1)[1]).decode("utf-8")
    assert "digraph" in decoded


# ---- render_composition_graph: error paths -------------------------------- #


@pytest.mark.integration
def test_render_composition_graph_rejects_non_composition_handle(
    all_curated_tools, _pnl
):
    h_mech = _make_transfer(_pnl, "solo")
    with pytest.raises(ValueError, match="not a Composition handle"):
        all_curated_tools["render_composition_graph"](
            composition=h_mech, fmt="dot"
        )


@pytest.mark.integration
def test_render_composition_graph_rejects_unknown_handle(
    all_curated_tools, _pnl
):
    with pytest.raises(KeyError):
        all_curated_tools["render_composition_graph"](
            composition="h_deadbeefcafe", fmt="dot"
        )


@pytest.mark.integration
def test_render_composition_graph_unknown_format_errors(
    all_curated_tools, _pnl
):
    h_comp = _make_composition(_pnl)
    with pytest.raises(ValueError, match="unknown fmt"):
        all_curated_tools["render_composition_graph"](
            composition=h_comp, fmt="bmp"
        )


@pytest.mark.integration
def test_render_composition_graph_raises_runtime_error_when_dot_missing(
    all_curated_tools, _pnl, _gv, monkeypatch
):
    """Simulate a machine without the ``dot`` binary by monkeypatching
    ``graphviz.Digraph.pipe`` to raise ``ExecutableNotFound``. Confirms
    the curated tool repackages it as a friendly ``RuntimeError`` with
    the install hint, instead of leaking the bare graphviz exception.
    """
    h_comp = _make_composition(_pnl)
    h_a = _make_transfer(_pnl, "missing_dot")
    all_curated_tools["add_node"]({"composition": h_comp, "node": h_a})

    def _boom(self, *args, **kwargs):  # noqa: ARG001
        raise _gv.ExecutableNotFound(["dot"])

    monkeypatch.setattr(_gv.Digraph, "pipe", _boom)

    with pytest.raises(RuntimeError, match="graphviz"):
        all_curated_tools["render_composition_graph"](
            composition=h_comp, fmt="png"
        )
