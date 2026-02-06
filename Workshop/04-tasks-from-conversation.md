# Workshop 04: Tasks from Conversation - MCP Prompts and Tool Integration

## Objective
Learn how to create MCP prompt templates that can analyze conversations and generate actionable tasks. You'll build functionality that extracts tasks from discussion context and automatically creates them using your existing `add_task` tool.

## What You'll Learn
- How to create MCP prompts using the `@mcp.prompt()` decorator
- Understanding MCP prompt templates and variable substitution
- Combining multiple MCP tools through prompt orchestration
- Converting prompts to tools for VS Code Chat compatibility
- Working with optional parameters and conditional logic

## Step 1: Understanding MCP Prompts vs Tools

**MCP Prompts** are templates for AI instructions:
- Provide structured instructions to AI systems
- Use variable substitution with `{variable}` syntax
- Great for complex, multi-step AI workflows
- **Note**: VS Code Chat doesn't currently support MCP prompts

**MCP Tools** are for direct actions:
- Execute specific functions with parameters
- Can call other tools programmatically
- Fully supported in VS Code Chat

## Step 2: Analyze the Task Creation Workflow

Your prompt needs to:
1. **Analyze the conversation** for actionable items
2. **Extract tasks** that need to be implemented
3. **Decide on structure** - individual tasks vs grouped under main task
4. **Use the `add_task` tool** to actually create the tasks

## Step 3: Create the Basic MCP Prompt

Add this prompt to your `server.py` file:

```python
@mcp.prompt()
def create_tasks_from_conversation() -> str:
    pass
```
References your existing `add_task` MCP tool in your prompt for ease of use. The resulting string will be a new set of instructions / prompt the AI has to follow to create tasks from the current discussion context. Potentially integrate the use of subtasks as well in your prompt for better results. 

## Step 4: Test with MCP Inspector First

Since VS Code Chat doesn't support prompts, test with MCP Inspector:

1. **Save your changes** and start your MCP server
2. **Open MCP Inspector** and connect to your server
3. **Look for the prompts section** in the inspector interface
4. **Test the prompt**:
   - Try `create_tasks_from_conversation()`
5. **Observe the generated instructions** - they should be different based on the title parameter

## Step 5: Convert to Tool for VS Code Chat Support

Since VS Code Chat doesn't support MCP prompts, create a tool version. Add this to your `server.py`:

```python
@mcp.tool()
async def create_tasks_from_conversation() -> str:
    pass
```
Specify in the description of this tool that the return value are the instructions to follow to analyze a conversation and will not just do it.

## Step 6: Test with VS Code Chat

1. **Save your changes** and restart your MCP server
2. **Provide context** by having a discussion in VS Code Chat about a project, such as:
    - \"I need to build a blog website\"
    - \"It should have user authentication\"
    - \"I want to add a comment system\"
    - \"Need to deploy it to production\"
2. **Test both approaches** in VS Code Chat:
    - Ask: \"Analyze our conversation for tasks\" (should create individual tasks)
3. **Observe the behavior** - the AI should automatically identify actionable items and use your `add_task` tool

## Key Takeaways

### MCP Prompts:
- Use `@mcp.prompt()` for AI instruction templates
- Support variable substitution and conditional logic
- Great for complex, multi-step AI workflows
- Test with MCP Inspector since VS Code Chat doesn't support them

### Tool Integration:
- MCP tools can orchestrate other MCP tools
- Prompts can reference and instruct use of other tools
- Converting prompts to tools enables VS Code Chat compatibility

### Best Practices:
- Provide clear, specific instructions in prompts
- Handle both individual and grouped task scenarios
- Test thoroughly with realistic conversation examples
- Always validate that referenced tools work independently

## Next Steps

In the next workshop, you'll learn how to:
- Create more sophisticated task management tools
- Handle task completion and status updates
- Build task search and filtering capabilities

Ready to continue? Head to `05-advanced-task-management.md`!