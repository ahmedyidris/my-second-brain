---
title: Jarvis X
tags: [jarvis-x, ai-os, sovereign, entity]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[the-council]], [[hermes-agent]], [[constitutional-autonomy]], [[jarvis-x-hardware]], [[universal-model-layer]], [[self-improvement-loop]], [[jarvis-x-app]], [[starnet]], [[ollama]], [[ipv6-dns-truncation-crostini]]
last_updated: 2026-09-24
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

## Current working state (2026-09-24)

Repo: https://github.com/ahmedyidris/jarvis-x, branch `master`. Latest commit `99652aa` — OpenAI-compatible `/v1/chat/completions` + `/v1/models` (see [[jarvis-x-app]]).

Services managed by `supervisord` under systemd unit `jarvis-supervisord.service`:

| Service | Status |
|---|---|
| hermes-agent | RUNNING |
| hermes-api (uvicorn, port 8000) | RUNNING |
| tts-worker | RUNNING — degraded, chatterbox model absent, `/synthesize` returns 500 |

Model tiers, all verified working via `POST /api/ask`:

| tier | provider | model |
|---|---|---|
| local | ollama | qwen2.5:3b |
| fast | groq | openai/gpt-oss-20b |
| smart | groq | openai/gpt-oss-120b |
| quality | gemini | gemini-3.6-flash |
| frontier | gemini | gemini-3.6-flash |

Note: `gemini-3.6-flash` does not appear in Google's models-list endpoint (stale listing) but works when called directly — do not "correct" it to a listed model.

**Hardware discrepancy flagged 2026-09-24:** [[jarvis-x-hardware]] describes the machine as a Lenovo Y50-70 running Pop!_OS. The 2026-09-24 handoff source describes the actual working environment as an ASUS Chromebook running Crostini (Debian 13 trixie) — 14GB RAM, 11th Gen i5, no GPU, 72GB disk. These are two different machines/environments. Not silently resolved — see the note in [[jarvis-x-hardware]] for detail. Treat the Crostini facts as current for day-to-day operational work as of this date.

Restart command:

```bash
sudo systemctl restart jarvis-supervisord.service
sleep 8
supervisorctl -c ~/jarvis-x/config/supervisord.conf status
```

Gotcha: systemd units don't inherit shell exports, so `jarvis-supervisord.service` needed an explicit `EnvironmentFile=/home/ahmedyidris/.jarvis-x/.env` drop-in (`/etc/systemd/system/jarvis-supervisord.service.d/env.conf`) plus `NODE_OPTIONS=--dns-result-order=ipv4first` — see [[ipv6-dns-truncation-crostini]].

A separate, parallel multi-agent platform, [[starnet]], is also under active development in this environment. Explicit direction: do not build StarNet out into a full Jarvis X clone — add a lighter "Station" view to Jarvis X's own frontend instead (see [[jarvis-x-app]]).

## v2 identity notes

The "X" = unknown variable + tenth iteration + sovereign edition. Shelved alternate public names: SIRAJ (سراج, "the guiding light"), HORUS, NADIM.

## Definition of "finished v2.0"

One installer script → services up → web UI on phone & laptop → voice chat in chosen accent → 3 automations live → content pipeline has produced 10 published pieces → daily market brief arriving → [[constitutional-autonomy]] + audit log active.

## Related

[[jarvis-x-hardware]] | [[the-council]] | [[universal-model-layer]] | [[constitutional-autonomy]] | [[jarvis-x-voice-engine]] | [[jarvis-x-content-engine]] | [[jarvis-x-trading-module]] | [[jarvis-x-income-roadmap]] | [[self-improvement-loop]]
