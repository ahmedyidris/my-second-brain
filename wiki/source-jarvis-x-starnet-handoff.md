---
title: Source — Jarvis X StarNet Handoff
tags: [source, jarvis-x, starnet, handoff, as-built]
sources:
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[starnet]], [[jarvis-x-station-view]], [[aider]], [[crostini]], [[ipv6-dns-truncation-crostini]], [[groq]], [[gemini]], [[openrouter]], [[free-api-tiers]], [[ollama]], [[hermes-agent]], [[jarvis-x-voice-engine]], [[jarvis-x-app]], [[jarvis-x-hardware]], [[universal-model-layer]], [[the-council]], [[constitutional-autonomy]], [[jarvis-x-plan-vs-reality]], [[source-jarvis-x-v2-ascension-plan]], [[source-deepseek-jarvis-x-master-plan]]
last_updated: 2026-09-25
---

# Source — Jarvis X StarNet Handoff

A technical handoff for [[jarvis-x]] and [[starnet]], dated 2026-09-24. The author line reads "session notes, Ahmed Yidris". It records what was actually built and running on the machine at that point: working state, the fixes that landed, open bugs, launch commands, gotchas and next steps. It is a point-in-time snapshot, not a plan. Read any wiki claim drawn from it as "as of the 2026-09-24 handoff". For the plans it follows, see [[source-deepseek-jarvis-x-master-plan]] and [[source-jarvis-x-v2-ascension-plan]].

## The source

