"""Test-suite-wide safety nets.

Anything that could otherwise reach a network or a real `gh` install on a
developer's machine gets forced into a known-safe default here. Individual
tests that need to exercise the live behaviour re-enable it via monkeypatch.
"""

from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def _disable_auto_issue_filing(monkeypatch):
    """Ensure no test ever opens a real GitHub issue against the corpus repo.

    The runtime path mirrors `feedback.log_runtime_error` to GitHub via
    `feedback_publisher.try_file`. Default-on is the right behaviour at
    runtime, but tests must default-off so a developer with `gh` installed
    and authed doesn't have unit tests posting issues to the corpus. Tests
    that exercise the publisher set this env back to ``"1"`` themselves.
    """
    monkeypatch.setenv("PSYNEULINK_MCP_AUTO_FILE_ISSUES", "0")
