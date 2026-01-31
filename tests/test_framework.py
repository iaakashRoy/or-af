"""Tests for the ORFramework class."""

import pytest
from or_af.framework import ORFramework
from or_af.agent import Agent


class MockAgent(Agent):
    """Mock agent for testing."""
    
    def execute(self, task: str, **kwargs):
        """Execute a mock task."""
        return f"MockAgent executed {task} with {kwargs}"


class TestORFramework:
    """Test ORFramework functionality."""
    
    def test_framework_creation(self):
        """Test framework can be created."""
        framework = ORFramework()
        assert framework.name == "OR-AF"
        assert framework.agents == []
    
    def test_framework_with_name(self):
        """Test framework creation with custom name."""
        framework = ORFramework(name="CustomFramework")
        assert framework.name == "CustomFramework"
    
    def test_register_agent(self):
        """Test registering an agent."""
        framework = ORFramework()
        agent = MockAgent(name="agent1")
        
        framework.register_agent(agent)
        assert len(framework.agents) == 1
        assert framework.agents[0] == agent
    
    def test_register_multiple_agents(self):
        """Test registering multiple agents."""
        framework = ORFramework()
        agent1 = MockAgent(name="agent1")
        agent2 = MockAgent(name="agent2")
        
        framework.register_agent(agent1)
        framework.register_agent(agent2)
        assert len(framework.agents) == 2
    
    def test_register_non_agent_raises_error(self):
        """Test that registering non-Agent raises TypeError."""
        framework = ORFramework()
        with pytest.raises(TypeError):
            framework.register_agent("not an agent")
    
    def test_get_agent(self):
        """Test retrieving an agent by name."""
        framework = ORFramework()
        agent = MockAgent(name="agent1")
        framework.register_agent(agent)
        
        retrieved = framework.get_agent("agent1")
        assert retrieved == agent
    
    def test_get_agent_not_found(self):
        """Test getting a non-existent agent returns None."""
        framework = ORFramework()
        assert framework.get_agent("nonexistent") is None
    
    def test_remove_agent(self):
        """Test removing an agent."""
        framework = ORFramework()
        agent = MockAgent(name="agent1")
        framework.register_agent(agent)
        
        result = framework.remove_agent("agent1")
        assert result is True
        assert len(framework.agents) == 0
    
    def test_remove_nonexistent_agent(self):
        """Test removing a non-existent agent returns False."""
        framework = ORFramework()
        result = framework.remove_agent("nonexistent")
        assert result is False
    
    def test_execute_task(self):
        """Test executing a task with an agent."""
        framework = ORFramework()
        agent = MockAgent(name="agent1")
        framework.register_agent(agent)
        
        result = framework.execute_task("agent1", "test_task", param="value")
        assert "test_task" in result
        assert "param" in result
    
    def test_execute_task_agent_not_found(self):
        """Test executing task with non-existent agent raises ValueError."""
        framework = ORFramework()
        with pytest.raises(ValueError):
            framework.execute_task("nonexistent", "task")
    
    def test_get_results(self):
        """Test getting execution results."""
        framework = ORFramework()
        agent = MockAgent(name="agent1")
        framework.register_agent(agent)
        
        framework.execute_task("agent1", "task1")
        framework.execute_task("agent1", "task2")
        
        results = framework.get_results()
        assert "agent1:task1" in results
        assert "agent1:task2" in results
    
    def test_reset(self):
        """Test resetting the framework."""
        framework = ORFramework()
        agent = MockAgent(name="agent1")
        framework.register_agent(agent)
        
        # Update agent state and execute task
        agent.update_state({"key": "value"})
        framework.execute_task("agent1", "task")
        
        # Reset
        framework.reset()
        
        # Verify results are cleared
        assert framework.get_results() == {}
        # Verify agent state is cleared
        assert agent.get_state() == {}
    
    def test_framework_repr(self):
        """Test framework string representation."""
        framework = ORFramework(name="TestFramework")
        agent = MockAgent(name="agent1")
        framework.register_agent(agent)
        
        repr_str = repr(framework)
        assert "TestFramework" in repr_str
        assert "1" in repr_str
