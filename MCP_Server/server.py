from fastmcp import FastMCP, Context
from fastmcp.resources.types import DirectoryResource
from fastmcp.tools.tool import ToolResult
import json

import files_util as fu

# Create an MCP server
mcp = FastMCP("notes-tools")
mcp.run(transport="stdio")