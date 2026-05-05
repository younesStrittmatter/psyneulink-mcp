"""Integration tests: ``load_python_script`` (replay + exec modes).

Replay mode round-trips a file written by :func:`export_python_script`
through the same MCP tool implementations, with handle strings rewritten
as new handles get minted. Exec mode loads a hand-written ``.py`` file
that was never journalled and registers any PNL objects it finds in the
module globals.

Marked ``integration`` because both modes import psyneulink.
"""

from __future__ import annotations

import re
import textwrap
from pathlib import Path
from typing import Any

import pytest

from psyneulink_mcp import feedback, handles
from psyneulink_mcp.tools.curated import composition as curated_composition
from psyneulink_mcp.tools.curated import persistence as curated_persistence

pytestmark = pytest.mark.integration


@pytest.fixture(autouse=True)
def _isolate_feedback_log(monkeypatch, tmp_path):
    monkeypatch.setenv(
        feedback.ENV_FEEDBACK_PATH, str(tmp_path / "issues.jsonl")
    )


class FakeMCP:
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
    curated_persistence.register(mcp)
    from psyneulink_mcp.tools.generated import (
        composition_add_linear_processing_pathway as _gen_pathway,
    )
    from psyneulink_mcp.tools.generated import (
        composition_add_node as _gen_add_node,
    )
    _gen_add_node.register(mcp)
    _gen_pathway.register(mcp)
    yield mcp.tools
    handles.clear_handles()


def _make_transfer_via_generated(name: str) -> str:
    from psyneulink_mcp.tools.generated import transfer_mechanism as t_mod

    return t_mod._impl({"name": name})["handle"]


def _make_composition_via_generated(name: str = "comp") -> str:
    from psyneulink_mcp.tools.generated import composition as c_mod

    return c_mod._impl({"name": name})["handle"]


_HANDLE_RE = re.compile(r"h_[0-9a-f]{12}")


def _strip_handle_ids(text: str) -> str:
    """Replace every ``h_<12 hex>`` with ``h_<HANDLE>`` for compare."""
    return _HANDLE_RE.sub("h_<HANDLE>", text)


def test_replay_mode_rebuilds_objects_from_journal(tools, tmp_path):
    h_in = _make_transfer_via_generated("replay_in")
    h_hidden = _make_transfer_via_generated("replay_hidden")
    h_out = _make_transfer_via_generated("replay_out")
    h_comp = _make_composition_via_generated("replay_comp")
    tools["add_linear_processing_pathway"](
        {"composition": h_comp, "pathway": [h_in, h_hidden, h_out]}
    )

    out_path = tmp_path / "model.py"
    first_export = tools["export_python_script"](
        composition=h_comp, path=str(out_path)
    )
    first_text = first_export["text"]

    # Wipe both the handle registry AND the journal — this simulates
    # loading the model into a fresh MCP subprocess.
    handles.clear_handles()
    assert handles.list_handles() == []
    assert handles.journal_snapshot() == []

    result = tools["load_python_script"](path=str(out_path))
    assert result["mode"] == "replay"
    assert "replayed" in result["summary"]
    assert "from journal" in result["summary"]

    handles_by_var = result["handles"]
    types = {payload["type"] for payload in handles_by_var.values()}
    assert "TransferMechanism" in types
    assert "Composition" in types

    # PsyNeuLink may suffix duplicate names within the same process
    # (e.g. ``replay_in`` → ``replay_in-1``); strip the trailing
    # ``-N`` before comparing for the round-trip check.
    def _base(name: str) -> str:
        return re.sub(r"-\d+$", "", name)

    names = {_base(payload["name"]) for payload in handles_by_var.values()}
    for expected in ("replay_in", "replay_hidden", "replay_out", "replay_comp"):
        assert expected in names

    # Re-export and compare the *structured* journals modulo handle IDs
    # and PNL's per-process name suffixing. Comparing raw text is too
    # fragile here: PNL keeps a global name registry that survives our
    # ``clear_handles()`` (it lives on the PNL classes themselves), so
    # the second-export run sees ``replay_comp`` already taken and
    # rebrands the new instance ``replay_comp-1``. Compare the journal
    # entry shapes instead.
    new_comp_handle = next(
        h["handle"]
        for h in handles_by_var.values()
        if h["type"] == "Composition"
    )
    second_path = tmp_path / "model_v2.py"
    second_export = tools["export_python_script"](
        composition=new_comp_handle, path=str(second_path)
    )

    def _journal_shape(text: str) -> list[tuple[str, str, list[str]]]:
        """Each entry as ``(tool_name, tool_layer, sorted(arg_keys))``."""
        decoded = curated_persistence._decode_journal_block(text)
        assert decoded is not None
        return [
            (e["tool_name"], e["tool_layer"], sorted((e["args"] or {}).keys()))
            for e in decoded
        ]

    assert _journal_shape(first_text) == _journal_shape(second_export["text"])


