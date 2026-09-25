---
title: Groq
tags: [provider, model-provider, cloud, free-tier, jarvis-x, entity]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/2026-09-25-model-landscape-research.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
related: [[universal-model-layer]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[free-api-tiers]], [[crostini]], [[starnet]], [[aider]], [[gemini]], [[openrouter]], [[ollama]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[source-model-landscape-research]], [[the-council]]
last_updated: 2026-09-25
---

# Groq

A cloud model provider behind the [[jarvis-x]] [[universal-model-layer]]. As of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]), Groq serves two Jarvis tiers, `fast` and `smart`, both on models the handoff lists as free API access. The handoff's [[aider]] launch command also names a Groq model. It is the provider named in StarNet's open Bug A.

Under the human's 2026-09-25 ruling ([[jarvis-x-model-priority]]), Groq's free tier fills slot 1: a free hosted tier for open-weight models. See "Under the 2026-09-25 ruling" below for the gpt-oss caveat.

\* Figures marked with an asterisk come from web-search excerpts in the 2026-09-25 research ([[source-model-landscape-research]]), not fetched pages. Treat them as medium confidence and possibly stale. The proxy blocked console.groq.com, so every figure from Groq's own docs carries the asterisk.

## In the plans

| Source | What it says about Groq |
|--------|-------------------------|
| v2 Ascension Plan, reframe table (v1 column) | "Router: local Ollama + Gemini/Groq/OpenRouter" |
| v2 Ascension Plan, §3 Universal Model Layer | Groq is a registered provider. One of the router rules is "fast loops → Groq". |

## As-built tiers (as of the 2026-09-24 handoff)

All verified working via `POST /api/ask`:

| tier     | provider | model                     |
|----------|----------|---------------------------|
| fast     | groq     | openai/gpt-oss-20b        |
| smart    | groq     | openai/gpt-oss-120b       |

In the [[jarvis-x-openai-compatible-api]], `fast` and `smart` resolve to `registry:fast` and `registry:smart`. The full five-tier table is on [[jarvis-x-runtime]].

Note: the plan's only router rule naming Groq is "fast loops → Groq". It doesn't put Groq on a `smart` tier. The as-built `smart` tier runs on Groq as well. The tier-by-tier disagreement is recorded on [[universal-model-layer]].

## Models on Groq (2026-09-25 research)

From Groq's models and deprecations pages, as seen in search excerpts:

| Model ID | Status | Notes |
|----------|--------|-------|
| `openai/gpt-oss-120b` | Listed* | The as-built `smart` tier |
| `openai/gpt-oss-20b` | Listed* | The as-built `fast` tier |
| `qwen/qwen3.8-27b` | Listed* | Paid price $0.80 in / $4.00 out per 1M tokens*. Its free-tier limits are unverified |
| `moonshotai/kimi-k2-instruct-0905` | **Deprecated**\* | Deprecation announced Mar 23, 2026. Replacement: `gpt-oss-120b`* |
| `qwen/qwen3-32b` | Deprecated* | Deprecation announced June 17, 2026* |
| `llama-4-scout` | Deprecated* | Deprecation announced June 17, 2026* |
| `llama-3.1-8b-instant` | Deprecated* | Deprecation announced June 17, 2026* |
| `llama-3.3-70b-versatile` | Deprecated* | Deprecation announced June 17, 2026* |

The research note gives the dates the deprecations were announced, not the dates the models stop working.

Chinese models on Groq now, per the research: Qwen yes (`qwen/qwen3.8-27b`); Kimi no (deprecated); DeepSeek none found. See [[chinese-open-source-models]].

Implication: Groq no longer offers a Kimi model, so it can't serve the Kimi K2.6 seat in [[the-council]].

## Free-tier limits (2026-09-25 research)

| Model | RPM | RPD | TPM | TPD | Source |
|-------|-----|-----|-----|-----|--------|
| `openai/gpt-oss-120b` | 30 | 1,000 | 8,000 | 200,000 | Measured Sept 14, 2026, in a fetched GitHub issue (a third party's project). Groq's own rate-limits page agrees in a search excerpt* |
| `openai/gpt-oss-20b` | 30* | 1,000* | 8,000* | 200,000* | Third-party excerpts only |
| `qwen/qwen3.8-27b` | — | — | — | — | Unverified |

The limits are per organization.

Implication: if Jarvis's `smart` tier and [[aider]] use the same Groq key, they share the 1,000 requests/day for `gpt-oss-120b`. Both load keys from `~/.jarvis-x/.env`. The handoff doesn't name the variable Jarvis's registry reads, so this is not confirmed.

## Under the 2026-09-25 ruling

The ruling's order is: (1) local models and free open-source tiers that "could work on any machine specially chrome os"; (2) Google, free; (3) Anthropic; (4) OpenAI. See [[jarvis-x-model-priority]].

- **Groq's free tier is slot 1**, as a free hosted tier for open-weight models. It uses no local RAM or disk, and both gpt-oss tiers were verified working through Jarvis on the Chromebook (StarNet's Bug A is a separate problem).
- **The gpt-oss caveat.** `gpt-oss-20b` and `gpt-oss-120b` are OpenAI-made open-weight models. The ruling ranks OpenAI last among the named providers (slot 4). [[jarvis-x-model-priority]] files Groq's free gpt-oss under slot 1 "as a free hosted tier", and that classification is interpretation. It is open for the human to confirm (question (a) on that page). If the human meant anything from OpenAI, the as-built `fast` and `smart` tiers move to slot 4.
- **Chinese open models.** `qwen/qwen3.8-27b` is a Chinese open model on Groq, but the research found only a paid price for it and its free limits are unverified. Too big to run locally: the smallest Ollama `qwen3.8` tag is about 18GB*. See [[chinese-open-source-models]].

