# Self-Assessment Answers: 01 - Hello World

### 1. What does the `@mcp.tool()` decorator do to a regular Python function?

It registers the function as an MCP tool, making it discoverable and callable by MCP clients. FastMCP handles all the protocol details (JSON-RPC, schema generation, etc.) automatically.

### 2. Why are type hints and docstrings important for MCP tools?

MCP uses type hints to generate the tool's input/output schema, which clients use to validate calls and present parameters. Docstrings become the tool's description, which LLMs use to decide **when** and **how** to invoke the tool.

### 3. How do default parameter values affect tool usability?

They make parameters optional, so the tool can be called with fewer arguments. This lets an LLM invoke the tool even when the user doesn't provide every detail, improving the conversational experience.

### 4. What protocol details does FastMCP handle for you behind the scenes?

FastMCP handles JSON-RPC message framing, tool schema generation from type hints, parameter validation and deserialization, transport setup (stdio, SSE, etc.), and the MCP handshake/capability negotiation.
