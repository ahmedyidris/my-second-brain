---
title: The Council
tags: [jarvis-x, multi-agent, architecture]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[hermes-agent]], [[universal-model-layer]], [[obsidian]], [[composio]]
last_updated: 2026-08-16
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
| PAL MCP *(no page yet — see note below)* | Team Connector | Seamless multi-model handoffs |

## Integration architecture

Claude Orchestrator → Claude Code / Codex CLI / Gemini CLI → PAL MCP Server → NotebookLM / Composio / Obsidian → [[hermes-agent]]

All council agents operate under the standing permissions and gated actions defined in [[constitutional-autonomy]].

## PAL MCP

Installed via `git clone https://github.com/BeehiveInnovations/pal-mcp-server.git && ./run-server.sh`.

Verification commands:
- "Use pal to list available models"
- "clink with codex to review this function"
- "clink with gemini to summarise the structure of this repo"

**Note (2026-08-16 heal pass):** PAL MCP is referenced here and in [[agent-secure-comms]] but has no dedicated wiki page — a confirmed missing-page gap (see [[audits/audit-2026-08-16]]). It was NOT created this pass: two prior unmerged heal branches (`wiki-heal/2026-08-02`, `wiki-heal/2026-08-09`) each already researched and drafted a `pal-mcp.md` page independently. Creating a third version here would conflict with both. Recommend merging one of those branches instead — see the audit for details.
