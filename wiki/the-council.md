---
title: The Council
tags: [jarvis-x, multi-agent, architecture]
sources:
  - raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-25-model-landscape-research.md
related: [[jarvis-x]], [[hermes-agent]], [[universal-model-layer]], [[constitutional-autonomy]], [[free-api-tiers]], [[gemini]], [[groq]], [[openrouter]], [[aider]], [[starnet]], [[jarvis-x-station-view]], [[jarvis-x-runtime]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[source-model-landscape-research]], [[ollama]], [[obsidian]], [[composio]]
last_updated: 2026-09-25
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
>
> **Resolved for the Kimi seat (human ruling, 2026-09-25):** "if kimi is not free treat as a paid subscription and put in paid tiers slot". The 2026-09-25 research finds the Kimi API paid ("There is no permanent Kimi API free tier for production usage", search excerpt, medium confidence), so the Kimi K2.6 seat goes in the paid slot. See [[jarvis-x-model-priority]] and the seat table below. The ruling doesn't answer the other unknowns in this callout (the Gemini seat's "1M+ token context" role, the Gemini CLI path, the other consumer subscriptions).

### What is actually running

- **Model tiers:** the as-built Jarvis tiers use only [[ollama]] (`qwen2.5:3b`), [[groq]] (`openai/gpt-oss-20b`, `openai/gpt-oss-120b`) and [[gemini]] (`gemini-3.6-flash`). See [[jarvis-x-runtime]]. Observation: Gemini shows up in that tier table (as `gemini-3.6-flash`); Claude, Kimi K2.6, DeepSeek V4-Pro and DeepSeek V4-Flash don't. The handoff doesn't tie the Groq tiers' `openai/gpt-oss-*` models to the Codex CLI (GPT) seat.
- **Coding agent:** [[aider]] is the coding agent in use, launched against Groq's `openai/gpt-oss-120b`. The handoff doesn't say how it relates to the Claude Code (Lead Developer) and Codex CLI (Code Reviewer) seats.
- **Multi-agent station:** [[starnet]] was being tried as a multi-agent station. As of the handoff only Ollama works as a StarNet provider, and the handoff's "working agent" is Raqib (Overseer) on Ollama `qwen2.5:7b`. The handoff recommends against chasing a StarNet clone and proposes a [[jarvis-x-station-view]] instead, with a roster file at `config/agents.yaml`.
- **Core agent:** `hermes-agent` and `hermes-api` (uvicorn, port 8000) show as RUNNING under supervisord. A `hermes` CLI is launched after sourcing `~/.jarvis-x/.env` ([[hermes-agent]], [[jarvis-x-runtime]]).
- **Not mentioned in the handoff:** PAL MCP, Codex CLI, Copilot, NotebookLM, Obsidian, Composio. Their as-built state is unknown. See [[jarvis-x-plan-vs-reality]].

## Seats under the 2026-09-25 priority ruling

On 2026-09-25 the human ruled a provider order for [[jarvis-x]] plans ([[jarvis-x-model-priority]]): (1) local models and free open-source tiers that work on any machine, especially ChromeOS, including top-tier Chinese open-source models via [[ollama]] ([[chinese-open-source-models]]); (2) the most free options from Google; (3) Anthropic; (4) OpenAI. Kimi goes in the paid slot if it isn't free. The ruling names providers, not seats, so placing each seat in a slot below is this page's reading of it.

The free-or-paid column comes from the 2026-09-25 research ([[source-model-landscape-research]]). **[F]** means the page was fetched and read; **[S]** means a search-result excerpt only, so medium confidence.

