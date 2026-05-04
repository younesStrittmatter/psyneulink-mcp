"""Adapter registry + selection.

Selection is env-only (``$PSYNEULINK_MCP_LLM_ADAPTER``) — matches the
rest of this repo's config style (see ``corpus.corpus_repo()`` and
``feedback.feedback_path()``).

Adding a third adapter is a one-line registry edit; no plugin
machinery.
"""

from __future__ import annotations

import os
from collections.abc import Callable

from .base import LLMAdapter, ToolSpec, validate_tool_spec

ENV_LLM_ADAPTER = "PSYNEULINK_MCP_LLM_ADAPTER"
DEFAULT_ADAPTER = "claude_cli"


class AdapterError(RuntimeError):
    """Raised by any adapter when generation cannot proceed.

    Always actionable: points at a missing binary, a missing
    dependency, a non-zero CLI exit, or a malformed LLM response, with
    the fix.
    """


def _make_claude_cli() -> LLMAdapter:
    from .claude_cli import ClaudeCLIAdapter

    return ClaudeCLIAdapter()


def _make_anthropic_api() -> LLMAdapter:
    from .anthropic_api import AnthropicAPIAdapter

    return AnthropicAPIAdapter()


ADAPTERS: dict[str, Callable[[], LLMAdapter]] = {
    "claude_cli": _make_claude_cli,
    "anthropic_api": _make_anthropic_api,
}


def get_adapter(name: str | None = None) -> LLMAdapter:
    """Return an adapter instance by name (env-default if ``name`` is None).

    Raises:
        AdapterError: if ``name`` is not in the registry or the
            adapter's constructor signals a missing prerequisite.
    """
    name = name or os.environ.get(ENV_LLM_ADAPTER, DEFAULT_ADAPTER)
    if name not in ADAPTERS:
        raise AdapterError(
            f"unknown adapter {name!r}; pick one of {sorted(ADAPTERS)}"
        )
    return ADAPTERS[name]()


__all__ = [
    "ADAPTERS",
    "DEFAULT_ADAPTER",
    "ENV_LLM_ADAPTER",
    "AdapterError",
    "LLMAdapter",
    "ToolSpec",
    "get_adapter",
    "validate_tool_spec",
]
