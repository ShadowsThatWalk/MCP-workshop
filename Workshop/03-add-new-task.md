# Workshop 03: Add New Task - Interactive MCP Tools

## Objective
Building on our note reading capabilities, we'll now create an interactive MCP tool that can add new tasks to your task board and handle user interaction when information is missing.

## What You'll Learn
- How to create async MCP tools that modify content
- Working with complex data types (lists) as parameters
- Using `ctx.elicit()` for interactive user input
- File manipulation and content formatting
- Error handling for file operations
- Default parameter handling with mutable types

## Step 1: Analyze Your Task File Structure

First, examine your `FakeNotes/tasks.md` file to understand the format you'll be working with. Notice:
- How tasks are structured (markdown format)
- How subtasks are nested
- The overall formatting pattern you need to maintain

## Step 2: Explore Available Utility Functions

Review your `files_util.py` for functions that might help with:
- Reading existing content: `read_lines(path)`
- Writing modified content back to files: `write_lines(path, content)`
- Inserting content at specific locations: `insert_lines_at(path, line_number, content)`
- Path normalization for safe file operations: `normalize_rel_path(path)`

Key functions you'll need:
```python
def read_lines(path: str) -> List[str]:
    """Reads and returns all lines from a file"""

def write_lines(path: str, content: List[str]) -> None:
    """Writes lines to a file"""
    
def insert_lines_at(path: str, line_number: int, content: List[str]) -> None:
    """Inserts lines at a specific line number in a file"""
```

## Step 3: Create the Basic Add Task Function

Start with a simple, non-interactive version. Add this function to your `server.py` file:

```python
@mcp.tool()
def add_task(title: str = "", subtasks: list[str] = []) -> str:
    pass
```

### Key Implementation Points:
- Use `fu.normalize_rel_path("tasks")` to get the correct file path
- Read existing content with `fu.read_lines(path)`
- Format tasks with `- [ ] ` prefix
- Format subtasks with tab indentation (`\t- [ ] subtask`)
- Add tasks under the "## Backlog" section
- Write changes back with `fu.write_lines(path, content)`
- Return a confirmation message

## Step 4: Test with MCP Inspector First

1. **Open MCP Inspector** and connect to your server
2. **Test the basic functionality**:
   - `add_task("Test task from inspector")`
   - `add_task("Task with subtasks", ["Subtask 1", "Subtask 2"])`
3. **Verify the results** in your `tasks.md` file

Make sure your basic implementation works before proceeding!

## Step 5: Test with VS Code Chat

1. **Ensure your MCP server is registered** with VS Code Chat
2. **Test the same functionality**:
   - Ask: "Add a task called 'Test task from agent'"
   - Ask: "Add a task 'Task with subtasks' that has subtasks 'Setup' and 'Testing'"
3. **Verify it works** the same way as in the inspector

Once basic functionality is confirmed working, proceed to add interactivity.

## Step 6: Add Interactive Title Collection

Now enhance your function to handle missing titles. Update your function signature:

```python
@mcp.tool()
async def add_task(ctx: Context[ServerSession, None], title: str | None = None, subtasks: list[str]) -> str:
    pass
```

We will now use `answer = ctx.elicit("some question to the user")` to gather more missing information from a user. In case a user says something like "add a new task", the function will automatically ask what the title of that task should be (instead of making something up, giving an empty string or worse giving an error).

### Key Changes:
1. **`async def`**: Function is now async
2. **`ctx: Context`**: Added context parameter for elicit functionality
3. **Interactive prompting**: Use `ctx.elicit()` when title is missing

## Step 7: Test Interactive Feature with Agent

1. **Save your updated function** and restart your MCP server
2. **Test the interactive feature** in VS Code Chat:
   - Ask: "Add a new task" (without specifying what)
   - The agent should prompt you for the task title
3. **Verify the interaction**:
   - After providing the title, the task should be added; Check your `tasks.md` file to confirm

## Key Takeaways

### Interactive MCP Tools:
- Use `async def` for functions that need `ctx.elicit()`
- `ctx.elicit()` allows gathering missing information from users
- Always await async operations properly

### File Operations:
- Use utility functions for consistent file handling
- Always handle potential file operation errors
- Maintain existing file formatting and structure

### Best Practices:
- Avoid mutable default arguments
- Provide clear user prompts with `ctx.elicit()`
- Return meaningful confirmation messages
- Validate input parameters before processing

## Next Steps

In the next workshop, you'll learn how to:
- Create more complex data manipulation tools
- Handle batch operations on multiple tasks
- Implement task completion and removal functionality

Ready to continue? Head to `04-task-management.md`!