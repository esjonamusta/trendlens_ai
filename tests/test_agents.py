import pytest
from trendlens_ai.agents.base_agent import BaseAgent
from trendlens_ai.agents.orchestrator import Orchestrator
from trendlens_ai.agents.tools.registry import ToolRegistry
from trendlens_ai.agents.tools import data_fetchers, processors, storage


def test_tool_registry_register_and_call():
    reg = ToolRegistry()
    reg.register("fetch_reddit", data_fetchers.fetch_reddit)
    tools = reg.list_tools()
    assert "fetch_reddit" in tools
    results = reg.call("fetch_reddit", "ai", limit=2)
    assert isinstance(results, list)
    assert len(results) == 2


class SimpleIngestionAgent(BaseAgent):
    def run(self, query: str):
        # call fetchers via tools
        reddit = self.call_tool("fetch_reddit", query, limit=3)
        hn = self.call_tool("fetch_hackernews", query, limit=2)
        gh = self.call_tool("fetch_github", query, limit=1)
        all_signals = reddit + hn + gh
        for s in all_signals:
            self.call_tool("save_signal", s)
        return all_signals


class SimpleClusteringAgent(BaseAgent):
    def run(self, signals):
        clusters = self.call_tool("cluster_by_similarity", signals)
        out = []
        for name, group in clusters:
            score = self.call_tool("score_by_engagement", group)
            trend = {"name": name, "size": len(group), "score": score}
            self.call_tool("save_trend", trend)
            out.append(trend)
        return out


def test_agents_end_to_end():
    storage.clear_storage()
    reg = ToolRegistry()
    # register tools
    reg.register("fetch_reddit", data_fetchers.fetch_reddit)
    reg.register("fetch_hackernews", data_fetchers.fetch_hackernews)
    reg.register("fetch_github", data_fetchers.fetch_github)
    reg.register("cluster_by_similarity", processors.cluster_by_similarity)
    reg.register("score_by_engagement", processors.score_by_engagement)
    reg.register("save_signal", storage.save_signal)
    reg.register("save_trend", storage.save_trend)

    # create agents
    ing = SimpleIngestionAgent("ingestion", tools={
        "fetch_reddit": reg.get("fetch_reddit"),
        "fetch_hackernews": reg.get("fetch_hackernews"),
        "fetch_github": reg.get("fetch_github"),
        "save_signal": reg.get("save_signal"),
    })
    cluster = SimpleClusteringAgent("clustering", tools={
        "cluster_by_similarity": reg.get("cluster_by_similarity"),
        "score_by_engagement": reg.get("score_by_engagement"),
        "save_trend": reg.get("save_trend"),
    })

    orch = Orchestrator([ing, cluster])
    result = orch.run_pipeline("ai agents")
    # check results were written to storage
    trends = storage.list_trends()
    signals = storage.list_signals()
    assert len(signals) > 0
    assert len(trends) > 0
    assert isinstance(result, list)
