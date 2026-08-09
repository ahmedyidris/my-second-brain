---
title: Obsidian
tags: [jarvis-x, tool, second-brain, knowledge-management]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[second-brain]], [[hermes-agent]], [[jarvis-x-hardware]], [[brain-mcp]]
last_updated: 2026-07-27
---

# Obsidian

The GUI markdown editor and second-brain layer in [[jarvis-x]]'s memory stack. Paired with ChromaDB for vector search, and connected to [[hermes-agent]] via `brain-mcp`.

## Role in Jarvis X

- Persistent knowledge store (Book V of the master plan: "The Memory")
- Provides RAG over the vault via plugins
- Connected to [[the-council]] as "Second Brain" member
- MCP interface via [[brain-mcp]] — 9 tools including `hybrid_search_tool`, `read_note_tool`, `create_note_tool` (full list on that page)

## Key plugins

| Plugin | Purpose |
|--------|---------|
| LLM Hub | Multi-provider AI chat, RAG, automation |
| Superpower Inside | GraphRAG, MCP tools, desktop AI copilot |
| Local LLM Helper | Works with any OpenAI-compatible LLM server |
| QVAC | Fully local vault chat with semantic search |

## LLM Hub config (Ollama)

```json
{
  "provider": "ollama",
  "baseUrl": "http://localhost:11434",
  "model": "llama3.2:3b"
}
```

## brain-mcp

See [[brain-mcp]] for the full tool list, technical stack (Chroma + Ollama embeddings + SQLite FTS5), and setup steps.

## Relationship to the LLM wiki pattern

Obsidian is a GUI-first, plugin-heavy approach to the [[second-brain]] concept. The [[llm-wiki-pattern]] used in this vault takes the opposite direction: pure markdown, no app dependency, grep-navigable. They are complementary — Obsidian handles the GUI layer for [[jarvis-x]], the wiki pattern handles the LLM-native layer.
