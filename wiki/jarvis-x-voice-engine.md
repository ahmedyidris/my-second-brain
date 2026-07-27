---
title: Jarvis X Voice Engine
tags: [jarvis-x, voice, tts, stt, v2]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[jarvis-x-hardware]]
last_updated: 2026-07-27
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
