---
title: Jarvis X Model Priority
tags: [jarvis-x, models, providers, ruling, local-first, chromebook]
sources:
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[universal-model-layer]], [[free-api-tiers]], [[ollama]], [[groq]], [[gemini]], [[openrouter]], [[the-council]], [[jarvis-x-hardware]], [[crostini]], [[jarvis-x]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-25
---

# Jarvis X Model Priority

The human's ruling, from 2026-09-25, on which models and providers [[jarvis-x]] plans should reach for first. It sits on top of the [[universal-model-layer]]: the layer says how providers plug in, and this page says in what order to prefer them.

## The ruling (verbatim)

> "priority for plans, local models and free open source tiers that could work on any machine specially chrome os, then most free available from google then Anthropic then open ai, if kimi is not free treat as a paid subscription and put in paid tiers slot but also include top tier Chinese open source models in local first, ollama…."

Source: `raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md`.

## The ladder

| Priority | Slot | What goes here |
|----------|------|----------------|
| 1 | **Local and free open-source** | Local models on [[ollama]] and free open-source tiers that "could work on any machine specially chrome os". This slot explicitly includes "top tier Chinese open source models" via Ollama. |
| 2 | **Google, free** | "the most free available from google" |
| 3 | **Anthropic** | Anthropic models |
| 4 | **OpenAI** | OpenAI models |
| Paid | **Paid subscriptions** | Kimi, "if kimi is not free" |

The ruling ranks Anthropic above OpenAI, but it doesn't say where Kimi sits relative to them inside the paid group. Open question for the human.

## What "any machine, especially ChromeOS" rules out

The current machine is the Chromebook ([[jarvis-x-hardware]]): CPU-only, 14GB RAM with Chrome using ~10GB of it, and ~11GB free disk. Implication: a slot-1 local model has to run on the CPU inside that memory and disk. Large open models can only fill slot 1 through a free hosted tier, not locally.

## How the as-built tiers line up

As of the 2026-09-24 handoff ([[jarvis-x-runtime]]):

| Tier | As built | Slot under the ruling |
|------|----------|-----------------------|
| `local` | [[ollama]] `qwen2.5:3b` (Alibaba's Qwen, a Chinese open model) | 1 |
| `fast` | [[groq]] `openai/gpt-oss-20b` | 1, as a free hosted tier (Bug E lists it as free API access) |
| `smart` | [[groq]] `openai/gpt-oss-120b` | 1, as a free hosted tier (Bug E lists it as free API access) |
| `quality` / `frontier` | [[gemini]] `gemini-3.6-flash` | 2 (Google, free: Bug E lists it as free API access) |

Implication: the as-built routing already follows the ruling's order, with no Anthropic or OpenAI API tier in use. The plan's `smart` = Anthropic ([[universal-model-layer]]) moves to slot 3 under the ruling.

## Related

[[universal-model-layer]] | [[free-api-tiers]] | [[ollama]] | [[groq]] | [[gemini]] | [[openrouter]] | [[the-council]] | [[jarvis-x-hardware]] | [[crostini]] | [[jarvis-x]] | [[jarvis-x-plan-vs-reality]]
