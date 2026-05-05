"""Curated PSYCHE tools: load + run + fit Compositions on behavioural data.

These four tools turn the MCP into a behavioural-modeling endpoint by
bridging a :class:`pandas.DataFrame` of trial-level observations
(validated against the PSYCHE convention from the sibling
``psyneulink-psyche`` package) into PNL ``Composition.run`` calls.

Surface:

* :func:`describe_psyche_convention` — agent introspects the canonical
  ``BEHAVIORAL_DATA_CONVENTION`` so it can plan a sensible
  ``input_mapping`` *before* loading any data.
* :func:`load_psyche_data` — load + validate a CSV / Parquet / JSONL
  file and register the underlying DataFrame as a handle.
* :func:`run_composition_on_psyche` — for each
  ``(subject_id, trial_global, step)`` row, build the composition's
  ``inputs`` dict from mapped columns, run, and join per-row predictions
  back to the original frame. Optional ``output_mapping`` yields per-
  output-node MSE / accuracy metrics.
* :func:`fit_composition_to_psyche` — search free parameter values that
  minimise an objective (MSE / NLL / accuracy) against behavioural data.
  ``method="grid"`` is the only backend shipped in this MVP;
  ``method="de"`` and ``method="pec"`` raise :class:`NotImplementedError`
  pointing at the follow-up so the surface is forward-compatible.

Both ``pandas`` and ``psyneulink_psyche`` are imported lazily inside
each tool via :func:`_require_psyche` so the MCP server starts even
when the ``[psyche]`` extra isn't installed; the install hint surfaces
at call time.
"""

from __future__ import annotations

import contextlib
import itertools
import math
from pathlib import Path
from typing import Any

from ... import handles
from ...feedback import captured_tool

# --------------------------------------------------------------------------- #
# lazy-import shim                                                            #
# --------------------------------------------------------------------------- #


def _require_psyche() -> tuple[Any, Any]:
    """Import ``pandas`` + ``psyneulink_psyche`` or raise an actionable error.

    Both packages live behind the ``[psyche]`` optional extra so the
    server can boot without them. Tools call this at the top of their
    body so the install hint is the user's first signal — not a bare
    ``ImportError`` traceback.
    """
    try:
        import pandas as pd
        import psyneulink_psyche as psyche
    except ImportError as exc:
        raise RuntimeError(
            "psyche tools require the [psyche] extra: "
            "uv sync --extra psyche  (or: pip install 'psyneulink-mcp[psyche]')"
        ) from exc
    return pd, psyche


def _column_kind(column: Any) -> str:
    """``Convention`` column → its ``"base" | "categorical" | "numeric" | "index"``.

    Reads the discriminator the pydantic models declare via
    ``Literal[...]`` ``kind`` fields, falls back to the class name on
    older psyche releases that don't expose ``kind``.
    """
    kind = getattr(column, "kind", None)
    if isinstance(kind, str):
        return kind
    cls_name = type(column).__name__.lower()
    for tag in ("categorical", "numeric", "index"):
        if tag in cls_name:
            return tag
    return "base"


def _resolve_convention(name: str, psyche: Any) -> Any:
    """Look a Convention up by short name. Only ``"behavioral"`` ships today."""
    key = (name or "").strip().lower()
    if key in ("", "behavioral", "behavioural"):
        return psyche.BEHAVIORAL_DATA_CONVENTION
    raise ValueError(
        f"unknown psyche convention: {name!r}; only 'behavioral' is shipped"
    )


def _detect_format(path: str) -> str:
    """File extension → ``"csv" | "parquet" | "jsonl"``."""
    suffix = Path(path).suffix.lower().lstrip(".")
    if suffix in ("csv",):
        return "csv"
    if suffix in ("parquet", "pq"):
        return "parquet"
    if suffix in ("jsonl", "ndjson"):
        return "jsonl"
    raise ValueError(
        f"could not auto-detect format from extension {suffix!r}; "
        "pass format='csv'|'parquet'|'jsonl' explicitly"
    )


# --------------------------------------------------------------------------- #
# composition execution helpers                                               #
# --------------------------------------------------------------------------- #


