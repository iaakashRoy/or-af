"""Tests for the Agent class."""

import pytest
from or_af.agent import Agent


class TestAgent(Agent):
    """Test implementation of Agent."""
    
    def execute(self, task: str, **kwargs):
        """Execute a test task."""
        return f"Executed {task}"


class TestAgentBasics:
    """Test basic Agent functionality."""
    
    def test_agent_creation(self):
        """Test agent can be created with basic parameters."""
        agent = TestAgent(name="test_agent")
        assert agent.name == "test_agent"
        assert agent.description == ""
        assert agent.capabilities == []
    
    def test_agent_with_capabilities(self):
        """Test agent creation with capabilities."""
        capabilities = ["capability1", "capability2"]
        agent = TestAgent(
            name="test_agent",
            description="A test agent",
            capabilities=capabilities
        )
        assert agent.name == "test_agent"
        assert agent.description == "A test agent"
        assert agent.capabilities == capabilities
    
    def test_agent_execute(self):
        """Test agent execution."""
        agent = TestAgent(name="test_agent")
        result = agent.execute("test_task")
        assert result == "Executed test_task"
    
    def test_agent_state_management(self):
        """Test agent state management."""
        agent = TestAgent(name="test_agent")
        
        # Initial state should be empty
        assert agent.get_state() == {}
        
        # Update state
        agent.update_state({"key": "value"})
        assert agent.get_state() == {"key": "value"}
        
        # Update more state
        agent.update_state({"another_key": "another_value"})
        state = agent.get_state()
        assert state["key"] == "value"
        assert state["another_key"] == "another_value"
        
        # Reset state
        agent.reset()
        assert agent.get_state() == {}
    
    def test_agent_repr(self):
        """Test agent string representation."""
        agent = TestAgent(
            name="test_agent",
            capabilities=["cap1", "cap2"]
        )
        repr_str = repr(agent)
        assert "test_agent" in repr_str
        assert "cap1" in repr_str


class TestAgentInheritance:
    """Test Agent inheritance and abstract methods."""
    
    def test_base_agent_execute_not_implemented(self):
        """Test that base Agent.execute raises NotImplementedError."""
        agent = Agent(name="base_agent")
        with pytest.raises(NotImplementedError):
            agent.execute("task")
