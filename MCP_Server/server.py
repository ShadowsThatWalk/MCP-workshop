from fastmcp import FastMCP, Context
from fastmcp.resources.types import DirectoryResource
from fastmcp.tools.tool import ToolResult
import json

import files_util as fu

# Create an MCP server
mcp = FastMCP("notes-toolss")

# --------------- task 01 ----------------
@mcp.tool(
    description="A simple tool that says hello.",
    tags={"example"}
)
def hello_world(name: str = "World") -> str:
    return f"Hello, {name}!"

#--------------- task 02 ----------------
@mcp.resource(
    uri="note://{path*}",
    description="Fetch the content of a note given its path.",
    tags={"notes"}
)
def get_note_content(path: str) -> str:
    """Fetch the content of a note given its path."""
    normalized_path = fu.normalize_rel_path(path)
    return fu.read_lines(normalized_path)

#--------------- task 03 ----------------
@mcp.tool(
    description="Add a task to the backlog.",
    tags={"tasks"}
)
async def add_task(ctx: Context, title: str | None = None, subtasks: list[str] = []) -> str:
    new_title = title
    if title is None:
        new_title = await ctx.elicit(
            message="What is the title of the task you want to add?",
            response_type="string"
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
    tags={"tasks", "conversation"},
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

#--------------- task 05 ----------------
def get_paths_resource() -> DirectoryResource:
    notes_directory = fu.load_config().get("notes_dir_path", "./FakeNotes/")
    return DirectoryResource(
        uri="resource://all-note-paths",
        path=notes_directory, # Path to the directory
        recursive=True, # Set to True to list subdirectories
        pattern="*.md"
    )
mcp.add_resource(get_paths_resource())

@mcp.prompt(
    description="List all notes in a directory.",
    tags={"notes"}
)
async def find_relevant_notes(ctx: Context, query: str):
    directory_paths = await ctx.read_resource("resource://all-note-paths")
    paths = json.loads(directory_paths[0].content)["files"]
    contextfull_paths = []

    for i, path in enumerate(paths):
        await ctx.report_progress(i, len(paths), f"Checking properties at: {path}")
        contextfull_paths.append({"path": path, "tags": fu.get_note_property(fu.normalize_rel_path(path), "tags")})

    return f"""Find the relevant notes for the given query:
    1. Given the query '{query}', find the relevant notes for the following note paths :\n - {"\n - ".join([f"{cp['path']} (tags: {cp['tags']})" for cp in contextfull_paths])}
    2. Use tool get_note_content to read the content of the relevant notes and find the most relevant information for the query.
    3. Return the relevant information from the notes that can help answer the query."""

mcp.run(transport="stdio")