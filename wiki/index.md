# Wiki Index

A catalog of every page in this wiki. When answering queries, read this file first to find relevant pages, then drill in.

Each entry: `- [[page-name]] — one-line summary`

## Entities

- [[research-vault]] — second LLM wiki at ~/research-vault; separate vault for research topics
- [[jarvis-x]] — sovereign self-improving personal AI OS; "the system that runs the house"
- [[hermes-agent]] — local self-improving core brain (Ollama, 70+ skills, cross-session memory)
- [[jarvis-x-hardware]] — Lenovo Y50-70 specs, CPU-only strategy, and hardware upgrade roadmap
- [[the-council]] — multi-agent team: Claude Orchestrator + 12 specialist agents
- [[obsidian]] — GUI markdown second-brain layer in Jarvis X; paired with ChromaDB via brain-mcp
- [[ollama]] — local model runtime; powers hermes-agent and the universal-model-layer local tier
- [[ruflo]] — self-learning agent architecture: CLI/MCP → Router → Swarm → Agents → Memory → LLM Providers + learning loop
- [[agent-secure-comms]] — agent-to-agent security protocol: secret stripping, signing, encryption, injection blocking, trust scores
- [[claude-flow]] — compatible project sharing Ruflo's federation plugin ecosystem; installs via npx claude-flow@latest
- [[composio]] — tool connector with 1000+ app integrations; bridges Jarvis X agents to external services via MCP
- [[jarvis-x-runtime]] — as-built Jarvis X (2026-09-24): repo, supervisord services, env file, launch/test commands, landed fixes
- [[jarvis-x-openai-compatible-api]] — Jarvis X `/v1/models` + `/v1/chat/completions` adapter; tier names as model ids
- [[starnet]] — separate multi-agent platform (androoAGI/starnet); web sidecar on :8787; only Ollama works, Groq crashes the sidecar (Bugs A, C open)
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
- [[jarvis-x-station-view]] — planned "Station" tab in Jarvis X's React UI; the recommended path instead of a StarNet clone
- [[free-api-tiers]] — consumer AI subscriptions don't grant API access; what is actually free (Gemini flash, Groq gpt-oss, OpenRouter)
- [[ipv6-dns-truncation-crostini]] — Crostini resolves IPv6 first, truncating POSTs to Cloudflare-fronted APIs; Node's https/c-ares ignores the usual fix

## Skills

- [[llm-wiki-setup-skill]] — installs the full Karpathy vault structure in one pass
- [[wiki-self-heal-skill]] — autonomous audit + research loop; full or audit-only mode
- [[agent-starter-kit]] — one-command installer: 6 skills + 6 Claude Code plugins across all agent types
- [[graphify]] — knowledge graph tool: maps project into queryable graph; MCP server mode for team/agent access (805 nodes, 1974 edges, 77 communities)

## Sources

- [[source-deepseek-jarvis-x-master-plan]] — comprehensive 12-book Jarvis X reference (DeepSeek, July 2026)
- [[source-jarvis-x-v2-ascension-plan]] — v2 Ascension Plan; overrides master plan where they conflict
- [[source-jarvis-x-starnet-handoff]] — 2026-09-24 technical handoff: as-built Jarvis X + StarNet state, 10 fixes, 5 open bugs, priorities

## Analyses

- [[jarvis-x-plan-vs-reality]] — earlier plans vs the 2026-09-24 as-built state; divergences flagged for the human

## Audits

- [[audits/audit-2026-07-27]] — first audit pass; 11 gaps (HIGH: 3 broken wikilinks, MEDIUM: 5 missing pages/cross-refs, LOW: 3)
