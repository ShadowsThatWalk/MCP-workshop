# Workshop 05: Find Relevant Notes - Advanced MCP Integration

## Objective
Bring together all MCP concepts learned so far to create an intelligent note discovery system. You'll build functionality that can analyze your entire notes directory structure, intelligently select relevant files, and retrieve their content based on user queries.

## What You'll Learn
- Creating MCP resources for directory structure exposure
- Building complex MCP prompts that orchestrate multiple tools
- Integrating resources, prompts, and tools in a cohesive workflow
- Advanced prompt engineering for content relevance determination
- Converting complex prompt workflows to tools for universal compatibility

## The Intelligent Note Discovery Workflow

Your system will follow this 3-step process:
1. **Get directory structure** - List all files and folders in your notes directory
2. **Intelligent file selection** - Let the LLM analyze the structure and choose most relevant files
3. **Content retrieval** - Get and return the content of the selected files

## Use Cases
This powerful combination enables queries like:
- "Give a summary of all notes that discuss content related to AI"
- "Find notes about project planning and management"
- "Show me anything related to workshop preparation"
- "What notes do I have about database design?"

## Step 1: Create a Directory Structure Resource

You'll need to create an MCP resource that exposes your notes directory structure. Consider:
- **Resource Pattern**: Design a URI pattern that represents your notes directory
- **Directory Traversal**: How to safely walk through your notes directory
- **Path Normalization**: Use your existing `load_config()` to get the base path
- **Security**: Ensure the resource only exposes files within your notes directory

### Implementation Tips:
- Use `os.walk()` or `os.listdir()` to traverse directories
- Filter for relevant file types (`.md`, `.markdown`)
- Return a structured representation (consider JSON format)
- Handle nested folder structures appropriately
- Include relative paths for easy reference

## Step 2: Design the Orchestration Prompt

Create an MCP prompt that coordinates the entire workflow:

**Prompt Purpose**: Analyze directory structure and retrieve relevant content

**Workflow Instructions**: Your prompt needs to guide the AI through:
1. Access the directory structure resource
2. Analyze filenames and folder structure for relevance
3. Select the most promising files (suggest 2-5 files max)
4. Use your existing `read_note` tool to get content
5. Present findings in a structured way

### Prompt Design Considerations:
- How specific should the file selection criteria be?
- Should you prioritize recent files or file names that match?
- How to handle when no relevant files are found?
- What format should the final output take?

## Step 3: Test with MCP Inspector First

Since VS Code Chat doesn't support prompts or resources:

1. **Test the directory resource separately** - Verify it returns proper structure
2. **Test the prompt in isolation** - Check the generated instructions
3. **Test the full workflow manually** - Follow the prompt instructions step by step
4. **Debug any issues** before proceeding to tool conversion

### Verification Steps:
- Does the directory resource show all your notes?
- Are the prompt instructions clear and actionable?
- Can you manually follow the workflow successfully?

## Step 4: Convert to Tool for VS Code Chat

Create a tool that implements the entire workflow programmatically:

**Tool Design**: How should your tool function work?
- Accept a query string parameter
- Programmatically get directory structure
- Implement logic to select relevant files
- Call your `read_note` tool for each selected file
- Return formatted results

### Implementation Challenges:
- How to replicate the AI's file selection logic in code?
- Should you use keyword matching, fuzzy search, or other algorithms?
- How to handle multiple file results efficiently?
- What's the best way to present multiple file contents?

## Step 5: Test with VS Code Chat

1. **Test various query types**:
   - Specific topics: "Find notes about database design"
   - General themes: "Show me project-related notes"
   - Technical terms: "Notes discussing API development"
   
2. **Verify the complete workflow**:
   - Directory structure is accessed correctly
   - File selection makes sense
   - Content is retrieved and presented well
   
3. **Test edge cases**:
   - Queries that match no files
   - Very broad queries that match many files
   - Typos in search terms

## Key Takeaways

### Advanced MCP Patterns:
- Resources can provide context for intelligent decision making
- Prompts can orchestrate complex multi-tool workflows
- Tools can implement the same logic for broader compatibility

### System Design:
- Break complex workflows into testable components
- Consider both AI-driven and programmatic approaches
- Design for both specific and general use cases

### Best Practices:
- Always test components individually before integration
- Consider performance implications of file system operations
- Provide clear feedback when no relevant content is found
- Design for extensibility and future enhancements

## Next Steps

You've now built a complete intelligent note discovery system that demonstrates advanced MCP integration. Consider how these patterns could apply to:
- Database query systems
- API documentation searches
- Code repository analysis
- Knowledge base management