def _ensure_graph_analyzed(comp: Any) -> None:
    """Force PNL to populate node-role assignments before role lookups.

    ``Composition.get_nodes_by_role`` returns ``[]`` for newly-added
    nodes until the graph has been analysed (PNL only does it lazily,
    typically at the start of ``run``). For our tools we need role
    information *before* running, so call the private analyser
    explicitly. Best-effort: not every PNL version exposes the same
    private method.
    """
    for attr in ("_analyze_graph", "_check_projection_initialization_status"):
        method = getattr(comp, attr, None)
        if callable(method):
            try:
                method()
                return
            except Exception:
                continue


def _input_node_set(comp: Any) -> set[Any]:
    """Set of nodes the composition treats as INPUT for ``run(inputs=...)``."""
    import psyneulink as pnl

    _ensure_graph_analyzed(comp)
    try:
        return set(comp.get_nodes_by_role(pnl.NodeRole.INPUT))
    except Exception:
        return set(getattr(comp, "nodes", []))


def _output_nodes(comp: Any) -> list[Any]:
    """Ordered list of OUTPUT nodes (falls back to all nodes on older PNL)."""
    import psyneulink as pnl

    _ensure_graph_analyzed(comp)
    try:
        return list(comp.get_nodes_by_role(pnl.NodeRole.OUTPUT))
    except Exception:
        return list(getattr(comp, "nodes", []))


def _validate_input_mapping(
    comp: Any, resolved_mapping: dict[Any, list[str]]
) -> None:
    """Fail fast if any node in ``resolved_mapping`` isn't an INPUT node."""
    input_nodes = _input_node_set(comp)
    for node in resolved_mapping:
        if node not in input_nodes:
            raise ValueError(
                f"node {getattr(node, 'name', node)!r} is not an INPUT node "
                f"of composition {getattr(comp, 'name', comp)!r}; "
                f"add it via add_linear_pathway / add_node first"
            )


def _resolve_data(data: str) -> Any:
    """Resolve a data handle to a ``pandas.DataFrame``.

    ``load_psyche_data`` registers the underlying ``BehavioralFrame.df``
    so handle resolution returns the ``DataFrame`` directly. Defensive
    fallback unwraps a ``BehavioralFrame`` if a future caller stores
    one of those instead.
    """
    obj = handles.resolve_handle(data)
    if hasattr(obj, "df") and not hasattr(obj, "iloc"):
        return obj.df
    return obj


def _flatten_output(value: Any) -> list[float]:
    """Coerce one output node's per-trial value to a flat list of floats."""
    import numpy as np

    arr = np.asarray(value, dtype=float).flatten()
    return arr.tolist()


def _len_results(comp: Any) -> int:
    """Length of ``comp.results``, treating numpy arrays correctly.

    ``Composition.results`` can be a Python list, a numpy ``ndarray``,
    or ``None``. The naive ``getattr(comp, "results", []) or []`` form
    triggers ``ValueError`` on numpy arrays because their truthiness
    is ambiguous; this helper avoids that by going through ``len``.
    """
    results = getattr(comp, "results", None)
    if results is None:
        return 0
    try:
        return len(results)
    except TypeError:
        return 0


def _materialise_results(comp: Any) -> list[Any]:
    """``comp.results`` flattened to a plain Python list.

    Iterating an ``ndarray`` already gives per-trial sub-arrays, so a
    list constructor is sufficient regardless of whether PNL returned
    a list or a numpy structure.
    """
    results = getattr(comp, "results", None)
    if results is None:
        return []
    try:
        return list(results)
    except TypeError:
        return []


def _try_reset(comp: Any) -> None:
    """Best-effort ``Composition.reset`` between fit iterations.

    Compositions accumulate integration / context state across runs.
    For grid fitting we want each parameter combination evaluated from
    the same starting state, so we reset before each batched run. Wrap
    in a contextlib.suppress because not every composition shape
    supports it.
    """
    with contextlib.suppress(Exception):
        comp.reset()


