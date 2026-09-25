---
title: Jarvis X Plan vs Reality
tags: [analysis, jarvis-x, as-built, plans]
sources:
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-25-model-landscape-research.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[source-jarvis-x-starnet-handoff]], [[source-jarvis-x-v2-ascension-plan]], [[source-deepseek-jarvis-x-master-plan]], [[jarvis-x-runtime]], [[jarvis-x-hardware]], [[crostini]], [[ollama]], [[universal-model-layer]], [[jarvis-x-openai-compatible-api]], [[hermes-agent]], [[jarvis-x-voice-engine]], [[jarvis-x-app]], [[constitutional-autonomy]], [[the-council]], [[starnet]], [[jarvis-x-station-view]], [[aider]], [[free-api-tiers]], [[groq]], [[gemini]], [[openrouter]], [[obsidian]], [[second-brain]], [[self-improvement-loop]], [[jarvis-x-content-engine]], [[jarvis-x-trading-module]], [[jarvis-x-income-roadmap]], [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[source-model-landscape-research]]
last_updated: 2026-09-25
---

# Jarvis X Plan vs Reality

This page compares what the plans for [[jarvis-x]] (v1 dated July 2026; v2 undated in its raw file) say with what the 2026-09-24 handoff reports as built. It's an analysis page. Each row cites the plan section and the handoff part it draws on. Where a source is silent, the cell says so and makes no guess. Nothing here resolves a disagreement: every open question is left for the human.

## Sources and conventions

| Short name | Source | Role |
|------------|--------|------|
| **v1** | [[source-deepseek-jarvis-x-master-plan]] (DeepSeek, 12 books, July 2026) | Original plan |
| **v2** | [[source-jarvis-x-v2-ascension-plan]] | Overrides v1 where the two conflict |
| **Handoff** | [[source-jarvis-x-starnet-handoff]] (2026-09-24, PARTs 1–8) | Snapshot of what is built and running |
| **Ruling** | [[jarvis-x-model-priority]] (`raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md`) | The human's 2026-09-25 decisions on the current machine and the provider order |
| **Research** | [[source-model-landscape-research]] (2026-09-25) | Web research on model options. **[F]** = fetched and read; **[S]** = search excerpt only, medium confidence |

The Status column uses three values:

- **matches**: the handoff agrees with the plan.
- **diverges**: the handoff contradicts the plan on at least one specific point. Where parts still overlap, the cell says which.
- **not covered by handoff**: the handoff is silent. That doesn't mean the thing doesn't exist. The handoff is a technical note about two repos, not a full inventory.

## Comparison

