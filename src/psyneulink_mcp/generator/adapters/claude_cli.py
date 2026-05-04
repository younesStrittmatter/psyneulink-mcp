"""Adapter that shells out to the local ``claude`` CLI.

This is the default adapter and the one that uses the user's Claude Max
subscription via the CLI's local OAuth — no API key needed. ``--bare``
is intentionally **not** passed because that mode forces
``ANTHROPIC_API_KEY`` and bypasses Max-plan auth.

Flag set used (verified against the installed CLI; adjust if Anthropic
renames any of these):

* ``--print`` — non-interactive, single response then exit
* ``--output-format json`` — wraps the response in a JSON envelope
* ``--json-schema <schema>`` — server-side structured-output validation
* ``--no-session-persistence`` — no resume garbage between runs
* ``--model <name>`` — alias or full model name
* ``--max-budget-usd <n>`` — optional spend cap
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from typing import Any

from . import AdapterError
from .base import ToolSpec, validate_tool_spec

ENV_CLAUDE_CMD = "PSYNEULINK_MCP_CLAUDE_CMD"
ENV_CLAUDE_MODEL = "PSYNEULINK_MCP_CLAUDE_MODEL"
ENV_CLAUDE_MAX_BUDGET_USD = "PSYNEULINK_MCP_CLAUDE_MAX_BUDGET_USD"
ENV_CLAUDE_TIMEOUT_S = "PSYNEULINK_MCP_CLAUDE_TIMEOUT_S"

DEFAULT_CMD = "claude"
DEFAULT_MODEL = "sonnet"
DEFAULT_TIMEOUT_S = 120


class ClaudeCLIAdapter:
    """Shells out to the local ``claude`` CLI in ``--print`` mode."""

    name = "claude_cli"

    def __init__(
        self,
        *,
        cmd: str | None = None,
        model: str | None = None,
        max_budget_usd: float | None = None,
        timeout_s: int | None = None,
    ) -> None:
        self.cmd = cmd or os.environ.get(ENV_CLAUDE_CMD, DEFAULT_CMD)
        self.model = model or os.environ.get(ENV_CLAUDE_MODEL, DEFAULT_MODEL)
        env_budget = os.environ.get(ENV_CLAUDE_MAX_BUDGET_USD)
        self.max_budget_usd = (
            max_budget_usd
            if max_budget_usd is not None
            else (float(env_budget) if env_budget else None)
        )
        env_timeout = os.environ.get(ENV_CLAUDE_TIMEOUT_S)
        self.timeout_s = (
            timeout_s
            if timeout_s is not None
            else (int(env_timeout) if env_timeout else DEFAULT_TIMEOUT_S)
        )

    def build_argv(self, schema: dict[str, Any]) -> list[str]:
        """Build the argv passed to ``subprocess.run``.

        Split out so tests can assert flag composition without mocking
        the full subprocess invocation.
        """
        argv = [
            self.cmd,
            "--print",
            "--output-format",
            "json",
            "--json-schema",
            json.dumps(schema, separators=(",", ":")),
            "--no-session-persistence",
            "--model",
            self.model,
        ]
        if self.max_budget_usd is not None:
            argv += ["--max-budget-usd", str(self.max_budget_usd)]
        return argv

    def generate(self, prompt: str, *, schema: dict[str, Any]) -> ToolSpec:
        if shutil.which(self.cmd) is None:
            raise AdapterError(
                f"`{self.cmd}` CLI not found on PATH. Install Claude Code from "
                "https://docs.anthropic.com/en/docs/claude-code or set "
                f"${ENV_CLAUDE_CMD} to a full path to the binary."
            )

        argv = self.build_argv(schema)
        try:
            result = subprocess.run(
                argv,
                input=prompt,
                capture_output=True,
                text=True,
                timeout=self.timeout_s,
                check=False,
            )
        except subprocess.TimeoutExpired as e:
            raise AdapterError(
                f"`claude` CLI timed out after {self.timeout_s}s"
            ) from e
        except FileNotFoundError as e:
            raise AdapterError(f"`{self.cmd}` exec failed: {e}") from e

        if result.returncode != 0:
            stderr = (result.stderr or "").strip()
            raise AdapterError(
                f"`claude` exited {result.returncode}: {stderr or '(no stderr)'}"
            )

        spec = _parse_cli_output(result.stdout)
        validate_tool_spec(spec, schema)
        return spec  # type: ignore[return-value]


def _parse_cli_output(stdout: str) -> Any:
    """Extract the structured-output payload from the CLI's JSON wrapper.

    With ``--output-format json`` the CLI wraps its response in
    ``{"type": "result", "result": "...", "structured_output": {...}, ...}``.

    Precedence:

    1. ``structured_output`` if present and non-empty — this is the
       schema-validated payload that ``--json-schema`` populates. The
       ``result`` field is typically empty when ``--json-schema`` is set.
    2. ``result`` otherwise — accepted as a parsed object or as a JSON
       string that we then parse.
    3. The wrapper itself, for the rare case where stdout is the bare
       ToolSpec.
    """
    text = stdout.strip()
    if not text:
        raise AdapterError("`claude` produced empty output")
    try:
        wrapper = json.loads(text)
    except json.JSONDecodeError as e:
        raise AdapterError(
            f"could not parse claude CLI output as JSON: {e}; "
            f"first 200 chars: {text[:200]!r}"
        ) from e

    if isinstance(wrapper, dict) and wrapper.get("structured_output"):
        return wrapper["structured_output"]

    if isinstance(wrapper, dict) and "result" in wrapper:
        payload = wrapper["result"]
    else:
        payload = wrapper

    if isinstance(payload, str):
        if not payload.strip():
            raise AdapterError(
                "`claude` returned an empty `result` field and no "
                "`structured_output`. Has the CLI flag set changed?"
            )
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError as e:
            raise AdapterError(
                f"`result` field is not valid JSON: {e}; "
                f"first 200 chars: {payload[:200]!r}"
            ) from e
    return payload
