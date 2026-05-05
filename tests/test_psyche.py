"""Tests for the curated PSYCHE tools.

Most of the surface here touches PNL (composition runs / fits) or
pandas (DataFrame loading); those tests are marked ``integration`` and
gated behind ``pytest.importorskip("psyneulink_psyche")`` so the suite
degrades gracefully when the optional ``[psyche]`` extra isn't
installed.

A small number of pure-Python tests cover the registration surface and
the ``method='de'/'pec'`` rejection path — they don't need PNL or
psyche and run unconditionally.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from psyneulink_mcp import feedback, handles
from psyneulink_mcp.tools.curated import psyche as curated_psyche

# --------------------------------------------------------------------------- #
# fixtures                                                                    #
# --------------------------------------------------------------------------- #


@pytest.fixture(autouse=True)
def _isolate_feedback_log(monkeypatch, tmp_path):
    """Steer captured-tool error logging into a tmp file so tests that
    deliberately raise (validation errors, max_evaluations guard, etc.)
    don't pollute the dev's real ``feedback/pending/issues.jsonl``."""
    monkeypatch.setenv(
        feedback.ENV_FEEDBACK_PATH, str(tmp_path / "issues.jsonl")
    )


class FakeMCP:
    """Capture registered tools so they're callable as plain functions."""

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
    curated_psyche.register(mcp)
    yield mcp.tools
    handles.clear_handles()


# --------------------------------------------------------------------------- #
# pure-Python tests (no PNL, no psyche extra required)                        #
# --------------------------------------------------------------------------- #


def test_psyche_tools_register_with_fake_mcp():
    """All four tools land in the FakeMCP tool dict."""
    mcp = FakeMCP()
    curated_psyche.register(mcp)
    assert set(mcp.tools) == {
        "describe_psyche_convention",
        "load_psyche_data",
        "run_composition_on_psyche",
        "fit_composition_to_psyche",
    }


def test_fit_composition_rejects_de(tools):
    """method='de' raises NotImplementedError before any handle resolution."""
    with pytest.raises(NotImplementedError, match="differential evolution"):
        tools["fit_composition_to_psyche"](
            composition="h_unused",
            data="h_unused",
            input_mapping={},
            output_mapping={},
            free_parameters={},
            method="de",
        )


def test_fit_composition_rejects_pec(tools):
    """method='pec' raises NotImplementedError before any handle resolution."""
    with pytest.raises(NotImplementedError, match="ParameterEstimationComposition"):
        tools["fit_composition_to_psyche"](
            composition="h_unused",
            data="h_unused",
            input_mapping={},
            output_mapping={},
            free_parameters={},
            method="pec",
        )


def test_fit_composition_rejects_unknown_method(tools):
    """Unknown methods raise ValueError, not NotImplementedError."""
    with pytest.raises(ValueError, match="unknown method"):
        tools["fit_composition_to_psyche"](
            composition="h_unused",
            data="h_unused",
            input_mapping={},
            output_mapping={},
            free_parameters={},
            method="random_search",
        )


# --------------------------------------------------------------------------- #
# psyche-only tests (need pandas + psyneulink_psyche, but not PNL)            #
# --------------------------------------------------------------------------- #

psyche = pytest.importorskip("psyneulink_psyche")
pd = pytest.importorskip("pandas")


def _valid_behavioral_rows(n_rows: int = 4, n_subjects: int = 2) -> Any:
    """Build a minimal DataFrame that satisfies BEHAVIORAL_DATA_CONVENTION.

    Keeps row identity unique by interleaving subjects across trials and
    using ``step=0`` everywhere (the single-step trial convention).
    """
    rows: list[dict[str, Any]] = []
    for trial_idx in range(n_rows):
        subject = f"S{trial_idx % n_subjects}"
        rows.append(
            {
                "subject_id": subject,
                "age": 25.0,
                "sex": "female",
                "gender": "woman",
                "subject_included": 1,
                "trial_global": trial_idx,
                "step": 0,
                "trial_block": 0,
                "trial_within_block": trial_idx,
                "exclude_trial_from_analysis": 0,
                "phase": "test",
                "correct_response": "A",
                "feedback": 1,
                "stimulus_id": f"stim_{trial_idx}",
                "stimulus_type": "text",
                "stimulus_spec": '{"text": "A"}',
                "response": "A",
                "correct": 1,
                "reaction_time": 0.5,
                "reaction_time_unit": "s",
                "reward": 1,
                "reward_value": 1.0,
                "reward_unit": "points",
            }
        )
    return pd.DataFrame(rows)