| Item | Value |
|------|-------|
| Heading (as written) | Jarvis X / StarNet — Technical Handoff |
| Date | 2026-09-24 |
| Author line | session notes, Ahmed Yidris |
| Type | Technical handoff: a snapshot of as-built state |
| Covers | Jarvis X (`~/jarvis-x`, repo https://github.com/ahmedyidris/jarvis-x, branch `master`) and StarNet (`~/starnet`, repo `androoAGI/starnet`, branch `feat/harness-backend`) |
| Machine | ASUS Chromebook, Crostini (Debian 13 trixie) |
| Structure | 8 parts, ending "END OF HANDOFF" |
| Vault copy | `raw/2026-09-24-jarvis-x-starnet-handoff.md` |

**Secrets:** the handoff contains no real keys. The only key-like strings are a truncated `gsk_...` (in the description of fix 1) and the local placeholder key `sk-jarvis-local` (in the StarNet launch command).

## Parts and where they live in the wiki

| Part | Heading | Integrated into |
|------|---------|-----------------|
| 1 | Current working state | [[jarvis-x-runtime]] (services, tiers, persona file), [[jarvis-x-openai-compatible-api]] (the `/v1` adapter), [[starnet]] (StarNet state, Raqib), [[jarvis-x-voice-engine]] (`tts-worker`) |
| 2 | Fixes that landed (with commands) | See the fixes table below |
| 3 | Bugs still open | See the bugs table below |
| 4 | Launch commands | [[jarvis-x-runtime]] (restart and test), [[starnet]] (web mode), [[aider]], [[hermes-agent]] (Hermes CLI) |
| 5 | Environment facts | [[crostini]] and [[jarvis-x-hardware]] (machine, RAM, CPU, disk), [[jarvis-x-runtime]] (Python, Node, key paths), [[ollama]] (models present) |
| 6 | Gotchas to remember | [[aider]] (1), [[jarvis-x-runtime]] (2, 9), [[starnet]] (3, 6, 8), [[gemini]] (4, 9), [[crostini]] (5, 7), [[jarvis-x-app]] (8), [[ollama]] (10) |
| 7 | What to try next | See the priorities table below |
| 8 | What not to do | See "What not to do" below |

## Fixes that landed (PART 2)

| # | Fix | Commit (per handoff) | Page |
|---|-----|----------------------|------|
| 1 | Jarvis env var quoting bug (`registry.js` kept quotes on `.env` values) | not stated | [[jarvis-x-runtime]] |
| 2 | Jarvis system prompt dropped on registry tiers (`hermes.py`) | `4281158` | [[jarvis-x-runtime]], [[hermes-agent]] |
| 3 | Groq fast model 404 (`groq/compound-mini` → `openai/gpt-oss-20b`) | `b634ed8` | [[groq]] |
| 4 | Gemini model name: keep `gemini-3.6-flash`; the models-list is stale | not stated | [[gemini]] |
| 5 | IPv6 truncation (Crostini + Cloudflare) | not stated | [[crostini]], [[ipv6-dns-truncation-crostini]] |
| 6 | systemd `EnvironmentFile` for Jarvis | not stated | [[jarvis-x-runtime]] |
| 7 | OpenAI-compatible adapter in Jarvis (`app.py`) | not stated in PART 2. PART 1's latest commit, `99652aa`, has the message "feat(api): OpenAI-compatible /v1/chat/completions + /v1/models", but the handoff doesn't explicitly tie it to fix 7. | [[jarvis-x-openai-compatible-api]] |
| 8 | Ollama model directory | not stated | [[ollama]] |
| 9 | StarNet provider env vars: correct names (no `SKYNET_` prefix) | not stated | [[starnet]] |
| 10 | StarNet message sanitization | `658dc7ce9` | [[starnet]] |

## Key takeaways

As of the 2026-09-24 handoff:

- **Jarvis X is running.** supervisord, under the systemd unit `jarvis-supervisord.service`, runs `hermes-agent`, `hermes-api` (uvicorn, port 8000) and a degraded `tts-worker`. Five model tiers are verified via `POST /api/ask`, and an OpenAI-compatible `/v1` adapter is live. The latest commit is `99652aa`. See [[jarvis-x-runtime]] and [[jarvis-x-openai-compatible-api]].
- **The machine is not the one in the plans.** (On 2026-09-25 the human confirmed it as the current machine; see [[jarvis-x-hardware]].) It is an ASUS Chromebook under Crostini (Debian 13 trixie), with an 11th Gen i5, no GPU, 14GB RAM and ~11GB free disk. Crostini resolves to IPv6 first, and on the IPv6 path, POST bodies to Cloudflare-fronted APIs (Groq, OpenRouter) get truncated. The fixes work system-wide and for Node, but not for Node's c-ares resolver. See [[crostini]] and [[jarvis-x-plan-vs-reality]].
- **Free API access is narrow (Bug E).** Consumer AI subscriptions don't give API access. The body names Google AI Pro and says it's the "Same for most consumer subscriptions". What's free on the API: [[gemini]] `gemini-3.6-flash`, [[groq]] `openai/gpt-oss-20b` and `openai/gpt-oss-120b`, and [[openrouter]] free models with shared-pool rate limits. The as-built cloud tiers use the Gemini and Groq models from that list. See [[free-api-tiers]].
- **StarNet works only with Ollama.** Groq runs kill its sidecar (Bug A, not diagnosed). The handoff's verdict is not to chase a StarNet clone and to add a "Station" tab to Jarvis instead (Priority 3). See [[starnet]] and [[jarvis-x-station-view]].
- **Observation: several failures gave no clear error.** In fix 1, every provider "rejected silently" the quoted keys. In fix 2, `fast`/`smart`/`frontier` all answered "I am Qwen" because the system prompt was dropped. Bug A, still open, has the same shape: the sidecar dies with no error in `/tmp/starnet.log`.
- **Rules (PART 8).** No YOLO-mode agents (the handoff says they destroyed the venv and the StarNet workspace), no API keys in git, no Tauri desktop shell for daily use, and no re-enabling `stream: false` on "the OpenAI-compatible adapter". The handoff doesn't say which adapter that is (see below). See [[constitutional-autonomy]].

## Open bugs (PART 3)

| Bug | Summary (handoff heading) | Status per handoff | Page |
|-----|---------------------------|--------------------|------|
| A | StarNet Groq runs kill the sidecar | "Not fixed. Not diagnosed." Three **hypotheses** ("likely one of"): streaming HTTP to Cloudflare-fronted endpoints fails silently on Crostini; an uncaught async error kills Node without logging; the provider adapter dereferences a field that doesn't exist for non-Ollama providers. A `stream: false` patch made it worse (broke Ollama too) and was reverted. | [[starnet]], [[groq]], [[crostini]] |
| B | Jarvis /v1 endpoint doesn't read files | "This is expected behavior." Callers (Aider, Continue, StarNet agents) must read the file themselves and include its content in the message. | [[jarvis-x-openai-compatible-api]], [[aider]] |
| C | StarNet custom provider verification rejects localhost | "Not investigated fully." Setting `CUSTOM_OPENAI_BASE_URL` at launch *may* bypass the UI verification if StarNet reads it at boot (unconfirmed). | [[starnet]], [[jarvis-x-openai-compatible-api]] |
| D | tts-worker degraded | Chatterbox TTS model not installed. The worker reports `{"loaded": false}` and returns 500 on `/synthesize`, which the handoff calls "intentional and honest". Fix: obtain the ~5GB `chatterbox-ckpt` and place it at `~/jarvis-x/voices/chatterbox-eg/`. | [[jarvis-x-voice-engine]] |
| E | Kimi / consumer AI subscriptions don't give API access | Stated as a limitation, with no fix. `gemini-3.1-pro-preview` has an API limit of 0 (paid API only), even though Google AI Pro unlocks 3.1 Pro in the consumer app. | [[free-api-tiers]], [[gemini]], [[the-council]] |

## Priorities (PART 7)

| Priority | Task (per handoff) | Page |
|----------|--------------------|------|
| 1 | StarNet Groq bug: find out why the sidecar dies on Groq calls. Run it in the foreground and watch the exit reason, or add logging around the fetch call in `sidecar/providers/openai-compatible.js`. | [[starnet]] |
| 2 | Route StarNet through Jarvis: get the custom-provider UI to accept localhost, OR confirm that the env-var path works. "Then all StarNet traffic goes through Jarvis, which handles fallbacks and never dies on truncation." | [[starnet]], [[jarvis-x-openai-compatible-api]] |
| 3 | Station view in Jarvis: a "Station" tab in Jarvis's existing React frontend, a roster at `config/agents.yaml`, four endpoints in `app.py` (list, chat, transcript, task), a simple grid UI and one background worker per agent. The handoff calls it "a real weekend project". | [[jarvis-x-station-view]] |
| 4 | Fix the voice pipeline: obtain the chatterbox checkpoint (~5GB), place it at `~/jarvis-x/voices/chatterbox-eg/`, and restart `tts-worker`. | [[jarvis-x-voice-engine]] |

## What not to do (PART 8)

| Rule (verbatim) | Page |
|-----------------|------|
| Do not chase a StarNet clone. Jarvis already has 80% of StarNet's useful features. Add a station view to Jarvis instead. | [[starnet]], [[jarvis-x-station-view]] |
| Do not build the Tauri desktop shell for daily use. Web UI is faster and identical in function. | [[starnet]], [[jarvis-x-app]] |
| Do not re-enable stream: false on the OpenAI-compatible adapter. It breaks all providers. | [[starnet]] (Bug A), [[jarvis-x-openai-compatible-api]] (see the ambiguity note below) |
| Do not put API keys in git. .env is gitignored — keep it that way. | [[jarvis-x-runtime]], [[constitutional-autonomy]] |
| Do not run YOLO-mode agents on this machine. The venv and StarNet workspace have both been destroyed by that pattern. | [[constitutional-autonomy]], [[starnet]] |

> **Ambiguity (`stream: false`):** the handoff doesn't say which "OpenAI-compatible adapter" this rule means. It uses the phrase for Jarvis's `/v1` adapter in `app.py` (PART 1, fix 7). The only `stream: false` change it records, though, is the patch under Bug A (the StarNet sidecar bug), and it doesn't say which file that patch changed. StarNet's own provider file is also OpenAI-compatible: `sidecar/providers/openai-compatible.js` (PART 1). The rule could mean StarNet's adapter, Jarvis's, or both. Nothing in the handoff says `stream: false` was ever applied to Jarvis's `app.py`. Left for the human to clarify.

> **Ambiguity (Tauri):** the only Tauri shell the handoff records is StarNet's (PART 1: "built successfully at one point, but deleted"). It doesn't say whether the PART 8 Tauri rule and the gotcha 8 build figures cover a Jarvis Tauri shell as well.

## Relationship to the plans

The plans, [[source-deepseek-jarvis-x-master-plan]] (v1, dated July 2026) and [[source-jarvis-x-v2-ascension-plan]] (v2, undated in its raw file), describe what was intended. This handoff describes what was built. It doesn't mention either plan, so it never says which plan decisions were changed on purpose.

Where the handoff disagrees with a page's plan-based content, that page has a **Disagreement** callout, left for the human to resolve. The full comparison, area by area, is in [[jarvis-x-plan-vs-reality]]. The main divergences:

- The hardware and OS: an ASUS Chromebook on Crostini, where both plans have a Lenovo Y50-70 on Pop!_OS (v1 Book II; v2 §10) ([[jarvis-x-hardware]], [[crostini]])
- The local models: the Qwen 2.5 family, where v1 has `llama3.2:3b`, `qwen3:1.5b` and `hermes3:8b` ([[ollama]], [[hermes-agent]])
- The tier names: `local | fast | smart | quality | frontier`, where v2 §3 has `local|fast|smart|long` ([[universal-model-layer]], [[jarvis-x-runtime]])
- The service layout: supervisord running `hermes-agent`, `hermes-api` and `tts-worker`, where v2 §5 has `jarvis-core`, `jarvis-scheduler` and `jarvis-voice` ([[constitutional-autonomy]])
- The TTS engine: Chatterbox, where v1 has Piper and v2 has Piper plus edge-tts ([[jarvis-x-voice-engine]])

Plan areas the handoff doesn't cover include the Obsidian + ChromaDB memory layer, `CONSTITUTION.md` with its audit log and `jj halt`, and the content, trading and income modules.

## Pages created from this source

[[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[starnet]] | [[jarvis-x-station-view]] | [[aider]] | [[crostini]] | [[ipv6-dns-truncation-crostini]] | [[groq]] | [[gemini]] | [[openrouter]] | [[free-api-tiers]] | [[jarvis-x-plan-vs-reality]]

## Existing pages this source affects

[[jarvis-x]] | [[hermes-agent]] | [[the-council]] | [[constitutional-autonomy]] | [[jarvis-x-app]] | [[jarvis-x-voice-engine]] | [[ollama]] | [[jarvis-x-hardware]] | [[universal-model-layer]] | [[source-jarvis-x-v2-ascension-plan]] | [[source-deepseek-jarvis-x-master-plan]]

## Provenance

The vault copy is `raw/2026-09-24-jarvis-x-starnet-handoff.md`, and it ends at "END OF HANDOFF". The human also asked for a copy at `~/jarvis-x/docs/HANDOFF_2026-09-24.md`, inside the Jarvis X repo and outside this vault. That request came with the paste but isn't part of the handoff text, so it isn't in the vault copy. This wiki doesn't track whether the copy was made.
