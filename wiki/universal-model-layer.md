---
title: Universal Model Layer
tags: [jarvis-x, v2, architecture, models, as-built]
sources:
  - raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-25-model-landscape-research.md
related: [[jarvis-x]], [[the-council]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[ollama]], [[groq]], [[gemini]], [[openrouter]], [[free-api-tiers]], [[hermes-agent]], [[source-jarvis-x-v2-ascension-plan]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[source-model-landscape-research]]
last_updated: 2026-09-25
---

# Universal Model Layer

A v2 addition to [[jarvis-x]]. One `providers/` interface, one config — every model provider behind a single abstraction with hot-swapping and free-tier fallbacks.

The sections from "CLI usage" to "Key constraint" describe the v2 plan ([[source-jarvis-x-v2-ascension-plan]]). "Implemented state" describes what the 2026-09-24 handoff shows was built ([[source-jarvis-x-starnet-handoff]]). "Provider priority" records the human's 2026-09-25 ruling on which providers plans should prefer ([[jarvis-x-model-priority]]).

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

> **Note (2026-09-24 re-check against the raw v2 plan):** the plan lists the registered providers, the tier names (`local|fast|smart|long`) and five router rules, three of which name a destination. It doesn't give each provider a tier. Those three rules support Ollama → `local`, Gemini → long-context and Groq → fast loops. The `Tier` values for OpenRouter, Anthropic, NVIDIA NIM and Mistral were filled in by this wiki; the plan text doesn't state them. The "1M+ context" note for Gemini comes from the DeepSeek master plan's Council table (Gemini, "The Analyst"), not from the v2 plan. The table is kept as it was; treat those cells as unsourced inferences.

## Router rules

- Privacy-sensitive → local only
- Long-context → Gemini
- Fast loops → Groq
- Fallback chain on quota errors
- Per-provider daily counters in SQLite

## Key constraint

Every provider is optional. [[jarvis-x]] must boot and function with zero cloud keys.

## Implemented state (2026-09-24 handoff)

As of the 2026-09-24 handoff, the layer runs as part of the [[jarvis-x-runtime]].

### Tier table

All verified working via POST /api/ask:

| tier     | provider | model                     |
|----------|----------|---------------------------|
| local    | ollama   | qwen2.5:3b                |
| fast     | groq     | openai/gpt-oss-20b        |
| smart    | groq     | openai/gpt-oss-120b       |
| quality  | gemini   | gemini-3.6-flash          |
| frontier | gemini   | gemini-3.6-flash          |

Provider pages: [[ollama]], [[groq]], [[gemini]].

### How it is wired

- **Interfaces.** The tiers are exercised through `POST /api/ask`. They are also exposed through the [[jarvis-x-openai-compatible-api]], whose `model` field accepts `local | fast | smart | quality | frontier`.
- **Tier resolution in the `/v1` adapter** (`app.py`, fix 7):

  ```python
  tier_to_model = {
      "local":    "qwen2.5:3b",
      "fast":     "registry:fast",
      "smart":    "registry:smart",
      "quality":  "registry:quality",
      "frontier": "registry:quality",
  }
  ```

  `local` goes straight to an Ollama model name. The cloud tiers resolve as `registry:<tier>`, and `frontier` reuses `registry:quality`.
