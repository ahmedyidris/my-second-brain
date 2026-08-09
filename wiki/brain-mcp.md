---
title: brain-mcp
tags: [tool-connector, mcp, obsidian, second-brain, ollama]
sources:
  - https://github.com/irahulstomar/brain-mcp (accessed 2026-08-09)
  - https://glama.ai/mcp/servers/irahulstomar/brain-mcp (accessed 2026-08-09)
related: [[obsidian]], [[ollama]], [[jarvis-x]], [[second-brain]]
last_updated: 2026-08-09
---

# brain-mcp

A local, private MCP server that turns a folder of Markdown notes — built for Obsidian vaults but works on any Markdown folder — into a searchable knowledge base for any MCP-compatible AI client (Claude Code, Claude Desktop, Cursor, etc.). Nothing leaves the machine.

Repo: [`irahulstomar/brain-mcp`](https://github.com/irahulstomar/brain-mcp). License: MIT.

## Tools exposed

Nine MCP tools, more than the three ([[obsidian]] previously documented only `hybrid_search_tool`, `read_note_tool`, `create_note_tool`):

| Tool | Purpose |
|------|---------|
| `hybrid_search_tool` | Merges semantic + keyword results via Reciprocal Rank Fusion |
| `semantic_search_tool` | Vector similarity only |
| `keyword_search_tool` | FTS5 full-text search |
| `read_note_tool` | Read a note |
| `create_note_tool` | Create a note |
| `append_to_note_tool` | Append to an existing note |
| `list_recent_tool` | List recently modified files |
| `save_conversation_tool` | Archive a conversation to a designated folder |
| `ingest_file_tool` | Import an external document |
| `reindex_tool` | Refresh the index |

## Technical stack

- **Embedding model:** Ollama's `nomic-embed-text`, kept resident to avoid Ollama unloading it after idle time
- **Vector store:** Chroma with cosine HNSW indexing
- **Keyword index:** SQLite + FTS5 (Porter stemming, Unicode61)
- Index storage lives in `~/.brain/`, separate from the notes folder itself

## Setup

Quick path: clone the repo, open it in Claude Code, say "set up the brain" — the agent handles dependency install, Ollama verification, vault auto-detection, MCP registration, indexing, and verification.

Manual path:

```bash
git clone https://github.com/irahulstomar/brain-mcp
cd brain-mcp && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
ollama pull nomic-embed-text
python brain_cli.py setup
```

## Role in Jarvis X

Connects [[hermes-agent]] to [[obsidian]]'s vault as a searchable knowledge base — the "MCP interface" referenced in [[obsidian]]'s memory-layer role. Uses [[ollama]]'s local embedding model rather than a cloud embeddings API, keeping the second-brain layer consistent with Jarvis X's zero-cloud-keys, local-first constraint.
