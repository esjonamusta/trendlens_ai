import pytest
from trendlens_ai.agents.langchain_agent import LangChainAgent


def test_langchain_agent_imports_and_runs():
    agent = LangChainAgent(name="test-agent", prompt_template="Say hello: {input}")
    result = agent.run("world")
    assert isinstance(result, dict)
    assert result["name"] == "test-agent"
    assert "output" in result
    assert "payload" in result
    assert result["payload"]["input"] == "world"
