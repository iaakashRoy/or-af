"""
Framework module for OR-AF.

This module provides the main ORFramework class that orchestrates
multiple agents for solving Operations Research problems.
"""

from typing import Any, Dict, List, Optional
from or_af.agent import Agent


class ORFramework:
    """
    Main framework class for orchestrating OR agents.
    
    The ORFramework manages multiple agents, coordinates their execution,
    and provides utilities for solving Operations Research problems.
    
    Attributes:
        name (str): The name of the framework instance.
        agents (List[Agent]): List of agents managed by the framework.
    """
    
    def __init__(self, name: str = "OR-AF"):
        """
        Initialize the OR Framework.
        
        Args:
            name: The name of the framework instance
        """
        self.name = name
        self.agents: List[Agent] = []
        self._results: Dict[str, Any] = {}
    
    def register_agent(self, agent: Agent) -> None:
        """
        Register an agent with the framework.
        
        Args:
            agent: The agent to register
        """
        if not isinstance(agent, Agent):
            raise TypeError("Only Agent instances can be registered")
        self.agents.append(agent)
    
    def remove_agent(self, agent_name: str) -> bool:
        """
        Remove an agent from the framework.
        
        Args:
            agent_name: The name of the agent to remove
            
        Returns:
            True if agent was removed, False if not found
        """
        for i, agent in enumerate(self.agents):
            if agent.name == agent_name:
                self.agents.pop(i)
                return True
        return False
    
    def get_agent(self, name: str) -> Optional[Agent]:
        """
        Get an agent by name.
        
        Args:
            name: The name of the agent to retrieve
            
        Returns:
            The agent if found, None otherwise
        """
        for agent in self.agents:
            if agent.name == name:
                return agent
        return None
    
    def execute_task(self, agent_name: str, task: str, **kwargs) -> Any:
        """
        Execute a task using a specific agent.
        
        Args:
            agent_name: The name of the agent to use
            task: The task to execute
            **kwargs: Additional arguments for task execution
            
        Returns:
            The result of task execution
            
        Raises:
            ValueError: If agent is not found
        """
        agent = self.get_agent(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found")
        
        result = agent.execute(task, **kwargs)
        self._results[f"{agent_name}:{task}"] = result
        return result
    
    def get_results(self) -> Dict[str, Any]:
        """
        Get all execution results.
        
        Returns:
            Dictionary of all results
        """
        return self._results.copy()
    
    def reset(self) -> None:
        """Reset the framework and all agents."""
        for agent in self.agents:
            agent.reset()
        self._results.clear()
    
    def __repr__(self) -> str:
        return f"ORFramework(name='{self.name}', agents={len(self.agents)})"
