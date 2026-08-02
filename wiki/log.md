# Wiki Log

Chronological, append-only. One entry per operation.

Format:
```
## [YYYY-MM-DD] <op> | <title>
```

Operations: `ingest`, `query`, `lint`, `update`, `init`.

Utility: `grep "^## \[" wiki/log.md | tail -5` returns the last 5 operations.

---

## [2026-08-02] lint | weekly self-heal

Full audit + top-3 research pass. Scanned all 26 pages, confirmed 2026-07-27 audit's 11 fixes hold with no regressions, no orphans found. Wrote [[audits/audit-2026-08-02]] (20 gaps: HIGH 3, MEDIUM 9, LOW 8).

Researched (≥2 sources each): created [[chromadb]] (open-source vector DB, Apache 2.0, backs Obsidian's memory layer), [[claude-flow]] (clarified: original pre-rename name of [[ruflo]], not a separate "compatible project" as previously recorded — corrected that framing in [[ruflo]]; flagged naming collision with unrelated `kodflow/claude-flow` fork), [[pal-mcp]] (Provider Abstraction Layer MCP server, `clink` multi-CLI orchestration, split out of a subsection in [[the-council]]).

Backfilled [[chromadb]] wikilinks into [[obsidian]], [[ollama]], [[ruflo]], [[second-brain]], [[source-deepseek-jarvis-x-master-plan]], [[jarvis-x]]. Backfilled [[pal-mcp]] into [[the-council]], [[agent-secure-comms]].

Mechanical fixes (no research needed): synced graphify stats in [[wiki/index.md]] (805/1974/77 → 811/1980/63, matches [[graphify]] and graph.json on disk). Added missing cross-refs: [[jarvis-x]] → [[jarvis-x-app]] + [[obsidian]]; [[the-council]] → [[obsidian]] + [[composio]]; [[jarvis-x-hardware]] → [[ollama]]; [[source-jarvis-x-v2-ascension-plan]] → [[jarvis-x-app]]; [[jarvis-x-trading-module]] ↔ [[ruflo]]; [[self-improvement-loop]] ↔ [[ruflo]]; [[universal-model-layer]] ↔ [[ruflo]].

Skipped: `n8n` missing-page (capped at 3 research gaps), jarvis-x-app Tauri-timeline possible stale claim (needs raw-source re-read, not web-researchable — flagged for human review), 3 LOW data-gap pages (thin tables, functional as-is), Gemini/Kimi naming (human judgment on whether it warrants a page).

Updated [[wiki/index.md]] with 2 new Entities ([[chromadb]], [[pal-mcp]]), corrected [[claude-flow]]'s one-liner, and new Audits entry.

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
