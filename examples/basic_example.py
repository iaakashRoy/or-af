"""
Basic example of using OR-AF.

This example demonstrates how to create a simple agent and use it
to perform tasks.
"""

from or_af import Agent


class OptimizationAgent(Agent):
    """Simple optimization agent example."""
    
    def execute(self, task: str, **kwargs):
        """Execute an optimization task."""
        problem_type = kwargs.get("problem_type", "unknown")
        data = kwargs.get("data", {})
        
        print(f"Executing {task} with problem type: {problem_type}")
        print(f"Data: {data}")
        
        # Simulate optimization
        result = {
            "status": "optimal",
            "objective_value": 42.0,
            "solution": [1, 2, 3]
        }
        
        return result


def main():
    """Main function."""
    print("OR-AF Basic Example")
    print("-" * 50)
    
    # Create an agent
    agent = OptimizationAgent(
        name="optimizer",
        description="Solves optimization problems",
        capabilities=["linear_programming", "integer_programming"]
    )
    
    print(f"Created agent: {agent}")
    print()
    
    # Execute a task
    result = agent.execute(
        "optimize",
        problem_type="linear",
        data={"constraints": 5, "variables": 10}
    )
    
    print(f"\nResult: {result}")
    
    # Update agent state
    agent.update_state({"last_result": result})
    print(f"\nAgent state: {agent.get_state()}")


if __name__ == "__main__":
    main()
