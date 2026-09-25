---
title: Jarvis X Hardware
tags: [jarvis-x, hardware, lenovo, chromebook, crostini, cpu-only, contradiction]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[hermes-agent]], [[crostini]], [[ipv6-dns-truncation-crostini]], [[ollama]], [[universal-model-layer]], [[jarvis-x-runtime]], [[starnet]], [[source-deepseek-jarvis-x-master-plan]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
---

# Jarvis X Hardware

Current body: **Lenovo Y50-70** running Pop!_OS 24.04 LTS.

That line is the July 2026 master plan's description. The 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]) describes a different machine: an ASUS Chromebook running [[crostini]]. See "Machine in the 2026-09-24 handoff" below.

> **Disagreement (2026-09-24 handoff vs DeepSeek Jarvis X Master Plan and Jarvis X v2 Ascension Plan):** the earlier plans describe a **Lenovo Y50-70 on Pop!_OS 24.04 LTS** (i7-4710HQ, 7.7GB RAM, 953GB SSD). The v2 plan's execution prompt still assumes a "CPU-only Y50-70" and "a fresh Pop!_OS terminal". The 2026-09-24 handoff describes an **ASUS Chromebook running Crostini (Debian 13 trixie)** (11th Gen i5, no GPU, 14GB RAM, 72GB disk). The wiki does not know whether the Lenovo was replaced, retired, or is a second machine. The handoff doesn't mention it. Both descriptions are kept. Left for the human to resolve.

> **Working assumption until the human decides (interpretation, not a resolution):** for day-to-day operational work, use the Chromebook/Crostini facts, because they come from a live operational handoff rather than a plan document. The Lenovo specs below stay as the plans' record.

## Current specs

The Lenovo Y50-70, from the July 2026 master plan.

| Component | Spec | Status |
|-----------|------|--------|
| CPU | Intel i7-4710HQ (4C/8T, Haswell) | Active |
| GPU | NVIDIA GTX 860M (2GB) | Currently undetected |
| RAM | 7.7 GB DDR3L | Must upgrade to 16GB |
| Storage | 953 GB SATA SSD | Active |
| OS | Pop!_OS 24.04 LTS | Active |

## CPU-only model strategy

Since GPU is undetected, all inference runs on CPU. This constraint directly shapes the [[universal-model-layer]] tier selection — privacy-sensitive and interactive queries must use the `local` tier:

| Model | Size | Speed |
|-------|------|-------|
| llama3.2:3b | ~2GB | 8–12 t/s (good) |
| qwen3:1.5b | ~1GB | 15–20 t/s (fast) |
| nomic-embed-text | ~0.5GB | Fast |
| hermes3:8b | ~5.5GB | 1–3 t/s (slow) |

The models on the handoff's machine are different: the `qwen2.5` family plus `nomic-embed-text`. See [[ollama]].

## Upgrade roadmap

| Phase | Upgrade | Cost | Priority |
|-------|---------|------|----------|
| 1 | 16GB DDR3L RAM + 2TB SSD | ~$125 | High |
| 2 | ADT-Link R43SG eGPU + 850W PSU | ~$135 | Medium |
| 3 | NVIDIA RTX 3090 (24GB VRAM) | ~$440 | Future |

The handoff says nothing about this roadmap. Its status is unknown.

## GPU fix commands

```bash
sudo prime-select nvidia   # force NVIDIA
sudo prime-select intel    # fallback if black screen
```

Implication: these commands target the Lenovo's NVIDIA GPU under Pop!_OS. The handoff's machine has "no GPU", so they don't apply there.

## Machine in the 2026-09-24 handoff

From PART 5 ("Environment facts"), as of the 2026-09-24 handoff:

| Component | Spec |
|-----------|------|
| Hardware | ASUS Chromebook |
| OS | Crostini (Debian 13 trixie) — see [[crostini]] |
| RAM | 14GB total, ~9-10GB free after Chrome |
| CPU | 11th Gen i5, no GPU |
| Disk | 72GB total, ~11GB free (after cleanup) |
| Python | 3.11 in `~/venv-ai` (uv-managed) |
| Node | 20.x (system), 22.x (bundled for Tauri) |

### Side by side

| | Earlier plans | 2026-09-24 handoff |
|---|---|---|
| Machine | Lenovo Y50-70 | ASUS Chromebook |
| OS | Pop!_OS 24.04 LTS | Crostini (Debian 13 trixie) |
| CPU | Intel i7-4710HQ (4C/8T, Haswell) | 11th Gen i5 |
| GPU | NVIDIA GTX 860M (2GB), undetected | no GPU |
| RAM | 7.7 GB DDR3L | 14GB |
| Storage | 953 GB SATA SSD | 72GB, ~11GB free |

**What still holds:** local inference is CPU-only on both machines. (The cloud tiers on Groq and Gemini run off the machine; see [[universal-model-layer]].) The Lenovo is CPU-only because its GPU is undetected. The Chromebook has no GPU. The local [[ollama]] tier on the Chromebook runs `qwen2.5:3b`. StarNet's Raqib runs `qwen2.5:7b` at "~10 tok/s", which the handoff calls "slow".

### Resource gotchas (from the handoff)

- **Chrome RAM (gotcha 7):** "Chrome tabs eat 10GB of your 14GB. Before any heavy build, close them. free -h should show 6GB+ available."
- **Tauri build (gotcha 8):** "The Tauri build is 30-60 min and needs 8GB disk + 6GB RAM. It's rebuildable but not useful for daily work on this hardware." PART 8: "Do not build the Tauri desktop shell for daily use. Web UI is faster and identical in function." See [[starnet]].
- **Disk:** ~11GB free after cleanup. The Ollama models present add up to about 13.5GB (arithmetic, see [[ollama]]). The chatterbox checkpoint for the voice pipeline is ~5GB (Bug D).
- **Networking:** Crostini's IPv6-first resolution truncates POST bodies to Cloudflare-fronted APIs. See [[crostini]] and [[ipv6-dns-truncation-crostini]].

See [[crostini]] for one inconsistency inside the handoff: "~9-10GB free after Chrome" vs "Chrome tabs eat 10GB of your 14GB". For what runs on this machine, see [[jarvis-x-runtime]].

## Related

[[jarvis-x]] | [[hermes-agent]] | [[crostini]] | [[ipv6-dns-truncation-crostini]] | [[ollama]] | [[universal-model-layer]] | [[jarvis-x-runtime]] | [[starnet]] | [[source-deepseek-jarvis-x-master-plan]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
