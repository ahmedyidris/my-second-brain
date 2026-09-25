---
title: OpenRouter
tags: [provider, model-provider, cloud, free-tier, jarvis-x, entity]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[universal-model-layer]], [[free-api-tiers]], [[crostini]], [[starnet]], [[groq]], [[gemini]], [[jarvis-x-runtime]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
---

# OpenRouter

A cloud model provider in the [[jarvis-x]] plans. The v2 plan registers it in the [[universal-model-layer]] for its free models. As of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]), OpenRouter is **not** in the as-built Jarvis tier table. The handoff mentions it in four places: as one of the Cloudflare-fronted APIs hit by IPv6 truncation (fix 5), as a plain env var name StarNet's registry reads (fix 9), as a key passed to [[starnet]] at launch, and as one of the three free API options in Bug E.

## In the plans

| Source | What it says about OpenRouter |
|--------|-------------------------------|
| v2 Ascension Plan, reframe table (v1 column) | "Router: local Ollama + Gemini/Groq/OpenRouter" |
| v2 Ascension Plan, §3 | Registered provider: "OpenRouter (28+ free models incl. DeepSeek/Llama)" |

Note: the raw v2 plan doesn't assign OpenRouter to a tier. None of its five router rules names OpenRouter. The three that name a destination are privacy-sensitive → local only, long-context → Gemini, and fast loops → Groq. The `fast` tier shown for OpenRouter in the provider table on [[universal-model-layer]] comes from this wiki's own compilation, not from the plan text.

## As-built status (as of the 2026-09-24 handoff)

The Jarvis tier table, verified via `POST /api/ask`, uses only `ollama`, `groq` and `gemini` (see [[jarvis-x-runtime]]). OpenRouter doesn't appear in it.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan registers OpenRouter as a Universal Model Layer provider (and the v1 router already included it). The as-built tier table has no OpenRouter tier. Unknown: whether OpenRouter was dropped, is not wired up yet, or sits behind Jarvis as an unlisted fallback. The handoff says nothing about the fallback chain's members. Left for the human to resolve.

## In StarNet

- **`OPENROUTER_API_KEY`**: one of the plain env var names StarNet's registry reads, with no `SKYNET_` prefix (fix 9).
- The StarNet web-mode launch passes it: `OPENROUTER_API_KEY="$OPENROUTER_API_KEY" \`, after `set -a && source ~/.jarvis-x/.env && set +a`.
- The handoff reports no StarNet run result for OpenRouter, working or failing. See [[starnet]].

Implication: the launch expects `OPENROUTER_API_KEY` to be defined in `~/.jarvis-x/.env`. The handoff doesn't confirm that the key is set or has been verified.

## Network — IPv6 truncation on Crostini

OpenRouter is one of the two providers the handoff calls Cloudflare-fronted: "For Cloudflare-fronted APIs (Groq, OpenRouter), the IPv6 path truncates POST bodies." The fixes, and their c-ares gap for Node clients, are on [[crostini]].

## Free API access (Bug E)

The handoff's list of free API access includes: "OpenRouter: free models with shared-pool rate limits". See [[free-api-tiers]].

Observation: the Gemini and Groq entries in that list are marked "verified". The OpenRouter entry is not.

The plan's "28+ free models" and the handoff's "free models with shared-pool rate limits" don't contradict each other. The handoff adds the rate-limit caveat. Neither source quantifies the limits or names specific free model IDs.

## Related

[[universal-model-layer]] | [[free-api-tiers]] | [[crostini]] | [[starnet]] | [[groq]] | [[gemini]] | [[jarvis-x-runtime]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
