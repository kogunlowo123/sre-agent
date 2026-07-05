"""SRE Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_define_slo():
    """Test Define an SLO with SLIs and error budget."""
    tools = AgentTools()
    result = await tools.define_slo(service="test", sli_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_error_budget():
    """Test Check remaining error budget for a service."""
    tools = AgentTools()
    result = await tools.check_error_budget(service="test", slo_name="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_plan_capacity():
    """Test Forecast capacity needs based on growth trends."""
    tools = AgentTools()
    result = await tools.plan_capacity(service="test", forecast_months=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_identify_toil():
    """Test Identify repetitive manual tasks that can be automated."""
    tools = AgentTools()
    result = await tools.identify_toil(team="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.sre_agent_agent import SreAgentAgent
    agent = SreAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
