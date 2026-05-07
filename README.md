# MCP Workshop

A hands-on workshop for developers to learn how to build **Model Context Protocol (MCP)** servers. You'll build a working MCP server step by step, adding tools, resources, and prompts that integrate with VS Code's GitHub Copilot agent.

## What You'll Build

A note-management MCP server that can read notes, manage tasks, and find relevant content — all accessible from within VS Code Chat.

## Prerequisites

- VS Code with GitHub Copilot (agent mode) or similar
- Python 3.10+

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Workshop Steps

| Step | Topic |
|------|-------|
| [00 – Register your server](Workshop/00-register-server.md) | Configure your MCP server so VS Code agents can discover and use it |
| [01 – Hello World](Workshop/01-hello-world.md) | Create your first MCP tool with the `@mcp.tool` decorator |
| [02 – Get Note Content](Workshop/02-get-note-content.md) | Expose notes as MCP resources and learn the difference between resources and tools |
| [03 – Add New Task](Workshop/03-add-new-task.md) | Build an interactive tool that modifies content and uses `ctx.elicit()` |
| [04 – Tasks from Conversation](Workshop/04-tasks-from-conversation.md) | Create MCP prompt templates that extract tasks from a conversation |
| [05 – Find Relevant Notes](Workshop/05-find-relevant-note.md) | Combine resources, prompts, and tools into an intelligent note discovery system |

## Project Structure

```
MCP_Server/       # Your MCP server code
FakeNotes/        # Sample notes used during the workshop
Workshop/         # Step-by-step exercise guides
requirements.txt  # Python dependencies
```
