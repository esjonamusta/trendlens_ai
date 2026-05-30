"""Base agent implementation.

This provides a lightweight BaseAgent class suitable for LangChain integration
in the future. It intentionally avoids heavy external dependencies so tests
can run in the hackathon environment.
"""
from typing import Any, Dict, Callable, Optional
import logging
import time

logger = logging.getLogger("trendlens.agents")
if not logger.handlers:
    handler = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class BaseAgent:
    """Minimal agent abstraction.

    Subclass and implement `run()` for agent behaviour. Use `call_tool`
    to access registered tool functions.
    """

    def __init__(self, name: str, tools: Optional[Dict[str, Callable]] = None):
        self.name = name
        self.tools = tools or {}
        self.log_context: Dict[str, Any] = {}
        logger.info("Initialized agent %s", self.name)

    def register_tool(self, name: str, func: Callable):
        self.tools[name] = func
        logger.debug("Agent %s registered tool %s", self.name, name)

    def call_tool(self, name: str, *args, **kwargs):
        if name not in self.tools:
            logger.error("Tool %s not found for agent %s", name, self.name)
            raise KeyError(name)
        logger.info("Agent %s calling tool %s", self.name, name)
        start = time.time()
        result = self.tools[name](*args, **kwargs)
        elapsed = time.time() - start
        logger.info("Tool %s finished in %.3fs", name, elapsed)
        return result

    def run(self, *args, **kwargs) -> Any:
        """Override in subclasses.

        Example:
            def run(self, product_desc):
                signals = self.call_tool("fetch_reddit", product_desc)
                return signals
        """
        raise NotImplementedError()
