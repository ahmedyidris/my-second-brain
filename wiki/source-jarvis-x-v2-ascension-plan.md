---
title: Source — Jarvis X v2 Ascension Plan
tags: [source, jarvis-x, v2]
sources:
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x]], [[universal-model-layer]], [[constitutional-autonomy]], [[jarvis-x-voice-engine]], [[jarvis-x-content-engine]], [[source-deepseek-jarvis-x-master-plan]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-runtime]], [[jarvis-x-app]], [[crostini]], [[free-api-tiers]], [[starnet]]
last_updated: 2026-09-25
---

# Source — Jarvis X v2 Ascension Plan

The v2 update to [[jarvis-x]]. Overrides [[source-deepseek-jarvis-x-master-plan]] where they conflict. Constraints: CPU-only Lenovo Y50-70, $0/month budget, 6–10 hrs/wk, Egypt/Payoneer, income-first 60/40.

## Key v2 changes over v1

| Area | v1 | v2 |
|------|----|----|
| Models | Ollama + Gemini/Groq | [[universal-model-layer]] — all providers, hot-swap |
| Platform | Pop!_OS only | Linux → Windows → PWA → macOS |
| Voice | Whisper + Piper scripts | Multi-accent [[jarvis-x-voice-engine]] |
| Autonomy | Approval gates | [[constitutional-autonomy]] |
| Income | Outlier + n8n gigs | + [[jarvis-x-content-engine]] as stream #3 |
| Trading | Excluded | [[jarvis-x-trading-module]] (testnet/paper) |
| Delivery | Scripts + CLI | The JARVIS X App (FastAPI + PWA + Tauri) |

## 12-week overlay

- Wk 1–2: extraction sprint + income + register handles
- Wk 3–4: [[universal-model-layer]] + [[constitutional-autonomy]] skeleton (while Claude sub lives)
- Wk 5–6: [[jarvis-x-voice-engine]] with accent config; PWA shell
- Wk 7–8: [[jarvis-x-content-engine]] v1 → first 5 bilingual pieces; Windows run-through
- Wk 9–10: [[jarvis-x-trading-module]] (testnet + daily brief)
- Wk 11–12: brand kit, installer, docs → tag v2.0

## Execute prompt

> JARVIS X Ascension — execute. Read the Unified Master Blueprint and the v2 Ascension Plan; v2 overrides v1 where they conflict, and constraints (CPU-only Y50-70, $0/month, 6–10 hrs/wk, Egypt/Payoneer, income-first 60/40) still bind everything.

## Later sources

[[source-jarvis-x-starnet-handoff]] (dated 2026-09-24) reports the as-built state of [[jarvis-x]]. It differs from this plan in several places. The full area-by-area comparison is in [[jarvis-x-plan-vs-reality]]. Examples, as of the 2026-09-24 handoff:

- **Hardware:** the plan's constraint is "CPU-only Y50-70". The handoff's machine is an ASUS Chromebook running Crostini (Debian 13 trixie), with an 11th Gen i5 and no GPU ([[crostini]]). It is still CPU-only.
- **Model layer (§3):** the plan has `jj ask "..." --tier local|fast|smart|long`. As built, the tiers are `local | fast | smart | quality | frontier`, served by Ollama, Groq and Gemini and verified via `POST /api/ask` ([[jarvis-x-runtime]], [[universal-model-layer]]).
- **Services (§5):** the plan has `jarvis-core`, `jarvis-scheduler` and `jarvis-voice` running under Jarvis's own Linux user in `~/jarvis/`. As built, supervisord runs `hermes-agent`, `hermes-api` and `tts-worker` under the systemd unit `jarvis-supervisord.service`, with the source in `~/jarvis-x` ([[constitutional-autonomy]]).
- **App (§8):** the plan wraps the web UI with Tauri "later for Windows/macOS desktop builds". The handoff says "Do not build the Tauri desktop shell for daily use. Web UI is faster and identical in function." But the only Tauri shell the handoff records is StarNet's (built, then deleted), so it doesn't say whether this rule covers a Jarvis Tauri wrapper, or a build for distribution rather than daily use ([[jarvis-x-app]], [[starnet]]).
- **Subscriptions:** the plan uses Claude/Gemini "while subs live". The handoff reports that consumer AI subscriptions don't give API access (Bug E) ([[free-api-tiers]]).

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan's binding constraints (§10) name a "CPU-only Y50-70", and the same §10 prompt asks for scripts "for a fresh Pop!_OS terminal". The handoff's machine is an ASUS Chromebook running Crostini (Debian 13 trixie). The handoff doesn't say whether the Y50-70 was retired or is still the target.

> **Resolved by the human (2026-09-25):** the Chromebook is the current machine ("Current machine is chrome boo[k]"). See [[jarvis-x-hardware]]. The plan's other constraints ($0/month, 6–10 hrs/wk, Egypt/Payoneer, income-first 60/40) are not affected by the ruling.
