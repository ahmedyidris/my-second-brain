---
title: Ruflo
tags: [agent-architecture, self-optimizing, cli, mcp]
sources:
  - raw/2026-07-27-ruflo-architecture.md
  - raw/2026-07-27-ruflo-install.md
related: [[jarvis-x]], [[the-council]], [[self-improvement-loop]], [[universal-model-layer]], [[hermes-agent]]
last_updated: 2026-07-27
---

# Ruflo

A self-learning, self-optimizing agent architecture. Entry point is a CLI/MCP interface; the system routes requests through a swarm of agents, persists results to memory, and feeds outcomes back into a learning loop that improves routing over time.

## Architecture

```
User --> Ruflo (CLI/MCP) --> Router --> Swarm --> Agents --> Memory --> LLM Providers
                          ^                           |
                          +---- Learning Loop <-------+
```

## Components

| Component | Role |
|-----------|------|
| **Ruflo (CLI/MCP)** | User-facing entry point; accepts commands, exposes MCP tools |
| **Router** | Directs each request to the right swarm or agent; learns from feedback |
| **Swarm** | Orchestrates parallel agents working on a task |
| **Agents** | Workers that execute tasks, call tools, produce outputs |
| **Memory** | Persistent storage agents read/write across sessions |
| **LLM Providers** | Model backends (local or cloud) |
| **Learning Loop** | Feedback path: agent outputs + memory → router improvement |

## The key innovation: the learning loop

The learning loop is what distinguishes Ruflo from a static multi-agent system. Agent outputs and memory state feed back to the router, allowing it to self-optimize — better routing, better swarm composition, better tool selection — without manual reconfiguration.

## Plugin system

Ruflo is plugin-based. Marketplace hosted at `ruvnet/ruflo`.

```
/plugin marketplace add ruvnet/ruflo
```

### Core plugins

| Plugin | Function |
|--------|----------|
| `ruflo-core@ruflo` | Core agent runtime — install first |
| `ruflo-swarm@ruflo` | Swarm orchestration layer |
| `ruflo-rag-memory@ruflo` | RAG-backed persistent memory |
| `ruflo-neural-trader@ruflo` | Trading/market intelligence module |

```
/plugin install ruflo-core@ruflo
/plugin install ruflo-swarm@ruflo
/plugin install ruflo-rag-memory@ruflo
/plugin install ruflo-neural-trader@ruflo
```

Note: `ruflo-neural-trader` is the trading module — maps directly to [[jarvis-x-trading-module]] in intent.
`ruflo-rag-memory` is the memory layer — maps to [[obsidian]] + ChromaDB in Jarvis X.

## Relationship to Jarvis X

Ruflo and [[jarvis-x]] share the same design instincts but at different layers:

| Dimension | Ruflo | Jarvis X |
|-----------|-------|---------|
| Entry point | CLI/MCP | CLI + voice + web UI |
| Orchestration | Router + Swarm | [[the-council]] |
| Self-improvement | Learning Loop | [[self-improvement-loop]] |
| Memory | Memory layer | Obsidian + ChromaDB |
| Model abstraction | LLM Providers | [[universal-model-layer]] |

Ruflo could serve as the orchestration backbone inside Jarvis X, with [[hermes-agent]] as the primary agent and [[universal-model-layer]] as the LLM Providers layer.
