# Wiki Index

A catalog of every page in this wiki. When answering queries, read this file first to find relevant pages, then drill in.

Each entry: `- [[page-name]] — one-line summary`

## Entities

- [[research-vault]] — second LLM wiki at ~/research-vault; separate vault for research topics
- [[jarvis-x]] — sovereign self-improving personal AI OS; "the system that runs the house"
- [[hermes-agent]] — local self-improving core brain (Ollama, 70+ skills, cross-session memory)
- [[jarvis-x-hardware]] — current machine: ASUS Chromebook (Crostini, CPU-only, 14GB); the Lenovo Y50-70 kept as the earlier plan machine
- [[the-council]] — multi-agent team: Claude Orchestrator + 12 specialist agents
- [[obsidian]] — GUI markdown second-brain layer in Jarvis X; paired with ChromaDB via brain-mcp
- [[ollama]] — local model runtime; powers hermes-agent and the universal-model-layer local tier
- [[ruflo]] — self-learning agent architecture: CLI/MCP → Router → Swarm → Agents → Memory → LLM Providers + learning loop
- [[agent-secure-comms]] — agent-to-agent security protocol: secret stripping, signing, encryption, injection blocking, trust scores
- [[claude-flow]] — compatible project sharing Ruflo's federation plugin ecosystem; installs via npx claude-flow@latest
- [[composio]] — tool connector with 1000+ app integrations; bridges Jarvis X agents to external services via MCP
- [[jarvis-x-runtime]] — as-built Jarvis X (2026-09-24): repo, supervisord services, env file, launch/test commands, landed fixes
- [[jarvis-x-openai-compatible-api]] — Jarvis X `/v1/models` + `/v1/chat/completions` adapter; tier names as model ids; can't serve StarNet (no streaming, last user turn only)
- [[jarvis-x-starnet-gateway]] — second OpenAI-compatible endpoint on :8010 so StarNet can use Jarvis's tiers (streamed replies, full history, tools); built in jarvis-x PR #37, not merged
- [[starnet]] — separate multi-agent platform (androoAGI/starnet); web sidecar on :8787; only Ollama works, Groq crashes the sidecar (Bugs A, C open; Bug C causes analysed 2026-09-26)
- [[aider]] — terminal coding agent; launched against Groq gpt-oss-120b; never paste shell commands into its prompt
- [[crostini]] — Debian 13 Linux env on the ASUS Chromebook; IPv6-first breaks Cloudflare POSTs; Node c-ares caveat
- [[groq]] — provider for the fast/smart tiers (openai/gpt-oss-20b / -120b); compound-mini 404 fix
- [[gemini]] — provider for the quality/frontier tiers (gemini-3.6-flash); models-list is stale; 3.1 Pro API is paid-only
- [[openrouter]] — provider with free models on shared-pool rate limits; Cloudflare-fronted; not in the as-built tier table

## Concepts

- [[llm-wiki-pattern]] — Karpathy wiki pattern: compile knowledge once, query the wiki not the sources; no RAG infrastructure
- [[second-brain]] — externalised persistent knowledge system; LLM variant uses the wiki pattern
- [[universal-model-layer]] — v2 unified provider abstraction; all models behind one CLI interface
- [[constitutional-autonomy]] — governance model: standing permissions, gated actions, kill switch
- [[self-improvement-loop]] — Hermes meta-agent reviews its own logs and generates new skills
- [[jarvis-x-voice-engine]] — offline Faster-Whisper/Piper + online edge-tts; EN/AR multi-accent
- [[jarvis-x-content-engine]] — bilingual content pipeline; income stream #3 (Arabic AI explainers)
- [[jarvis-x-trading-module]] — market intelligence, paper-trading; hard gates before live
- [[jarvis-x-income-roadmap]] — bilingual AI operations specialist path; platforms + certifications
- [[jarvis-x-app]] — v2 delivery: FastAPI + PWA + Tauri; Linux → Windows → mobile → macOS
- [[jarvis-x-station-view]] — "Station" tab in Jarvis X's React UI: 4 text-only agents (Raqib + 3 StarNet-derived roles); built in jarvis-x PR #38, awaiting merge and one app.py mount call
- [[jarvis-x-model-priority]] — the human's 2026-09-25 ladder: local + free open-source (incl. Chinese open models via Ollama) → Google free → Anthropic → OpenAI; Kimi in the paid slot
- [[chinese-open-source-models]] — Qwen, DeepSeek, GLM, Kimi, MiniMax, MiniCPM: what fits the Chromebook via Ollama, what's cloud-only, where it's free-hosted
- [[free-api-tiers]] — consumer AI subscriptions don't grant API access; what is actually free (Gemini flash, Groq gpt-oss, OpenRouter)
- [[ipv6-dns-truncation-crostini]] — Crostini resolves IPv6 first, truncating POSTs to Cloudflare-fronted APIs; Node's https/c-ares ignores the usual fix

## Skills

- [[llm-wiki-setup-skill]] — installs the full Karpathy vault structure in one pass
- [[wiki-self-heal-skill]] — autonomous audit + research loop; full or audit-only mode
- [[agent-starter-kit]] — one-command installer: 6 skills + 6 Claude Code plugins across all agent types
- [[graphify]] — knowledge graph tool: maps project into queryable graph; MCP server mode for team/agent access (1,132 nodes, 2,527 edges, 97 communities as of 2026-09-25)

## Sources

- [[source-deepseek-jarvis-x-master-plan]] — comprehensive 12-book Jarvis X reference (DeepSeek, July 2026)
- [[source-jarvis-x-v2-ascension-plan]] — v2 Ascension Plan; overrides master plan where they conflict
- [[source-jarvis-x-starnet-handoff]] — 2026-09-24 technical handoff: as-built Jarvis X + StarNet state, 10 fixes, 5 open bugs, priorities
- [[source-model-landscape-research]] — 2026-09-25 web research on local, free and paid model options for the Chromebook; [F]/[S] confidence marks

## Analyses

- [[jarvis-x-plan-vs-reality]] — earlier plans vs the 2026-09-24 as-built state; divergences flagged for the human

## Audits

- [[audits/audit-2026-07-27]] — first audit pass; 11 gaps (HIGH: 3 broken wikilinks, MEDIUM: 5 missing pages/cross-refs, LOW: 3)
- [[audits/audit-2026-09-25]] — lint after the handoff and rulings: 8 fixed (claude-flow page, schema log order, Phase 1 error, titles, orphans, machine question, graphify advice), 5 flagged (research confidence, legacy unsourced text, open questions)
