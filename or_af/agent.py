"""
Agent module for OR-AF framework.

This module provides the base Agent class for creating intelligent agents
in Operations Research applications.
"""

from typing import Any, Dict, List, Optional


class Agent:
    """
    Base Agent class for Operations Research applications.
    
    An Agent represents an autonomous entity that can perform operations,
    make decisions, and interact with OR problems.
    
    Attributes:
        name (str): The name of the agent.
        description (str): A description of the agent's purpose.
        capabilities (List[str]): List of capabilities the agent has.
    """
    
    def __init__(
        self,
        name: str,
        description: str = "",
        capabilities: Optional[List[str]] = None
    ):
        """
        Initialize an Agent.
        
        Args:
            name: The name of the agent
            description: A description of the agent's purpose
            capabilities: List of capabilities the agent possesses
        """
        self.name = name
        self.description = description
        self.capabilities = capabilities or []
        self._state: Dict[str, Any] = {}
    
    def execute(self, task: str, **kwargs) -> Any:
        """
        Execute a task.
        
        Args:
            task: The task to execute
            **kwargs: Additional arguments for task execution
            
        Returns:
            The result of task execution
        """
        raise NotImplementedError("Subclasses must implement execute method")
    
    def get_state(self) -> Dict[str, Any]:
        """
        Get the current state of the agent.
        
        Returns:
            Dictionary containing the agent's state
        """
        return self._state.copy()
    
    def update_state(self, updates: Dict[str, Any]) -> None:
        """
        Update the agent's state.
        
        Args:
            updates: Dictionary of state updates
        """
        self._state.update(updates)
    
    def reset(self) -> None:
        """Reset the agent's state."""
        self._state.clear()
    
    def __repr__(self) -> str:
        return f"Agent(name='{self.name}', capabilities={self.capabilities})"
