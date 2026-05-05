"""In-process registry of live PsyNeuLink objects.

Generated tools that construct a non-JSON-serialisable PNL object (a
Mechanism, a Composition, a Function, a Projection) push the instance
into this registry and return a small ``HandleRef`` payload — a stable
string ID plus light metadata. Subsequent tool calls (e.g. ``add_node``,
``run_composition``, or even another generated constructor with a
``function=<handle>`` argument) take handle strings as inputs; the impl
walks its kwargs and rehydrates each handle into the live object before
calling into PNL.

The registry is **process-scoped**: a fresh MCP subprocess starts with
an empty dict, and entries live until the process dies. Each
``psyneulink-agent --chat`` session spawns its own MCP, which matches
the natural "modeling session" lifecycle. We deliberately do not
persist handles or share them across sessions — the moment we'd need
that, the right move is real PNL serialisation, not a pickle of opaque
strings.
"""

from __future__ import annotations

import re
import uuid
from typing import Any

HANDLE_PREFIX = "h_"
HANDLE_PATTERN = re.compile(r"^h_[0-9a-f]{12}$")

_HANDLES: dict[str, Any] = {}


def is_handle_string(value: Any) -> bool:
    """True iff *value* looks like a registered handle ID."""
    return isinstance(value, str) and HANDLE_PATTERN.match(value) is not None


def _handle_payload(handle: str, obj: Any) -> dict[str, Any]:
    return {
        "handle": handle,
        "type": type(obj).__name__,
        "name": getattr(obj, "name", None) or "",
        "repr": repr(obj),
    }


def register_handle(obj: Any) -> dict[str, Any]:
    """Stash *obj* and return its handle payload.

    ``None`` and primitives that round-trip through JSON are returned
    as-is; the agent should never see a handle for something it could
    just read directly.
    """
    if obj is None:
        return None  # type: ignore[return-value]
    handle = HANDLE_PREFIX + uuid.uuid4().hex[:12]
    _HANDLES[handle] = obj
    return _handle_payload(handle, obj)


def resolve_handle(handle: str) -> Any:
    """Return the live object for *handle*, raising on miss."""
    try:
        return _HANDLES[handle]
    except KeyError as exc:
        raise KeyError(
            f"unknown handle: {handle!r}. "
            "Either it was never created in this session or the MCP "
            "subprocess restarted and lost in-memory state."
        ) from exc


def resolve_in(value: Any) -> Any:
    """Walk *value* recursively, swapping handle strings for live objects.

    Used by every generated tool's ``_impl`` so an agent can pass a
    previously-returned handle anywhere a PNL constructor expects an
    object: ``create_transfer_mechanism(args={"function": "h_abc..."})``
    just works.
    """
    if is_handle_string(value):
        return resolve_handle(value)
    if isinstance(value, list):
        return [resolve_in(item) for item in value]
    if isinstance(value, tuple):
        return tuple(resolve_in(item) for item in value)
    if isinstance(value, dict):
        return {key: resolve_in(item) for key, item in value.items()}
    return value


def list_handles() -> list[dict[str, Any]]:
    """Snapshot of every handle currently alive in this MCP process."""
    return [_handle_payload(handle, obj) for handle, obj in _HANDLES.items()]


def describe_handle(handle: str) -> dict[str, Any]:
    """Single-handle view (errors if unknown)."""
    return _handle_payload(handle, resolve_handle(handle))


def clear_handles() -> int:
    """Drop everything; primarily for tests. Returns count cleared."""
    n = len(_HANDLES)
    _HANDLES.clear()
    return n
