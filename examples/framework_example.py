"""
Framework example demonstrating multi-agent coordination.

This example shows how to use the ORFramework to manage and
coordinate multiple agents.
"""

from or_af import ORFramework, Agent


class DataPreprocessingAgent(Agent):
    """Agent for preprocessing data."""
    
    def execute(self, task: str, **kwargs):
        """Execute data preprocessing."""
        data = kwargs.get("data", [])
        print(f"Preprocessing {len(data)} data points...")
        # Simulate preprocessing
        processed_data = [x * 2 for x in data]
        return {"preprocessed_data": processed_data}


class OptimizationAgent(Agent):
    """Agent for solving optimization problems."""
    
    def execute(self, task: str, **kwargs):
        """Execute optimization."""
        data = kwargs.get("data", [])
        print(f"Optimizing with {len(data)} data points...")
        # Simulate optimization
        return {
            "optimal_solution": sum(data) / len(data) if data else 0,
            "status": "optimal"
        }


class ReportingAgent(Agent):
    """Agent for generating reports."""
    
    def execute(self, task: str, **kwargs):
        """Generate a report."""
        results = kwargs.get("results", {})
        print(f"Generating report with {len(results)} results...")
        # Simulate report generation
        report = f"Report:\n{'-' * 40}\n"
        for key, value in results.items():
            report += f"{key}: {value}\n"
        return report


def main():
    """Main function."""
    print("OR-AF Framework Example")
    print("=" * 50)
    
    # Create framework
    framework = ORFramework(name="OR-Pipeline")
    
    # Create and register agents
    preprocessor = DataPreprocessingAgent(
        name="preprocessor",
        capabilities=["data_cleaning", "normalization"]
    )
    optimizer = OptimizationAgent(
        name="optimizer",
        capabilities=["linear_programming"]
    )
    reporter = ReportingAgent(
        name="reporter",
        capabilities=["report_generation"]
    )
    
    framework.register_agent(preprocessor)
    framework.register_agent(optimizer)
    framework.register_agent(reporter)
    
    print(f"Framework: {framework}")
    print(f"Registered agents: {[a.name for a in framework.agents]}\n")
    
    # Execute a pipeline of tasks
    print("Executing pipeline...")
    print("-" * 50)
    
    # Step 1: Preprocess data
    raw_data = [1, 2, 3, 4, 5]
    preprocess_result = framework.execute_task(
        "preprocessor",
        "preprocess",
        data=raw_data
    )
    
    # Step 2: Optimize
    optimization_result = framework.execute_task(
        "optimizer",
        "optimize",
        data=preprocess_result["preprocessed_data"]
    )
    
    # Step 3: Generate report
    all_results = {
        "raw_data": raw_data,
        "preprocessed": preprocess_result,
        "optimization": optimization_result
    }
    report = framework.execute_task(
        "reporter",
        "generate_report",
        results=all_results
    )
    
    print("\n" + "=" * 50)
    print(report)
    
    # Show all results
    print("\nAll framework results:")
    for key, value in framework.get_results().items():
        print(f"  {key}: {type(value).__name__}")


if __name__ == "__main__":
    main()
