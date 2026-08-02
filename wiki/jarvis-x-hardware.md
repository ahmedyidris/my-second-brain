---
title: Jarvis X Hardware
tags: [jarvis-x, hardware, lenovo, cpu-only]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[hermes-agent]], [[ollama]]
last_updated: 2026-07-27
---

# Jarvis X Hardware

Current body: **Lenovo Y50-70** running Pop!_OS 24.04 LTS.

## Current specs

| Component | Spec | Status |
|-----------|------|--------|
| CPU | Intel i7-4710HQ (4C/8T, Haswell) | Active |
| GPU | NVIDIA GTX 860M (2GB) | Currently undetected |
| RAM | 7.7 GB DDR3L | Must upgrade to 16GB |
| Storage | 953 GB SATA SSD | Active |
| OS | Pop!_OS 24.04 LTS | Active |

## CPU-only model strategy

Since GPU is undetected, all inference runs on CPU. This constraint directly shapes the [[universal-model-layer]] tier selection — privacy-sensitive and interactive queries must use the `local` tier, served via [[ollama]]:

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