## Fix 3 — fast model 404

The handoff says: "registry.js had fast: 'groq/compound-mini'. That model doesn't exist on this account. Correct name: openai/gpt-oss-20b."

Fix:

```bash
sed -i "s|fast: 'groq/compound-mini'|fast: 'openai/gpt-oss-20b'|" code/providers/registry.js
```

Committed as `b634ed8`. The handoff doesn't say which project fix 3 belongs to, or which directory the relative path `code/providers/registry.js` starts from. The model it sets matches the Jarvis `fast` tier above. "Doesn't exist on this account" is the handoff's wording. It doesn't say whether `groq/compound-mini` exists for other accounts. (The 2026-09-25 research doesn't mention `groq/compound-mini`.)

## API key

- **`GROQ_API_KEY`**: StarNet's registry reads this plain name, with no `SKYNET_` prefix (fix 9, see [[starnet]]). The StarNet launch and Priority 1 debug commands pass it explicitly as `GROQ_API_KEY="$GROQ_API_KEY"`.
- Keys live in `~/.jarvis-x/.env` (chmod 600). They are loaded with `set -a && source ~/.jarvis-x/.env && set +a` before the StarNet, Aider and Hermes CLI launches.
- The handoff names the variables for StarNet's registry. It doesn't list the ones Jarvis's own registry reads.

### Fix 1 — quoting bug (affected every cloud call)

"`registry.js` read `.env` as text and kept surrounding quotes on every key. Every cloud call went out as `Authorization: Bearer "gsk_..."` — quotes and all. Every provider rejected silently."

```bash
sed -i 's/^\([A-Z_]*\)="\(.*\)"$/\1=\2/' ~/.jarvis-x/.env
```

See [[jarvis-x-runtime]] for the full fix list.

## Network — IPv6 truncation on Crostini

Groq is one of the two providers the handoff calls Cloudflare-fronted: "For Cloudflare-fronted APIs (Groq, OpenRouter), the IPv6 path truncates POST bodies." The `gai.conf` and `NODE_OPTIONS` workarounds are on [[crostini]].

The workarounds have a known gap. Node's `https.get` uses c-ares and ignores both of them, so it "still times out on nodejs.org, api.groq.com, etc." curl works because it uses glibc's resolver.

## In StarNet — Bug A

As of the 2026-09-24 handoff, Groq does not work from [[starnet]]:

- PART 1: "Groq/Gemini: keys verify as VALID but every run either returns HTTP 400 or kills the sidecar".
- **Bug A:** "after picking Groq and sending a message, the sidecar process dies with no error in /tmp/starnet.log. The log ends normally after 'connectors up'." It is not fixed and not diagnosed. The handoff lists three **hypotheses** ("likely one of"):
  1. Streaming HTTP to Cloudflare-fronted endpoints fails silently on Crostini ([[crostini]])
  2. Some uncaught async error kills Node without logging
  3. The provider adapter dereferences a field that doesn't exist for non-Ollama providers
- "The stream: false patch made it worse (broke Ollama too). It was reverted." The handoff doesn't say which file the patch changed. PART 8 separately says: "Do not re-enable stream: false on the OpenAI-compatible adapter. It breaks all providers." Ambiguous: that could mean StarNet's `sidecar/providers/openai-compatible.js` or Jarvis's `/v1` adapter in `app.py` (fix 7). The handoff doesn't say which.
- The launch instructions end with "(Do NOT pick Groq — Bug A.)". Raqib runs on Ollama `qwen2.5:7b` instead ([[ollama]]).

Priority 1 diagnostic step (the sidecar in the foreground). It passes `GROQ_API_KEY` explicitly, but `set -a && source ~/.jarvis-x/.env && set +a` exports every variable in `.env` first:

```bash
# Start sidecar in foreground to see the death
cd ~/starnet
set -a && source ~/.jarvis-x/.env && set +a
NODE_OPTIONS="--dns-result-order=ipv4first" \
GROQ_API_KEY="$GROQ_API_KEY" \
node sidecar/index.js
```

Priority 2 is to route StarNet through Jarvis, "which handles fallbacks and never dies on truncation".

Implication: the same Groq models are verified working through Jarvis (`POST /api/ask`), and the keys verify as VALID in StarNet. So the failure looks tied to StarNet's calling path rather than to the Groq account. That fits hypotheses 2 and 3 as well as hypothesis 1, so it doesn't narrow Bug A down.

## Aider

The handoff's [[aider]] launch command (PART 4) names the same model as the `smart` tier, with a `groq/` prefix:

```bash
aider --model groq/openai/gpt-oss-120b --no-show-model-warnings
```

The handoff doesn't say how Aider reaches Groq. Bug B separately lists Aider among the callers of Jarvis's `/v1` endpoint.

## Free API access (Bug E)

Bug E lists Groq among the free API access that works: "Groq: openai/gpt-oss-20b, openai/gpt-oss-120b (verified)". The 2026-09-25 research still finds both models listed* and gives the free-tier limits above. See [[free-api-tiers]].

## Related

[[universal-model-layer]] | [[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[free-api-tiers]] | [[crostini]] | [[starnet]] | [[aider]] | [[gemini]] | [[openrouter]] | [[ollama]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]] | [[jarvis-x-model-priority]] | [[chinese-open-source-models]] | [[source-model-landscape-research]] | [[the-council]]
