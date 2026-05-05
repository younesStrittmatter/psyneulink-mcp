"""Integration tests: ``export_python_script`` against real PsyNeuLink.

We build a tiny composition through the curated tools, export it, and
both lint the rendered file and shell out to ``python <file>`` to prove
it actually runs standalone (the contract from
``plans/mdf-loader.md``).

Marked ``integration`` because ``import psyneulink`` is slow.
"""

from __future__ import annotations

import base64
import json
import subprocess
import sys
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
    yield mcp.tools
    handles.clear_handles()


def _make_transfer_via_generated(name: str) -> str:
    """Create a TransferMechanism via the *generated* tool's ``_impl``.

    Going through the generated tool — not just calling
    ``handles.register_handle(pnl.TransferMechanism(...))`` — is what
    populates the session journal with a ``create_transfer_mechanism``
    entry, which is the whole point of these tests.
    """
    from psyneulink_mcp.tools.generated import transfer_mechanism as t_mod

    payload = t_mod._impl({"name": name})
    return payload["handle"]


def _make_composition_via_generated(name: str = "comp") -> str:
    from psyneulink_mcp.tools.generated import composition as c_mod

    payload = c_mod._impl({"name": name})
    return payload["handle"]


def test_export_writes_runnable_script_with_journal_block(tools, tmp_path):
    h_in = _make_transfer_via_generated("in_node")
    h_hidden = _make_transfer_via_generated("hidden")
    h_out = _make_transfer_via_generated("out_node")
    h_comp = _make_composition_via_generated("c")

    tools["add_linear_pathway"](
        composition=h_comp, nodes=[h_in, h_hidden, h_out]
    )
    tools["run_composition"](composition=h_comp, inputs={h_in: [[1.0]]})

    out_path = tmp_path / "model.py"
    result = tools["export_python_script"](
        composition=h_comp, path=str(out_path)
    )

    assert result["path"] == str(out_path)
    assert out_path.exists()
    text = out_path.read_text()

    assert text == result["text"]
    assert result["n_objects"] == 4  # 3 mechanisms + 1 composition
    assert result["n_operations"] == 2  # add_linear_pathway + run_composition

    assert "import psyneulink as pnl" in text
    assert "pnl.TransferMechanism(" in text
    assert "pnl.Composition(" in text
    assert "add_linear_processing_pathway" in text
    assert 'if __name__ == "__main__":' in text
    assert ".run(" in text
    assert 'print("results:"' in text

    assert "# psyneulink-mcp:journal" in text
    assert "# psyneulink-mcp:end-journal" in text


def test_journal_block_round_trips_through_json(tools, tmp_path):
    h_a = _make_transfer_via_generated("a")
    h_b = _make_transfer_via_generated("b")
    h_comp = _make_composition_via_generated("rt")
    tools["add_node"](composition=h_comp, node=h_a)
    tools["add_node"](composition=h_comp, node=h_b)

    out_path = tmp_path / "rt.py"
    result = tools["export_python_script"](path=str(out_path))
    text = result["text"]

    begin = text.index("# psyneulink-mcp:journal")
    end = text.index("# psyneulink-mcp:end-journal")
    body = text[begin + len("# psyneulink-mcp:journal") : end]
    encoded = "".join(
        line.lstrip("#").strip() for line in body.splitlines() if line.strip()
    )

    decoded = json.loads(base64.b64decode(encoded.encode()).decode())
    assert isinstance(decoded, list)
    tool_names = [e["tool_name"] for e in decoded]
    assert tool_names.count("create_transfer_mechanism") == 2
    assert tool_names.count("create_composition") == 1
    assert tool_names.count("add_node") == 2
    # Handle strings inside args were preserved verbatim:
    add_entries = [e for e in decoded if e["tool_name"] == "add_node"]
    add_handles = {e["args"]["node"] for e in add_entries}
    assert add_handles == {h_a, h_b}