- **`registry.js`.** The provider registry. Per fix 1 it "read `.env` as text" (the fix's `sed` targets `~/.jarvis-x/.env`), and it holds the per-tier model names (fixes 3 and 4). Fix 3's `sed` targets the relative path `code/providers/registry.js`. The handoff doesn't say which directory that path starts from, and doesn't label fix 3 with a project. The model it sets matches the Jarvis `fast` tier.
- **`registry:` branch in `hermes.py`.** Fix 2 (commit `4281158`) made this branch prepend the system prompt. Before that, fast/smart/frontier "all answered 'I am Qwen'". See [[hermes-agent]].

Implication: the `registry:<tier>` values in the adapter appear to feed the `registry:` branch in `hermes.py`, which calls `registry.js`. The handoff names all three pieces but doesn't spell out the call path.

### Fixes that touched the layer

| # | Fix | Commit | Detail |
|---|-----|--------|--------|
| 1 | `.env` quoting bug: keys kept their quotes, so "Every cloud call went out as `Authorization: Bearer "gsk_..."`" and "Every provider rejected silently" | — | [[jarvis-x-runtime]] |
| 2 | System prompt dropped on registry tiers | `4281158` | [[hermes-agent]] |
| 3 | Groq `fast` model 404: `groq/compound-mini` → `openai/gpt-oss-20b` | `b634ed8` | [[groq]] |
| 4 | Gemini model name: keep `gemini-3.6-flash` even though Google's models-list doesn't show it | — | [[gemini]] |
| 6 | systemd `EnvironmentFile` so the services get the API keys | — | [[jarvis-x-runtime]] |

### Fallbacks

The plan calls for a "fallback chain on quota errors". The handoff gives two pieces of evidence that some fallback exists:

- **Gotcha 9:** "Jarvis's quality tier maps to Gemini. If it returns ollama responses, the Gemini key is missing or invalid." Implication: when the Gemini key is missing or invalid, `quality` appears to fall back to Ollama rather than erroring. The handoff doesn't say which Ollama model answers, or whether other Gemini failures fall back the same way.
- **Priority 2:** routing StarNet through Jarvis would mean all StarNet traffic "goes through Jarvis, which handles fallbacks and never dies on truncation". This is the handoff's claim; it doesn't show the mechanism.

The handoff doesn't describe the chain's order, its triggers (quota errors or other failures), or its members.

### Not covered by the handoff

The handoff says nothing about:

- privacy-sensitive → local-only routing
- per-provider daily counters in SQLite
- a zero-cloud-keys boot test

Their as-built state is unknown.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan's tiers are `local|fast|smart|long`, with long-context routed to Gemini. The provider table above (this wiki's compilation) puts Anthropic on `smart`. The as-built tiers are `local | fast | smart | quality | frontier`:
>
> - `smart` is Groq `openai/gpt-oss-120b`
> - `quality` and `frontier` are both Gemini `gemini-3.6-flash`
> - there is no `long` tier
> - OpenRouter, Anthropic, NVIDIA NIM and Mistral are not in the as-built table
>
> Unknown: whether `quality`/`frontier` replaced `long`; whether the missing providers were dropped, deferred, or sit behind the fallback chain; and why `frontier` duplicates `quality`. Left for the human to resolve.
>
> The human's 2026-09-25 priority ruling puts Anthropic in slot 3 and Google's free tier in slot 2; the as-built routing (local Qwen, then free Groq gpt-oss, then free Gemini flash) already follows that order. The ruling settles provider order only. The tier-names question (the plan's `long` vs the as-built `quality`/`frontier`) was open.
>
> **Resolved (2026-09-25, follow-up ruling 4):** "Tier names should be as they are, copy Starnet way, it should be either by provider using api or local". The as-built names `local`, `fast`, `smart`, `quality` and `frontier` stay. Each tier is a route, either local (Ollama) or a provider's API, the way StarNet picks "provider → model". Why `frontier` currently duplicates `quality` is not addressed. See [[jarvis-x-model-priority]].

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan's interface is a CLI, `jj ask "..." --tier ...`. The handoff shows HTTP interfaces (`POST /api/ask`, `GET /v1/models`, `POST /v1/chat/completions`) and a `hermes` CLI, but it doesn't mention `jj` at all, so whether the `jj ask` CLI exists is unknown. Left for the human to resolve.

Possibly relevant to the choice of cloud models (the handoff doesn't draw this connection itself): see [[free-api-tiers]]. Bug E says consumer subscriptions don't give API access, and the free API list is Gemini `gemini-3.6-flash`, Groq `openai/gpt-oss-20b`/`-120b`, and OpenRouter's rate-limited free models. [[openrouter]] is on that list but not in the tier table. The 2026-09-25 research ([[source-model-landscape-research]]) puts numbers on these free tiers and adds more free routes. See [[free-api-tiers]].

## Provider priority (ruling, 2026-09-25)

The human ruled on the order in which Jarvis X plans should prefer providers ([[jarvis-x-model-priority]], from `raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md`). The same ruling names the Chromebook as the current machine.

| Priority | Slot | In the ruling's words |
|----------|------|-----------------------|
| 1 | Local and free open-source | "local models and free open source tiers that could work on any machine specially chrome os", and "include top tier Chinese open source models in local first, ollama" |
| 2 | Google, free | "most free available from google" |
| 3 | Anthropic | "then Anthropic" |
| 4 | OpenAI | "then open ai" |
| Paid | Paid subscriptions | "if kimi is not free treat as a paid subscription and put in paid tiers slot" |

How the plan's registered providers (table above) line up. This is interpretation: the ruling names only Google, Anthropic, OpenAI and Kimi.

| Provider | Slot under the ruling | Note |
|----------|-----------------------|------|
| Ollama (local) | 1 | Local-first. This also matches the key constraint: boot with zero cloud keys. Chinese open models: [[chinese-open-source-models]] |
| Groq | 1 | A free hosted tier for open-weight models. Its gpt-oss models are made by OpenAI, and They're free, so they're in slot 1 under their official names (follow-up ruling 1). See [[groq]] |
| OpenRouter | 1 | `:free` open models, availability unverified. See [[openrouter]] |
| Gemini CLI/API | 2 | Free API tier and the Gemini CLI quota. See [[gemini]] |
| Anthropic | 3 | Was `smart` in this wiki's compilation of the plan. No ongoing free API tier, only "a small amount of free credits" for new users ([[free-api-tiers]]) |
| NVIDIA NIM, Mistral | Not placed | The ruling doesn't name them, and the 2026-09-25 research doesn't cover them |
| OpenAI | 4 | Not in the plan's provider table. Its open-weight gpt-oss reaches Jarvis through Groq |
| Kimi | Paid | Not in the plan's provider table. It sits on [[the-council]]. Its API is paid, per a search excerpt in the research |

Observation: the as-built tiers (see "Tier table" above) use only slot-1 and slot-2 routes. They are local Qwen on Ollama, then free Groq gpt-oss, then free Gemini flash.

Still open after the ruling:

- ~~the tier names~~: resolved, they stay as they are (ruling 4, above);
- ~~where Kimi sits in the paid group~~: resolved, paid Kimi models are standalone paid entries (ruling 3, [[jarvis-x-model-priority]]);
- ~~whether "$0/month" still holds~~: resolved, "Still zero but leave it as an option" (ruling 7);
- why `frontier` duplicates `quality`: not addressed;
- a Flash-Lite tier or fallback for more free tokens: recommended after ruling 8 ("we need more tokens"), not yet made (see [[jarvis-x-model-priority]], "Getting more tokens").

## Related

[[jarvis-x]] | [[the-council]] | [[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[ollama]] | [[groq]] | [[gemini]] | [[openrouter]] | [[free-api-tiers]] | [[hermes-agent]] | [[source-jarvis-x-v2-ascension-plan]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]] | [[jarvis-x-model-priority]] | [[chinese-open-source-models]] | [[source-model-landscape-research]]
