# Self-Assessment Answers: 05 - Find Relevant Notes

### 1. How can MCP resources provide context that improves an LLM's decision-making?

By exposing structured data (like a directory listing) as a resource, the LLM can inspect the available information before deciding which tools to call. This turns a blind tool call into an informed one — e.g., scanning file names to pick relevant notes instead of guessing paths.

### 2. What are the trade-offs between AI-driven file selection (via prompts) and programmatic file selection (via tools)?

AI-driven selection is flexible and handles fuzzy/semantic queries well but is non-deterministic and slower. Programmatic selection is fast, reproducible, and testable but requires explicit matching logic (keywords, regex, tags) that can miss semantic relevance.

### 3. Why should complex MCP workflows be broken into individually testable components?

Each component (resource, prompt, tool) can fail independently. Testing in isolation makes failures easy to diagnose. It also lets you verify each step's output before composing the full workflow, preventing cascading errors.

### 4. What security considerations apply when exposing file system access through MCP resources?

You must prevent path traversal attacks (e.g., `../../etc/passwd`) by normalizing paths and verifying they stay within the allowed directory. Only expose intended file types, and avoid leaking sensitive file metadata or system paths in responses.

### 5. How do you design an MCP system for extensibility when requirements will evolve?

Keep components loosely coupled: resources expose data, prompts define strategies, tools execute actions. Use clear URI patterns and consistent naming. This lets you add new resources or swap prompt strategies without rewriting the entire system.
