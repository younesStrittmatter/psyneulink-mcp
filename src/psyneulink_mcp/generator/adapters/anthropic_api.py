"""Adapter that calls the Anthropic API via the ``anthropic`` SDK.

The SDK is an **optional extra**. ``import anthropic`` is lazy and
deferred to constructor time so the rest of the codebase — including
``psyneulink_mcp.server`` — keeps importing cleanly when the extra is
not installed.

Install with::

    uv pip install 'psyneulink-mcp[anthropic-api]'

Structured output is enforced by passing a synthetic ``emit_tool_spec``
tool whose ``input_schema`` IS the :data:`ToolSpec` schema and forcing
the model to call it via ``tool_choice``. Same guarantee as the CLI's
``--json-schema``.
"""

from __future__ import annotations

import os
from typing import Any

from . import AdapterError
from .base import ToolSpec, validate_tool_spec

ENV_ANTHROPIC_MODEL = "PSYNEULINK_MCP_ANTHROPIC_MODEL"
ENV_ANTHROPIC_TIMEOUT_S = "PSYNEULINK_MCP_ANTHROPIC_TIMEOUT_S"

DEFAULT_MODEL = "claude-sonnet-4-5"
DEFAULT_TIMEOUT_S = 120
EMIT_TOOL_NAME = "emit_tool_spec"


class AnthropicAPIAdapter:
    """Calls ``client.messages.create`` with a forced ``tool_use`` turn."""

    name = "anthropic_api"

    def __init__(
        self,
        *,
        model: str | None = None,
        timeout_s: int | None = None,
    ) -> None:
        try:
            import anthropic  # noqa: F401
        except ImportError as e:
            raise AdapterError(
                "anthropic SDK not installed. "
                "install with: uv pip install 'psyneulink-mcp[anthropic-api]'"
            ) from e
        self._anthropic = anthropic
        self.model = model or os.environ.get(ENV_ANTHROPIC_MODEL, DEFAULT_MODEL)
        env_timeout = os.environ.get(ENV_ANTHROPIC_TIMEOUT_S)
        self.timeout_s = (
            timeout_s
            if timeout_s is not None
            else (int(env_timeout) if env_timeout else DEFAULT_TIMEOUT_S)
        )
        self._client = self._anthropic.Anthropic(timeout=float(self.timeout_s))

    def generate(self, prompt: str, *, schema: dict[str, Any]) -> ToolSpec:
        tool = {
            "name": EMIT_TOOL_NAME,
            "description": (
                "Emit the structured ToolSpec for the requested PNL symbol. "
                "Call this exactly once."
            ),
            "input_schema": schema,
        }
        try:
            msg = self._client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}],
                tools=[tool],
                tool_choice={"type": "tool", "name": EMIT_TOOL_NAME},
            )
        except Exception as e:  # noqa: BLE001 — surface SDK error
            raise AdapterError(f"anthropic API call failed: {e}") from e

        for block in msg.content:
            if (
                getattr(block, "type", None) == "tool_use"
                and getattr(block, "name", None) == EMIT_TOOL_NAME
            ):
                spec = block.input
                validate_tool_spec(spec, schema)
                return spec  # type: ignore[return-value]

        raise AdapterError(
            "anthropic API response did not include the forced tool_use block"
        )