| Seat | Provider | Slot under the ruling | Free or paid, per the research |
|------|----------|-----------------------|--------------------------------|
| Claude (Sonnet), Orchestrator/CEO | Anthropic | 3 | Paid API. There's no ongoing free API tier: "New users receive a small amount of free credits to test the API" [F]. Sonnet 5 is $2 in / $10 out per MTok [F]. |
| Claude Code, Lead Developer | Anthropic | 3 | Paid API, as above [F]. |
| Codex CLI (GPT), Code Reviewer | OpenAI | 4 | Unverified: OpenAI's pricing page was blocked. The rate-limits guide lists a "Free" usage tier ("User must be in an allowed geography", $100/month usage limit), but which models it covers is unverified [S]. |
| Kimi K2.6, Long-Horizon Builder | Moonshot (Kimi) | Paid slot | Paid API: "no permanent Kimi API free tier" [S]; K2.6 costs $0.95 in / $4.00 out per 1M tokens [S]. Open weights exist (Kimi K2 under a Modified MIT License [F]) but are far too big for local use (`kimi-k2` is 1T total / 32B active, and every Kimi model on Ollama is cloud [S]). OpenRouter lists `moonshotai/kimi-k2.6:free` [S], but whether it's live is unverified. Groq's Kimi K2 is deprecated [S]. |
| DeepSeek V4-Pro, Refactorer; DeepSeek V4-Flash, Fast Sub-Agent | DeepSeek (a Chinese model family; the research lists it among the Chinese open-source families on Ollama) | 1, via small local R1 builds or free hosting | V4-Pro and V4-Flash are cloud-only on Ollama (`deepseek-v4-pro:cloud`, `deepseek-v4-flash:cloud`, 1M context) [S]; Ollama cloud is billed per token beyond a small free starter allowance whose model list is unverified [S]. The small DeepSeek-R1 tags `deepseek-r1:7b` (4.7GB) and `deepseek-r1:8b` (5.2GB) fit locally [S]. OpenRouter lists `deepseek/deepseek-v4-flash:free` and `deepseek/deepseek-r1:free` [S], availability unverified. |
| Gemini, The Analyst | Google | 2 | Free tier: the Gemini API pricing page says "Start building free of charge with generous limits" [S], and `gemini-3.6-flash` is listed and GA with free-tier input "Free of charge" [S]. The Gemini CLI gives "1,000 requests/day with personal Google account" via Google login [F]. The CLI's API-key route conflicts between two docs (1,000/day vs 250/day, Flash only) [F]. `gemini-3.1-pro-preview` stays paid-API only (Bug E, above). |
| Copilot, UI/UX Specialist | Not stated in the sources | Not covered | Neither the ruling nor the research covers Copilot. |
| NotebookLM, Research Engine | Not stated in the ruling or the research | Not covered | Neither the ruling nor the research covers NotebookLM. Observation: the DeepSeek master plan gives its URL as `https://notebooklm.google`, but whether it counts as slot 2 ("the most free available from google") isn't stated. |
| [[hermes-agent]], [[obsidian]], [[composio]], PAL MCP | Not model providers | n/a | These seats are an agent, a knowledge store, a tool connector and a team connector. The provider order applies to the models they call, not to them. |

Notes on the table:

- **Chinese open models in slot 1:** two seats are Chinese families, Kimi (Moonshot) and DeepSeek; the research lists both among the Chinese open-source families on Ollama. Kimi has no slot-1 route that the research could verify (too big for local use, paid API), which leaves DeepSeek. The local R1 tags are a different model line from V4, with 128K context [S] (the research suggests `deepseek-r1:8b` for reasoning, as its own inference), so whether they can fill the V4 seats' roles (terminal automation with "1M context"; boilerplate and parallel bulk work) isn't in any source. The as-built `local` tier already runs a Chinese open model, Alibaba's `qwen2.5:3b` ([[jarvis-x-model-priority]]).
- **Kimi's place in the paid slot:** this was open. **Resolved (2026-09-25, follow-up ruling 3):** "Kimi is Kimi". Each paid Kimi model is a standalone paid entry, and any free Kimi route is listed under the provider that serves it (e.g. OpenRouter `moonshotai/kimi-k2.6:free`, if live). See [[jarvis-x-model-priority]].
- **gpt-oss:** [[jarvis-x-model-priority]] reads the as-built Groq tiers (`openai/gpt-oss-20b`, `openai/gpt-oss-120b`) as slot 1, free hosted tiers. They're OpenAI's open-weight models, so their slot was an open question. **Resolved (2026-09-25, follow-up ruling 1):** free counts as free, keeping the official name, so Groq's free `openai/gpt-oss-*` models are in the free tier (slot 1). The handoff doesn't tie them to the Codex CLI seat (see "What is actually running" above).
