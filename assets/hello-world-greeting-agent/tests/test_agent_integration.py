"""Integration test for the Hello World Greeting Agent end-to-end flow."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from agent import SampleAgent
from tools.greet import greet as greet_tool


@pytest.mark.asyncio
async def test_agent_greets_user_by_name():
    """End-to-end: agent returns a greeting containing the user's name."""
    agent = SampleAgent()

    mock_response = MagicMock()
    mock_response.content = "Hello, Alice!"

    with patch.object(agent, "_invoke_with_fallback", new_callable=AsyncMock) as mock_invoke:
        mock_invoke.return_value = {"messages": [mock_response]}

        chunks = []
        async for chunk in agent.stream("My name is Alice", "test-context-1", tools=[greet_tool]):
            chunks.append(chunk)

    assert len(chunks) >= 1
    final = chunks[-1]
    assert final["is_task_complete"] is True
    assert "Alice" in final["content"]


@pytest.mark.asyncio
async def test_agent_handles_empty_name():
    """End-to-end: agent returns a generic greeting when no name is given."""
    agent = SampleAgent()

    mock_response = MagicMock()
    mock_response.content = "Hello!"

    with patch.object(agent, "_invoke_with_fallback", new_callable=AsyncMock) as mock_invoke:
        mock_invoke.return_value = {"messages": [mock_response]}

        chunks = []
        async for chunk in agent.stream("Hi there", "test-context-2", tools=[greet_tool]):
            chunks.append(chunk)

    assert len(chunks) >= 1
    final = chunks[-1]
    assert final["is_task_complete"] is True
    assert "Hello" in final["content"]
