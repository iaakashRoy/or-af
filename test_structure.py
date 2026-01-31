"""
Test script to verify the new OR-AF module structure works correctly.
"""

print("=" * 60)
print("Testing OR-AF v0.3.0 Module Structure")
print("=" * 60)

# Test 1: Core module
try:
    from or_af.core import Agent, Tool
    print("✓ or_af.core imports OK (Agent, Tool)")
except Exception as e:
    print(f"✗ or_af.core import error: {e}")

# Test 2: MCP module
try:
    from or_af.mcp import MCPServer, MCPClient, MCPServerStatus
    print("✓ or_af.mcp imports OK (MCPServer, MCPClient)")
except Exception as e:
    print(f"✗ or_af.mcp import error: {e}")

# Test 3: Workflow module
try:
    from or_af.workflow import (
        WorkflowGraph, Sequential, Parallel, 
        Node, EdgeCondition, visualize_workflow
    )
    print("✓ or_af.workflow imports OK (WorkflowGraph, Sequential, etc.)")
except Exception as e:
    print(f"✗ or_af.workflow import error: {e}")

# Test 4: A2A module
try:
    from or_af.a2a import A2AProtocol, A2AMessage, AgentCard, MessageType
    print("✓ or_af.a2a imports OK (A2AProtocol, A2AMessage)")
except Exception as e:
    print(f"✗ or_af.a2a import error: {e}")

# Test 5: Models module
try:
    from or_af.models import (
        AgentConfig, AgentResponse, ToolSchema, ToolResult,
        IterationState, EventType
    )
    print("✓ or_af.models imports OK (AgentConfig, ToolSchema, etc.)")
except Exception as e:
    print(f"✗ or_af.models import error: {e}")

# Test 6: Callbacks module
try:
    from or_af.callbacks import (
        CallbackHandler, ConsoleCallback, FileCallback, MetricsCallback
    )
    print("✓ or_af.callbacks imports OK (CallbackHandler, ConsoleCallback)")
except Exception as e:
    print(f"✗ or_af.callbacks import error: {e}")

# Test 7: Exceptions module
try:
    from or_af.exceptions import (
        ORAFError, MCPServerError, WorkflowError, 
        ToolNotFoundError, AgentExecutionError
    )
    print("✓ or_af.exceptions imports OK (ORAFError, MCPServerError)")
except Exception as e:
    print(f"✗ or_af.exceptions import error: {e}")

# Test 8: Utils module
try:
    from or_af.utils import default_logger, LogLevel, get_logger
    print("✓ or_af.utils imports OK (default_logger, LogLevel)")
except Exception as e:
    print(f"✗ or_af.utils import error: {e}")

# Test 9: Main __init__ exports
try:
    from or_af import (
        Agent, Tool, MCPServer, MCPClient,
        WorkflowGraph, Sequential, Parallel, visualize_workflow,
        A2AProtocol, A2AMessage, AgentCard,
        CallbackHandler, ConsoleCallback
    )
    print("✓ or_af main exports OK")
except Exception as e:
    print(f"✗ or_af main exports error: {e}")

print()
print("=" * 60)
print("Testing MCP Server and Workflow Creation")
print("=" * 60)

# Test MCP Server creation
try:
    mcp = MCPServer(name="test_server")
    
    @mcp.tool()
    def add(x: int, y: int) -> int:
        """Add two numbers"""
        return x + y
    
    print(f"✓ MCPServer created: {mcp.name}")
    print(f"  Tools: {mcp.list_tools()}")
except Exception as e:
    print(f"✗ MCPServer creation error: {e}")

# Test Workflow creation
try:
    wf = WorkflowGraph(name="test_workflow")
    
    step1 = lambda x: f"processed: {x}"
    step2 = lambda x: f"finalized: {x}"
    
    n1 = wf.add_node(step1, name="step1", is_entry=True)
    n2 = wf.add_node(step2, name="step2", is_exit=True)
    wf.add_edge(n1, n2, condition=EdgeCondition.ON_SUCCESS)
    wf.compile()
    
    print(f"✓ WorkflowGraph created: {wf.name}")
    print(f"  Nodes: {len(wf.nodes)}, Edges: {len(wf.edges)}")
except Exception as e:
    print(f"✗ WorkflowGraph creation error: {e}")

# Test visualization
try:
    viz = wf.visualize(format="text", show_details=False)
    print("✓ Workflow visualization working")
    print("  Sample output:")
    for line in viz.split('\n')[:5]:
        print(f"    {line}")
except Exception as e:
    print(f"✗ Visualization error: {e}")

print()
print("=" * 60)
print("All tests completed!")
print("=" * 60)
