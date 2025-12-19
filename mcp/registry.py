# mcp/registry.py
from typing import Dict, Callable

class MCPRegistry:
    def __init__(self):
        self.tools: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable):
        self.tools[name] = func

    def get_tools(self):
        return self.tools


mcp_registry = MCPRegistry()
