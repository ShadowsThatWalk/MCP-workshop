## Notes
### Intro meeting
praktisch hands-on MCP server bouwen met skills / resulsable prompts 
Goeie prompts schrijven

focus op techies => voorbeelden naar devs

- guardrails
- skills
### AI Agents
### Planning
- **Pitstop 0 (10–15m):** Context & why
	- What are knowledge documents
	- What are skills (reusable, filesystem-based modular capability)
	- What MCP is (host/client/server, tools/resources/prompts)
- **Pitstop 1 (45–60m): Build an MCP server**
	- Minimal server exposing 1–2 tools + one prompt template
	- Test locally with MCP Inspector
- **Pitstop 2 (30–45m): Put it in an agent**
	- Install server in Claude Desktop / Copilot agent mode (depending on audience)
	- Demonstrate the “agent” can now reliably call the tool
- **Pitstop 3 (30–60m): Turn it into a Skill**
	- Package instructions/templates/resources as an Agent Skill (Copilot/Claude)
	- Teach “when to use the MCP tool vs when to follow a checklist”
#### Context
- knowledge doc
  If it answers “**how does this system work?**”
- playbook
  If it answers “**what steps do I take?**”
- Skill
  If it answers “**how should the agent behave and what steps/templates should it apply?**”

they’re packaged and written for agent consumption (tight scope, triggers, examples, and crisp criteria). The difference in how they are treated internally is how the host treats them in the agent stack; retrieved reference vs instructional skill layer.

- Knowledge docs / playbook
  RAG searched for relevant chunks and sets that as additional context
- Skills
  loaded with a trigger and a list of instructions to follow. They are loaded with the trigger is relevant and placed higher in priority instructional skill layer (system-level). The skill is written as text but loaded as a checklist to be seen as repeatable instructions.

Local vs personal skill (`./.github/skills` vs `~/.github/skills`)
### Skills
Define a skill in 3 layers:
1 - metadata (always loaded)
```
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```
> contain description and "when to trigger"

2 - instructions (loaded when triggered)
```
# PDF Processing

## Quick start

Use pdfplumber to extract text from PDFs:

python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()

For advanced form filling, see [FORMS.md](FORMS.md).
```
> instructions in the form of text
#### Making your own MCP
- downloading tools
- making your own server tools
##### Lazy loading
lazy loading + search of tools
documentation for knowledge of tools (for itself and to explain the capabilities to the user)
```
{
	"name": "my-awesome-server",
	"command": "node",
	"args": ["server.js"],
	"instructions": "documentation"
}
```

## Steps
### Theory
See [[MCP Servers]]
### Practical