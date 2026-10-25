"""The regression marker is registered with the other kit markers."""

from __future__ import annotations

import pytest


def test_regression_marker_is_registered(pytestconfig: pytest.Config) -> None:
    """pytestconfig: this run's config. regression names the broad-suite tier."""
    markers = pytestconfig.getini("markers")
    names = [str(line).split(":", 1)[0].strip() for line in markers]
    assert "regression" in names
