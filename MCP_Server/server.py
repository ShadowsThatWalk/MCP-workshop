from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession
from mcp.types import ElicitRequestURLParams, DirectoryResource
from mcp.server.fastmcp.resources.types import DirectoryResource

from typing import Optional

import files_util as fu

# Create an MCP server
mcp = FastMCP("notes-tools")
mcp.run(transport="stdio")

#--------------- task 01 ----------------
@mcp.tool(
    description="A simple tool that says hello.",
    tags=["greeting"]
)
def hello_world(name: str = "World") -> str:
    return f"Hello, {name}!"

#--------------- task 02 ----------------
@mcp.resource(
    uri="note://{path*}",
    description="Fetch the content of a note given its path.",
    tags=["notes"]
)
def get_note_content(path: str) -> str:
    """Fetch the content of a note given its path."""
    normalized_path = fu.normalize_rel_path(path)
    return fu.read_lines(normalized_path)

#--------------- task 03 ----------------
@mcp.tool(
    description="Add a task to the backlog.",
    tags=["tasks"]
)
async def add_task(ctx: Context[ServerSession, None], title: str | None = None, subtasks: list[str] = []) -> str:
    new_title = title
    if title is None:
        new_title = await ctx.elicit(
            ElicitRequestURLParams(
                tool_name="add_task",
                param_name="title",
                description="The title of the task to add.",
            )
        )

    tasks_file_path = fu.normalize_rel_path(fu.load_config().get("tasks_file_path", "tasks.md"))

    text_lines = fu.format_task_lines(new_title, subtasks)

    header = fu.extract_header(tasks_file_path, "Backlog")

    if header is None:
        fu.append_lines(tasks_file_path, ["# Backlog\n"] + text_lines)
    else:
        fu.insert_lines_at(tasks_file_path, header.line_number + 1, text_lines)

    # Here you would add the task to your task manager, e.g. by calling an API or updating a database
    # For demonstration purposes, we'll just return a success message
    return f"Task '{new_title}' added successfully with {len(subtasks)} subtasks."

#--------------- task 04 ----------------
@mcp.prompt(
    description="Create tasks from a conversation.",
    tags=["tasks", "conversation"],
)
def create_tasks_from_conversation() -> str:
    return """Given the following conversation, extract any tasks mentioned and add them to the backlog. 
    If a task has subtasks, add them as well. 
    Conversation:
    ---
    User: I need to prepare for the meeting tomorrow.
    Assistant: What do you need to prepare?
    User: I need to create a presentation and review the project report.
    ---
    In this example, you would create a task "Prepare for the meeting tomorrow" with two subtasks: "Create a presentation" and "Review the project report". 
    Please extract the tasks and subtasks from the conversation and add them to the backlog using the add_task tool."""