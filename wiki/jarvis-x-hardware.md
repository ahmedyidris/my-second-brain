---
title: Jarvis X Hardware
tags: [jarvis-x, hardware, chromebook, crostini, cpu-only, lenovo]
sources:
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[crostini]], [[ipv6-dns-truncation-crostini]], [[jarvis-x-model-priority]], [[ollama]], [[hermes-agent]], [[universal-model-layer]], [[jarvis-x-runtime]], [[starnet]], [[source-deepseek-jarvis-x-master-plan]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-25
---

# Jarvis X Hardware

Current body: an **ASUS Chromebook** running Linux under [[crostini]] (Debian 13 trixie). CPU-only, with no GPU.

> **Resolved by the human (2026-09-25):** "Current machine is chrome boo[k]." The July plans described a Lenovo Y50-70 on Pop!_OS, and the 2026-09-24 handoff described this Chromebook. The ruling settles which one is current. The Lenovo specs are kept below as the plans' record ("Earlier plan machine").

## Current machine (Chromebook)

From the handoff's PART 5 ("Environment facts"), as of 2026-09-24:

| Component | Spec |
|-----------|------|
| Hardware | ASUS Chromebook |
| OS | Crostini (Debian 13 trixie). See [[crostini]] |
| CPU | 11th Gen i5, no GPU |
| RAM | 14GB total, ~9–10GB free after Chrome |
| Disk | 72GB total, ~11GB free (after cleanup) |
| Python | 3.11 in `~/venv-ai` (uv-managed) |
| Node | 20.x (system), 22.x (bundled for Tauri) |

### What this machine means for models

- All local inference runs on the CPU. The handoff's StarNet agent Raqib runs `qwen2.5:7b` at "~10 tok/s", which it calls "slow". The Jarvis `local` tier runs `qwen2.5:3b`.
- The human's priority for plans puts local models and free open-source tiers that "could work on any machine specially chrome os" first. See [[jarvis-x-model-priority]] for the ladder, and [[ollama]] for which local models fit this machine.
- The cloud tiers run off the machine, on [[groq]] and [[gemini]]. See [[universal-model-layer]].

### Resource gotchas (from the handoff)

- **Chrome RAM (gotcha 7):** "Chrome tabs eat 10GB of your 14GB. Before any heavy build, close them. free -h should show 6GB+ available."
- **Tauri build (gotcha 8):** "The Tauri build is 30-60 min and needs 8GB disk + 6GB RAM. It's rebuildable but not useful for daily work on this hardware." PART 8: "Do not build the Tauri desktop shell for daily use. Web UI is faster and identical in function." See [[starnet]] and [[jarvis-x-app]].
- **Disk:** ~11GB free after cleanup. The Ollama models present add up to about 13.5GB (arithmetic; see [[ollama]]). The Chatterbox checkpoint for the voice pipeline is ~5GB (Bug D, [[jarvis-x-voice-engine]]). Implication: every new local model has to fit in that ~11GB.
- **Networking:** Crostini's IPv6-first resolution truncates POST bodies to Cloudflare-fronted APIs. See [[crostini]] and [[ipv6-dns-truncation-crostini]].

See [[crostini]] for one inconsistency inside the handoff: "~9-10GB free after Chrome" vs "Chrome tabs eat 10GB of your 14GB". For what runs on this machine, see [[jarvis-x-runtime]].

## Earlier plan machine (Lenovo Y50-70)

This is how the July master plan described the body. It is kept as the plans' record; the 2026-09-25 ruling makes the Chromebook current. The ruling doesn't say what happened to the Lenovo.

| Component | Spec | Status (per the master plan) |
|-----------|------|--------|
| CPU | Intel i7-4710HQ (4C/8T, Haswell) | Active |
| GPU | NVIDIA GTX 860M (2GB) | Currently undetected |
| RAM | 7.7 GB DDR3L | Must upgrade to 16GB |
| Storage | 953 GB SATA SSD | Active |
| OS | Pop!_OS 24.04 LTS | Active |

### The plan's CPU-only model strategy (Lenovo)

Since the GPU was undetected, the plan ran all inference on the CPU. That constraint shaped the [[universal-model-layer]] tier selection: privacy-sensitive and interactive queries use the `local` tier.

| Model | Size | Speed (per the plan) |
|-------|------|-------|
| llama3.2:3b | ~2GB | 8–12 t/s (good) |
| qwen3:1.5b | ~1GB | 15–20 t/s (fast) |
| nomic-embed-text | ~0.5GB | Fast |
| hermes3:8b | ~5.5GB | 1–3 t/s (slow) |

The Chromebook runs a different set: the `qwen2.5` family plus `nomic-embed-text` ([[ollama]]).

### The plan's upgrade roadmap (Lenovo)

| Phase | Upgrade | Cost | Priority |
|-------|---------|------|----------|
| 1 | 16GB DDR3L RAM + 2TB SSD | ~$125 | High |
| 2 | ADT-Link R43SG eGPU + 850W PSU | ~$135 | Medium |
| 3 | NVIDIA RTX 3090 (24GB VRAM) | ~$440 | Future |

This roadmap was written for the Lenovo. Neither the handoff nor the ruling says whether any of it still applies now that the Chromebook is current. Open question for the human.

### GPU fix commands (Lenovo only)

```bash
sudo prime-select nvidia   # force NVIDIA
sudo prime-select intel    # fallback if black screen
```

These target the Lenovo's NVIDIA GPU under Pop!_OS. The Chromebook has "no GPU", so they don't apply to it.

### Side by side

| | Earlier plan (Lenovo) | Current (Chromebook) |
|---|---|---|
| Machine | Lenovo Y50-70 | ASUS Chromebook |
| OS | Pop!_OS 24.04 LTS | Crostini (Debian 13 trixie) |
| CPU | Intel i7-4710HQ (4C/8T, Haswell) | 11th Gen i5 |
| GPU | NVIDIA GTX 860M (2GB), undetected | no GPU |
| RAM | 7.7 GB DDR3L | 14GB |
| Storage | 953 GB SATA SSD | 72GB, ~11GB free |

**What still holds:** local inference is CPU-only on both.

## Related

[[jarvis-x]] | [[crostini]] | [[ipv6-dns-truncation-crostini]] | [[jarvis-x-model-priority]] | [[ollama]] | [[hermes-agent]] | [[universal-model-layer]] | [[jarvis-x-runtime]] | [[starnet]] | [[source-deepseek-jarvis-x-master-plan]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
