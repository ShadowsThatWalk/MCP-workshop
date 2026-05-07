# Self-Assessment Answers: 04 - Tasks from Conversation

### 1. What is the difference between an MCP prompt and an MCP tool?

A **prompt** is a template that generates instructions for an AI to follow — it produces text that guides the LLM's behavior. A **tool** is a function the LLM can call to perform a concrete action. Prompts shape AI reasoning; tools execute operations.

### 2. Why would you convert an MCP prompt into a tool?

Because not all clients support prompts. VS Code Chat, for example, only supports tools. Wrapping the prompt logic in a tool makes the functionality universally accessible while preserving the orchestration behavior.

### 3. How can an MCP prompt reference and orchestrate other MCP tools?

The prompt's text can include explicit instructions telling the LLM to call specific tools by name (e.g., "Use the `add_task` tool to create each identified task"). The LLM then invokes those tools as part of following the prompt's instructions.

### 4. What are the advantages of using prompt templates with variable substitution over hardcoded prompts?

Variable substitution makes prompts reusable across different contexts. A single prompt template can handle different project types, conversation topics, or output formats without duplicating the orchestration logic.

### 5. Why is it important to test prompt-driven workflows with realistic conversation examples?

Prompts guide LLM behavior, which is inherently non-deterministic. Realistic test data reveals edge cases — like ambiguous wording, overlapping tasks, or conversations with no actionable items — that synthetic examples miss.