def test_describe_convention_returns_well_formed_payload(tools):
    payload = tools["describe_psyche_convention"]()
    assert payload["name"] == "Behavioral Data Standard"
    assert isinstance(payload["version"], str) and payload["version"]
    assert isinstance(payload["row_identity"], str)
    assert "subject_id" in payload["row_identity"]
    columns = payload["columns"]
    assert isinstance(columns, list) and len(columns) > 5
    column_names = {c["name"] for c in columns}
    assert {"subject_id", "trial_global", "step", "response"} <= column_names
    for col in columns:
        assert col["kind"] in {"base", "categorical", "numeric", "index"}
        assert isinstance(col["description"], str) and col["description"]


def test_describe_convention_unknown_name_raises(tools):
    with pytest.raises(ValueError, match="unknown psyche convention"):
        tools["describe_psyche_convention"](name="not-a-convention")


def test_load_psyche_data_csv_round_trip(tools, tmp_path):
    target = tmp_path / "behaviour.csv"
    df = _valid_behavioral_rows(n_rows=6, n_subjects=3)
    df.to_csv(target, index=False)

    out = tools["load_psyche_data"](path=str(target))
    assert out["n_rows"] == 6
    assert out["n_subjects"] == 3
    assert out["n_columns"] == len(df.columns)
    assert "subject_id" in out["columns"]
    handle = out["data_handle"]
    resolved = handles.resolve_handle(handle)
    assert isinstance(resolved, pd.DataFrame)
    assert len(resolved) == 6


def test_load_psyche_data_jsonl_format_autodetect(tools, tmp_path):
    target = tmp_path / "behaviour.jsonl"
    df = _valid_behavioral_rows(n_rows=3, n_subjects=1)
    df.to_json(target, orient="records", lines=True)

    out = tools["load_psyche_data"](path=str(target))
    assert out["n_rows"] == 3
    assert out["n_subjects"] == 1


def test_load_psyche_data_parquet_format_autodetect(tools, tmp_path):
    pyarrow = pytest.importorskip("pyarrow")
    del pyarrow
    target = tmp_path / "behaviour.parquet"
    df = _valid_behavioral_rows(n_rows=3, n_subjects=1)
    df.to_parquet(target, index=False)

    out = tools["load_psyche_data"](path=str(target))
    assert out["n_rows"] == 3


def test_load_psyche_data_explicit_format_overrides_extension(tools, tmp_path):
    target = tmp_path / "behaviour.txt"
    df = _valid_behavioral_rows(n_rows=2, n_subjects=1)
    df.to_csv(target, index=False)

    out = tools["load_psyche_data"](path=str(target), format="csv")
    assert out["n_rows"] == 2


def test_load_psyche_data_validation_error_surfaces(tools, tmp_path):
    """Missing required columns should bubble up as ValidationError."""
    target = tmp_path / "broken.csv"
    pd.DataFrame({"only_one_column": [1, 2, 3]}).to_csv(target, index=False)
    with pytest.raises(ValueError) as exc_info:
        tools["load_psyche_data"](path=str(target))
    assert "Missing required column" in str(exc_info.value)


def test_load_psyche_data_unknown_extension_errors(tools, tmp_path):
    target = tmp_path / "data.unknown_ext"
    target.write_text("a,b\n1,2\n")
    with pytest.raises(ValueError, match="auto-detect format"):
        tools["load_psyche_data"](path=str(target))


def test_load_psyche_data_missing_file_errors(tools, tmp_path):
    target = tmp_path / "missing.csv"
    with pytest.raises(FileNotFoundError):
        tools["load_psyche_data"](path=str(target))


# --------------------------------------------------------------------------- #
# integration tests (need PsyNeuLink)                                         #
# --------------------------------------------------------------------------- #


@pytest.fixture
def pnl_imported():
    """Import PNL once and skip the test if it isn't installed."""
    pnl = pytest.importorskip("psyneulink")
    return pnl


