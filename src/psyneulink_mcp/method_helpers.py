"""Runtime helpers shared by every generated *method* tool.

Generated method modules (``tools/generated/composition_add_*.py`` etc.)
delegate their ``_impl`` body to :func:`call_method_tool`. The helper:

1. Pops the bound-instance kwarg (always ``composition`` for the
   ``Composition.*`` methods this codebase ships today; the
   ``instance_kwarg`` parameter exists so we can extend cleanly to
   ``mechanism`` / ``pathway`` later without touching the generator
   template).
2. Resolves the remaining kwargs through :func:`handles.resolve_in`
   (which already swaps handle strings for live PNL objects and
   resolves class-name strings under known function-type keys).
3. Dispatches ``getattr(instance, method_name)(**resolved_rest)``.
4. Bumps the composition's revision counter on success.
5. Appends one ``JournalEntry`` (``tool_layer="generated"``,
   ``result_handle`` set when a handle was minted).

Per-method special cases live here, not in the generator template,
because the LLM-generated metadata (description / parameters / notes)
is regenerated every loop iteration but the runtime behaviour must
not be — keeping the impl in a hand-written module pins it.

Currently special-cased:

* ``add_projection`` — defensively adds ``sender`` and ``receiver`` to
  the composition first (PNL silently no-ops if they're already in)
  and treats ``DuplicateProjectionError`` as a no-op success. Both
  patterns trace directly to the captured failures in
  ``feedback/pending/issues.jsonl``.

The helper itself imports ``psyneulink`` lazily so a fresh clone
without PNL still imports the runtime cleanly (the generator-emitted
modules already import ``psyneulink`` at module load, so once a tool
runs PNL is guaranteed to be present).
"""

from __future__ import annotations

import json
from typing import Any

from . import handles


def call_method_tool(
    *,
    owner_cls: type,
    method_name: str,
    kwargs: dict[str, Any],
    tool_name: str,
    instance_kwarg: str = "composition",
) -> Any:
    """Generic dispatcher for generated method tools.

    See module docstring for the contract. Returns the same shape the
    constructor template uses: a JSON-friendly payload, a handle
    payload dict, or a small status dict for the no-op-success case.
    """
    if instance_kwarg not in kwargs:
        raise ValueError(
            f"{tool_name}: missing required kwarg {instance_kwarg!r} "
            "(must hold a Composition handle so the call has an instance to bind to)"
        )

    instance_handle = kwargs[instance_kwarg]
    if not isinstance(instance_handle, str):
        raise TypeError(
            f"{tool_name}: {instance_kwarg!r} must be a handle string, "
            f"got {type(instance_handle).__name__}"
        )

    instance = handles.resolve_handle(instance_handle)
    if not isinstance(instance, owner_cls):
        raise TypeError(
            f"{tool_name}: handle {instance_handle!r} resolved to "
            f"{type(instance).__name__}, expected {owner_cls.__name__}"
        )

    rest_pre_resolve = {k: v for k, v in kwargs.items() if k != instance_kwarg}
    resolved_rest = handles.resolve_in(rest_pre_resolve)

    if method_name == "add_projection":
        return _call_add_projection(
            tool_name=tool_name,
            instance_handle=instance_handle,
            instance=instance,
            pre_resolve_kwargs=kwargs,
            resolved_rest=resolved_rest,
        )

    method = getattr(instance, method_name)
    result = method(**resolved_rest)
    handles.bump_revision(instance_handle)
    return _wrap_result(
        tool_name=tool_name,
        pre_resolve_kwargs=kwargs,
        instance_handle=instance_handle,
        result=result,
    )


