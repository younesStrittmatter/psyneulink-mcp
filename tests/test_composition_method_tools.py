"""Integration tests for the *generated* Composition-method tools.

The three composition-mutating surfaces — ``add_node``,
``add_projection``, ``add_linear_processing_pathway`` — used to live in
``tools/curated/composition.py``. They migrated to the generated layer
once captured failures gave the regen loop enough signal to warrant
iterating on. The runtime behaviour they share now lives in
:mod:`psyneulink_mcp.method_helpers`.

These tests target the helper directly because that's the unit
boundary that owns the interesting behaviour (defensive
sender/receiver pre-add, ``DuplicateProjectionError`` swallow,
revision bumping, journal recording). The generated modules are thin
shims that just call into the helper.

Marked ``integration`` because they import psyneulink.
"""

from __future__ import annotations

from typing import Any

import pytest

from psyneulink_mcp import feedback, handles, method_helpers

pytestmark = pytest.mark.integration


@pytest.fixture(autouse=True)
def _isolate_feedback_log(monkeypatch, tmp_path):
    monkeypatch.setenv(
        feedback.ENV_FEEDBACK_PATH, str(tmp_path / "issues.jsonl")
    )


@pytest.fixture(autouse=True)
def _clear_handles():
    handles.clear_handles()
    yield
    handles.clear_handles()


def _comp(name: str = "test_comp"):
    import psyneulink as pnl

    return handles.register_handle(pnl.Composition(name=name))["handle"]


def _transfer(name: str, default_variable=None):
    import psyneulink as pnl

    kwargs: dict[str, Any] = {"name": name}
    if default_variable is not None:
        kwargs["default_variable"] = default_variable
    return handles.register_handle(pnl.TransferMechanism(**kwargs))["handle"]


def _name_of(handle: str) -> str:
    return handles.resolve_handle(handle).name


# --------------------------------------------------------------------------- #
# add_node                                                                    #
# --------------------------------------------------------------------------- #


def test_add_node_appears_in_composition():
    import psyneulink as pnl

    h_comp = _comp()
    h_node = _transfer("a")
    result = method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_node",
        kwargs={"composition": h_comp, "node": h_node},
        tool_name="add_node",
    )
    assert isinstance(result, dict)
    comp = handles.resolve_handle(h_comp)
    assert any(getattr(n, "name", None) == _name_of(h_node) for n in comp.nodes)


def test_add_node_bumps_revision():
    import psyneulink as pnl

    h_comp = _comp()
    assert handles.get_revision(h_comp) == 0
    h_node = _transfer("a")
    method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_node",
        kwargs={"composition": h_comp, "node": h_node},
        tool_name="add_node",
    )
    assert handles.get_revision(h_comp) == 1


def test_add_node_journal_records_generated_layer():
    import psyneulink as pnl

    h_comp = _comp()
    h_node = _transfer("a")
    method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_node",
        kwargs={"composition": h_comp, "node": h_node},
        tool_name="add_node",
    )
    snapshot = handles.journal_snapshot()
    assert snapshot
    last = snapshot[-1]
    assert last.tool_name == "add_node"
    assert last.tool_layer == "generated"
    # journal preserves PRE-resolved kwargs (handle strings, not objects)
    assert last.args["composition"] == h_comp
    assert last.args["node"] == h_node


# --------------------------------------------------------------------------- #
# add_projection                                                              #
# --------------------------------------------------------------------------- #


def test_add_projection_with_keyword_matrix_succeeds():
    """Captured failure: ``matrix='IDENTITY_MATRIX'`` on the curated tool
    blew up with ``'matrix' is not in MappingProjection.parameter_ports``.
    The helper translates it to ``default_matrix`` and routes through
    ``Composition.add_projection`` directly, sidestepping the
    deferred-MappingProjection bug."""
    import psyneulink as pnl

    h_a = _transfer("ka")
    h_b = _transfer("kb")
    h_comp = _comp(name="kw_comp")

    result = method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_projection",
        kwargs={
            "composition": h_comp,
            "sender": h_a,
            "receiver": h_b,
            "matrix": "IDENTITY_MATRIX",
        },
        tool_name="add_projection",
    )
    assert result is not None
    comp = handles.resolve_handle(h_comp)
    # both endpoints should be in the composition; the helper added them defensively
    names = {n.name for n in comp.nodes}
    assert _name_of(h_a) in names
    assert _name_of(h_b) in names
    assert handles.get_revision(h_comp) == 1


def test_add_projection_auto_adds_sender_and_receiver():
    """Captured failure: agents called add_projection before adding the
    endpoints. The helper now pre-adds both."""
    import psyneulink as pnl

    h_a = _transfer("aa_a")
    h_b = _transfer("aa_b")
    h_comp = _comp(name="aa_comp")
    comp = handles.resolve_handle(h_comp)
    assert len(comp.nodes) == 0

    method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_projection",
        kwargs={
            "composition": h_comp,
            "sender": h_a,
            "receiver": h_b,
            "default_matrix": [[2.0]],
        },
        tool_name="add_projection",
    )
    names = {n.name for n in comp.nodes}
    assert _name_of(h_a) in names
    assert _name_of(h_b) in names


