# Self-Assessment Answers: 02 - Get Note Content

### 1. What is the key difference between an MCP resource and an MCP tool?

A **resource** represents data that can be read/accessed via a URI (like `note://tasks.md`), designed for browsing and referencing structured content. A **tool** performs an action or computation when called with parameters. Resources are nouns, tools are verbs.

### 2. When would you choose to expose functionality as a resource rather than a tool?

When the data is naturally addressable by a URI and the client may want to browse or list available items — e.g., files, database records, or configuration entries. Resources make the data discoverable without requiring the client to know specific function signatures.

### 3. Why might you need to provide both a resource and a tool for the same data?

Not all MCP clients support resources. VS Code Chat, for example, currently only supports tools. Providing both ensures maximum compatibility: the resource for clients that support browsing, and a tool fallback for those that don't.

### 4. What does the `{path*}` syntax in a resource URI pattern do?

It's a wildcard capture that matches the remainder of the URI path, including slashes. This allows a single resource definition to handle any nested path, e.g., `note://recipes/pancakes.md`.

### 5. Why is it important to handle errors gracefully in MCP tools that access the file system?

File system operations can fail for many reasons (missing files, permission errors, encoding issues). Without graceful error handling, the MCP client receives an opaque protocol error instead of a useful message the LLM can relay to the user.