def _call_add_projection(
    *,
    tool_name: str,
    instance_handle: str,
    instance: Any,
    pre_resolve_kwargs: dict[str, Any],
    resolved_rest: dict[str, Any],
) -> Any:
    """``Composition.add_projection`` with defensive node-adding + dup swallow.

    Captured failures (``feedback/pending/issues.jsonl``) showed two
    dominant failure modes for the curated tool that lived here before:

    * ``CompositionError: ... has a sender ... that is not (yet) in
      it`` — agents call ``add_projection`` before adding the endpoints.
      Pre-adding both is safe: PNL's own ``add_node`` no-ops on an
      already-present node.
    * ``DuplicateProjectionError`` — agents retry an ``add_projection``
      that already succeeded (or that PNL auto-wired via a pathway
      earlier). The desired wiring exists; the caller's intent is met.

    We translate ``matrix`` → ``default_matrix`` so the public tool
    surface keeps the historical ``matrix=`` kwarg the curated tool
    advertised, while the underlying call uses
    :meth:`psyneulink.Composition.add_projection`'s actual parameter
    name. Constructing a free-standing ``MappingProjection`` first
    (which the old curated tool did) tripped a separate PNL bug for
    keyword-string matrices like ``IDENTITY_MATRIX`` — calling
    ``Composition.add_projection`` directly bypasses it because the
    Composition supplies the right context for parameter-port
    instantiation.
    """
    import psyneulink as pnl
    from psyneulink.core.components.projections.projection import (
        DuplicateProjectionError,
    )

    sender = resolved_rest.get("sender")
    receiver = resolved_rest.get("receiver")
    if sender is not None:
        try:
            instance.add_node(sender)
        except Exception:  # noqa: BLE001 — defensive; we only care that we tried
            pass
    if receiver is not None:
        try:
            instance.add_node(receiver)
        except Exception:  # noqa: BLE001
            pass

    call_kwargs: dict[str, Any] = {}
    for key in ("sender", "receiver", "feedback", "name"):
        if key in resolved_rest:
            call_kwargs[key] = resolved_rest[key]
    matrix_value: Any = None
    if "matrix" in resolved_rest and resolved_rest["matrix"] is not None:
        matrix_value = resolved_rest["matrix"]
    elif (
        "default_matrix" in resolved_rest
        and resolved_rest["default_matrix"] is not None
    ):
        matrix_value = resolved_rest["default_matrix"]
    if matrix_value is not None:
        call_kwargs["default_matrix"] = _resolve_matrix_keyword(matrix_value, pnl)

    try:
        result: Any = instance.add_projection(**call_kwargs)
    except DuplicateProjectionError:
        handles.bump_revision(instance_handle)
        handles.record_call(
            tool_name,
            pre_resolve_kwargs,
            result_handle=None,
            tool_layer="generated",
        )
        return {
            "composition": instance_handle,
            "duplicate": True,
            "note": (
                "projection already exists between sender and receiver; "
                "treated as no-op success"
            ),
        }
    except Exception:
        # Re-raise so ``captured_tool`` logs feedback. Other PNL errors
        # (CompositionError for unknown sender/receiver after node
        # add_node hooks above) are real bugs the agent should see.
        raise

    # Some PNL versions return ``None`` on duplicate even with
    # ``allow_duplicates=False`` — treat that the same as the explicit
    # exception path above.
    if result is None:
        handles.bump_revision(instance_handle)
        handles.record_call(
            tool_name,
            pre_resolve_kwargs,
            result_handle=None,
            tool_layer="generated",
        )
        return {
            "composition": instance_handle,
            "duplicate": True,
            "note": "projection already existed; treated as no-op success",
        }

    handles.bump_revision(instance_handle)
    return _wrap_result(
        tool_name=tool_name,
        pre_resolve_kwargs=pre_resolve_kwargs,
        instance_handle=instance_handle,
        result=result,
    )


# PNL exposes its matrix keywords under names like ``IDENTITY_MATRIX``
# (the constant name) but the value at that name is a different string
# (``"IdentityMatrix"``) that PNL expects in its parameter parsing. The
# JSON-Schema agent contract advertises the SCREAMING_SNAKE_CASE name
# (which is what users / docs call them), so we translate at the helper
# boundary. Resolved against the live ``pnl`` module so a PNL upgrade
# that adds a new keyword automatically becomes callable without a
# regen.
_MATRIX_KEYWORDS: tuple[str, ...] = (
    "IDENTITY_MATRIX",
    "FULL_CONNECTIVITY_MATRIX",
    "HOLLOW_MATRIX",
    "RANDOM_CONNECTIVITY_MATRIX",
    "AUTO_ASSIGN_MATRIX",
    "DEFAULT_MATRIX",
)


def _resolve_matrix_keyword(value: Any, pnl_module: Any) -> Any:
    """Translate a ``MATRIX_KEYWORD`` constant name to PNL's expected value.

    Numeric matrices (lists / arrays) and any unrecognised value pass
    through untouched.
    """
    if not isinstance(value, str):
        return value
    if value not in _MATRIX_KEYWORDS:
        # Pass through any unrecognised string — PNL may know what to do
        # with it (e.g. a Function class name resolved upstream).
        return value
    resolved = getattr(pnl_module, value, None)
    return resolved if resolved is not None else value


def _wrap_result(
    *,
    tool_name: str,
    pre_resolve_kwargs: dict[str, Any],
    instance_handle: str,
    result: Any,
) -> Any:
    """Mirror the constructor template's return-shape contract.

    JSON-friendly results pass through; non-JSON results get registered
    as handles and returned as the ``{handle, type, name, repr}``
    payload. Either way one ``JournalEntry`` is appended.
    """
    if result is None:
        handles.record_call(
            tool_name,
            pre_resolve_kwargs,
            result_handle=None,
            tool_layer="generated",
        )
        return {"composition": instance_handle}

    try:
        json.dumps(result)
    except (TypeError, ValueError):
        payload = handles.register_handle(result)
        handles.record_call(
            tool_name,
            pre_resolve_kwargs,
            result_handle=(
                payload.get("handle") if isinstance(payload, dict) else None
            ),
            tool_layer="generated",
        )
        return payload

    handles.record_call(
        tool_name,
        pre_resolve_kwargs,
        result_handle=None,
        tool_layer="generated",
    )
    return result
