# Why the LLM Wiki Pattern Exists

## Why this exists

Most people's AI workflow: paste context into a chat, get an answer, start a new chat, paste everything again. Knowledge evaporates between sessions. Nothing compounds.

The wiki pattern is different. The LLM reads every source once, extracts the knowledge, and writes it into an interlinked set of markdown files — a persistent wiki that sits between you and your raw sources. When you ask a question, it reads the wiki (not the sources). When you add a source, it integrates, flags contradictions, and strengthens the synthesis. Knowledge is compiled once and kept current.

No vector database. No embeddings. No chunking pipeline. The folder is the app.

## How it works

A three-layer mental model:

1. **The map** — CLAUDE.md at the vault root. The AI reads this first, every time. It contains the folder structure, the routing table ("for task X, read these files"), naming conventions, workflows, and guardrails. Think of it as the floor plan posted at the entrance of a building.

2. **The rooms** — raw/ (immutable sources, read-only) and wiki/ (LLM-owned markdown). The map tells the AI which room to enter for which task. Each room has its own rules.

3. **The workspace** — the actual markdown files inside each room. Pages linked by [[wikilinks]], cataloged in wiki/index.md, timelined in wiki/log.md.

Three operations: ingest (read source → write into wiki), query (answer questions from the wiki), lint (find and fill gaps). The llm-wiki-setup skill installs the whole structure. The wiki-self-heal skill runs the lint loop on demand or on a schedule.
