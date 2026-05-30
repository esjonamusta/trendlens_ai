"""Simple orchestrator to run agents in sequence.

The orchestrator is intentionally minimal for the MVP: it executes a list of
agents in order, passing outputs between them when needed.
"""
from typing import List, Any
import logging

logger = logging.getLogger("trendlens.orchestrator")


class Orchestrator:
    def __init__(self, agents: List[Any]):
        self.agents = agents
        logger.info("Orchestrator initialized with %d agents", len(agents))

    def run_pipeline(self, *args, **kwargs):
        """Run each agent sequentially. The output of one agent is passed to the
        next as the first positional argument.
        """
        output = None
        for i, agent in enumerate(self.agents):
            logger.info("Running agent %d: %s", i, getattr(agent, "name", agent))
            if output is None:
                output = agent.run(*args, **kwargs)
            else:
                output = agent.run(output)
        return output