def _run_over_data(
    comp: Any,
    data_df: Any,
    input_mapping: dict[str, list[str]],
    num_trials: int | None,
    pd: Any,
    *,
    reset_first: bool = False,
) -> tuple[Any, int, list[Any], list[Any]]:
    """Batched per-row execution.

    Returns ``(predictions_df, n_skipped, output_nodes, valid_index)``.
    ``predictions_df`` is a copy of the (possibly-truncated) input frame
    with ``prediction_<node_name>_<i>`` columns appended. Rows containing
    NaN in any input column are skipped; their prediction columns hold
    NaN. ``valid_index`` is the pandas index of rows that actually ran,
    in the order PNL returned results — callers needing strict
    alignment between ``comp.results`` and DataFrame rows should index
    via this list rather than re-deriving from the input frame.
    """
    resolved_mapping = {
        handles.resolve_handle(h): list(cols) for h, cols in input_mapping.items()
    }
    _validate_input_mapping(comp, resolved_mapping)

    work_df = data_df if num_trials is None else data_df.head(int(num_trials))
    work_df = work_df.copy()

    all_input_cols: list[str] = []
    for cols in resolved_mapping.values():
        for c in cols:
            if c not in work_df.columns:
                raise ValueError(
                    f"input column {c!r} is not present in the data frame"
                )
            if c not in all_input_cols:
                all_input_cols.append(c)

    nan_mask = work_df[all_input_cols].isna().any(axis=1)
    valid_df = work_df.loc[~nan_mask]
    n_skipped = int(nan_mask.sum())

    output_nodes = _output_nodes(comp)

    if len(valid_df) == 0:
        return work_df, n_skipped, output_nodes, []

    inputs: dict[Any, list[list[float]]] = {}
    for node, cols in resolved_mapping.items():
        per_node: list[list[float]] = []
        for _, row in valid_df.iterrows():
            per_node.append([float(row[c]) for c in cols])
        inputs[node] = per_node

    if reset_first:
        _try_reset(comp)

    n_results_before = _len_results(comp)
    comp.run(inputs=inputs)
    all_results = _materialise_results(comp)
    new_results = all_results[n_results_before:]

    n_trials = len(valid_df)
    if len(new_results) != n_trials:
        new_results = all_results[-n_trials:] if all_results else []

    pred_columns: dict[str, Any] = {}
    for out_idx, out_node in enumerate(output_nodes):
        per_trial_flat: list[list[float]] = []
        for trial_result in new_results:
            try:
                node_value = trial_result[out_idx]
            except (IndexError, TypeError):
                node_value = []
            per_trial_flat.append(_flatten_output(node_value))

        max_len = max((len(v) for v in per_trial_flat), default=0)
        for i in range(max_len):
            col_name = f"prediction_{out_node.name}_{i}"
            col_series = pd.Series(index=work_df.index, dtype=float)
            for trial_idx, val in zip(valid_df.index, per_trial_flat, strict=False):
                col_series.loc[trial_idx] = (
                    val[i] if i < len(val) else float("nan")
                )
            pred_columns[col_name] = col_series

    pred_df = work_df.copy()
    for col_name, series in pred_columns.items():
        pred_df[col_name] = series

    return pred_df, n_skipped, output_nodes, list(valid_df.index)


# --------------------------------------------------------------------------- #
# metrics                                                                     #
# --------------------------------------------------------------------------- #


