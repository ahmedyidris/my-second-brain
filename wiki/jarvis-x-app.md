---
title: Jarvis X App
tags: [jarvis-x, v2, delivery, pwa, app]
sources:
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[jarvis-x-hardware]], [[universal-model-layer]], [[constitutional-autonomy]]
last_updated: 2026-08-16
---

# Jarvis X App

The v2 delivery architecture for [[jarvis-x]]: one branded product that runs on Linux, Windows, iPhone, Android, and eventually macOS — all from a single codebase.

## Architecture

- **Backend:** FastAPI daemon (already the core service)
- **Frontend:** web UI served locally → installable as a **PWA** on any device
- **Desktop (later):** same UI wrapped with **Tauri** for Windows/macOS native builds

## Platform rollout order

| Order | Platform | Why |
|-------|----------|-----|
| ① | Linux (Pop!_OS) | Native, already running |
| ② | Windows | Biggest client market for AI gigs |
| ③ | PWA (iOS + Android) | Covers mobile at $0 — no Apple developer fee needed |
| ④ | macOS / native iOS | After GPU box + revenue; needs Mac hardware + $99/yr |

## Brand kit (self-generated)

- **Name:** JARVIS X
- **Mark:** arc-reactor ring forming the letter X
- **Palette:** obsidian black + arc gold (Gothic-Arcane doctrine)
- **Voice:** calm, precise, bilingual (EN + AR)

JARVIS X generates its own brand assets as one of its first [[jarvis-x-content-engine]] jobs — *the system literally brands itself.*

## Definition of done (v2.0)

One installer script → services up → web UI on phone & laptop → voice chat in chosen accent → 3 automations live → content pipeline has produced 10 published pieces → daily market brief arriving → [[constitutional-autonomy]] + audit log active.

## Timeline

Built in Wk 5–6 of the 12-week overlay: PWA-ready web UI shell after voice engine.

**Correction (2026-08-16 heal pass):** this page previously said "Tauri Windows build in Wk 7–8," which overstated the raw source. Re-reading `raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md` directly: Wk 7–8 is "[[jarvis-x-content-engine]] v1 → first 5 bilingual pieces; **Windows run-through**" (a test pass on Windows, not necessarily a packaged Tauri build), and the installer itself doesn't land until **Wk 11–12** ("brand kit, installer, docs → tag v2.0"), per [[source-jarvis-x-v2-ascension-plan]]'s 12-week overlay. Flagged as a possible stale claim needing a raw-source re-read by a prior (unmerged) heal pass; resolved here directly from the raw source.
