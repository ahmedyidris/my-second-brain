---
title: The Council
tags: [jarvis-x, multi-agent, architecture]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[hermes-agent]], [[universal-model-layer]], [[constitutional-autonomy]], [[free-api-tiers]], [[gemini]], [[groq]], [[openrouter]], [[aider]], [[starnet]], [[jarvis-x-station-view]], [[jarvis-x-runtime]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
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
| Obsidian | Second Brain | Persistent knowledge, RAG |
| Composio | Tool Connector | 1000+ app integrations |
| PAL MCP | Team Connector | Seamless multi-model handoffs |

## Integration architecture

Claude Orchestrator → Claude Code / Codex CLI / Gemini CLI → PAL MCP Server → NotebookLM / Composio / Obsidian → [[hermes-agent]]

All council agents operate under the standing permissions and gated actions defined in [[constitutional-autonomy]].

## PAL MCP

Installed via `git clone https://github.com/BeehiveInnovations/pal-mcp-server.git && ./run-server.sh`.

Verification commands:
- "Use pal to list available models"
- "clink with codex to review this function"
- "clink with gemini to summarise the structure of this repo"

## Practical state (2026-09-24 handoff)

The roster above comes from the earlier plans. The 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]) shows what was actually wired up on the machine at that point. As of the 2026-09-24 handoff:

### API access (Bug E)

The handoff files this as Bug E: "Kimi / consumer AI subscriptions don't give API access".

- "Google AI Pro unlocks 3.1 Pro in the consumer app. The API tier for gemini-3.1-pro-preview is limit: 0 — paid API only. Same for most consumer subscriptions."

Free API access, per the handoff, is limited to:

| Provider | Free API access |
|----------|-----------------|
| [[gemini]] | `gemini-3.6-flash` (verified working) |
| [[groq]] | `openai/gpt-oss-20b`, `openai/gpt-oss-120b` (verified) |
| [[openrouter]] | Free models with shared-pool rate limits |

See [[free-api-tiers]].

> **Implication (not stated in the handoff):** A consumer Kimi subscription won't give API access for the **Kimi K2.6** seat. The **Gemini** "Analyst" seat is limited to `gemini-3.6-flash` if it runs on the free API, because `gemini-3.1-pro-preview` needs a paid API. Unknown: whether `gemini-3.6-flash` meets the "1M+ token context" role in the table; whether the Gemini CLI path in the integration architecture above is affected; and which other seats "most consumer subscriptions" covers. The handoff names only Kimi and Google AI Pro.

### What is actually running

- **Model tiers:** the as-built Jarvis tiers use only [[ollama]] (`qwen2.5:3b`), [[groq]] (`openai/gpt-oss-20b`, `openai/gpt-oss-120b`) and [[gemini]] (`gemini-3.6-flash`). See [[jarvis-x-runtime]]. Observation: Gemini shows up in that tier table (as `gemini-3.6-flash`); Claude, Kimi K2.6, DeepSeek V4-Pro and DeepSeek V4-Flash don't. The handoff doesn't tie the Groq tiers' `openai/gpt-oss-*` models to the Codex CLI (GPT) seat.
- **Coding agent:** [[aider]] is the coding agent in use, launched against Groq's `openai/gpt-oss-120b`. The handoff doesn't say how it relates to the Claude Code (Lead Developer) and Codex CLI (Code Reviewer) seats.
- **Multi-agent station:** [[starnet]] was being tried as a multi-agent station. As of the handoff only Ollama works as a StarNet provider, and the handoff's "working agent" is Raqib (Overseer) on Ollama `qwen2.5:7b`. The handoff recommends against chasing a StarNet clone and proposes a [[jarvis-x-station-view]] instead, with a roster file at `config/agents.yaml`.
- **Core agent:** `hermes-agent` and `hermes-api` (uvicorn, port 8000) show as RUNNING under supervisord. A `hermes` CLI is launched after sourcing `~/.jarvis-x/.env` ([[hermes-agent]], [[jarvis-x-runtime]]).
- **Not mentioned in the handoff:** PAL MCP, Codex CLI, Copilot, NotebookLM, Obsidian, Composio. Their as-built state is unknown. See [[jarvis-x-plan-vs-reality]].