def test_replay_skips_run_composition(tools, tmp_path):
    """Loading a model must not silently re-execute it."""
    h_in = _make_transfer_via_generated("noexec_in")
    h_out = _make_transfer_via_generated("noexec_out")
    h_comp = _make_composition_via_generated("noexec_comp")
    tools["add_linear_processing_pathway"]({"composition": h_comp, "pathway": [h_in, h_out]})
    tools["run_composition"](composition=h_comp, inputs={h_in: [[1.0]]})

    out_path = tmp_path / "noexec.py"
    tools["export_python_script"](composition=h_comp, path=str(out_path))

    handles.clear_handles()
    result = tools["load_python_script"](path=str(out_path))

    assert result["mode"] == "replay"
    skipped_summary = " ".join(result["skipped"])
    assert "run_composition" in skipped_summary
    # The model was loaded but never run, so the composition's
    # ``.results`` list should be empty (or at least not contain the
    # original-session run output).
    comp_payload = next(
        p for p in result["handles"].values() if p["type"] == "Composition"
    )
    new_comp = handles.resolve_handle(comp_payload["handle"])
    assert not getattr(new_comp, "results", []), (
        "load_python_script accidentally ran the model — "
        "run_composition entries must be skipped on replay"
    )


def test_exec_mode_registers_handcrafted_pnl_objects(tools, tmp_path):
    """No journal block → fall back to exec mode and walk module globals."""
    script = textwrap.dedent(
        '''\
        """Hand-written PNL model — no MCP journal block."""
        import psyneulink as pnl

        in_node = pnl.TransferMechanism(name="exec_in")
        out_node = pnl.TransferMechanism(name="exec_out")
        comp = pnl.Composition(name="exec_comp")
        comp.add_linear_processing_pathway([in_node, out_node])
        '''
    )
    script_path = tmp_path / "handwritten.py"
    script_path.write_text(script)

    handles.clear_handles()
    result = tools["load_python_script"](path=str(script_path))

    assert result["mode"] == "exec"
    assert "warning" in result
    assert "trust" in result["warning"]

    handles_by_var = result["handles"]
    assert "in_node" in handles_by_var
    assert "out_node" in handles_by_var
    assert "comp" in handles_by_var

    assert handles_by_var["in_node"]["type"] == "TransferMechanism"
    assert handles_by_var["comp"]["type"] == "Composition"


def test_load_rejects_missing_or_non_py(tools, tmp_path):
    with pytest.raises(FileNotFoundError):
        tools["load_python_script"](path=str(tmp_path / "no_such.py"))

    not_py = tmp_path / "model.txt"
    not_py.write_text("not python")
    with pytest.raises(ValueError, match=r"must end in \.py"):
        tools["load_python_script"](path=str(not_py))


def test_replay_handles_filtered_export(tools, tmp_path):
    """A composition-filtered export must replay successfully."""
    h_in = _make_transfer_via_generated("filt_in")
    h_out = _make_transfer_via_generated("filt_out")
    h_comp = _make_composition_via_generated("filt_comp")
    tools["add_linear_processing_pathway"]({"composition": h_comp, "pathway": [h_in, h_out]})
    # Add an unrelated mechanism that should NOT appear in the filtered export.
    _make_transfer_via_generated("filt_unrelated")

    out_path = tmp_path / "filt.py"
    tools["export_python_script"](composition=h_comp, path=str(out_path))

    handles.clear_handles()
    result = tools["load_python_script"](path=str(out_path))

    names = {
        re.sub(r"-\d+$", "", payload["name"])
        for payload in result["handles"].values()
    }
    assert "filt_in" in names
    assert "filt_out" in names
    assert "filt_comp" in names
    assert "filt_unrelated" not in names