@pytest.fixture
def composition_with_one_input(pnl_imported, tools):
    """Single-Mechanism Composition + a 4-row valid behavioural DataFrame.

    The mechanism is a default ``TransferMechanism`` (1-D input, Linear
    function, slope=1, intercept=0, noise=0). Inputs come from a
    custom numeric column ``cue`` we tack onto the otherwise-canonical
    behavioural DataFrame; the convention permits extra columns
    (warnings only).
    """
    pnl = pnl_imported
    mech = pnl.TransferMechanism(name="m_in", default_variable=[0.0])
    comp = pnl.Composition(name="c_one")
    comp.add_node(mech)

    mech_handle = handles.register_handle(mech)["handle"]
    comp_handle = handles.register_handle(comp)["handle"]

    base = _valid_behavioral_rows(n_rows=4, n_subjects=1)
    base["cue"] = [0.5, 1.0, 1.5, 2.0]
    base["target_value"] = [0.5, 1.0, 1.5, 2.0]
    df_handle = handles.register_handle(base)["handle"]

    return {
        "mech_handle": mech_handle,
        "comp_handle": comp_handle,
        "df_handle": df_handle,
        "mech": mech,
        "comp": comp,
        "df": base,
    }


@pytest.mark.integration
def test_run_composition_on_psyche_smoke(tools, composition_with_one_input):
    fixture = composition_with_one_input
    out = tools["run_composition_on_psyche"](
        composition=fixture["comp_handle"],
        data=fixture["df_handle"],
        input_mapping={fixture["mech_handle"]: ["cue"]},
    )
    assert out["n_rows_run"] == 4
    assert out["n_rows_skipped"] == 0
    pred_df = handles.resolve_handle(out["predictions_handle"])
    pred_cols = [c for c in pred_df.columns if c.startswith("prediction_")]
    assert pred_cols, "expected at least one prediction_<node>_<i> column"


@pytest.mark.integration
def test_run_composition_on_psyche_with_output_mapping_metrics(
    tools, composition_with_one_input
):
    fixture = composition_with_one_input
    out = tools["run_composition_on_psyche"](
        composition=fixture["comp_handle"],
        data=fixture["df_handle"],
        input_mapping={fixture["mech_handle"]: ["cue"]},
        output_mapping={fixture["mech_handle"]: "target_value"},
    )
    assert "metrics" in out
    metrics = out["metrics"]
    assert len(metrics) == 1
    only_metric = next(iter(metrics.values()))
    assert "mse" in only_metric
    assert only_metric["n_compared"] == 4
    assert only_metric["mse"] == pytest.approx(0.0, abs=1e-6)


@pytest.mark.integration
def test_run_composition_on_psyche_skips_nan_input_rows(
    tools, composition_with_one_input
):
    fixture = composition_with_one_input
    df = fixture["df"].copy()
    df.loc[1, "cue"] = float("nan")
    df_handle = handles.register_handle(df)["handle"]

    out = tools["run_composition_on_psyche"](
        composition=fixture["comp_handle"],
        data=df_handle,
        input_mapping={fixture["mech_handle"]: ["cue"]},
    )
    assert out["n_rows_run"] == 3
    assert out["n_rows_skipped"] == 1


@pytest.mark.integration
def test_run_composition_on_psyche_rejects_non_input_node(
    pnl_imported, tools, composition_with_one_input
):
    """Mapping an unrelated mechanism should raise before any trial runs."""
    pnl = pnl_imported
    fixture = composition_with_one_input
    stranger = pnl.TransferMechanism(name="stranger")
    stranger_handle = handles.register_handle(stranger)["handle"]
    with pytest.raises(ValueError, match="not an INPUT node"):
        tools["run_composition_on_psyche"](
            composition=fixture["comp_handle"],
            data=fixture["df_handle"],
            input_mapping={stranger_handle: ["cue"]},
        )


@pytest.mark.integration
def test_run_composition_on_psyche_rejects_missing_column(
    tools, composition_with_one_input
):
    fixture = composition_with_one_input
    with pytest.raises(ValueError, match="not present in the data frame"):
        tools["run_composition_on_psyche"](
            composition=fixture["comp_handle"],
            data=fixture["df_handle"],
            input_mapping={fixture["mech_handle"]: ["does_not_exist"]},
        )


