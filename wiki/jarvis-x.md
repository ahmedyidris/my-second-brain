---
title: Jarvis X
tags: [jarvis-x, ai-os, sovereign, entity]
sources:
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[the-council]], [[hermes-agent]], [[constitutional-autonomy]], [[jarvis-x-hardware]], [[universal-model-layer]], [[self-improvement-loop]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[jarvis-x-app]], [[starnet]], [[jarvis-x-station-view]], [[jarvis-x-plan-vs-reality]], [[source-jarvis-x-starnet-handoff]], [[ipv6-dns-truncation-crostini]], [[free-api-tiers]], [[crostini]], [[aider]], [[ollama]], [[groq]], [[gemini]]
last_updated: 2026-09-25
---

# Jarvis X

**Just A Rather Very Intelligent System — X.** A sovereign, self-improving personal AI operating system running on local hardware. Not a chatbot or API wrapper — a resident intelligence that owns its home directory and governs itself by a constitution.

Brand line: *"JARVIS X — the system that runs the house."* / *«جارفيس إكس — النظام اللي بيدير البيت»*

Bilingual by design: Egyptian Arabic and English are both first-class citizens.

## Core capabilities

| # | Capability | How |
|---|-----------|------|
| 1 | Thinks | [[hermes-agent]] as reasoning engine |
| 2 | Remembers | Obsidian + ChromaDB second brain |
| 3 | Learns | Meta-agent [[self-improvement-loop]] |
| 4 | Acts | Tool-calling, real system operations |
| 5 | Creates | [[jarvis-x-content-engine]] |
| 6 | Analyzes | [[jarvis-x-trading-module]] |
| 7 | Speaks | [[jarvis-x-voice-engine]] |

## Sovereignty principles

- **Local-first** — all models, data, logic run on your hardware
- **Private** — nothing leaves the machine without explicit permission
- **Open-source** — every component is free and auditable
- **Portable** — entire system can be replicated and backed up
- **Zero-subscription** — must boot and function with zero cloud keys

## Current working state (2026-09-24 handoff)

What actually exists, as of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]). Full detail on [[jarvis-x-runtime]].

- **Repo:** https://github.com/ahmedyidris/jarvis-x (branch `master`), checked out at `~/jarvis-x`. Latest commit `99652aa` — feat(api): OpenAI-compatible /v1/chat/completions + /v1/models. See [[jarvis-x-openai-compatible-api]].
- **Machine:** ASUS Chromebook, Crostini (Debian 13 trixie). See [[crostini]] and [[jarvis-x-hardware]].
- **Multi-agent:** a separate, parallel app, [[starnet]], is under active development in this environment. The explicit direction is not to build StarNet out into a full Jarvis X clone, but to add a "Station" tab to Jarvis X's own frontend instead ([[jarvis-x-station-view]]).
- **Coding agent:** [[aider]], launched from `~/jarvis-x` with `aider --model groq/openai/gpt-oss-120b --no-show-model-warnings`.
- **Plan vs as-built:** [[jarvis-x-plan-vs-reality]].

Services managed by `supervisord` under systemd unit `jarvis-supervisord.service`:

| Service | Status |
|---|---|
| hermes-agent | RUNNING ([[hermes-agent]]) |
| hermes-api (uvicorn, port 8000) | RUNNING |
| tts-worker | RUNNING — degraded, chatterbox model absent, `/synthesize` returns 500 ([[jarvis-x-voice-engine]]) |

Model tiers, all verified working via `POST /api/ask` (see [[universal-model-layer]]):

| tier | provider | model |
|---|---|---|
| local | [[ollama]] | qwen2.5:3b |
| fast | [[groq]] | openai/gpt-oss-20b |
| smart | [[groq]] | openai/gpt-oss-120b |
| quality | [[gemini]] | gemini-3.6-flash |
| frontier | [[gemini]] | gemini-3.6-flash |

Note: `gemini-3.6-flash` does not appear in Google's models-list endpoint (the handoff calls the listing stale), but it works when called directly. Do not "correct" it to a listed model.

**Hardware discrepancy (flagged 2026-09-24):** [[jarvis-x-hardware]] describes the machine as a Lenovo Y50-70 running Pop!_OS. The handoff describes the working environment as an ASUS Chromebook running Crostini (Debian 13 trixie), with 14GB RAM, an 11th Gen i5, no GPU and a 72GB disk. **Resolved by the human on 2026-09-25:** the Chromebook is the current machine. The Lenovo stays on [[jarvis-x-hardware]] as the plans' record.

Restart command:

```bash
sudo systemctl restart jarvis-supervisord.service
sleep 8
supervisorctl -c ~/jarvis-x/config/supervisord.conf status
```

Gotcha: systemd units don't inherit shell exports. So `jarvis-supervisord.service` needed an explicit `EnvironmentFile=/home/ahmedyidris/.jarvis-x/.env` drop-in (`/etc/systemd/system/jarvis-supervisord.service.d/env.conf`), plus `NODE_OPTIONS=--dns-result-order=ipv4first`. See [[jarvis-x-runtime]] and [[ipv6-dns-truncation-crostini]].

Cloud tiers on Groq and Gemini are in active use alongside the local Ollama tier. Their models (`openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `gemini-3.6-flash`) are the ones the handoff lists under free API access (Bug E; see [[free-api-tiers]]). The handoff does not say whether the system boots and functions with zero cloud keys (the "Zero-subscription" principle above), and reports no test of it.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan / DeepSeek Master Plan):** this page's sovereignty principles (above, drawn from the plans) say "all models, data, logic run on your hardware" and "nothing leaves the machine without explicit permission", while the as-built routes `fast`, `smart`, `quality` and `frontier` to Groq and Gemini. The plans themselves also register cloud providers ([[universal-model-layer]], with "privacy-sensitive → local only"). The handoff does not say whether privacy-based routing to `local` is implemented. Left for the human to resolve.

## v2 identity notes

The "X" = unknown variable + tenth iteration + sovereign edition. Shelved alternate public names: SIRAJ (سراج, "the guiding light"), HORUS, NADIM.

## Definition of "finished v2.0"

One installer script → services up → web UI on phone & laptop → voice chat in chosen accent → 3 automations live → content pipeline has produced 10 published pieces → daily market brief arriving → [[constitutional-autonomy]] + audit log active.

## Related

[[jarvis-x-hardware]] | [[the-council]] | [[universal-model-layer]] | [[constitutional-autonomy]] | [[jarvis-x-voice-engine]] | [[jarvis-x-content-engine]] | [[jarvis-x-trading-module]] | [[jarvis-x-income-roadmap]] | [[self-improvement-loop]] | [[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[jarvis-x-app]] | [[starnet]] | [[jarvis-x-station-view]] | [[jarvis-x-plan-vs-reality]] | [[crostini]] | [[ipv6-dns-truncation-crostini]] | [[aider]] | [[free-api-tiers]] | [[source-jarvis-x-starnet-handoff]]
