---
title: PAL MCP
tags: [tool-connector, mcp, multi-model, council]
sources:
  - https://github.com/BeehiveInnovations/pal-mcp-server (accessed 2026-08-09)
  - https://github.com/BeehiveInnovations/pal-mcp-server/blob/main/README.md (accessed 2026-08-09)
related: [[the-council]], [[agent-secure-comms]], [[jarvis-x]], [[ruflo]]
last_updated: 2026-08-09
---

# PAL MCP

An MCP server (Provider Abstraction Layer) that lets a primary AI CLI — Claude Code, Codex CLI, Gemini CLI, Cursor, or the Claude Dev VS Code extension — delegate work to other AI models within the same conversation, keeping context in the primary agent while a specialist model handles a sub-task.

Repo: [`BeehiveInnovations/pal-mcp-server`](https://github.com/BeehiveInnovations/pal-mcp-server). License: Apache 2.0.

## What it does

- Orchestrates multiple models/providers inside one conversation for code review, debugging, and planning
- Preserves conversation context when handing a task to another model ("context revival") — one model can remind another of prior discussion
- Supports conversation threading so a CLI can run multi-model debates or get a second opinion
- Selectively enables tools — each enabled tool adds to context window usage, so the README recommends enabling only what's needed

## Supported providers / models

Gemini, OpenAI, Azure OpenAI, X.AI (Grok), OpenRouter, DIAL, and Ollama — spanning GPT-5-series, Gemini 3.0 Pro, O3, and local models (Llama, Mistral, etc.).

## Installation

```bash
git clone https://github.com/BeehiveInnovations/pal-mcp-server.git
cd pal-mcp-server
./run-server.sh   # auto-configures Claude Desktop, Claude Code, Gemini CLI, Codex CLI, Qwen CLI
```

Alternative: `uvx`-based instant setup via `~/.claude/settings.json`. Either path requires API keys for whichever providers are enabled.

## Role in Jarvis X

In [[the-council]], PAL MCP is the "Team Connector" — the transport that lets Claude (Orchestrator), Codex CLI, and Gemini CLI hand work to each other and to NotebookLM/Composio/Obsidian without each council member needing its own point-to-point integration.

[[agent-secure-comms]] notes that council members exchanging messages over PAL MCP are exactly the kind of agent-to-agent traffic its protocol (identity verification, secret stripping, injection blocking) is meant to protect — PAL MCP provides the transport, [[agent-secure-comms]] is the security layer riding on top of it.