@pytest.mark.integration
def test_fit_composition_grid_finds_known_minimum(pnl_imported, tools):
    """Grid-fit ``noise`` of a TransferMechanism on data with target = noise.

    With ``cue = 0`` and the default Linear function (slope=1,
    intercept=0), the mechanism's output reduces to the noise constant.
    The target column is constant at 0.7, so MSE is minimised at
    ``noise = 0.7``.
    """
    pnl = pnl_imported
    mech = pnl.TransferMechanism(name="fit_m", default_variable=[0.0])
    comp = pnl.Composition(name="fit_c")
    comp.add_node(mech)

    mech_handle = handles.register_handle(mech)["handle"]
    comp_handle = handles.register_handle(comp)["handle"]

    df = _valid_behavioral_rows(n_rows=3, n_subjects=1)
    df["cue"] = 0.0
    df["target_value"] = 0.7
    df_handle = handles.register_handle(df)["handle"]

    out = tools["fit_composition_to_psyche"](
        composition=comp_handle,
        data=df_handle,
        input_mapping={mech_handle: ["cue"]},
        output_mapping={mech_handle: "target_value"},
        free_parameters={mech_handle: {"noise": [0.0, 0.3, 0.7, 1.0]}},
        objective="mse",
        method="grid",
    )
    assert out["n_evaluations"] == 4
    assert out["objective"] == "mse"
    assert out["fitted_composition"] == comp_handle
    assert out["best_params"] == {"fit_m": {"noise": 0.7}}
    assert out["best_score"] == pytest.approx(0.0, abs=1e-6)
    scores = [r["score"] for r in out["report"]]
    assert scores == sorted(scores)


@pytest.mark.integration
def test_fit_composition_max_evaluations_guard(pnl_imported, tools):
    """A grid larger than ``max_evaluations`` raises ValueError up front."""
    pnl = pnl_imported
    mech = pnl.TransferMechanism(name="big_m", default_variable=[0.0])
    comp = pnl.Composition(name="big_c")
    comp.add_node(mech)

    mech_handle = handles.register_handle(mech)["handle"]
    comp_handle = handles.register_handle(comp)["handle"]

    df = _valid_behavioral_rows(n_rows=2, n_subjects=1)
    df["cue"] = 0.0
    df["target_value"] = 0.0
    df_handle = handles.register_handle(df)["handle"]

    with pytest.raises(ValueError, match="exceeds max_evaluations"):
        tools["fit_composition_to_psyche"](
            composition=comp_handle,
            data=df_handle,
            input_mapping={mech_handle: ["cue"]},
            output_mapping={mech_handle: "target_value"},
            free_parameters={mech_handle: {"noise": list(range(10))}},
            method="grid",
            max_evaluations=5,
        )


@pytest.mark.integration
def test_fit_composition_unknown_param_fails_fast(pnl_imported, tools):
    """A free_parameters key that doesn't exist on the node raises early."""
    pnl = pnl_imported
    mech = pnl.TransferMechanism(name="u_m", default_variable=[0.0])
    comp = pnl.Composition(name="u_c")
    comp.add_node(mech)

    mech_handle = handles.register_handle(mech)["handle"]
    comp_handle = handles.register_handle(comp)["handle"]

    df = _valid_behavioral_rows(n_rows=2, n_subjects=1)
    df["cue"] = 0.0
    df["target_value"] = 0.0
    df_handle = handles.register_handle(df)["handle"]

    with pytest.raises(ValueError, match="no parameter"):
        tools["fit_composition_to_psyche"](
            composition=comp_handle,
            data=df_handle,
            input_mapping={mech_handle: ["cue"]},
            output_mapping={mech_handle: "target_value"},
            free_parameters={
                mech_handle: {"definitely_not_a_real_param": [1.0, 2.0]}
            },
            method="grid",
        )


def test_unused_paths_for_coverage(tmp_path):
    """Touch helpers that the tool surface doesn't otherwise exercise."""
    assert curated_psyche._detect_format("a.csv") == "csv"
    assert curated_psyche._detect_format("a.parquet") == "parquet"
    assert curated_psyche._detect_format("a.pq") == "parquet"
    assert curated_psyche._detect_format("a.jsonl") == "jsonl"
    assert curated_psyche._detect_format("a.ndjson") == "jsonl"
    with pytest.raises(ValueError):
        curated_psyche._detect_format("a.weird")
    p: Path = tmp_path / "ignored"
    del p
