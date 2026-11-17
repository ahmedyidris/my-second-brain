---
title: Universal Model Layer
tags: [jarvis-x, v2, architecture, models]
sources:
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[the-council]]
last_updated: 2026-07-27
---

# Universal Model Layer

A v2 addition to [[jarvis-x]]. One `providers/` interface, one config — every model provider behind a single abstraction with hot-swapping and free-tier fallbacks.

## CLI usage

```bash
jj ask "..." --tier local|fast|smart|long
```

## Registered providers

| Provider | Tier | Notes |
|----------|------|-------|
| Ollama (local) | local | Privacy-sensitive queries only |
| Gemini CLI/API | long | 1M+ context |
| Groq | fast | Fast inference loops |
| OpenRouter | fast | 28+ free models (DeepSeek, Llama) |
| Anthropic | smart | While sub lives, then optional API |
| NVIDIA NIM | fast | Free tier |
| Mistral | fast | Free tier |

## Router rules

- Privacy-sensitive → local only
- Long-context → Gemini
- Fast loops → Groq
- Fallback chain on quota errors
- Per-provider daily counters in SQLite

## Key constraint

Every provider is optional. [[jarvis-x]] must boot and function with zero cloud keys.
