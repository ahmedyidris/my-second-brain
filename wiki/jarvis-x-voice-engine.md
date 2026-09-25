---
title: Jarvis X Voice Engine
tags: [jarvis-x, voice, tts, stt, v2]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[jarvis-x-hardware]], [[jarvis-x-runtime]], [[crostini]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
---

# Jarvis X Voice Engine

The speech pipeline for [[jarvis-x]]. Two layers: an offline core (always works) and an online accent pack (free, needs internet).

## Offline core

| Component | Tool | Purpose |
|-----------|------|---------|
| STT | Faster-Whisper | Auto-detects EN/AR |
| TTS | Piper | Multiple voices, male & female |
| Wake word | Porcupine / openWakeWord | Hands-free activation |

```bash
pip install faster-whisper piper-tts pvporcupine
```

## Online accent pack (edge-tts, $0)

Microsoft neural voices via `edge-tts`:

| Language | Accents |
|----------|---------|
| English | American, British, Irish (en-IE), Australian, Indian |
| Arabic | Egyptian (ar-EG, m/f), formal MSA (ar-SA) |

Note: Scottish is thinnest in free TTS — nearest match via community Piper voices, flagged best-effort.

## Config

`voice:` block in `config.yaml`:
```yaml
accent: us|gb|ie|eg|msa
gender: m|f
engine: piper|edge
```

One command switches the entire manner of speech.

## Future (GPU box)

XTTS-class local voice cloning for a custom signature "Jarvis voice."

## ESP32-S3-BOX-3 satellite

Hardware satellite for room-based voice interaction. Configured via ESPHome with `hey_jarvis` wake word, noise suppression, and auto-gain.

## As-built (2026-09-24 handoff)

As of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]), the running deployment ([[jarvis-x-runtime]]) includes a `tts-worker` supervisord service, state **RUNNING (degraded)**.

| Item | State |
|------|-------|
| TTS engine | Chatterbox TTS |
| Model | Not installed |
| Worker | Starts, reports `{"loaded": false}` |
| `/synthesize` | Returns 500 |

The handoff (Bug D) calls this "intentional and honest — it refuses rather than returning silent audio."

### Fix (Bug D / Priority 4)

Obtain the chatterbox checkpoint (~5GB, `chatterbox-ckpt`). Place at `~/jarvis-x/voices/chatterbox-eg/`. Restart `tts-worker`.

The handoff gives no download source for the checkpoint and no restart command specific to `tts-worker`; the whole stack restarts with `sudo systemctl restart jarvis-supervisord.service` (see [[jarvis-x-runtime]]).

Implication: the handoff lists ~11GB free disk on the current machine, so a ~5GB checkpoint would use roughly half of it (see [[jarvis-x-hardware]] and [[crostini]]).

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan / DeepSeek Master Plan):** the plans specify Piper as the offline TTS (both plans) and edge-tts as the online accent pack (v2 plan). The running `tts-worker` in the handoff targets Chatterbox TTS. The handoff does not mention Piper, edge-tts, Faster-Whisper or a wake word, so it is unknown whether any of those are also wired in, or whether Chatterbox replaced Piper. The directory name `chatterbox-eg` is recorded as given; the handoff does not explain it. Left for the human to resolve.
