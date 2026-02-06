# Exercise 0: Register your MCP Server for agents to use

## Overview

Make your MCP server available for all agents to use

## Instructions

### 0. Install all needed packages
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
cd MCP_Server
```

### 1. Make an MCP server

Declare a new MCP server instance
```python
mcp = FastMCP("your mcp server name here")
```

Start this server
```python
mcp.run(transport="stdio")
```

### 2. Check with the inspector

```bash
npm install -D @modelcontextprotocol/inspector
npx @modelcontextprotocol/inspector python3 server.py
```
This will start the server and open an inspector in your browser to connect to your server. From there, you can check that it can connect and all the currently registered tools, prompts and resources (which are currently non-existant). Use the "ping" tab to double check that your MCP server is responsive.

### 3. Register your MCP server

**VSCode**
Ctrl+shift+P > MCP:Add Server

**Cursor**
Cursor settings > MCP > Add new global MCP Server

#### Manually
**VSCode**
Open the mcp.json file directly;
 - MCP server for agetns in a specific repo: open `./.vscode/mcp.json` 
 - MCP server usable by all agents in all repos:
    - macOS: `~/.vscode/mcp.json`
    - Windows: `%APPDATA%\Code\User\mcp.json`
    - Linux: `~/.vscode-server/data/User/mcp.json`

**Cursor**
Open the mcp.json file directly;
 - MCP server for agetns in a specific repo: open `./.vscode/mcp.json` 
 - MCP server usable by all agents in all repos:
    - macOS: `~/.cursor/mcp.json`
    - Windows: `%APPDATA%\Cursor\mcp.json`
    - Linux: `~/.config/cursor/mcp.json`

Then add a new mcp server definition in the json
```json
{
    "servers": {
        "my-python-mcp": {
            "command": "../.venv/bin/python",
            "args": ["index.py"],
            "cwd": "somepath/tomcp/server"
        }
    }
}
```

