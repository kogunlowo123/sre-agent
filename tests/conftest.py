"""Test configuration for SRE Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "sre-agent", "category": "DevOps & Platform Engineering"}
