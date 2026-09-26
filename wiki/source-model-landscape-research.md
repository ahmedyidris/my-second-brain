---
title: Source — Model Landscape Research
tags: [source, research, models, providers, free-tiers, chromebook]
sources:
  - raw/2026-09-25-model-landscape-research.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
related: [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[ollama]], [[groq]], [[gemini]], [[openrouter]], [[free-api-tiers]], [[the-council]], [[jarvis-x-hardware]]
last_updated: 2026-09-25
---

# Source — Model Landscape Research

Web research done on 2026-09-25 to fill in the human's model-priority ruling ([[jarvis-x-model-priority]]) with concrete options. It asks which models and free tiers work for [[jarvis-x]] on the current machine: a CPU-only Chromebook with 14GB RAM, of which Chrome uses ~10GB, and ~11GB free disk ([[jarvis-x-hardware]]). The vault copy is `raw/2026-09-25-model-landscape-research.md`.

## How far to trust it

- **Written by a research subagent, not the human.** It is a snapshot of pages as of 2026-09-25, and model catalogues change monthly.
- **Most primary pages could not be fetched.** The network proxy blocked ollama.com, console.groq.com, ai.google.dev, openrouter.ai, openai.com and platform.kimi.ai. Only GitHub, claude.com and platform.claude.com were read directly.
- Each fact is tagged **[F]** (fetched and read) or **[S]** (from a search-result excerpt for that exact URL, medium confidence). Wiki pages carry the distinction forward with an asterisk or a note.
- The "recommended local-first stack" in the note is the researcher's inference, not a fact.

## Key findings

| Topic | Finding | Confidence | Page |
|-------|---------|------------|------|
| Local Chinese open models that fit | qwen3 0.6b–8b (8b at 5.2GB), qwen3.5 up to 4b, qwen3-vl 2b/4b, qwen2.5 / qwen2.5-coder up to 7b, deepseek-r1 1.5b–8b, glm4:9b (5.5GB, borderline), minicpm-v 8b (borderline) | [S] | [[chinese-open-source-models]], [[ollama]] |
| Too big or cloud-only | qwen3.6 / 3.8 / qwen3-coder (18GB and up), glm-4.7-flash, all Kimi, MiniMax, DeepSeek-V4 and GLM-5 models | [S] | [[chinese-open-source-models]] |
| Google open models that fit | gemma3 1b/4b, gemma4:e2b-it-qat (4.3GB) | [S] | [[ollama]], [[gemini]] |
| OpenAI open-weight | gpt-oss:20b is a 14GB download and doesn't fit locally; it's free hosted on Groq | [S] | [[groq]] |
| Groq free tier | gpt-oss-20b/120b still listed; qwen3.8-27b listed; Kimi K2 deprecated (Mar 2026); gpt-oss-120b free limits 30 RPM / 1K RPD / 8K TPM / 200K TPD | [F] limits via a GitHub issue; rest [S] | [[groq]], [[free-api-tiers]] |
| OpenRouter free | `:free` variants for DeepSeek, Qwen, Kimi, GLM, MiniMax, Gemma, gpt-oss (live availability unverified); 50 requests/day, or 1,000/day after a one-time $10 | [S] | [[openrouter]] |
| Google free | Gemini API free tier; gemini-3.6-flash listed and GA; newer 3.7 / 3.8 Flash; Gemini CLI 1,000 requests/day with Google login | CLI [F]; rest [S] | [[gemini]] |
| Kimi | API paid ("no permanent Kimi API free tier"); K2.6 $0.95 / $4.00 per 1M; open weights (K2 Modified MIT, K3 license) but far too big for local | licenses [F]; pricing [S] | [[jarvis-x-model-priority]] |
| Anthropic | No ongoing free API tier; small free credits for new users; Haiku 4.5 $1 / $5, Sonnet 5 $2 / $10 per MTok | [F] | [[jarvis-x-model-priority]] |
| OpenAI | Pricing page blocked; a "Free" usage tier exists, but its models are unverified | [S] | [[jarvis-x-model-priority]] |

## What it could not verify

Everything on the blocked sites beyond search excerpts; the Ollama cloud free starter-model list and Pro/Max prices; Groq's Qwen free limits; whether each OpenRouter `:free` model is live; whether Gemini 3.8 Flash and 3.1 Pro have a free tier (excerpts conflict); the Gemini CLI API-key quota (1,000/day in the README vs 250/day, Flash only, in the quota doc); OpenAI prices. Some Ollama sizes (the Gemma 4 e2b/e4b builds) look odd; check them with `ollama show` before pulling.

## Related

[[jarvis-x-model-priority]] | [[chinese-open-source-models]] | [[ollama]] | [[groq]] | [[gemini]] | [[openrouter]] | [[free-api-tiers]] | [[the-council]] | [[jarvis-x-hardware]]
