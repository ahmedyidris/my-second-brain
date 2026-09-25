---
title: OpenRouter
tags: [provider, model-provider, cloud, free-tier, jarvis-x, entity]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/2026-09-25-model-landscape-research.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
related: [[universal-model-layer]], [[free-api-tiers]], [[crostini]], [[starnet]], [[groq]], [[gemini]], [[jarvis-x-runtime]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[source-model-landscape-research]], [[the-council]], [[ollama]]
last_updated: 2026-09-25
---

# OpenRouter

A cloud model provider in the [[jarvis-x]] plans. The v2 plan registers it in the [[universal-model-layer]] for its free models. As of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]), OpenRouter is **not** in the as-built Jarvis tier table. The handoff mentions it in four places: as one of the Cloudflare-fronted APIs hit by IPv6 truncation (fix 5), as a plain env var name StarNet's registry reads (fix 9), as a key passed to [[starnet]] at launch, and as one of the three free API options in Bug E.

Under the human's 2026-09-25 ruling ([[jarvis-x-model-priority]]), OpenRouter's free models fill slot 1: a free hosted tier for open-source models. The 2026-09-25 research ([[source-model-landscape-research]]) lists the `:free` model IDs and the limits.

\* Figures marked with an asterisk come from web-search excerpts in the 2026-09-25 research, not fetched pages. Treat them as medium confidence and possibly stale. The proxy blocked openrouter.ai, so **everything on this page from the research carries the asterisk**.

## In the plans

| Source | What it says about OpenRouter |
|--------|-------------------------------|
| v2 Ascension Plan, reframe table (v1 column) | "Router: local Ollama + Gemini/Groq/OpenRouter" |
| v2 Ascension Plan, §3 | Registered provider: "OpenRouter (28+ free models incl. DeepSeek/Llama)" |

Note: the raw v2 plan doesn't assign OpenRouter to a tier. None of its five router rules names OpenRouter. The three that name a destination are privacy-sensitive → local only, long-context → Gemini, and fast loops → Groq. The `fast` tier shown for OpenRouter in the provider table on [[universal-model-layer]] comes from this wiki's own compilation, not from the plan text.

## As-built status (as of the 2026-09-24 handoff)

The Jarvis tier table, verified via `POST /api/ask`, uses only `ollama`, `groq` and `gemini` (see [[jarvis-x-runtime]]). OpenRouter doesn't appear in it.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan registers OpenRouter as a Universal Model Layer provider (and the v1 router already included it). The as-built tier table has no OpenRouter tier. Unknown: whether OpenRouter was dropped, is not wired up yet, or sits behind Jarvis as an unlisted fallback. The handoff says nothing about the fallback chain's members. Left for the human to resolve.

The 2026-09-25 ruling puts OpenRouter's free models in slot 1, but it doesn't say whether OpenRouter should be wired into the tier table. That question stays open.

## Free models (2026-09-25 research)

**Availability is unverified for every row.** The IDs come from search excerpts, and retired model pages can stay in search indexes, so a listed `:free` model may no longer be live.

| Vendor | `:free` IDs found* |
|--------|--------------------|
| DeepSeek | `deepseek/deepseek-v4-flash:free`, `deepseek/deepseek-r1:free`, `deepseek/deepseek-chat-v3-0324:free` |
| Qwen (Alibaba) | `qwen/qwen3.8-27b:free`, `qwen/qwen3-coder:free`, `qwen/qwen3.6-plus:free` |
| Kimi (Moonshot) | `moonshotai/kimi-k2.6:free`, `moonshotai/kimi-k2:free`, `moonshotai/kimi-dev-72b:free` |
| GLM (Zhipu / Z.ai) | `z-ai/glm-5.2:free`, `z-ai/glm-5.1:free`, `z-ai/glm-4.5-air:free` |
| MiniMax | `minimax/minimax-m2.5:free`, `minimax/minimax-m2:free` |
| Gemma (Google) | `google/gemma-4-31b-it:free`, `google/gemma-4-26b-a4b-it:free`, `google/gemma-3-27b-it:free`, `google/gemma-3-4b-it:free`, `google/gemma-3n-e4b-it:free` |
| gpt-oss (OpenAI) | `openai/gpt-oss-120b:free`, `openai/gpt-oss-20b:free` |

