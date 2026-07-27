---
title: Jarvis X App
tags: [jarvis-x, v2, delivery, pwa, app]
sources:
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[jarvis-x-hardware]], [[universal-model-layer]], [[constitutional-autonomy]]
last_updated: 2026-07-27
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

Built in Wk 5–6 of the 12-week overlay: PWA-ready web UI shell after voice engine. Tauri Windows build in Wk 7–8.
