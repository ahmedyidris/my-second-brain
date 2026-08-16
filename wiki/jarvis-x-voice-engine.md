---
title: Jarvis X Voice Engine
tags: [jarvis-x, voice, tts, stt, v2]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - https://github.com/SYSTRAN/faster-whisper (accessed 2026-08-16)
  - https://github.com/rhasspy/piper (accessed 2026-08-16)
  - https://github.com/OHF-Voice/piper1-gpl (accessed 2026-08-16)
  - https://github.com/Picovoice/porcupine (accessed 2026-08-16)
  - https://picovoice.ai/docs/faq/porcupine/ (accessed 2026-08-16)
  - https://github.com/dscripka/openWakeWord (accessed 2026-08-16)
related: [[jarvis-x]], [[jarvis-x-hardware]], [[constitutional-autonomy]]
last_updated: 2026-08-16
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

### Component depth (added 2026-08-16 heal pass — was a data-gap, all four rows were single-line stubs)

**Faster-Whisper** — reimplementation of OpenAI Whisper on CTranslate2 (a fast Transformer inference engine): up to 4× faster than `openai/whisper` at equal accuracy, using less memory; 8-bit quantization on CPU and GPU for further speedup. MIT-licensed, actively maintained at `github.com/SYSTRAN/faster-whisper`. `pip install faster-whisper` — no FFmpeg dependency, unlike stock Whisper.

**Piper — ⚠️ stale claim corrected.** This page previously cited Piper as if it were an actively-maintained MIT project at `github.com/rhasspy/piper`. As of this pass (checked 2026-08-16): **that repo was archived on 2025-10-06** (now read-only) — development has moved to **`github.com/OHF-Voice/piper1-gpl`**, now stewarded by the Open Home Foundation. Two consequences worth flagging explicitly (never silently resolving a contradiction, per this vault's guardrails):
1. **License changed: MIT → GPL-3.0.** Anything in Jarvis X that bundles or links against the new `piper1-gpl` package inherits GPL-3.0 obligations — worth checking against [[jarvis-x]]'s "every component is free and auditable" principle before shipping a packaged build.
2. Still a fast, fully local, ONNX/VITS-based neural TTS system (unchanged architecture); still installs via `pip install piper-tts`; still used in Home Assistant, NVDA, and embedded targets. The rename/governance change doesn't affect offline capability.
3. The Open Home Foundation's own repo notes it is actively **looking for maintainers** — worth a periodic re-check, not a one-time fact.

**Wake word: Porcupine vs openWakeWord — a real contradiction with [[jarvis-x]]'s sovereignty principles.** These two options were listed as interchangeable ("Porcupine / openWakeWord") with no distinction. They are not equivalent:
- **Porcupine** (Picovoice, Apache-2.0 SDK + bundled models) requires a **Picovoice AccessKey** obtained from an online console, and versions since 2.0 need periodic contact with Picovoice's servers to activate/validate that key. Inference itself runs on-device, but the activation step is an online, third-party-account dependency.
- **openWakeWord** (`github.com/dscripka/openWakeWord`, Apache-2.0) needs **no account, no key, no phone-home** — fully self-contained, pre-trained models ship with the repo.

[[jarvis-x]]'s stated sovereignty principles include "Zero-subscription — must boot and function with zero cloud keys" and this page's own framing of the offline core as "always works." Porcupine's AccessKey requirement is in tension with both. **Recommendation, not yet a human decision:** default to openWakeWord for the zero-cloud-key build; treat Porcupine as an optional convenience layer only if the human explicitly accepts the Picovoice account dependency. This is flagged, not silently fixed — the actual engine choice is a human call.

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
