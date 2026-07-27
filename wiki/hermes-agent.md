---
title: Hermes Agent
tags: [jarvis-x, component, agent, local-ai]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[the-council]], [[self-improvement-loop]]
last_updated: 2026-07-27
---

# Hermes Agent

The core reasoning brain of [[jarvis-x]]. A self-improving local agent with 70+ default skills and cross-session memory. Runs entirely on local hardware via Ollama.

## Key features

- Writes its own new skills automatically (automatic skill creation)
- Cross-session conversation memory
- 70+ default tools: file edit, command run, web browse
- Structured JSON function/tool calling
- Local-first: no cloud dependency

## Models

| Model | Use case | Speed on CPU |
|-------|----------|-------------|
| llama3.2:3b | Primary (CPU) | 8–12 t/s |
| qwen3:1.5b | Fast alternative | 15–20 t/s |
| hermes3:8b | Future (GPU/16GB RAM) | 1–3 t/s |

## Installation

```bash
ollama launch hermes
# or
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

## Role in the system

Part of [[the-council]] as "Core Agent Brain". Powers the [[self-improvement-loop]] — analyzes its own daily logs, generates improved prompts and new tools, auto-implements with safety checks.