| Area | Plan says (cite which plan) | Handoff says (2026-09-24) | Status | Open question for the human |
|------|-----------------------------|---------------------------|--------|-----------------------------|
| Hardware / machine | v1 Book II: Lenovo Y50-70 with an Intel i7-4710HQ (4C/8T, Haswell), an NVIDIA GTX 860M (2GB) that is "Currently Undetected", 7.7 GB DDR3L ("Must Upgrade to 16GB") and a 953 GB SATA SSD. The upgrade roadmap goes Phase 1 "16GB DDR3L RAM + 2TB SSD" → Phase 2 "ADT-Link R43SG + 850W PSU" → Phase 3 "NVIDIA RTX 3090 (24GB VRAM)". v2 §10 constraints: "CPU-only Y50-70". See [[jarvis-x-hardware]]. | PART 5: ASUS Chromebook with an 11th Gen i5 and no GPU. RAM is 14GB total, ~9-10GB free after Chrome. Disk is 72GB total, ~11GB free after cleanup. See [[crostini]]. | diverges → **resolved 2026-09-25**: the human ruled the Chromebook current (CPU-only still holds) | Resolved: the Chromebook is current. Still open: does the Lenovo upgrade roadmap still apply? |
| OS | v1 Book II: Pop!_OS 24.04 LTS. v2 §2 changes "Pop!_OS only" to "Linux-first → Windows → PWA (iOS/Android) → macOS". v2 §10 asks for scripts "for a fresh Pop!_OS terminal". | PART 5: Crostini (Debian 13 trixie). Crostini resolves to IPv6 first, which truncates POST bodies to Cloudflare-fronted APIs. It's fixed with `/etc/gai.conf` and `NODE_OPTIONS`, but not for Node's c-ares resolver (PART 2 fix 5, gotcha 5). See [[crostini]]. | diverges (still Linux, so v2's "Linux-first" holds). The 2026-09-25 ruling makes the Crostini machine current | Should scripts and installers now target Debian 13 on Crostini instead of Pop!_OS? (Implied by the ruling, but not stated.) |
| Local models | v1 Books II, III and IX: `llama3.2:3b` (primary for CPU, ~2GB), `qwen3:1.5b` (fast alternative, ~1GB), `nomic-embed-text` (embeddings for ChromaDB, ~0.5GB) and `hermes3:8b` (future, needs GPU/16GB RAM, ~5.5GB). | PART 5 lists the models present: `qwen2.5:7b` (4.7GB), `qwen2.5:3b` (1.9GB), `qwen2.5-coder:7b` (4.7GB), `qwen2.5-coder:3b` (1.9GB) and `nomic-embed-text` (274MB). The `local` tier is `qwen2.5:3b` (PART 1). StarNet's Raqib runs `qwen2.5:7b` at ~10 tok/s. See [[ollama]]. | diverges (`nomic-embed-text` matches). **Ruling 2026-09-25:** slot 1 asks for top-tier Chinese open-source models locally via Ollama. The installed Qwen 2.5 family is Alibaba's, a Chinese open model. Options that fit the Chromebook are on [[chinese-open-source-models]] and [[ollama]] | Why the Qwen 2.5 family instead of `llama3.2:3b` and `qwen3:1.5b`? Is `hermes3:8b` still planned? Are the coder models meant for [[aider]]? Which Chinese open models, if any, should replace or join the Qwen 2.5 family? (The research's suggested local stack is its own inference.) |
| Model tiers and provider roles | v2 §3 ([[universal-model-layer]]): one `providers/` interface and `jj ask "..." --tier local\|fast\|smart\|long`. Providers are Ollama, Gemini CLI/API, Groq, OpenRouter (28+ free models), Anthropic ("while sub lives"), NVIDIA NIM free and Mistral free. Router rules: privacy-sensitive → local only, long-context → Gemini, fast loops → Groq, a fallback chain on quota errors, and per-provider daily counters in SQLite. v2 §2 summarises v1 as "Router: local Ollama + Gemini/Groq/OpenRouter". | PART 1, all verified via `POST /api/ask`: `local` = ollama `qwen2.5:3b`, `fast` = groq `openai/gpt-oss-20b`, `smart` = groq `openai/gpt-oss-120b`, `quality` and `frontier` = gemini `gemini-3.6-flash`. The registry is `registry.js` (fix 3 edits `code/providers/registry.js`), and `frontier` resolves to `registry:quality` (fix 7). PART 7 says Jarvis "handles fallbacks". OpenRouter appears in StarNet's env vars and launch command (fix 9, PART 4), in the IPv6 fix (fix 5) and in Bug E's free-access list, but not in the Jarvis tier table. Anthropic, NVIDIA NIM and Mistral aren't mentioned. See [[jarvis-x-runtime]], [[groq]], [[gemini]], [[openrouter]]. | diverges (the Ollama, Groq and Gemini roles overlap; Groq on `fast` matches "fast loops → Groq"; the tier names differ). **Ruling 2026-09-25:** the human ruled a provider order: local and free open-source → Google free → Anthropic → OpenAI, with Kimi in the paid slot ([[jarvis-x-model-priority]]). The as-built order already matches it: `local` is slot 1, the Groq gpt-oss tiers are slot 1 as free hosted tiers (per [[jarvis-x-model-priority]]), and the Gemini tiers are slot 2 | Resolved: the provider order. Still open: the tier names (did `quality`/`frontier` replace `long`?). Should `frontier` get its own model? Are privacy routing and the SQLite counters built? Do the gpt-oss tiers count as slot 1 or slot 4 (OpenAI)? |
| Local-first / zero cloud keys | v1 Book I: "All models, data, and logic run on your hardware" and "Nothing leaves your machine unless explicitly allowed". v2 §3: "Every provider is optional. JARVIS X must boot and function with zero cloud keys." | Four of the five tiers (`fast`, `smart`, `quality`, `frontier`) call Groq or Gemini (PART 1). Gotcha 9: if the quality tier returns ollama responses, the Gemini key is missing or invalid. No zero-key boot test is reported. | diverges in part (routing is cloud-heavy); zero-key boot not covered by handoff | Does Jarvis boot and answer with an empty `.env`? Is "privacy-sensitive → local only" enforced anywhere? (Also flagged on [[jarvis-x]].) |
| CLI vs HTTP interface | v2 §3: the `jj ask ... --tier` CLI. v2 §5: the `jj halt` kill switch. v2 §8: "FastAPI backend (already the daemon)". v2 §2 summarises v1 delivery as "Scripts + CLI". | HTTP: `POST /api/ask`, plus the OpenAI-compatible `GET /v1/models` and `POST /v1/chat/completions` at `127.0.0.1:8000`, where `model` is a tier name (PART 1). CLI: `hermes`, which needs `~/venv-ai/bin` on PATH (PART 4). No `jj` command appears. See [[jarvis-x-openai-compatible-api]]. | diverges (FastAPI matches; `jj` not covered by handoff) | Does `jj` exist, or have the `/v1` adapter and the `hermes` CLI taken its place? |
| Core agent (Hermes) | v1 Book III: Hermes Agent, "Self-improving • 70+ default skills • Cross-session memory", "Runs entirely on your hardware", installed with `ollama launch hermes`. v1 Book XII: the [[self-improvement-loop]]. | PART 1: the supervisord services `hermes-agent` and `hermes-api` are RUNNING. `hermes.py` has a `registry:` branch that serves the cloud tiers (fix 2, `4281158`). PART 4: a `hermes` CLI. Skills, memory and self-improvement aren't mentioned. See [[hermes-agent]]. | matches in name only; features not covered by handoff | Is this Nous Research's Hermes Agent? Is the self-improvement loop running? |
| Voice stack | v1 Book VI: Faster-Whisper (STT), Piper (TTS), Porcupine/openWakeWord and an ESP32-S3-BOX-3 satellite. v2 §4: an offline Faster-Whisper + Piper core, an online edge-tts accent pack, a `voice:` block in config.yaml, and later XTTS-class cloning on a GPU box. v2 §5 lists a `jarvis-voice` service. | PART 1 and Bug D: `tts-worker` is RUNNING but degraded. The Chatterbox TTS model isn't installed, so the worker reports `{"loaded": false}` and returns 500 on `/synthesize`. Priority 4: obtain the ~5GB checkpoint, place it at `~/jarvis-x/voices/chatterbox-eg/` and restart `tts-worker`. STT, wake word, Piper and edge-tts aren't mentioned. See [[jarvis-x-voice-engine]]. | diverges | Did Chatterbox replace Piper and edge-tts, or was it added alongside them? Is there an STT path? Is there disk space for ~5GB (~11GB free per PART 5)? |
| App delivery (PWA / Tauri) | v2 §8: a FastAPI backend and one web UI served locally, installable as a PWA; "Same UI wrapped with Tauri later for Windows/macOS desktop builds". Platform order: ① Linux ② Windows ③ PWA ④ macOS/native iOS. v2 §9: Wk 5-6 "PWA-ready web UI shell", Wk 7-8 "Windows run-through". v1 Book XII lists a Portable Installer and an iOS Companion App as "Coming". | Jarvis has an "existing React frontend" (Priority 3). `app.py` has an SPA wildcard route, `@app.get("/{full_path:path}")`, that serves `index.html` (fix 7). StarNet's Tauri shell was built once and then deleted ("was slow, no benefit over web"). The Tauri build takes 30-60 min, needs 8GB disk + 6GB RAM, and is "not useful for daily work on this hardware" (gotcha 8). PART 8: "Do not build the Tauri desktop shell for daily use." The only Tauri shell the handoff records is StarNet's, so it isn't stated whether the gotcha and the rule cover a Jarvis Tauri wrapper. There's no mention of a PWA or phone access. See [[jarvis-x-app]]. | diverges (the local web UI matches; PWA not covered by handoff; Tauri set aside for daily use, though whether that means a Jarvis shell is ambiguous) | Does a Tauri Windows build stay in the roadmap for distribution? Can the React frontend be installed as a PWA? |
| Service layout | v2 §5: systemd services `jarvis-core`, `jarvis-scheduler` and `jarvis-voice`, running "under its own Linux user with full ownership of `~/jarvis/` (vault, DB, skills, media workspace)". They auto-start on boot, restart themselves on a crash and run a weekly self-test. v1 appendix: a `jarvis-x/` repo with `jarvis_core.py`, `jarvis_council.py`, `jarvis_voice.py`, `jarvis_content.py`, `jarvis_trading.py`, `config/`, `scripts/`, `docs/` and `vault/`. | PART 1: supervisord, under the systemd unit `jarvis-supervisord.service`, runs `hermes-agent`, `hermes-api` (uvicorn, port 8000) and `tts-worker`. The source is in `~/jarvis-x`. Keys come from `EnvironmentFile=/home/ahmedyidris/.jarvis-x/.env` (fix 6). Config is in `~/jarvis-x/config/` (`system_prompt.txt`, `supervisord.conf`). The code files named are `app.py`, `hermes.py` and `code/providers/registry.js`. See [[jarvis-x-runtime]], [[constitutional-autonomy]]. | diverges (the `jarvis-x` directory name matches v1's appendix, not v2's `~/jarvis/`) | Is there a dedicated Linux user? Were the three planned services renamed, merged or never built? Is there a scheduler or a weekly self-test? |
| Multi-agent | v1 Book IV, [[the-council]]: 13 members (Claude Sonnet 3.7 as orchestrator, Claude Code, Codex CLI, Kimi K2.6, DeepSeek V4-Pro/Flash, Gemini, Copilot, NotebookLM, Hermes, Obsidian, Composio, PAL MCP). v1 Book III: CrewAI/LangGraph orchestration (Orchestrator → Researcher → Executor → Meta-Reviewer). v1 appendix: `jarvis_council.py` and `config/agents.yaml`. v2 §6: content scripts "drafted by the Council". | [[starnet]] (`androoAGI/starnet`, web sidecar on :8787): the working agent is Raqib (Overseer), on Ollama `qwen2.5:7b`, and only Ollama works as a provider. Groq runs kill the sidecar (Bug A), and the UI rejects the Jarvis localhost provider (Bug C). PART 8: "Do not chase a StarNet clone." Priority 3 is the [[jarvis-x-station-view]]: a "Station" tab, a roster at `config/agents.yaml`, four endpoints (list, chat, transcript, task), a grid UI and one background worker per agent. | diverges (the `config/agents.yaml` path matches v1's appendix). **Ruling 2026-09-25:** the Claude seats fall to slot 3, Codex CLI to slot 4 and Kimi K2.6 to the paid slot (its API is paid [S]). See the seat table on [[the-council]] | Is the station view meant to succeed the Council? Which Council seats are still realistic, given Bug E? (Partly answered: the ruling ranks the seats' providers. Kimi's order within the paid slot is still open.) |
| Coding agent | v1 Book IV: Claude Code (Lead Developer), Codex CLI (Code Reviewer) and Copilot (UI/UX Specialist). PAL MCP "Links Claude Code, Codex, Gemini". v2 §9: the Wk 3-4 "Claude Code sprint", run "while you still have Claude". | PART 4: [[aider]] runs from `~/jarvis-x` with `aider --model groq/openai/gpt-oss-120b --no-show-model-warnings`. Claude Code, Codex CLI, Copilot and PAL MCP aren't mentioned. | not covered by handoff (for the Council seats); Aider doesn't appear in either plan. **Ruling 2026-09-25:** Claude Code (Anthropic) is slot 3 and Codex CLI (OpenAI) is slot 4. Aider's as-launched model, Groq's free `openai/gpt-oss-120b`, is slot 1 as a free hosted tier (per [[jarvis-x-model-priority]]), and the installed `qwen2.5-coder` models would be a local slot-1 option ([[aider]]) | Is Aider a stand-in for Claude Code or an addition to it? Is the Claude subscription still live? |
| Autonomy and safety | v2 §5, [[constitutional-autonomy]]: standing permissions, and one-tap approval for "anything irreversible or external", including "deleting outside its home". Also `CONSTITUTION.md` in git, an append-only audit log and the `jj halt` kill switch. "Fully unsupervised self-modification stays out — permanently." v1 Book XII: self-improvement "Auto-Implements (with safety checks)". | PART 8: "Do not run YOLO-mode agents on this machine. The venv and StarNet workspace have both been destroyed by that pattern." Also "Do not put API keys in git. .env is gitignored — keep it that way." Keys live in `~/.jarvis-x/.env` (chmod 600, PART 5). `CONSTITUTION.md`, the audit log and `jj halt` aren't mentioned. | not covered by handoff (constitution, audit log, kill switch) | Have any of the constitution pieces been built? Should the YOLO-mode rule be written into `CONSTITUTION.md`? |
| Budget / subscriptions | v2 §10 constraints: "$0/month". v2 §2: "incl. Claude/Gemini while subs live, hot-swap free tiers after". v2 §3: Anthropic "while sub lives, then optional API". v1 Book I: "No subscriptions. No dependencies." v1's Council lists Kimi K2.6, Gemini (1M+ context), DeepSeek V4 and Claude. | Bug E: consumer subscriptions don't give API access. "Google AI Pro unlocks 3.1 Pro in the consumer app", but the `gemini-3.1-pro-preview` API is "limit: 0 — paid API only", and it's the "Same for most consumer subscriptions". The free API options are `gemini-3.6-flash`, `openai/gpt-oss-20b`/`-120b` on Groq, and OpenRouter free models with shared-pool rate limits. See [[free-api-tiers]]. | diverges in part (the free-tier stance fits $0/month; "while subs live" doesn't extend to API access). **Ruling 2026-09-25:** Kimi goes in the paid slot, and the research finds its API paid [S]. Consumer subscriptions still give no API access (Bug E). The free tiers per the research: the Gemini API free tier [S] and the Gemini CLI's 1,000 requests/day with Google login [F]; Groq's free `openai/gpt-oss-120b` at 30 RPM / 1,000 RPD / 8,000 TPM / 200,000 TPD [F]; OpenRouter `:free` models at 50 requests/day, or 1,000/day after a one-time $10 credit purchase [S], with each model's availability unverified. Anthropic gives new users small free credits only [F]. See [[free-api-tiers]] and [[source-model-landscape-research]] | Is $0/month still binding, or is a paid API acceptable for a `frontier` tier? Which subscriptions are still live? |
| Memory / second brain | v1 Book V: [[obsidian]] + ChromaDB. Its setup commands install brain-mcp and pull `nomic-embed-text`, which Book III labels "Embeddings for ChromaDB". v1 Book III also lists brain-mcp's tools (`hybrid_search_tool`, `read_note_tool`, `create_note_tool`). v1 Book III: NotebookLM as the RAG engine. v2 §5: `~/jarvis/` holds the "vault, DB, skills", and indexing anything dropped into `inbox/` is a standing permission. | Only `nomic-embed-text` (274MB) is present in Ollama (PART 5). Obsidian, ChromaDB, brain-mcp, NotebookLM, a vault and `inbox/` aren't mentioned. | not covered by handoff | Has the memory layer been built? Is this vault ([[second-brain]]) meant to be that memory? |
| Content, trading and income modules | v2 §6, [[jarvis-x-content-engine]]: topic queue → Council script → edge-tts/Piper voiceover → ffmpeg → approval → publish. v2 §7, [[jarvis-x-trading-module]]: Binance Spot Testnet, paper trading and hard gates. v1 Book X, [[jarvis-x-income-roadmap]]: Bilingual AI Operations Specialist, via Mindrift and Outlier. v2 §8 definition of done: "10 published pieces" and a "daily market brief arriving". | None of these is mentioned. PART 7's four priorities are the StarNet bug, routing StarNet through Jarvis, the station view and the voice pipeline. | not covered by handoff | Has any content been produced, or the testnet module started? How do these rank against the handoff's priorities? |
| Schedule | v2 §9, the 12-week overlay: Wk 1-2 extraction + income + handles; Wk 3-4 Universal Model Layer + constitution skeleton; Wk 5-6 voice + PWA shell; Wk 7-8 content engine + Windows run-through; Wk 9-10 Market Intelligence; Wk 11-12 brand kit, installer and docs, then tag v2.0. v1 Book XII: an evolution timeline from Genesis (Week 1-2) to Transcendence (Month 6+). | No week numbers, milestones or version tags. The work is organised as Priorities 1-4 (PART 7). | not covered by handoff | Which overlay week does the human consider current? Is the overlay still the schedule? |

## Rulings since the handoff (2026-09-25)

The human answered part of the handoff's open questions on 2026-09-25 (`raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md`).

**Resolved:**

- **Current machine:** the Chromebook on Crostini ([[jarvis-x-hardware]], [[crostini]]). See the Hardware and OS rows.
- **Provider order for plans:** (1) local models and free open-source tiers that work on any machine, especially ChromeOS, including top-tier Chinese open-source models via Ollama; (2) the most free options from Google; (3) Anthropic; (4) OpenAI ([[jarvis-x-model-priority]]). The as-built tier order already matches it.
- **Kimi:** in the paid slot, because it isn't free (the research finds its API paid [S]).

**Still open:**

- The "do not re-enable stream: false" warning: does it refer to StarNet's adapter or to Jarvis's `/v1` adapter? The ruling didn't answer it.
- The tier names: did `quality`/`frontier` replace the plan's `long`?
- The Lenovo upgrade roadmap: does it still apply?
- Kimi's order within the paid slot, relative to Anthropic and OpenAI.
- Whether gpt-oss (OpenAI's open-weight model, served free on Groq) counts as slot 1 or slot 4.

The other open questions in the table are unchanged.

## At a glance

**Matches, or partial matches, the handoff confirms:**

- CPU-only inference: the Chromebook has no GPU
- A Linux host
- A FastAPI backend with a locally served web UI (v2 §8)
- Ollama, Groq and Gemini as providers, with Groq on the `fast` tier
- `nomic-embed-text` installed
- Cloud tiers that use only models the handoff lists as free on the API (Bug E)
- The repo directory name `jarvis-x/` and the path `config/agents.yaml`, both from v1's appendix file structure. As built, the repo is at `~/jarvis-x`, and `config/agents.yaml` is the planned station roster.

**Divergences with a callout on the affected page:**

- [[jarvis-x]]: local-first vs cloud tiers
- [[jarvis-x-hardware]], [[crostini]], [[source-jarvis-x-v2-ascension-plan]] and [[source-deepseek-jarvis-x-master-plan]]: the Y50-70 on Pop!_OS vs the Chromebook on Crostini
- [[ollama]] and [[hermes-agent]]: the planned models vs the Qwen 2.5 family; [[hermes-agent]] also has cloud routing
- [[universal-model-layer]] and [[gemini]]: `local|fast|smart|long` vs the five as-built tiers; [[universal-model-layer]] also has the `jj` CLI vs HTTP
- [[jarvis-x-runtime]]: service layout, tier names, hardware
- [[openrouter]] and [[free-api-tiers]]: registered providers (OpenRouter, NVIDIA NIM, Mistral) vs the as-built tiers and free-access list
- [[constitutional-autonomy]]: services
- [[jarvis-x-app]]: Tauri, Pop!_OS
- [[jarvis-x-voice-engine]]: Piper/edge-tts vs Chatterbox

**Named in the plans but absent from the handoff:**

- `jj` (`ask`, `halt`)
- `CONSTITUTION.md` and the audit log
- SQLite provider counters
- Anthropic, NVIDIA NIM and Mistral providers
- Obsidian, ChromaDB, brain-mcp and NotebookLM
- PAL MCP, Composio, Codex CLI and Copilot
- CrewAI/LangGraph, n8n and LM Studio
- Faster-Whisper, Piper, edge-tts, the wake word and the ESP32 satellite
- The content, trading and income modules
- The installer and the PWA

## Reading

**Interpretation (not stated in any source):** these are tentative readings of the table. The human should confirm or correct them.

- **The build moved to a different machine.** Most of the handoff's environment problems come from the Chromebook and Crostini: IPv6 truncation, c-ares, Chrome using 10GB of the 14GB RAM, ~11GB free disk, and the cost of a Tauri build. Neither plan mentions any of them. The plan sections that depend on hardware (the Y50-70 upgrade roadmap, the GPU fix commands, `hermes3:8b` marked "Future (GPU/16GB RAM)") may need re-baselining before they guide work again.
- **The model layer exists, in a different shape.** There are five tiers instead of four, and the cloud providers carry four of them. The provider set has shrunk to what the handoff says is free on the API (Bug E). The plan's promise of zero-key operation is neither confirmed nor refuted by the handoff.
- **The work so far has gone into plumbing.** The handoff's content is services, env handling, provider bugs, an OpenAI-compatible API and a multi-agent experiment. The plan's memory, governance and revenue modules don't come up. That is absence of evidence, not evidence of absence.
- **Multi-agent ambitions have been scaled down.** The handoff calls its own direction achievable: "StarNet is the ambition; a station tab in Jarvis is achievable". The move goes from a 13-seat Council, to an external multi-agent app ([[starnet]]), to a proposed roster file inside Jarvis. The roster path `config/agents.yaml` already appears in v1's file structure.
- **Priorities and schedule have come apart.** The handoff's Priorities 1-4 don't follow the order of the v2 12-week overlay. Whether the overlay still governs is a question for the human.

## Related

[[source-jarvis-x-starnet-handoff]] | [[source-jarvis-x-v2-ascension-plan]] | [[source-deepseek-jarvis-x-master-plan]] | [[jarvis-x]] | [[jarvis-x-runtime]] | [[jarvis-x-hardware]] | [[crostini]] | [[universal-model-layer]] | [[jarvis-x-openai-compatible-api]] | [[hermes-agent]] | [[jarvis-x-voice-engine]] | [[jarvis-x-app]] | [[constitutional-autonomy]] | [[the-council]] | [[starnet]] | [[jarvis-x-station-view]] | [[aider]] | [[free-api-tiers]] | [[ollama]] | [[groq]] | [[gemini]] | [[openrouter]] | [[jarvis-x-model-priority]] | [[chinese-open-source-models]] | [[source-model-landscape-research]]
