---
title: Obsidian
tags: [jarvis-x, tool, second-brain, knowledge-management]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
related: [[jarvis-x]], [[second-brain]], [[hermes-agent]], [[jarvis-x-hardware]], [[jarvis-x-model-priority]], [[ollama]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-25
---

# Obsidian

The GUI markdown editor and second-brain layer in [[jarvis-x]]'s memory stack. Paired with ChromaDB for vector search, and connected to [[hermes-agent]] via `brain-mcp`.

## Role in Jarvis X

- Persistent knowledge store (Book V of the master plan: "The Memory")
- Provides RAG over the vault via plugins
- Connected to [[the-council]] as "Second Brain" member
- MCP interface via `brain-mcp` exposes `hybrid_search_tool`, `read_note_tool`, `create_note_tool`

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

> **Note (2026-09-25):** the `llama3.2:3b` above comes from the master plan. On the current machine, the Chromebook ([[jarvis-x-hardware]]), the installed local models are the Qwen 2.5 family (`qwen2.5:7b`, `qwen2.5:3b`, `qwen2.5-coder:7b`, `qwen2.5-coder:3b`), and `llama3.2:3b` isn't among the models the 2026-09-24 handoff lists as present. `nomic-embed-text`, which the brain-mcp setup below pulls, is present (274MB, per the handoff). Under the 2026-09-25 ruling, the choice of local model follows [[jarvis-x-model-priority]] and [[ollama]]. The handoff doesn't mention Obsidian, so whether LLM Hub is set up on the Chromebook is unknown ([[jarvis-x-plan-vs-reality]]).
>
> **Suggestion (not in any source):** if LLM Hub is set up on the Chromebook, point `model` at an installed model such as `qwen2.5:3b` instead of pulling `llama3.2:3b`.

## brain-mcp setup

```bash
git clone https://github.com/irahulstomar/brain-mcp
cd brain-mcp && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
ollama pull nomic-embed-text
python brain_cli.py setup
```

## Relationship to the LLM wiki pattern

Obsidian is a GUI-first, plugin-heavy approach to the [[second-brain]] concept. The [[llm-wiki-pattern]] used in this vault takes the opposite direction: pure markdown, no app dependency, grep-navigable. They are complementary — Obsidian handles the GUI layer for [[jarvis-x]], the wiki pattern handles the LLM-native layer.