def _compute_metrics(
    pred_df: Any,
    output_mapping: dict[str, str],
    output_nodes: list[Any],
    pd: Any,
) -> dict[str, dict[str, Any]]:
    """Per-output-node ``{mse, accuracy, n_compared}`` against target columns.

    ``accuracy`` is ``None`` for non-binary targets. The first
    prediction port (``prediction_<node>_0``) is the comparison target;
    multi-port outputs are out of scope for the MVP metric surface.
    """
    metrics: dict[str, dict[str, Any]] = {}
    output_node_by_handle = {
        h: handles.resolve_handle(h) for h in output_mapping
    }
    for handle, target_col in output_mapping.items():
        node = output_node_by_handle[handle]
        if node not in output_nodes:
            raise ValueError(
                f"node {getattr(node, 'name', node)!r} is not an OUTPUT node "
                f"of the composition; cannot compare predictions to "
                f"{target_col!r}"
            )
        if target_col not in pred_df.columns:
            raise ValueError(
                f"target column {target_col!r} is not present in the data frame"
            )

        pred_col = f"prediction_{node.name}_0"
        if pred_col not in pred_df.columns:
            metrics[node.name] = {
                "mse": None,
                "accuracy": None,
                "n_compared": 0,
            }
            continue

        target = pd.to_numeric(pred_df[target_col], errors="coerce")
        prediction = pd.to_numeric(pred_df[pred_col], errors="coerce")
        mask = ~(target.isna() | prediction.isna())
        target_valid = target[mask].astype(float)
        pred_valid = prediction[mask].astype(float)
        n = int(mask.sum())

        if n == 0:
            metrics[node.name] = {
                "mse": None,
                "accuracy": None,
                "n_compared": 0,
            }
            continue

        mse = float(((target_valid - pred_valid) ** 2).mean())

        unique_targets = set(target_valid.unique())
        accuracy: float | None = None
        if unique_targets <= {0.0, 1.0}:
            pred_binary = (pred_valid >= 0.5).astype(float)
            accuracy = float((pred_binary == target_valid).mean())

        metrics[node.name] = {
            "mse": mse,
            "accuracy": accuracy,
            "n_compared": n,
        }
    return metrics


# --------------------------------------------------------------------------- #
# objectives                                                                  #
# --------------------------------------------------------------------------- #


def _objective_score(
    pred_df: Any,
    output_mapping: dict[str, str],
    output_nodes: list[Any],
    objective: str,
    pd: Any,
) -> float:
    """Single scalar to minimise across (target, prediction) column pairs.

    * ``mse`` — average per-row squared error across all (output_node,
      target_col) pairs, then mean over pairs.
    * ``nll`` — Bernoulli negative log-likelihood; predictions clipped
      to ``[1e-6, 1-1e-6]``.
    * ``accuracy`` — minimised as ``1 - accuracy``; targets must be 0/1.
    """
    obj = objective.lower()
    if obj not in ("mse", "nll", "accuracy"):
        raise ValueError(
            f"unknown objective {objective!r}; expected 'mse' | 'nll' | 'accuracy'"
        )

    metrics = _compute_metrics(pred_df, output_mapping, output_nodes, pd)
    if not metrics:
        return float("inf")

    output_node_by_handle = {
        h: handles.resolve_handle(h) for h in output_mapping
    }

    if obj == "mse":
        scores: list[float] = []
        for _, m in metrics.items():
            if m["mse"] is None:
                continue
            scores.append(float(m["mse"]))
        return float(sum(scores) / len(scores)) if scores else float("inf")

    if obj == "nll":
        nlls: list[float] = []
        for handle, target_col in output_mapping.items():
            node = output_node_by_handle[handle]
            pred_col = f"prediction_{node.name}_0"
            if pred_col not in pred_df.columns:
                continue
            target = pd.to_numeric(pred_df[target_col], errors="coerce")
            prediction = pd.to_numeric(pred_df[pred_col], errors="coerce")
            mask = ~(target.isna() | prediction.isna())
            t = target[mask].astype(float)
            p = prediction[mask].astype(float).clip(1e-6, 1.0 - 1e-6)
            if len(t) == 0:
                continue
            nll = -((t * p.apply(math.log)) + ((1.0 - t) * (1.0 - p).apply(math.log))).mean()
            nlls.append(float(nll))
        return float(sum(nlls) / len(nlls)) if nlls else float("inf")

    accuracies: list[float] = []
    for _, m in metrics.items():
        if m["accuracy"] is None:
            continue
        accuracies.append(float(m["accuracy"]))
    if not accuracies:
        raise ValueError(
            "objective='accuracy' requires binary 0/1 target columns; "
            "none of the mapped targets were binary"
        )
    return float(1.0 - sum(accuracies) / len(accuracies))


# --------------------------------------------------------------------------- #
# parameter setter (cross-version PNL)                                        #
# --------------------------------------------------------------------------- #


