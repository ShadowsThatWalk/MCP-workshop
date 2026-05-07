# Self-Assessment Answers: 03 - Add New Task

### 1. When does an MCP tool need to be `async`, and what triggers this requirement?

An MCP tool must be `async` when it uses `await` — most commonly when calling `ctx.elicit()` for interactive user input. Any I/O-bound operation that benefits from non-blocking execution also warrants `async`.

### 2. What does `ctx.elicit()` do and when should you use it?

`ctx.elicit()` sends an interactive prompt back to the user through the MCP client, requesting additional information. Use it when a required parameter is missing or ambiguous, rather than guessing, erroring out, or using an empty default.

### 3. Why are mutable default arguments (like `[]`) dangerous in Python, and how should you handle them in MCP tools?

Python evaluates default arguments once at function definition time, so all calls share the same list instance — mutations persist across calls. Use `None` as the default and create a new list inside the function body: `if subtasks is None: subtasks = []`.

### 4. Why is it important to return meaningful confirmation messages from tools that modify data?

The LLM uses the return value to inform the user about what happened. A clear confirmation (e.g., "Added task 'Deploy app' with 3 subtasks to Backlog") lets the user verify the action without manually checking the file.

### 5. Why should you validate input parameters before performing file operations?

Validating early prevents partial writes and corrupted files. It also produces clear, actionable error messages instead of cryptic file-system errors deep in the call stack.
