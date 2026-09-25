---
title: Jarvis X
tags: [jarvis-x, ai-os, sovereign, entity]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[the-council]], [[hermes-agent]], [[constitutional-autonomy]], [[jarvis-x-hardware]], [[universal-model-layer]], [[self-improvement-loop]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[jarvis-x-app]], [[starnet]], [[jarvis-x-station-view]], [[jarvis-x-plan-vs-reality]], [[source-jarvis-x-starnet-handoff]], [[free-api-tiers]], [[crostini]], [[aider]], [[ollama]], [[groq]], [[gemini]]
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

## v2 identity notes

The "X" = unknown variable + tenth iteration + sovereign edition. Shelved alternate public names: SIRAJ (سراج, "the guiding light"), HORUS, NADIM.

## Definition of "finished v2.0"

One installer script → services up → web UI on phone & laptop → voice chat in chosen accent → 3 automations live → content pipeline has produced 10 published pieces → daily market brief arriving → [[constitutional-autonomy]] + audit log active.

## Build state (2026-09-24 handoff)

What actually exists, as of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]). Full detail on [[jarvis-x-runtime]].

- **Repo:** https://github.com/ahmedyidris/jarvis-x (branch `master`), checked out at `~/jarvis-x`. Latest commit `99652aa` — feat(api): OpenAI-compatible /v1/chat/completions + /v1/models.
- **Running:** supervisord (under systemd unit `jarvis-supervisord.service`) runs `hermes-agent`, `hermes-api` (uvicorn, port 8000) and `tts-worker` (degraded — Chatterbox model absent; see [[jarvis-x-voice-engine]]).
- **Machine:** ASUS Chromebook, Crostini (Debian 13 trixie) — see [[crostini]] and [[jarvis-x-hardware]].
- **Model tiers:** `local` on [[ollama]] (`qwen2.5:3b`), `fast`/`smart` on [[groq]], `quality`/`frontier` on [[gemini]] — all verified via `POST /api/ask`. See [[jarvis-x-runtime]] and [[universal-model-layer]].
- **API:** an OpenAI-compatible adapter at `http://127.0.0.1:8000/v1` — [[jarvis-x-openai-compatible-api]].
- **Multi-agent:** a separate app, [[starnet]], is being run alongside Jarvis; the handoff recommends a "Station" tab inside Jarvis instead of a StarNet clone — [[jarvis-x-station-view]].
- **Coding agent:** [[aider]], launched from `~/jarvis-x` with `aider --model groq/openai/gpt-oss-120b --no-show-model-warnings`.
- **Plan vs as-built:** [[jarvis-x-plan-vs-reality]].

Cloud tiers on Groq and Gemini are in active use alongside the local Ollama tier. Their models (`openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `gemini-3.6-flash`) are the ones the handoff lists under free API access (Bug E; see [[free-api-tiers]]). The handoff does not say whether the system boots and functions with zero cloud keys (the "Zero-subscription" principle above), and reports no test of it.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan / DeepSeek Master Plan):** this page's sovereignty principles (above, drawn from the plans) say "all models, data, logic run on your hardware" and "nothing leaves the machine without explicit permission", while the as-built routes `fast`, `smart`, `quality` and `frontier` to Groq and Gemini. The plans themselves also register cloud providers ([[universal-model-layer]], with "privacy-sensitive → local only"). The handoff does not say whether privacy-based routing to `local` is implemented. Left for the human to resolve.

## Related

[[jarvis-x-hardware]] | [[the-council]] | [[universal-model-layer]] | [[constitutional-autonomy]] | [[jarvis-x-voice-engine]] | [[jarvis-x-content-engine]] | [[jarvis-x-trading-module]] | [[jarvis-x-income-roadmap]] | [[self-improvement-loop]] | [[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[jarvis-x-app]] | [[starnet]] | [[jarvis-x-station-view]] | [[jarvis-x-plan-vs-reality]] | [[crostini]] | [[aider]] | [[free-api-tiers]] | [[source-jarvis-x-starnet-handoff]]
