# Wiki Log

Chronological, append-only. One entry per operation.

Format:
```
## [YYYY-MM-DD] <op> | <title>
```

Operations: `ingest`, `query`, `lint`, `update`, `init`.

Utility: `grep "^## \[" wiki/log.md | tail -5` returns the last 5 operations.

---

## [2026-09-25] update | Reconcile two parallel ingests of the 2026-09-24 handoff

The same source (`raw/2026-09-24-jarvis-x-starnet-handoff.md`, byte-identical on both sides) was ingested twice: once on master by the local session (the second entry below, which created [[starnet]] and [[ipv6-dns-truncation-crostini]]), and once on the `claude/jarvis-starnet-handoff-plqfqv` branch (the entry directly below). Merged master into the branch and kept both sides' content:

- [[starnet]]: both sides created it. Kept the branch version, which covers every section of master's, and added master's "separate multi-agent platform developed in parallel" framing, its tags and a link to [[ipv6-dns-truncation-crostini]].
- [[jarvis-x]]: master's "Current working state" section and the branch's "Build state" section are merged into one section. It has master's service and tier tables, restart command and systemd gotcha, plus the branch's pointers and Disagreement callout. Master's "these are two different machines" is softened to "may be", since the handoff doesn't say.
- [[jarvis-x-app]]: master's full adapter and Station-tab sections are condensed into the As-built bullets, linking to [[jarvis-x-openai-compatible-api]] and [[jarvis-x-station-view]]. Every fact in them was checked as present on those pages first, so nothing was dropped.
- [[hermes-agent]], [[ollama]], [[jarvis-x-hardware]]: kept the branch versions and added master's unique content: `tts-worker` alongside the Hermes services, the "check override.conf before re-pulling" tip, the `contradiction` tag, and the working assumption to use the Crostini facts day-to-day until the human decides (labelled as an interpretation, not a resolution). Master's "Hermes usable as a coding agent via Aider, pointed at the `smart` tier" is reworded: the handoff launches [[aider]] directly on Groq with the same model as `smart`, not through Hermes.
- [[ipv6-dns-truncation-crostini]] (master's page) is kept. "A strong suspect behind Bug A" is corrected to "one of three likely causes", with none confirmed, matching the handoff. It is now cross-linked with [[crostini]], [[groq]], [[openrouter]], [[jarvis-x-runtime]] and [[source-jarvis-x-starnet-handoff]].
- `wiki/index.md`: one [[starnet]] entry, plus [[ipv6-dns-truncation-crostini]] under Concepts alongside the branch's new pages.

Both ingest entries below are kept (the log is append-only).

---

## [2026-09-24] ingest | Jarvis X / StarNet technical handoff

Read `raw/2026-09-24-jarvis-x-starnet-handoff.md` (as-built Jarvis X + StarNet state, 10 landed fixes, open Bugs A–E, launch commands, 10 gotchas, 4 priorities, 5 "what not to do" rules). All 86 distinct items in the source are captured, and every code block matches it verbatim.

Created: [[source-jarvis-x-starnet-handoff]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[starnet]], [[jarvis-x-station-view]], [[aider]], [[crostini]], [[groq]], [[gemini]], [[openrouter]], [[free-api-tiers]], [[jarvis-x-plan-vs-reality]] (first page under Analyses).

Updated: [[jarvis-x]], [[hermes-agent]], [[ollama]], [[universal-model-layer]], [[jarvis-x-hardware]], [[jarvis-x-voice-engine]], [[jarvis-x-app]], [[the-council]], [[constitutional-autonomy]], [[source-jarvis-x-v2-ascension-plan]], [[source-deepseek-jarvis-x-master-plan]], `wiki/index.md`.

Disagreements flagged with callouts, not resolved (human to decide): machine (Lenovo Y50-70 / Pop!_OS in the plans vs ASUS Chromebook / Crostini in the handoff); tier names and roles (`local|fast|smart|long` with smart = Anthropic vs as-built `local|fast|smart|quality|frontier` with smart = Groq gpt-oss-120b, quality/frontier = gemini-3.6-flash); local models (llama3.2/qwen3/hermes3 vs the qwen2.5 family); service layout (jarvis-core/scheduler/voice under its own user vs supervisord hermes-agent/hermes-api/tts-worker); TTS (Piper + edge-tts vs Chatterbox); Tauri (planned Windows build vs "do not build for daily use"); Hermes "no cloud dependency" vs cloud-routed registry tiers.

Open ambiguities in the source itself: which adapter PART 8's "do not re-enable stream: false" refers to (StarNet's sidecar vs Jarvis's app.py); whether HTTP 400s still occur after 658dc7ce9; whether `CUSTOM_OPENAI_BASE_URL` bypasses Bug C; which project `code/providers/registry.js` belongs to.

Pre-existing issues noticed, not fixed (lint candidates): `[[claude-flow]]` is listed in the index but has no page; [[ollama]]'s "Unlocked after Phase 1 hardware upgrade (16GB RAM + GPU)" doesn't match the master plan, whose Phase 1 is RAM + SSD and whose GPU arrives in Phases 2–3.

`graphify update` was not run from the cloud session: its manifest covers local-only, gitignored files. Run it on the local machine.

---

## [2026-09-24] ingest | Jarvis X / StarNet technical handoff (2026-09-24)

Read `raw/2026-09-24-jarvis-x-starnet-handoff.md` (full session handoff: working state, landed fixes, open bugs, launch commands, environment facts, gotchas).

Created: [[starnet]] (new entity — multi-agent platform, config, Bug A/Bug C, launch command, strategic "don't clone it" direction), [[ipv6-dns-truncation-crostini]] (new concept — Crostini IPv6/Cloudflare truncation bug and the Node c-ares gap).

Updated: [[jarvis-x]] (current working state: latest commit, service table, model tier table, hardware discrepancy flag, restart command, StarNet relationship), [[jarvis-x-app]] (OpenAI-compatible `/v1/chat/completions` + `/v1/models` adapter now live, tier-to-model mapping, proposed Station tab), [[jarvis-x-hardware]] (**flagged unresolved contradiction** — page says Lenovo Y50-70/Pop!_OS, handoff source says ASUS Chromebook/Crostini; documented both, did not silently overwrite, need human to confirm which machine is current), [[ollama]] (systemd `OLLAMA_MODELS` permission fix, models observed on Crostini), [[hermes-agent]] (operational status under supervisord, CLI + Aider usage).

Added cross-links: [[jarvis-x]] ↔ [[starnet]], [[jarvis-x-app]] ↔ [[starnet]], [[jarvis-x-hardware]] ↔ [[ipv6-dns-truncation-crostini]], [[ollama]] ↔ [[starnet]].

Flag for human: hardware contradiction above needs a decision — is the Crostini Chromebook a new/current machine replacing the Lenovo Y50-70, or a separate environment? Left both documented, current Crostini facts marked as operationally authoritative for now since they come from live service behavior rather than a plan doc.

Updated [[wiki/index.md]] with 2 new entries (starnet under Entities, ipv6-dns-truncation-crostini under Concepts).

---

## [2026-07-28] update | Graphify — vault query example added

Ran `graphify query "show auth flow"` on the vault. No auth code — matched wiki Workflow headings in CLAUDE.md. Added result as an example in [[graphify]] showing semantic miss behavior in a pure markdown vault.

---

## [2026-07-28] update | Graphify — MCP server registered + [mcp] extra documented

Installed `graphifyy[mcp]` extra (adds mcp, uvicorn, httpx). Registered graphify MCP server in `~/.claude.json` via `claude mcp add`. Updated [[graphify]] with correct install command, uv Python path, Claude Code registration command, and note that stdio servers exit immediately (expected — spawned on demand by client).

---

## [2026-07-28] update | Graphify — MCP server mode + advanced query flags

Updated [[graphify]] with: MCP server section (stdio/HTTP transports, `--api-key`, Kimi Code registration, `--graph` flag), advanced `--graph` flag for query targeting. Fixed vault stats in [[graphify]] and [[wiki/index.md]] (1199→805 nodes, 2497→1974 edges, 109→77 communities post-.graphifyignore).

---

## [2026-07-28] ingest | Graphify output structure + first graph run

Read `raw/2026-07-28-graphify-output-structure.md`. Created [[graphify]] with output structure, commands, vault stats (1199 nodes, 2497 edges, 109 communities), and CLAUDE.md workflow. Updated [[wiki/index.md]] Skills section.

---

## [2026-07-28] ingest | Agent Starter Kit install commands

Read `raw/2026-07-28-agent-starter-kit-install.md`. Created [[agent-starter-kit]] with Tier 1 skills, Tier 2 plugins, and all install variants (`--agent cursor/codex/'*'`, `--skills-only`). Updated [[wiki/index.md]] Skills section.

---

## [2026-07-27] ingest | Composio CLI setup

Read `raw/2026-07-27-composio-setup.md`. Created [[composio]] with install path, login flow, MCP endpoint, and role in [[the-council]]. Updated [[wiki/index.md]].

---

## [2026-07-27] ingest | Ruflo federation plugin + claude-flow

Read `raw/2026-07-27-ruflo-federation-plugin.md`. Updated [[ruflo]] (added ruflo-federation to plugin table, noted claude-flow install path). Updated [[agent-secure-comms]] (added Enabling layer section). Added [[claude-flow]] stub to index.

---

## [2026-07-27] ingest | Agent-to-Agent Secure Communication protocol

Read `raw/2026-07-27-agent-secure-comms.md`. Created [[agent-secure-comms]] with send path, receive path, trust layer, and cross-links to [[ruflo]], [[the-council]], [[constitutional-autonomy]]. Updated [[wiki/index.md]].

---

## [2026-07-27] ingest | Ruflo plugin system + install commands

Read `raw/2026-07-27-ruflo-install.md`. Updated [[ruflo]] — added Plugin system section with marketplace source, 4 core plugins, and cross-links to [[jarvis-x-trading-module]] and [[obsidian]].

---

## [2026-07-27] ingest | Ruflo architecture diagram

Read `raw/2026-07-27-ruflo-architecture.md`. Created [[ruflo]] with component table and comparison to [[jarvis-x]]. Updated [[wiki/index.md]].

---

## [2026-07-27] update | heal pass — all 11 audit gaps fixed

HIGH (broken wikilinks): Created [[second-brain]], [[wiki-self-heal-skill]], [[llm-wiki-setup-skill]].
MEDIUM (missing pages): Created [[obsidian]], [[ollama]], [[jarvis-x-app]].
MEDIUM (cross-refs): Added [[constitutional-autonomy]] → [[the-council]] link; [[the-council]] → [[constitutional-autonomy]] link; [[jarvis-x-hardware]] → [[universal-model-layer]] link.
LOW: Anchored income roadmap dates to July 2026; added brand kit to [[jarvis-x-content-engine]]; cleaned template artifacts from [[wiki/index.md]].
Updated [[wiki/index.md]] with 6 new pages + new Skills section.

---

## [2026-07-27] lint | first audit pass (dry run)

Scanned 15 pages. Found 11 gaps (HIGH: 3, MEDIUM: 5, LOW: 3). No wiki pages changed.
Created [[audits/audit-2026-07-27]]. Updated [[wiki/index.md]] Audits section.

HIGH: 3 broken wikilinks in [[llm-wiki-pattern]] (second-brain, wiki-self-heal-skill, llm-wiki-setup-skill).
MEDIUM: 2 missing pages (obsidian, ollama), 2 missing cross-refs (the-council↔constitutional-autonomy, hardware→universal-model-layer), 1 missing page (jarvis-x-app).
LOW: relative dates in income roadmap, missing brand kit, template artifacts in index.

---

## [2026-07-27] ingest | wiki-self-heal trigger prompt

Read `raw/2026-07-27-llm-wiki-self-heal-prompt.md`. Updated [[llm-wiki-pattern]] (added autonomous self-heal to Example queries section).

---

## [2026-07-27] ingest | LLM wiki query patterns

Read `raw/2026-07-27-llm-wiki-query-patterns.md`. Updated [[llm-wiki-pattern]] (added Example queries section).

---

## [2026-07-27] ingest | research-vault setup

Read `raw/2026-07-27-research-vault-setup.md`. Created [[research-vault]]. Updated [[wiki/index.md]].

---

## [2026-07-27] ingest | LLM Wiki Skills — installation recipe

Read `raw/2026-07-27-llm-wiki-skills-install.md`. Updated [[llm-wiki-pattern]] (added Installation section).

---

## [2026-07-27] ingest | LLM Wiki Pattern — vault structure diagram

Read `raw/2026-07-27-llm-wiki-vault-structure.md`. Updated [[llm-wiki-pattern]] (added vault structure section and source reference).

---

## [2026-07-27] ingest | LLM Wiki Pattern — Why It Exists

Read `raw/2026-07-27-llm-wiki-pattern-why.md`. Created [[llm-wiki-pattern]]. Updated [[wiki/index.md]].

---

## [2026-07-27] ingest | DeepSeek Jarvis X Master Plan + v2 Ascension Plan

Read `raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md` (12-book reference) and
`raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md` (v2 update, overrides master plan where they conflict).

Created: [[jarvis-x]], [[the-council]], [[hermes-agent]], [[universal-model-layer]],
[[constitutional-autonomy]], [[jarvis-x-voice-engine]], [[jarvis-x-hardware]],
[[jarvis-x-content-engine]], [[jarvis-x-trading-module]], [[jarvis-x-income-roadmap]],
[[self-improvement-loop]], [[source-deepseek-jarvis-x-master-plan]], [[source-jarvis-x-v2-ascension-plan]].

Updated: [[wiki/index.md]] with all 13 new pages across Entities, Concepts, Sources sections.

---

## [2026-07-27] init | wiki created

Wiki initialized with the `llm-wiki-setup` skill. Layout: `flat`.

Ready to ingest. Drop a source into `raw/` and ask: "Ingest the new source I just added."
