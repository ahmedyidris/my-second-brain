# Wiki Log

Newest first, add-only: new entries go at the top, and past entries are never edited or deleted. One entry per operation.

Format:
```
## [YYYY-MM-DD] <op> | <title>
```

Operations: `ingest`, `query`, `lint`, `update`, `init`.

Utility: `grep "^## \[[0-9]" wiki/log.md | head -5` returns the 5 most recent operations.

---

## [2026-09-26] ingest | StarNet gateway and Station tab build notes

Read `raw/2026-09-26-starnet-gateway-and-station-build.md`: session notes from building the human's "A then C" in jarvis-x. A is StarNet routed through Jarvis (PR #37); C is the Station tab (PR #38). Both are drafts, CI-green or pending, not merged, and not yet run on the Chromebook.

Created [[jarvis-x-starnet-gateway]].

Updated:
- [[jarvis-x-station-view]]: status is built; new "As built" section; the open questions answered by the build.
- [[starnet]]: Bug C code analysis with ranked causes and a workaround; Bug A mitigation; a Disagreement on the Priority 2 target (:8000 vs :8010); the direction question marked Resolved ("A then C").
- [[jarvis-x-openai-compatible-api]]: why StarNet can't use it, with a Disagreement against the handoff; streaming partly answered (app.py doesn't stream).
- [[jarvis-x-runtime]]: a ports table (8000, 8001 tts-worker, 8002 dashboard, 8010 gateway, 8787, 11434); Priority 2/3 status.
- [[index]]: new gateway entry; station-view, starnet and API lines refreshed.

Flags for the human:
- The gateway's first port (8001) collided with tts-worker. It was fixed before merge.
- app.py still needs one mount call for the Station, added by the local session.
- The Bug C causes come from upstream StarNet code, not the local `feat/harness-backend` branch.

## [2026-09-25] update | Apply the human's follow-up rulings (free vs paid, by-provider catalog, tier names, direction)

Source added: `raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md` (verbatim reply to the eight open questions).

Resolved:
- **gpt-oss:** free counts as free, under its official name, so it's slot 1.
- **Gemma:** listed in both slot 1 and slot 2.
- **Kimi:** each paid Kimi model is a standalone paid entry. Free models are listed under every provider that serves them.
- **Tier names:** they stay as they are, picked StarNet-style (local, or a provider's API).
- **Lenovo roadmap:** parked.
- **Budget:** $0/month still binds, with paid routes as options.
- **Tokens:** "we need more tokens". Recommended adding Gemini Flash-Lite and spreading load across the free providers; not yet made in Jarvis.

Still open: which adapter the stream:false warning means (the human: "I don't know").

New direction, recorded on [[starnet]], [[jarvis-x-station-view]] and [[jarvis-x]]: complete both StarNet and Jarvis and merge them. It is kept alongside the handoff's "do not chase a StarNet clone" as an explicit Disagreement. What "merge" means concretely, and in which repo, is left for the human.

Pages touched:
- [[jarvis-x-model-priority]]: restructured into a catalog by access route (Local/Ollama, Groq, OpenRouter, Ollama cloud, Google, then paid standalone Anthropic, OpenAI and Kimi); a new "Getting more tokens" section.
- [[universal-model-layer]], [[free-api-tiers]], [[groq]], [[openrouter]], [[gemini]], [[the-council]], [[aider]], [[chinese-open-source-models]], [[jarvis-x-hardware]], [[jarvis-x-plan-vs-reality]].

---

## [2026-09-25] update | Graphify refresh (structural, merge-only)

The committed graph was purely structural (all 811 nodes had `_origin: ast`). 411 of its nodes come from gitignored files that exist only on the human's machine.

In a scratch copy:
- re-extracted the 47 files changed since `df27757` with graphify's structural extractor;
- merged them into the existing graph with `build_merge` and pruning off;
- re-clustered;
- kept community names where at least 40% of the members overlap an old community, and named new communities after their main file;
- re-signed `.graphify_labels.json.sig`;
- regenerated `graph.html` and `GRAPH_REPORT.md`.

Result: 1,119 nodes, 2,514 edges, 103 communities. All 411 local-only nodes were kept, and the health check found 0 dangling edges.

`manifest.json` and the cache were left unchanged, so the human's next `/graphify . --update` on the Chromebook sees the real local state. Updated the stats on [[graphify]] and in the index.

---

## [2026-09-25] lint | Audit after the handoff ingest and rulings

Script checks over all 44 pages: links, frontmatter, source paths, titles and filenames, index coverage, orphans and secrets. Wrote [[audits/audit-2026-09-25]].

Fixed:
- 4 broken `[[claude-flow]]` links: created [[claude-flow]].
- Two title/filename mismatches: [[agent-secure-comms]] and [[ipv6-dns-truncation-crostini]] retitled; files not renamed.
- Two orphans: [[graphify]] and [[agent-starter-kit]] now have reciprocal links.
- The [[ollama]] Phase 1 error.
- Schema: the log is newest-first (`head -5`), and `Skills` is now a valid index category (`CLAUDE.md`, `AGENTS.md`, log header).

Flagged, not fixed:
- search-excerpt confidence on the model research;
- legacy wiki text not in its raw source;
- two skill pages citing gitignored sources;
- the open questions for the human.

No broken wikilinks remain, apart from the `[[page-name]]` format example in the index header.

---

## [2026-09-25] update | Apply the human's 2026-09-25 rulings (Chromebook current; model priority) with web research

Sources added:
- `raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md` (verbatim ruling);
- `raw/2026-09-25-model-landscape-research.md` (web research, with [F]/[S] confidence marks);
- `raw/2026-09-25-graphify-update-cloud-test.md` (recorded tool output).

Created:
- [[jarvis-x-model-priority]]: the ruling's ladder — local and free open-source first, then Google free, then Anthropic, then OpenAI, with Kimi in the paid slot — plus concrete options per slot and a recommended Chromebook stack, labelled as inference;
- [[chinese-open-source-models]];
- [[source-model-landscape-research]].

Updated for the machine ruling:
- [[jarvis-x-hardware]]: the Chromebook first; the Lenovo kept as the earlier plan machine.
- "Resolved" lines on [[crostini]], [[jarvis-x]], [[jarvis-x-runtime]], [[jarvis-x-app]], [[jarvis-x-plan-vs-reality]], [[source-deepseek-jarvis-x-master-plan]], [[source-jarvis-x-v2-ascension-plan]] and [[source-jarvis-x-starnet-handoff]].

Updated for the model ruling and the research:
- [[ollama]] (reworked around the Chromebook);
- [[hermes-agent]], [[free-api-tiers]], [[groq]], [[gemini]], [[openrouter]], [[universal-model-layer]];
- [[the-council]] (a seat-by-slot table; Kimi in the paid slot);
- [[jarvis-x]], [[jarvis-x-plan-vs-reality]] (new "Rulings since the handoff" section), [[source-jarvis-x-v2-ascension-plan]];
- [[obsidian]], [[aider]];
- single cross-links on [[self-improvement-loop]], [[ruflo]] and [[jarvis-x-content-engine]].

Also updated [[graphify]] and `CLAUDE.md`: `graphify update .` is code-only and shrank the graph in a cloud checkout.

Kept open for the human:
- gpt-oss: slot 1 or slot 4?
- Gemma: slot 1, slot 2 or both?
- Kimi's order within the paid slot, and whether a live OpenRouter `:free` route moves it up.
- Tier names.
- The Lenovo roadmap.
- The stream:false adapter question.
- Whether $0/month still binds.
- `gemini-3.6-flash` vs the Flash-Lite models.

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
