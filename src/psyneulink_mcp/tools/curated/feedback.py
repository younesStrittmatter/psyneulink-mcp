"""Curated tool: agents call this to report problems with other tools."""

from __future__ import annotations

from typing import Any, Literal

from ...feedback import captured_tool, log_agent_report, lookup_tool_layer

IssueType = Literal[
    "unclear_description",
    "wrong_schema",
    "missing_arg",
    "wrong_behavior",
    "other",
]


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="curated")
    def report_tool_issue(
        tool_name: str,
        issue_type: IssueType,
        description: str,
        suggested_fix: str | None = None,
        agent_context: str | None = None,
    ) -> dict[str, Any]:
        """Report a problem with another tool exposed by this MCP server.

        WHEN TO CALL: after using a tool, if its description was misleading,
        its JSON schema didn't match the actual signature, an obvious arg was
        missing, or the behavior differed from what the description promised.

        DO NOT CALL for ordinary domain errors (e.g. an invalid PsyNeuLink
        configuration, a value out of range) — only for problems with the
        *tool surface itself*. Runtime exceptions are auto-captured already,
        so you don't need to re-report crashes.

        Args:
            tool_name: Name of the tool the issue is about.
            issue_type: One of "unclear_description", "wrong_schema",
                "missing_arg", "wrong_behavior", "other".
            description: What was wrong, in plain language.
            suggested_fix: Optional — what would have made the tool usable.
            agent_context: Optional — what you were trying to accomplish.

        Returns:
            {"recorded": True} on success. Recording is best-effort and
            never raises; failures are logged to stderr.
        """
        log_agent_report(
            tool_name=tool_name,
            tool_layer=lookup_tool_layer(tool_name),
            issue_type=issue_type,
            description=description,
            suggested_fix=suggested_fix,
            agent_context=agent_context,
        )
        return {"recorded": True}
