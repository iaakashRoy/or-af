# OR-AF: Operation Research Agentic Framework

An agentic framework for Operations Research application development.

## Overview

OR-AF (Operations Research Agentic Framework) is a Python framework designed to help developers build intelligent agent-based systems for solving Operations Research problems. It provides a flexible architecture for creating agents that can autonomously perform optimization tasks, make decisions, and coordinate complex OR workflows.

## Features

- **Agent-Based Architecture**: Build autonomous agents for OR tasks
- **Flexible Framework**: Easy-to-extend base classes for custom implementations
- **State Management**: Built-in state management for agents
- **Multi-Agent Coordination**: Framework for orchestrating multiple agents
- **Type-Safe**: Type hints throughout the codebase
- **Lightweight**: Minimal dependencies for maximum compatibility

## Installation

Install from PyPI:

```bash
pip install or-af
```

Install from source:

```bash
git clone https://github.com/iaakashRoy/or-af.git
cd or-af
pip install -e .
```

## Quick Start

### Creating a Simple Agent

```python
from or_af import Agent

class OptimizationAgent(Agent):
    def execute(self, task: str, **kwargs):
        # Your optimization logic here
        return f"Executed {task} with parameters {kwargs}"

# Create and use the agent
agent = OptimizationAgent(
    name="optimizer",
    description="Solves optimization problems",
    capabilities=["linear_programming", "integer_programming"]
)

result = agent.execute("optimize", problem_type="linear")
print(result)
```

### Using the Framework

```python
from or_af import ORFramework, Agent

class SchedulingAgent(Agent):
    def execute(self, task: str, **kwargs):
        # Scheduling logic
        return f"Scheduled {kwargs.get('jobs', 0)} jobs"

# Create framework
framework = ORFramework(name="OR-System")

# Register agents
agent = SchedulingAgent(name="scheduler", capabilities=["job_shop"])
framework.register_agent(agent)

# Execute tasks
result = framework.execute_task("scheduler", "schedule", jobs=10)
print(result)
```

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/iaakashRoy/or-af.git
cd or-af

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black or_af/
```

## Project Structure

```
or-af/
├── or_af/              # Main package directory
│   ├── __init__.py     # Package initialization
│   ├── agent.py        # Base Agent class
│   └── framework.py    # ORFramework class
├── tests/              # Test directory
├── pyproject.toml      # Package configuration
├── LICENSE             # MIT License
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Aakash Roy**
- GitHub: [@iaakashRoy](https://github.com/iaakashRoy)

## Roadmap

- [ ] Add support for common OR solvers (PuLP, OR-Tools)
- [ ] Implement pre-built agents for common OR problems
- [ ] Add visualization utilities
- [ ] Enhance multi-agent communication
- [ ] Add more examples and tutorials

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/iaakashRoy/or-af).
