---
title: Groq
tags: [provider, model-provider, cloud, free-tier, jarvis-x, entity]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[universal-model-layer]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[free-api-tiers]], [[crostini]], [[starnet]], [[aider]], [[gemini]], [[openrouter]], [[ollama]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
---

# Groq

A cloud model provider behind the [[jarvis-x]] [[universal-model-layer]]. As of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]), Groq serves two Jarvis tiers, `fast` and `smart`, both on models the handoff lists as free API access. The handoff's [[aider]] launch command also names a Groq model. It is the provider named in StarNet's open Bug A.

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

## Fix 3 — fast model 404

The handoff says: "registry.js had fast: 'groq/compound-mini'. That model doesn't exist on this account. Correct name: openai/gpt-oss-20b."

Fix:

```bash
sed -i "s|fast: 'groq/compound-mini'|fast: 'openai/gpt-oss-20b'|" code/providers/registry.js
```

Committed as `b634ed8`. The handoff doesn't say which project fix 3 belongs to, or which directory the relative path `code/providers/registry.js` starts from. The model it sets matches the Jarvis `fast` tier above. "Doesn't exist on this account" is the handoff's wording. It doesn't say whether `groq/compound-mini` exists for other accounts.

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

Bug E lists Groq among the free API access that works: "Groq: openai/gpt-oss-20b, openai/gpt-oss-120b (verified)". See [[free-api-tiers]].

## Related

[[universal-model-layer]] | [[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[free-api-tiers]] | [[crostini]] | [[starnet]] | [[aider]] | [[gemini]] | [[openrouter]] | [[ollama]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
