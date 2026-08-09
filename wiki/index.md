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
- [[composio]] — tool connector with 1000+ app integrations; bridges Jarvis X agents to external services via MCP
- [[pal-mcp]] — Provider Abstraction Layer MCP server; lets Claude Code/Codex/Gemini CLI delegate to other AI models mid-conversation
- [[brain-mcp]] — local MCP server turning an Obsidian vault into a searchable knowledge base (Chroma + Ollama embeddings)

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

## Skills

- [[llm-wiki-setup-skill]] — installs the full Karpathy vault structure in one pass
- [[wiki-self-heal-skill]] — autonomous audit + research loop; full or audit-only mode
- [[agent-starter-kit]] — one-command installer: 6 skills + 6 Claude Code plugins across all agent types
- [[graphify]] — knowledge graph tool: maps project into queryable graph; MCP server mode for team/agent access (811 nodes, 1980 edges, 63 communities, per graphify-out/GRAPH_REPORT.md)

## Sources

- [[source-deepseek-jarvis-x-master-plan]] — comprehensive 12-book Jarvis X reference (DeepSeek, July 2026)
- [[source-jarvis-x-v2-ascension-plan]] — v2 Ascension Plan; overrides master plan where they conflict

## Analyses

## Audits

- [[audits/audit-2026-07-27]] — first audit pass; 11 gaps (HIGH: 3 broken wikilinks, MEDIUM: 5 missing pages/cross-refs, LOW: 3)
- [[audits/audit-2026-08-09]] — weekly self-heal; 8 gaps found (HIGH: 3, MEDIUM: 4, LOW: 1); 3 researched (claude-flow/Ruflo rename correction, [[pal-mcp]], [[brain-mcp]]) + cross-ref/stale-stat cleanup