def test_exported_script_runs_standalone(tools, tmp_path):
    h_in = _make_transfer_via_generated("standalone_in")
    h_out = _make_transfer_via_generated("standalone_out")
    h_comp = _make_composition_via_generated("standalone_comp")
    tools["add_linear_pathway"](composition=h_comp, nodes=[h_in, h_out])
    tools["run_composition"](composition=h_comp, inputs={h_in: [[1.0]]})

    out_path = tmp_path / "runnable.py"
    tools["export_python_script"](composition=h_comp, path=str(out_path))

    proc = subprocess.run(
        [sys.executable, str(out_path)],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert proc.returncode == 0, (
        f"exported script failed:\nstdout={proc.stdout!r}\nstderr={proc.stderr!r}"
    )
    assert "results:" in proc.stdout


def test_default_path_under_psyneulink_models(tools, tmp_path, monkeypatch):
    """Default path lands under the per-user models dir with a UTC stamp."""
    h_comp = _make_composition_via_generated("default_path")
    monkeypatch.setattr(
        curated_persistence, "_DEFAULT_EXPORT_DIR", tmp_path / "models"
    )

    result = tools["export_python_script"](composition=h_comp)
    out_path = Path(result["path"])
    assert out_path.parent == tmp_path / "models"
    assert out_path.suffix == ".py"
    assert out_path.exists()


def test_path_must_end_in_py(tools, tmp_path):
    h_comp = _make_composition_via_generated("badpath")
    with pytest.raises(ValueError, match=r"must end in \.py"):
        tools["export_python_script"](
            composition=h_comp, path=str(tmp_path / "model.txt")
        )


def test_dry_run_returns_text_without_writing_file(tools, tmp_path):
    """``dry_run=True`` is the live-preview path: render the script and
    hand back the text *without* persisting anything. Front-ends like the
    UI's code pane poll this on every composition revision; an actual
    write per poll would litter ``~/Documents/psyneulink-models/`` with
    junk files (and race the same default path).
    """
    h_in = _make_transfer_via_generated("dry_in")
    h_out = _make_transfer_via_generated("dry_out")
    h_comp = _make_composition_via_generated("dry_comp")
    tools["add_linear_pathway"](composition=h_comp, nodes=[h_in, h_out])

    sentinel_path = tmp_path / "should_not_be_written.py"

    result = tools["export_python_script"](
        composition=h_comp, path=str(sentinel_path), dry_run=True
    )

    assert result["path"] is None
    assert "import psyneulink as pnl" in result["text"]
    assert "dry_in" in result["text"]
    assert "dry_out" in result["text"]
    assert result["n_objects"] == 3  # 2 mechanisms + 1 composition
    assert result["n_operations"] == 1
    # ``path`` was supplied but dry_run takes precedence — nothing on disk.
    assert not sentinel_path.exists()
    # Default-path branch is also skipped.
    assert not (_default_export_dir := tmp_path / "models").exists()


def test_dry_run_without_path_does_not_create_default_dir(tools, tmp_path, monkeypatch):
    """Even without ``path``, dry_run must not touch the default export dir."""
    monkeypatch.setattr(
        curated_persistence, "_DEFAULT_EXPORT_DIR", tmp_path / "untouched"
    )
    h_comp = _make_composition_via_generated("nopath_dry")

    result = tools["export_python_script"](composition=h_comp, dry_run=True)

    assert result["path"] is None
    assert "import psyneulink as pnl" in result["text"]
    assert not (tmp_path / "untouched").exists()


def test_dry_run_text_matches_real_export(tools, tmp_path):
    """``dry_run=True`` renders byte-for-byte the same script the
    write-to-disk path would produce. If the two ever drift, the live
    preview pane would lie about what saving the model produces."""
    h_in = _make_transfer_via_generated("parity_in")
    h_out = _make_transfer_via_generated("parity_out")
    h_comp = _make_composition_via_generated("parity_comp")
    tools["add_linear_pathway"](composition=h_comp, nodes=[h_in, h_out])

    real = tools["export_python_script"](
        composition=h_comp, path=str(tmp_path / "real.py")
    )
    dry = tools["export_python_script"](composition=h_comp, dry_run=True)

    assert dry["text"] == real["text"]
    assert dry["n_objects"] == real["n_objects"]
    assert dry["n_operations"] == real["n_operations"]


def test_filter_excludes_unrelated_objects(tools, tmp_path):
    h_in = _make_transfer_via_generated("filtered_in")
    h_out = _make_transfer_via_generated("filtered_out")
    h_comp = _make_composition_via_generated("filtered_comp")
    tools["add_linear_pathway"](composition=h_comp, nodes=[h_in, h_out])

    h_unrelated = _make_transfer_via_generated("unrelated_node")

    out_path = tmp_path / "filt.py"
    result = tools["export_python_script"](
        composition=h_comp, path=str(out_path)
    )
    text = result["text"]

    # `unrelated_node` was never wired into `filtered_comp` so the
    # filtered render should leave it out.
    assert "unrelated_node" not in text
    assert "filtered_in" in text
    assert "filtered_out" in text
    # Sanity check: omitting the filter pulls it back in.
    full_path = tmp_path / "all.py"
    result_all = tools["export_python_script"](path=str(full_path))
    assert "unrelated_node" in result_all["text"]
    # Make sure the unused unrelated handle didn't cause a NameError.
    _ = h_unrelated
