# Workshop 02: Get Note Content - Resources vs Tools

We wil now try to create an MCP tool that can manage a few notes, use the content of these notes and edit a task board. In actually this is just one of the many examples one could take. 

## Objective
Learn how to create MCP resources for structured data access and understand the difference between MCP resources and tools. You'll build functionality to read note content from your notes directory.

## What You'll Learn
- How to create MCP resources using the `@mcp.resource` decorator
- Understanding MCP resource URIs and patterns
- Working with file system operations using utility functions
- The difference between MCP resources and tools
- Testing with MCP Inspector vs VS Code Chat limitations
- Converting resources to tools when needed

## Understanding MCP Resources vs Tools

**MCP Resources** are for structured data that can be referenced by URI:
- Represent data that can be "read" or "accessed"
- Have unique URIs (like `note://tasks.md`)
- Great for content that clients can browse or reference
- **Note**: VS Code Chat doesn't currently support MCP resources or prompts

**MCP Tools** are for actions and operations:
- Perform actions or computations
- Called with parameters, return results
- Fully supported in VS Code Chat and other MCP clients

## Step 1: Explore Available Utility Functions

Your `files_util.py` contains helpful functions for working with notes:

```python
def read_lines(path: str) -> List[str]:
    """Reads and returns all lines from a file"""

def normalize_rel_path(path: str) -> str:
    """Expands and normalizes a relative path within the notes directory"""
```
Make sure your environment is configured properly. Create or update `.env` file:

```env
NOTES_DIR_PATH=/home/fx/projects/ae/bench/MCP-workshop/FakeNotes
```

## Step 3: Create Your First MCP Resource

Add this resource to your `server.py` file after your hello_world function:

```python
@mcp.resource(
    uri="note://{path*}"
)
def get_note_content(path: str) -> str:
    pass
```

1. **`@mcp.resource()` decorator**: Marks this as an MCP resource
2. **URI pattern**: `"note://{path*}"` - the `{path*}` captures the path parameter

## Step 4: Test with MCP Inspector

Since VS Code Chat doesn't support resources yet, test using MCP Inspector:

1. Test your tool through the inspector: 
```bash
npx @modelcontextprotocol/inspector .venv/bin/python3 MCP_Server/server.py
```
   - Look for resources section in the inspector
   - Try accessing `note://tasks` or `note://tasks.md`
   - Verify you can see the content from your FakeNotes directory

## Step 5: Convert to a Tool for VS Code Chat Support

Since VS Code Chat doesn't support MCP resources, let's also create a tool version. Add this to your `server.py`:

```python
@mcp.tool()
def read_note(path: str) -> str:
    pass
```

## Step 6: Test Both Implementations

### Test the Tool (VS Code Chat or MCP Inspector):
Test the tool through your MCP client (like Claude Desktop or another MCP-compatible application):
- Try calling `read_note("tasks")`
- Try calling `read_note("tasks.md")`
- Try to prompt it to read the content of your note at tasks.md (which should implicitly call the tool)

When working correctly, all should return the content of your `tasks.md` file, which contains your workshop planning notes.

## Key Takeaways

### MCP Resources:
- Perfect for exposing structured content via URIs
- Great for browsing and referencing data
- Not yet supported in all MCP clients (like VS Code Chat)
- Use URI patterns to capture parameters

### MCP Tools:
- Better for actions and computations
- Widely supported across MCP clients
- Can do everything resources can do, just with function calls

### Best Practices:
- Use utility functions for common operations
- Always handle errors gracefully
- Provide clear documentation in docstrings
- Consider creating both resource and tool versions for maximum compatibility

## Next Steps

In the next workshop, you'll learn how to:
- Create tools that modify content (not just read)
- Handle more complex data structures
- Work with prompts and user interaction

Ready to continue? Head to `03-add-new-task.md`!