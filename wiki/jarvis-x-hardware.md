---
title: Jarvis X Hardware
tags: [jarvis-x, hardware, lenovo, cpu-only, contradiction]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x]], [[hermes-agent]], [[ipv6-dns-truncation-crostini]]
last_updated: 2026-09-24
---

# Jarvis X Hardware

Current body: **Lenovo Y50-70** running Pop!_OS 24.04 LTS.

> **⚠ Unresolved contradiction (flagged 2026-09-24):** the 2026-09-24 technical handoff source (`raw/2026-09-24-jarvis-x-starnet-handoff.md`) describes the actual working environment for both [[jarvis-x]] and [[starnet]] as an **ASUS Chromebook, Crostini (Debian 13 trixie)** — 14GB RAM total (~9–10GB free after Chrome), 11th Gen i5 CPU, **no GPU**, 72GB disk (~11GB free after cleanup). This directly contradicts the Lenovo Y50-70 / Pop!_OS / GTX 860M specs below, sourced from the earlier DeepSeek master plan (2026-07-27). Per this wiki's guardrails, this is **not silently resolved** — the two sources may describe different physical machines (a later migration), or one source may be stale/aspirational. Flagging for the human to confirm which machine is current. Until confirmed, treat the Crostini facts (see below) as the ones matching *actual observed service behavior* as of 2026-09-24, since they come from a live operational handoff rather than a plan document.

## Environment observed 2026-09-24 (Crostini)

| Component | Spec |
|-----------|------|
| Hardware | ASUS Chromebook |
| Container | Crostini (Debian 13 trixie) |
| CPU | 11th Gen Intel i5, no GPU |
| RAM | 14GB total, ~9–10GB free after Chrome |
| Disk | 72GB total, ~11GB free after cleanup |
| Python | 3.11 in `~/venv-ai` (uv-managed) |
| Node | 20.x system, 22.x bundled for Tauri |

Practical implication: Chrome tabs alone can eat ~10GB of the 14GB total. Close them before any heavy build; `free -h` should show 6GB+ available first. The Tauri build (30–60 min, needs 8GB disk + 6GB RAM) is rebuildable but was judged not worth it for daily use on this hardware — see [[jarvis-x-app]] and [[starnet]].

Networking quirk specific to this Crostini environment: see [[ipv6-dns-truncation-crostini]].

## Current specs

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

## Upgrade roadmap

| Phase | Upgrade | Cost | Priority |
|-------|---------|------|----------|
| 1 | 16GB DDR3L RAM + 2TB SSD | ~$125 | High |
| 2 | ADT-Link R43SG eGPU + 850W PSU | ~$135 | Medium |
| 3 | NVIDIA RTX 3090 (24GB VRAM) | ~$440 | Future |

## GPU fix commands

```bash
sudo prime-select nvidia   # force NVIDIA
sudo prime-select intel    # fallback if black screen
```