def _set_node_param(
    node: Any, param_name: str, value: Any, context: Any | None = None
) -> None:
    """Set a parameter on a live PNL node, trying the modern API first.

    Order of attempts:

    1. ``node.parameters.<name>.set(value)`` plus, when ``context`` is
       given, ``node.parameters.<name>.set(value, context=context)``.
       PNL keeps per-execution-context parameter values; setting both
       the default *and* the composition's context value is what
       actually changes the value the next ``Composition.run`` reads
       (without the context-scoped set, a previously-run composition
       keeps using the value it cached at first run).
    2. ``node.defaults.<name> = value`` — older PNL releases.
    3. ``setattr(node, name, value)`` — last-ditch attribute set.

    Each strategy is tried independently so a partial failure on the
    first surface (e.g. a parameter that exists but rejects ``set``)
    doesn't mask the existence of a working alternative.
    """
    last_exc: BaseException | None = None
    succeeded = False

    param = (
        getattr(node.parameters, param_name, None)
        if hasattr(node, "parameters")
        else None
    )
    if param is not None:
        try:
            param.set(value)
            succeeded = True
        except Exception as exc:
            last_exc = exc
        if context is not None:
            try:
                param.set(value, context=context)
                succeeded = True
            except Exception as exc:
                last_exc = exc
        if succeeded:
            return

    defaults = getattr(node, "defaults", None)
    if defaults is not None and hasattr(defaults, param_name):
        try:
            setattr(defaults, param_name, value)
            return
        except Exception as exc:
            last_exc = exc

    if hasattr(node, param_name):
        try:
            setattr(node, param_name, value)
            return
        except Exception as exc:
            last_exc = exc

    raise AttributeError(
        f"could not set parameter {param_name!r} on node "
        f"{getattr(node, 'name', node)!r}: no working setter "
        f"(last error: {last_exc!r})"
    )


def _validate_free_parameters(
    free_parameters: dict[str, dict[str, list[Any]]],
) -> dict[Any, dict[str, list[Any]]]:
    """Resolve handle keys, ensure each (node, param) is addressable.

    Returns a dict keyed by live node objects so the inner fitting loop
    doesn't pay handle-resolution cost on every iteration. Fails fast
    with a clear message if a parameter doesn't exist on the resolved
    node — discoverable before grinding through 100 grid combinations.
    """
    resolved: dict[Any, dict[str, list[Any]]] = {}
    for node_handle, param_grid in free_parameters.items():
        node = handles.resolve_handle(node_handle)
        for param_name, candidates in param_grid.items():
            if not isinstance(candidates, (list, tuple)):
                raise ValueError(
                    f"free_parameters[{node_handle!r}][{param_name!r}] must be "
                    f"a list of candidate values, got {type(candidates).__name__}"
                )
            if not candidates:
                raise ValueError(
                    f"free_parameters[{node_handle!r}][{param_name!r}] is empty"
                )
            has_param = (
                hasattr(node, "parameters")
                and getattr(node.parameters, param_name, None) is not None
            ) or (
                hasattr(node, "defaults") and hasattr(node.defaults, param_name)
            ) or hasattr(node, param_name)
            if not has_param:
                raise ValueError(
                    f"node {getattr(node, 'name', node)!r} has no parameter "
                    f"{param_name!r}; check the spelling against PNL's API"
                )
        resolved[node] = {p: list(v) for p, v in param_grid.items()}
    return resolved


def _grid_combinations(
    resolved: dict[Any, dict[str, list[Any]]],
) -> list[list[tuple[Any, str, Any]]]:
    """Cartesian product of every (node, param) candidate list.

    Each combination is a list of ``(node, param_name, value)`` triples
    so the fit loop can apply them in one pass per iteration.
    """
    flat_axes: list[list[tuple[Any, str, Any]]] = []
    for node, param_grid in resolved.items():
        for param_name, candidates in param_grid.items():
            flat_axes.append([(node, param_name, v) for v in candidates])

    if not flat_axes:
        return [[]]
    return [list(c) for c in itertools.product(*flat_axes)]


