"""Unit tests for the per-process session journal in ``handles``.

These exercise the journal mechanics directly — no PsyNeuLink import,
no MCP wiring — so they're cheap, deterministic, and easy to keep
running on every save.
"""

from __future__ import annotations

import warnings

import pytest

from psyneulink_mcp import handles


@pytest.fixture(autouse=True)
def _reset_registry():
    handles.clear_handles()
    handles._JOURNAL_CAP_WARNED = False
    yield
    handles.clear_handles()
    handles._JOURNAL_CAP_WARNED = False


def test_record_call_appends_entry_with_handle_strings_preserved():
    handles.record_call(
        "create_transfer_mechanism",
        {"name": "x", "input_shapes": 2},
        result_handle="h_aaaaaaaaaaaa",
        tool_layer="generated",
    )
    handles.record_call(
        "add_node",
        {"composition": "h_bbbbbbbbbbbb", "node": "h_aaaaaaaaaaaa"},
        tool_layer="curated",
    )

    snap = handles.journal_snapshot()
    assert len(snap) == 2
    assert snap[0].tool_name == "create_transfer_mechanism"
    assert snap[0].args == {"name": "x", "input_shapes": 2}
    assert snap[0].result_handle == "h_aaaaaaaaaaaa"
    assert snap[0].tool_layer == "generated"
    # Handle strings inside args are NOT resolved — that's the contract.
    assert snap[1].args["node"] == "h_aaaaaaaaaaaa"
    assert snap[1].tool_layer == "curated"
    assert snap[1].result_handle is None


def test_journal_snapshot_returns_a_copy():
    handles.record_call("a", {})
    snap = handles.journal_snapshot()
    snap.clear()
    assert len(handles.journal_snapshot()) == 1


def test_record_call_deep_copies_args():
    """Caller-side mutation must not leak into the recorded entry.

    The generated-tool template hands the same kwargs dict to
    ``handles.resolve_in`` (which mutates dict values in place during
    rehydration) and then to ``record_call``. Without a deep copy the
    recorded args would silently turn into live PNL objects.
    """
    args = {"nested": {"x": 1, "list": [1, 2, 3]}}
    handles.record_call("tool", args)

    args["nested"]["x"] = 999
    args["nested"]["list"].append(99)

    snap = handles.journal_snapshot()
    assert snap[0].args == {"nested": {"x": 1, "list": [1, 2, 3]}}


def test_clear_handles_clears_journal_too():
    handles.record_call("a", {})
    handles.record_call("b", {})
    assert len(handles.journal_snapshot()) == 2
    handles.clear_handles()
    assert handles.journal_snapshot() == []


def test_clear_journal_returns_count():
    handles.record_call("a", {})
    handles.record_call("b", {})
    handles.record_call("c", {})
    assert handles.clear_journal() == 3
    assert handles.journal_snapshot() == []


def test_cap_warning_fires_once(monkeypatch):
    """Crossing ``_JOURNAL_CAP`` warns exactly once per process."""
    monkeypatch.setattr(handles, "_JOURNAL_CAP", 3)

    for _ in range(3):
        handles.record_call("noisy", {})

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        handles.record_call("noisy", {})  # crosses the cap → warns
        handles.record_call("noisy", {})  # over the cap, but already warned
        handles.record_call("noisy", {})

    cap_warnings = [w for w in caught if "session journal exceeded" in str(w.message)]
    assert len(cap_warnings) == 1
    assert handles._JOURNAL_CAP_WARNED is True