def test_add_projection_duplicate_is_noop_success():
    """Captured failure: agents retried add_projection for an already-wired
    pair and got DuplicateProjectionError. Helper swallows it."""
    import psyneulink as pnl

    h_a = _transfer("dup_a")
    h_b = _transfer("dup_b")
    h_comp = _comp(name="dup_comp")

    first = method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_projection",
        kwargs={
            "composition": h_comp,
            "sender": h_a,
            "receiver": h_b,
            "default_matrix": [[1.0]],
        },
        tool_name="add_projection",
    )
    assert first is not None

    second = method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_projection",
        kwargs={
            "composition": h_comp,
            "sender": h_a,
            "receiver": h_b,
            "default_matrix": [[1.0]],
        },
        tool_name="add_projection",
    )
    # Either an exception-swallowed status dict or a returned existing
    # projection (PNL versions vary). Either shape must NOT raise.
    if isinstance(second, dict) and second.get("duplicate"):
        assert second["composition"] == h_comp
    else:
        # PNL silently returned the existing Projection — also acceptable.
        assert second is not None

    # Revision bumped twice: once per call (even no-op duplicates count
    # as a revision bump because the agent's intent was registered).
    assert handles.get_revision(h_comp) == 2


def test_add_projection_records_generated_layer():
    import psyneulink as pnl

    h_a = _transfer("rc_proj_a")
    h_b = _transfer("rc_proj_b")
    h_comp = _comp(name="rc_proj_comp")

    method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_projection",
        kwargs={
            "composition": h_comp,
            "sender": h_a,
            "receiver": h_b,
            "matrix": "IDENTITY_MATRIX",
        },
        tool_name="add_projection",
    )

    snapshot = handles.journal_snapshot()
    assert snapshot
    last = snapshot[-1]
    assert last.tool_name == "add_projection"
    assert last.tool_layer == "generated"
    # ``matrix`` (the original kwarg) is preserved verbatim in the
    # journal — that's what export_python_script needs.
    assert last.args.get("matrix") == "IDENTITY_MATRIX"


# --------------------------------------------------------------------------- #
# add_linear_processing_pathway                                               #
# --------------------------------------------------------------------------- #


def test_add_linear_processing_pathway_runs_end_to_end():
    """Tool produces a real Pathway and the composition runs."""
    import psyneulink as pnl

    h_in = _transfer("lp_in")
    h_hidden = _transfer("lp_hidden")
    h_out = _transfer("lp_out")
    h_comp = _comp(name="lp_comp")

    method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_linear_processing_pathway",
        kwargs={
            "composition": h_comp,
            "pathway": [h_in, h_hidden, h_out],
        },
        tool_name="add_linear_processing_pathway",
    )
    comp = handles.resolve_handle(h_comp)
    names = {n.name for n in comp.nodes}
    for h in (h_in, h_hidden, h_out):
        assert _name_of(h) in names

    out = comp.run(inputs={handles.resolve_handle(h_in): [[1.0]]})
    assert out is not None
    assert handles.get_revision(h_comp) == 1


def test_add_linear_processing_pathway_records_generated_layer():
    import psyneulink as pnl

    h_a = _transfer("lpr_a")
    h_b = _transfer("lpr_b")
    h_comp = _comp(name="lpr_comp")

    method_helpers.call_method_tool(
        owner_cls=pnl.Composition,
        method_name="add_linear_processing_pathway",
        kwargs={"composition": h_comp, "pathway": [h_a, h_b]},
        tool_name="add_linear_processing_pathway",
    )

    snapshot = handles.journal_snapshot()
    assert snapshot
    last = snapshot[-1]
    assert last.tool_name == "add_linear_processing_pathway"
    assert last.tool_layer == "generated"


# --------------------------------------------------------------------------- #
# Helper input validation                                                     #
# --------------------------------------------------------------------------- #


def test_call_method_tool_rejects_missing_composition_kwarg():
    import psyneulink as pnl

    with pytest.raises(ValueError, match="composition"):
        method_helpers.call_method_tool(
            owner_cls=pnl.Composition,
            method_name="add_node",
            kwargs={"node": "h_dontexist"},
            tool_name="add_node",
        )


def test_call_method_tool_rejects_wrong_owner_class():
    """If the agent passes a Mechanism handle where a Composition is
    expected, fail clearly rather than calling the wrong attribute."""
    import psyneulink as pnl

    h_node = _transfer("wrong_owner")
    with pytest.raises(TypeError, match="Composition"):
        method_helpers.call_method_tool(
            owner_cls=pnl.Composition,
            method_name="add_node",
            kwargs={"composition": h_node, "node": h_node},
            tool_name="add_node",
        )


# --------------------------------------------------------------------------- #
# Generated module wires straight to the helper                               #
# --------------------------------------------------------------------------- #


def test_generated_module_dispatches_through_helper():
    """Smoke: the regen-emitted ``composition_add_node._impl`` reaches the
    same code path as a direct ``call_method_tool`` invocation.
    """
    from psyneulink_mcp.tools.generated import composition_add_node

    h_comp = _comp(name="gm_comp")
    h_node = _transfer("gm_node")
    composition_add_node._impl(
        {"composition": h_comp, "node": h_node}
    )
    comp = handles.resolve_handle(h_comp)
    assert any(n.name == _name_of(h_node) for n in comp.nodes)
    assert handles.get_revision(h_comp) == 1