# --------------------------------------------------------------------------- #
# registration                                                                #
# --------------------------------------------------------------------------- #


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="curated")
    def describe_psyche_convention(name: str = "behavioral") -> dict[str, Any]:
        """Return the canonical PSYCHE convention for ``name``.

        WHEN TO CALL: before suggesting an ``input_mapping`` or
        ``output_mapping`` for ``run_composition_on_psyche`` — the
        column list tells you which columns can carry stimulus inputs,
        which can carry behavioural targets, and which categorical
        levels are legal.

        Args:
            name: Convention short name. Only ``"behavioral"`` ships
                today; other names raise ``ValueError``.

        Returns:
            ``{"name": str, "version": str, "row_identity": str,
            "columns": [{"name": str, "kind": "base"|"categorical"|
            "numeric"|"index", "levels": list | None,
            "description": str}, ...]}``.
        """
        _, psyche = _require_psyche()
        convention = _resolve_convention(name, psyche)
        columns_payload = []
        for col in convention.columns:
            levels = getattr(col, "levels", None)
            columns_payload.append(
                {
                    "name": col.name,
                    "kind": _column_kind(col),
                    "levels": list(levels) if levels is not None else None,
                    "description": col.description,
                }
            )
        return {
            "name": convention.name,
            "version": getattr(convention, "version", psyche.PSYCHE_VERSION),
            "row_identity": psyche.BEHAVIORAL_ROW_IDENTITY,
            "columns": columns_payload,
        }

    @captured_tool(mcp, layer="curated")
    def load_psyche_data(
        path: str,
        format: str | None = None,
    ) -> dict[str, Any]:
        """Load + validate a behavioural data file; register the DataFrame.

        WHEN TO CALL: after the user provides a path to a CSV, Parquet
        or JSONL file that conforms to ``BEHAVIORAL_DATA_CONVENTION``
        (see :func:`describe_psyche_convention`). The returned handle
        feeds straight into :func:`run_composition_on_psyche` and
        :func:`fit_composition_to_psyche`.

        Args:
            path: Filesystem path. ``~`` is expanded.
            format: ``"csv" | "parquet" | "jsonl"``. Auto-detected from
                the file extension when ``None`` (``.csv`` → csv,
                ``.parquet`` / ``.pq`` → parquet, ``.jsonl`` /
                ``.ndjson`` → jsonl).

        Returns:
            ``{"data_handle": "h_...", "n_rows": int, "n_subjects":
            int, "n_columns": int, "columns": [str, ...],
            "warnings": [str, ...], "summary": str}``.

        Raises:
            ValidationError: subclass of ``ValueError``, raised when
                the file is structurally malformed against the
                convention. The message contains the full
                :class:`ValidationReport`.
        """
        _, psyche = _require_psyche()
        target = Path(path).expanduser()
        if not target.exists():
            raise FileNotFoundError(
                f"load_psyche_data: no such file: {target}"
            )

        fmt = (format or _detect_format(str(target))).lower()
        if fmt == "csv":
            bf = psyche.load_csv(target)
        elif fmt == "parquet":
            bf = psyche.load_parquet(target)
        elif fmt == "jsonl":
            bf = psyche.load_jsonl(target)
        else:
            raise ValueError(
                f"unknown format {format!r}; expected 'csv'|'parquet'|'jsonl'"
            )

        payload = handles.register_handle(bf.df)
        return {
            "data_handle": payload["handle"],
            "n_rows": int(bf.n_rows),
            "n_subjects": int(bf.n_subjects),
            "n_columns": int(len(bf.df.columns)),
            "columns": [str(c) for c in bf.df.columns],
            "warnings": list(bf.validation.warnings),
            "summary": (
                f"loaded {bf.n_rows} rows × {len(bf.df.columns)} columns "
                f"({bf.n_subjects} subjects) from {target}"
            ),
        }

    @captured_tool(mcp, layer="curated")
    def run_composition_on_psyche(
        composition: str,
        data: str,
        input_mapping: dict[str, list[str]],
        output_mapping: dict[str, str] | None = None,
        num_trials: int | None = None,
    ) -> dict[str, Any]:
        """Run a Composition over each row of a behavioural DataFrame.

        WHEN TO CALL: after a Composition has been wired (input nodes,
        pathways, projections) and a behavioural DataFrame has been
        loaded with :func:`load_psyche_data`. The composition runs once
        per row in batched form (one trial per row, all in one
        ``Composition.run`` call) so PNL can compile / vectorise.

        Args:
            composition: Handle returned by ``create_composition``.
            data: Handle returned by :func:`load_psyche_data`.
            input_mapping: ``{<input_node_handle>: [<column_name>, ...]}``.
                For each INPUT node, the columns whose row values become
                its input vector for that trial. Multi-column lists
                produce multi-element input vectors; column order is
                preserved. Every key MUST resolve to a node already
                marked as INPUT in the composition or this call raises
                before any trial executes.
            output_mapping: Optional ``{<output_node_handle>:
                <target_column_name>}`` for metric computation. Each
                target column is compared element-wise against
                ``prediction_<node_name>_0`` (the first port of the
                output node's prediction).
            num_trials: Optional cap on the number of rows processed.
                Defaults to running every row.

        Returns:
            ``{"predictions_handle": "h_...", "n_rows_run": int,
            "n_rows_skipped": int, "metrics": {<node_name>: {"mse":
            float, "accuracy": float|None, "n_compared": int}, ...},
            "summary": str}``.

            ``predictions_handle`` resolves to a DataFrame containing
            the original (possibly truncated) rows plus
            ``prediction_<node_name>_<i>`` columns for each output
            node's value vector. ``n_rows_skipped`` counts rows
            dropped due to NaN in any input column.
            ``metrics`` is omitted when ``output_mapping`` is ``None``.
        """
        pd, _ = _require_psyche()
        handles.record_call(
            "run_composition_on_psyche",
            {
                "composition": composition,
                "data": data,
                "input_mapping": dict(input_mapping),
                "output_mapping": dict(output_mapping) if output_mapping else None,
                "num_trials": num_trials,
            },
            result_handle=None,
            tool_layer="curated",
        )

        comp = handles.resolve_handle(composition)
        data_df = _resolve_data(data)

        pred_df, n_skipped, output_nodes, valid_index = _run_over_data(
            comp, data_df, input_mapping, num_trials, pd, reset_first=False
        )
        n_rows_run = len(valid_index)

        result: dict[str, Any] = {
            "predictions_handle": handles.register_handle(pred_df)["handle"],
            "n_rows_run": n_rows_run,
            "n_rows_skipped": n_skipped,
            "summary": (
                f"ran composition over {n_rows_run} row(s); "
                f"skipped {n_skipped} row(s) with NaN inputs"
            ),
        }
        if output_mapping:
            result["metrics"] = _compute_metrics(
                pred_df, output_mapping, output_nodes, pd
            )
        return result

    @captured_tool(mcp, layer="curated")
    def fit_composition_to_psyche(
        composition: str,
        data: str,
        input_mapping: dict[str, list[str]],
        output_mapping: dict[str, str],
        free_parameters: dict[str, dict[str, list[Any]]],
        objective: str = "mse",
        method: str = "grid",
        max_evaluations: int = 200,
    ) -> dict[str, Any]:
        """Search free parameter values that minimise an objective on data.

        WHEN TO CALL: when the user wants to fit one or more numeric
        parameters of nodes in an already-built composition to a
        behavioural DataFrame. Use ``method="grid"`` with small,
        explicit candidate lists per parameter — the MVP backend is a
        cartesian-product sweep and pays linearly per cell.

        The winning parameter values are written **in place** on the
        provided composition's nodes; the returned ``fitted_composition``
        handle is the same handle as ``composition`` (so any handle the
        agent already holds keeps working). If you need to preserve the
        original parameter values, snapshot them with
        :func:`describe_handle` before calling.

        Args:
            composition: Composition handle.
            data: DataFrame handle.
            input_mapping: Same shape as
                :func:`run_composition_on_psyche`.
            output_mapping: Same shape as
                :func:`run_composition_on_psyche`. REQUIRED here — you
                cannot fit without target columns.
            free_parameters: ``{<node_handle>: {<param_name>:
                [candidate_value, ...]}}``. Only discrete candidate
                lists are supported; continuous bounds land with the
                ``"de"`` backend in a follow-up.
            objective: ``"mse"`` (default) | ``"nll"`` (Bernoulli
                negative log-likelihood, predictions clipped to
                ``[1e-6, 1-1e-6]``) | ``"accuracy"`` (minimises
                ``1 - accuracy``; requires binary 0/1 targets).
            method: ``"grid"`` is the only backend in this MVP.
                ``"de"`` and ``"pec"`` raise ``NotImplementedError``
                pointing at the follow-up so the surface is
                forward-compatible.
            max_evaluations: Hard cap on grid combinations evaluated.
                A grid with more cells than this raises ``ValueError``
                up front so the agent can prune the candidate lists.

        Returns:
            ``{"fitted_composition": "h_...", "best_params":
            {<node_name>: {<param_name>: <value>}}, "best_score":
            float, "objective": str, "n_evaluations": int, "report":
            [{"params": {...}, "score": float}, ...], "summary":
            str}``. ``report`` is sorted by score (ascending — lower
            is better since all objectives are minimised).
        """
        if method == "de":
            raise NotImplementedError(
                "method='de' (differential evolution) is not yet implemented; "
                "method='grid' is the MVP backend"
            )
        if method == "pec":
            raise NotImplementedError(
                "method='pec' (ParameterEstimationComposition) is not yet "
                "implemented; method='grid' is the MVP backend"
            )
        if method != "grid":
            raise ValueError(
                f"unknown method {method!r}; expected 'grid' | 'de' | 'pec'"
            )

        pd, _ = _require_psyche()
        handles.record_call(
            "fit_composition_to_psyche",
            {
                "composition": composition,
                "data": data,
                "input_mapping": dict(input_mapping),
                "output_mapping": dict(output_mapping),
                "free_parameters": dict(free_parameters),
                "objective": objective,
                "method": method,
                "max_evaluations": max_evaluations,
            },
            result_handle=None,
            tool_layer="curated",
        )

        comp = handles.resolve_handle(composition)
        data_df = _resolve_data(data)

        resolved = _validate_free_parameters(free_parameters)
        combinations = _grid_combinations(resolved)
        n_combinations = len(combinations)

        if n_combinations > max_evaluations:
            raise ValueError(
                f"grid has {n_combinations} combinations, exceeds "
                f"max_evaluations={max_evaluations}; either prune the "
                f"candidate lists or raise max_evaluations explicitly"
            )

        best_score: float | None = None
        best_assignment: list[tuple[Any, str, Any]] | None = None
        report: list[dict[str, Any]] = []

        for assignment in combinations:
            for node, param_name, value in assignment:
                _set_node_param(node, param_name, value, context=comp)

            pred_df, _n_skipped, output_nodes, _valid_idx = _run_over_data(
                comp, data_df, input_mapping, None, pd, reset_first=True
            )
            score = _objective_score(
                pred_df, output_mapping, output_nodes, objective, pd
            )

            params_payload: dict[str, dict[str, Any]] = {}
            for node, param_name, value in assignment:
                node_name = getattr(node, "name", repr(node))
                params_payload.setdefault(node_name, {})[param_name] = value
            report.append({"params": params_payload, "score": score})

            if best_score is None or score < best_score:
                best_score = score
                best_assignment = assignment

        if best_assignment is not None:
            for node, param_name, value in best_assignment:
                _set_node_param(node, param_name, value, context=comp)

        best_params: dict[str, dict[str, Any]] = {}
        if best_assignment:
            for node, param_name, value in best_assignment:
                node_name = getattr(node, "name", repr(node))
                best_params.setdefault(node_name, {})[param_name] = value

        report.sort(key=lambda r: r["score"])

        return {
            "fitted_composition": composition,
            "best_params": best_params,
            "best_score": float(best_score) if best_score is not None else float("inf"),
            "objective": objective,
            "n_evaluations": n_combinations,
            "report": report,
            "summary": (
                f"grid-fit {n_combinations} combination(s) on objective "
                f"{objective!r}; best score {best_score!r}"
            ),
        }
