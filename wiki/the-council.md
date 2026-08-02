---
title: The Council
tags: [jarvis-x, multi-agent, architecture]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[hermes-agent]], [[universal-model-layer]]
last_updated: 2026-07-27
---

# The Council

The multi-agent team architecture at the heart of [[jarvis-x]]. Each agent has a specialized role; Claude acts as Orchestrator/CEO driving sessions.

## Members

| Model | Role | Best For |
|-------|------|----------|
| Claude (Sonnet) | Orchestrator/CEO | Intent, strategic planning |
| Claude Code | Lead Developer | Implementation, refactoring |
| Codex CLI (GPT) | Code Reviewer | Edge cases, security audits |
| Kimi K2.6 | Long-Horizon Builder | 300 concurrent sub-agents, multi-day builds |
| DeepSeek V4-Pro | Refactorer | Terminal automation, 1M context |
| DeepSeek V4-Flash | Fast Sub-Agent | Boilerplate, parallel bulk work |
| Gemini | The Analyst | 1M+ token context, large codebases |
| Copilot | UI/UX Specialist | Frontend, visual design |
| NotebookLM | Research Engine | Zero-token ingest of URLs/PDFs/videos |
| [[hermes-agent]] | Core Agent Brain | Self-improving, skill creation |
| [[obsidian]] | Second Brain | Persistent knowledge, RAG |
| [[composio]] | Tool Connector | 1000+ app integrations |
| [[pal-mcp]] | Team Connector | Seamless multi-model handoffs |

## Integration architecture

Claude Orchestrator → Claude Code / Codex CLI / Gemini CLI → [[pal-mcp]] Server → NotebookLM / [[composio]] / [[obsidian]] → [[hermes-agent]]

All council agents operate under the standing permissions and gated actions defined in [[constitutional-autonomy]].

## PAL MCP

See [[pal-mcp]] for full details. Installed via `git clone https://github.com/BeehiveInnovations/pal-mcp-server.git && ./run-server.sh`.

Verification commands:
- "Use pal to list available models"
- "clink with codex to review this function"
- "clink with gemini to summarise the structure of this repo"
