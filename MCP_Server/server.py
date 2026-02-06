from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession
from mcp.shared.exceptions import UrlElicitationRequiredError
from mcp.types import ElicitRequestURLParams

from typing import Optional

import files_util as fu

# Create an MCP server
mcp = FastMCP("notes-tools")
mcp.run(transport="stdio")