from typing import Callable, Dict, Optional
import logging

logger = logging.getLogger("trendlens.tools")


class ToolRegistry:
    """Simple registry for agent tools."""

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable):
        logger.debug("Registering tool %s", name)
        self._tools[name] = func

    def get(self, name: str) -> Optional[Callable]:
        return self._tools.get(name)

    def call(self, name: str, *args, **kwargs):
        func = self.get(name)
        if func is None:
            raise KeyError(f"Tool {name} not found")
        return func(*args, **kwargs)

    def list_tools(self):
        return list(self._tools.keys())
