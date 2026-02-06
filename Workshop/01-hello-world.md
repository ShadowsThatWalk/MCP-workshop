# Workshop 01: Hello World MCP Tool

## Objective
Create your first MCP (Model Context Protocol) tool - a simple "hello world" function that demonstrates the basic structure of an MCP tool.

## What You'll Learn
- How to create a basic MCP tool using the `@mcp.tool` decorator
- Proper function documentation for MCP tools
- How to handle basic parameters and return values
- Testing your MCP tool

## Prerequisites
- MCP server setup (completed in 00-register-server.md)

## Step 2: Create Your First MCP Tool

Add the following function to your `server.py` file. Place it after the server initialization:

```python
@mcp.tool()
def hello_world(name: str = "World") -> str:
    pass
```

### Key Components Explained:

1. **`@mcp.tool()` decorator**: This tells FastMCP that this function should be exposed as an MCP tool
2. **Type hints**: `name: str` and `-> str` help MCP understand the expected input/output types

## Step 3: Add the Complete Hello World Function

Make the tool return a custom greeting like `"hello world! welcome my MCP tool"`
Use the extra paramters in `@mcp.tool()` to optionally set the description, tags, etc. More info [here](https://fastmcp.wiki/en/servers/tools#decorator-arguments). This gives more context to the LLM to know when and how to use this tool. 

## Step 4: Test Your MCP Tool

1. Test your tool through the inspector: 
```bash
npm install -D @modelcontextprotocol/inspector
npx @modelcontextprotocol/inspector .venv/bin/python3 MCP_Server/server.py
```

2. Test the tool through your MCP client (like Claude Desktop or another MCP-compatible application):
   - Try calling `hello_world()` with no parameters
   - Try calling `hello_world(name="Alice")` with a specific name
   - Try to prompt it to greet the world (which should implicitly call the tool)

## Next Steps

Congratulations! You've created your first MCP tool. In the next workshop, you'll learn how to:
- Work with file operations
- Handle more complex data types
- Create tools that interact with external resources

## Key Takeaways

- MCP tools are regular Python functions with the `@mcp.tool()` decorator
- Type hints and docstrings are crucial for MCP tool discovery and usability
- Default parameters make tools more user-friendly
- FastMCP handles all the protocol details automatically