**The auto-router.** `openrouter/free` picks a free model automatically*.

The table lists 21 `:free` IDs. It is a record of what the research found, not a complete catalogue, so it neither confirms nor refutes the plan's "28+ free models". It has DeepSeek IDs but no Llama IDs, and the research note doesn't say whether it looked for Llama.

Several of these families are cloud-only on [[ollama]]: all Kimi models, DeepSeek-V4, GLM-5 and MiniMax*. So they can't run locally on the Chromebook (see [[chinese-open-source-models]]). Implication: they can fill slot 1 at no cost only through a hosted free tier. That means this one, or Ollama cloud's free starter set if it includes them, which is unverified ([[free-api-tiers]]).

## Limits (2026-09-25 research)

| Account state | Requests/day | Requests/min |
|---------------|--------------|--------------|
| No credits purchased | 50* | 20* |
| After a one-time $10 credit purchase | 1,000* | 20* |

Source (per the research note): `openrouter.ai/docs/api_reference/limits`, seen in a search excerpt only.

Implication: 50 requests a day is below the ~1,000/day free Groq allowance for `gpt-oss-120b` ([[groq]]). The 1,000/day cap costs a one-time $10, which sits awkwardly with the v2 plan's "$0/month" constraint and the ruling's "free" wording. Whether that purchase is acceptable is for the human ([[free-api-tiers]]).

## Under the 2026-09-25 ruling

The ruling's slot 1 is "local models and free open source tiers that could work on any machine specially chrome os", and it asks to "include top tier Chinese open source models". See [[jarvis-x-model-priority]].

- **Slot 1.** OpenRouter's `:free` models are free hosted open models. They need no local RAM or disk. Classing them as slot 1 is how [[jarvis-x-model-priority]] and this wiki read "free open source tiers".
- **Chinese families.** DeepSeek, Qwen, Kimi, GLM and MiniMax all have `:free` listings*. See [[chinese-open-source-models]].
- **Kimi.** The ruling says: "if kimi is not free treat as a paid subscription and put in paid tiers slot". The Kimi API itself is paid*, and Groq has deprecated its Kimi model* ([[groq]]). The research note's verdict, which is its own inference, is that the Kimi `:free` listings here (`moonshotai/kimi-k2.6:free`, `moonshotai/kimi-k2:free`) are the only possible free route, and only if still live. This bears on the Kimi K2.6 seat in [[the-council]]. Checking whether `moonshotai/kimi-k2.6:free` still answers would settle whether Kimi has a free route.
- **gpt-oss `:free`.** These are OpenAI-made. They raise the same classification question as Groq's gpt-oss: slot 1 as a free open-weight tier, or slot 4 as OpenAI. See question (a) on [[jarvis-x-model-priority]], and [[groq]].
- **Gemma `:free`.** These are Google-made open models. See [[gemini]] for how Gemma fits the ladder.

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

The plan's "28+ free models" and the handoff's "free models with shared-pool rate limits" don't contradict each other. The handoff adds the rate-limit caveat. Neither source quantifies the limits or names specific free model IDs. The 2026-09-25 research does both, at medium confidence (see "Free models" and "Limits" above). It gives per-account caps and says nothing about a "shared pool", so the handoff's wording is still unexplained.

## Related

[[universal-model-layer]] | [[free-api-tiers]] | [[crostini]] | [[starnet]] | [[groq]] | [[gemini]] | [[jarvis-x-runtime]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]] | [[jarvis-x-model-priority]] | [[chinese-open-source-models]] | [[source-model-landscape-research]] | [[the-council]] | [[ollama]]
