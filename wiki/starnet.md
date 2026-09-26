---
title: StarNet
tags: [starnet, ai-os, multi-agent, entity, sidecar, node, jarvis-x]
sources:
  - raw/2026-09-26-ahmed-ruling-3-starnet-itself-on-chromeos.md
  - raw/2026-09-26-starnet-on-chromeos-install-findings.md
  - raw/2026-09-26-starnet-gateway-and-station-build.md
  - raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x]], [[jarvis-x-station-view]], [[jarvis-x-openai-compatible-api]], [[jarvis-x-runtime]], [[ollama]], [[groq]], [[gemini]], [[openrouter]], [[crostini]], [[ipv6-dns-truncation-crostini]], [[the-council]], [[constitutional-autonomy]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-app]], [[jarvis-x-hardware]], [[jarvis-x-plan-vs-reality]], [[free-api-tiers]], [[jarvis-x-starnet-gateway]]
last_updated: 2026-09-26
---

# StarNet

A separate multi-agent platform developed in parallel with [[jarvis-x]]. It is a web app (the handoff: "Runs as web app") from the `androoAGI/starnet` repo, run locally next to [[jarvis-x]] on the [[crostini]] Chromebook. The 2026-09-24 handoff shows these parts of it: named agents (the working one is **Raqib**, the Overseer), a Node **sidecar** that serves a web UI, a provider registry, "connectors", channel tokens for Discord/Telegram bots, workspace state on disk, and a Tauri desktop shell (built once, since deleted). The handoff says nothing more about what StarNet is for. Its verdict is to stop chasing a StarNet clone and build a [[jarvis-x-station-view]] inside Jarvis instead.

## State (as of the 2026-09-24 handoff)

| Item | Value |
|------|-------|
| Repo | `androoAGI/starnet` |
| Local branch | `feat/harness-backend` |
| Working commit | `658dc7ce9` (agentId sanitization) |
| Source | `~/starnet` |
| State | `~/.local/share/StarNet/workspaces/` |
| Run mode | Web app: `node sidecar/index.js` → http://127.0.0.1:8787 |
| Log (from the launch command) | `/tmp/starnet.log` |
| Working agent | Raqib (Overseer) |
| Working model | `qwen2.5:7b` via Ollama (slow — ~10 tok/s) |
| Working provider file | `sidecar/providers/openai-compatible.js` |
| Tauri desktop shell | Built successfully at one point, but deleted (was slow, no benefit over web) |

## Provider status (as of the 2026-09-24 handoff)

| Provider | Status in StarNet |
|----------|-------------------|
| [[ollama]] | **Works.** The only working provider. |
| [[groq]] / [[gemini]] | Keys verify as VALID, but every run either returns HTTP 400 or kills the sidecar. Sidecar death on Groq is tracked as Bug A. |
| [[openrouter]] | `OPENROUTER_API_KEY` is passed at launch. The handoff reports no StarNet run result for it. (OpenRouter's free models are on the Bug E free-access list — see [[free-api-tiers]].) |
| Custom (Jarvis `/v1`) | The UI's verification rejects `http://127.0.0.1:8000/v1` (Bug C). |

Note: fix 10 (below) is listed as landed for the HTTP 400s caused by internal message fields. PART 1 of the handoff still lists "returns HTTP 400" as a Groq/Gemini failure mode, though. The handoff doesn't say whether HTTP 400s still happen after `658dc7ce9`.

## Provider environment variables (fix 9)

The registry reads these plain names (no `SKYNET_` prefix):

| Variable | Purpose (per handoff) |
|----------|-----------------------|
| `GROQ_API_KEY` | [[groq]] key |
| `GEMINI_API_KEY` | [[gemini]] key |
| `OPENROUTER_API_KEY` | [[openrouter]] key |
| `CUSTOM_OPENAI_BASE_URL` | Custom OpenAI-compatible endpoint base URL |
| `CUSTOM_OPENAI_KEY` | Key for the custom endpoint |

**Gotcha — the `SKYNET_` prefix:** the `SKYNET_<PROVIDER>_API_KEY` pattern in `secrets.js` is for Discord/Telegram bot tokens, NOT provider keys. In the handoff's words: "The SKYNET_ prefix is for channel tokens, not provider keys. Provider keys use plain names."

## Message sanitization (fix 10)

StarNet attaches internal fields (agentId and others) to outgoing messages. Strict validators reject them with HTTP 400. The fix, in `sidecar/providers/openai-compatible.js`, filters message objects down to the OpenAI schema before sending:

```javascript
req.messages.map(m => {
  const o = {};
  for (const k of ['role','content','tool_calls','tool_call_id','name','function_call']) {
    if (k in m) o[k] = m[k];
  }
  return o;
})
```

Committed on branch `feat/harness-backend` as `658dc7ce9`.

## Launch (web mode)

```bash
pkill -f "node sidecar/index.js"
sleep 2
cd ~/starnet
set -a && source ~/.jarvis-x/.env && set +a
NODE_OPTIONS="--dns-result-order=ipv4first" \
GROQ_API_KEY="$GROQ_API_KEY" \
GEMINI_API_KEY="$GEMINI_API_KEY" \
OPENROUTER_API_KEY="$OPENROUTER_API_KEY" \
CUSTOM_OPENAI_BASE_URL="http://127.0.0.1:8000/v1" \
CUSTOM_OPENAI_KEY="sk-jarvis-local" \
nohup node sidecar/index.js > /tmp/starnet.log 2>&1 &
```

Open http://127.0.0.1:8787
Set Raqib's model to OLLAMA → qwen2.5:7b
(Do NOT pick Groq — Bug A.)

Keys come from `~/.jarvis-x/.env` (chmod 600), the same file [[jarvis-x-runtime]] uses. `CUSTOM_OPENAI_KEY` is set to the literal string `sk-jarvis-local` for the Jarvis endpoint. The handoff doesn't say whether Jarvis's `/v1` checks this key.

Implication: the launch sets `NODE_OPTIONS="--dns-result-order=ipv4first"`. According to the handoff, that setting does NOT cover Node's c-ares resolver ([[crostini]]). The handoff doesn't establish which resolver path the sidecar's provider calls use.

## Gotcha — workspace lock (`WORKSPACE_BUSY`)

"StarNet's workspace lock is fragile. After any ungraceful exit, the sidecar refuses to start with WORKSPACE_BUSY." Fix:

```bash
cat ~/.local/share/StarNet/workspaces/.starnet-workspace-owner.json
# note the PID, kill it if it's dead
pkill -f "node sidecar/index.js"
rm ~/.local/share/StarNet/workspaces/.starnet-workspace-owner.json
```

## Open bugs (as of the 2026-09-24 handoff)

### Bug A — Groq runs kill the sidecar

**Symptom:** after you pick Groq and send a message, the sidecar process dies with no error in `/tmp/starnet.log`. The log ends normally after "connectors up".

**Status:** not fixed and not diagnosed. The handoff gives three **hypotheses** ("likely one of"). None is confirmed:

1. Streaming HTTP to Cloudflare-fronted endpoints fails silently on Crostini (see [[crostini]], [[ipv6-dns-truncation-crostini]], [[groq]])
2. Some uncaught async error kills Node without logging
3. The provider adapter dereferences a field that doesn't exist for non-Ollama providers

**Tried and reverted:** "The stream: false patch made it worse (broke Ollama too). It was reverted."

**Mitigation built (2026-09-26, not yet tested on the machine):** [[jarvis-x-starnet-gateway]] makes StarNet stream only from 127.0.0.1, while Jarvis makes non-streamed calls to Groq. If hypothesis 1 is right, Bug A no longer bites on that route. It does not diagnose Bug A. PART 8 adds: "Do not re-enable stream: false on the OpenAI-compatible adapter. It breaks all providers."

Interpretation: read alongside Bug A, "the OpenAI-compatible adapter" in PART 8 most likely means StarNet's `sidecar/providers/openai-compatible.js`. The handoff also calls Jarvis's `/v1` layer the "OpenAI-compatible adapter" ([[jarvis-x-openai-compatible-api]]), so it's not fully explicit which one is meant.

### Bug C — custom provider verification rejects localhost

When you add `http://127.0.0.1:8000/v1` as a custom provider in the StarNet UI, verification fails even with a valid key. The registry supports the `CUSTOM_OPENAI_BASE_URL` env var correctly, but the UI-side verification blocks it.

**Status:** not fully investigated. The env-var path (setting `CUSTOM_OPENAI_BASE_URL` at launch, as the launch block above does) *may* bypass the UI verification if StarNet reads it at boot. **Unconfirmed.**

**Analysis from StarNet's code (2026-09-26).** Source: `raw/2026-09-26-starnet-gateway-and-station-build.md`. This read upstream `androoAGI/starnet`, not the local `feat/harness-backend` branch, and nothing was confirmed on the machine.

- The custom provider needs no key.
- The key check runs only when a key is typed. It streams "Reply with OK." to the selected model (or the first listed) with a hard **15s** budget.
- The settings form adds `https://` to a URL typed without a scheme.

Candidate causes, ranked:
1. The 15s check hit a slow model. app.py's `/v1/models` lists `local` first, and app.py sends no headers until the answer exists.
2. A missing `http://` was turned into `https://`, which fails TLS against a plain-HTTP server.
3. The local branch differs from upstream.

Workaround: type the URL with `http://`, and leave the key empty so the check never runs. The env-var path is real: `providerRuntimeBaseUrl` falls back to `CUSTOM_OPENAI_BASE_URL`.

### Bug B (context) — agents must send file contents themselves

Jarvis's `/v1/chat/completions` is a chat API and doesn't read the filesystem. Callers, StarNet agents included, "must read the file themselves and include its content in the message." This is expected behaviour. See [[jarvis-x-openai-compatible-api]].

## Next steps (PART 7)

### Priority 1 — StarNet Groq bug

Find out why the sidecar dies on Groq calls:

```bash
# Start sidecar in foreground to see the death
cd ~/starnet
set -a && source ~/.jarvis-x/.env && set +a
NODE_OPTIONS="--dns-result-order=ipv4first" \
GROQ_API_KEY="$GROQ_API_KEY" \
node sidecar/index.js
```

Then send a message and watch the terminal. The exit reason will appear there. Alternatively, add logging to `sidecar/providers/openai-compatible.js` around the fetch call.

### Priority 2 — Route StarNet through Jarvis

"Get the custom provider UI to accept localhost, OR confirm the env-var path works. Then all StarNet traffic goes through Jarvis, which handles fallbacks and never dies on truncation." The target is Jarvis's OpenAI-compatible endpoint at `http://127.0.0.1:8000/v1` ([[jarvis-x-openai-compatible-api]]). Its `model` field takes `local | fast | smart | quality | frontier`.

> **Disagreement (2026-09-24 handoff vs 2026-09-26 code reading):** the handoff targets `http://127.0.0.1:8000/v1`. StarNet's own adapter, run against app.py's reply shape, reads **zero** text events from it: app.py answers with one JSON body, while StarNet parses only a streamed (SSE) reply. app.py's `/v1` also sends headers only after the full answer, keeps only the last user turn, and drops tools. Source: `raw/2026-09-26-starnet-gateway-and-station-build.md`.
>
> What was built instead: a separate gateway on `http://127.0.0.1:8010/v1` ([[jarvis-x-starnet-gateway]], jarvis-x PR #37). It is not yet run on the Chromebook.

## Tauri desktop shell

- Built successfully at one point, then deleted (slow, no benefit over web).
- "The Tauri build is 30-60 min and needs 8GB disk + 6GB RAM. It's rebuildable but not useful for daily work on this hardware."
- Node 22.x is bundled for Tauri (the system Node is 20.x).
- PART 8: "Do not build the Tauri desktop shell for daily use. Web UI is faster and identical in function."
- Before any heavy build, close Chrome tabs: they "eat 10GB of your 14GB", and `free -h` should show 6GB+ available ([[crostini]], [[jarvis-x-hardware]]).
- The v2 plan's own Tauri wrapper for Jarvis (for Windows/macOS builds) is a separate question, discussed on [[jarvis-x-app]]. The handoff doesn't say whether the PART 8 rule covers it.

## Safety note

"Do not run YOLO-mode agents on this machine. The venv and StarNet workspace have both been destroyed by that pattern." See [[constitutional-autonomy]].

## Direction from the human (2026-09-25)

Source: `raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md`.

> "I was actually trying to set up Starnet and merge with Jarvis, then I was thinking of building Jarvis using Starnet but it didn't work with me then I thought it could be built as part of Jarvis, now I want to complete both and merge in this repo in a meaning that I want to continue working on Jarvis when I setup Starnet"

In order, the attempts were:

1. set StarNet up and merge it with Jarvis;
2. build Jarvis using StarNet, which didn't work;
3. build StarNet's ideas as part of Jarvis (the handoff's [[jarvis-x-station-view]]).

The goal now is to **complete both and merge them**, so that setting up StarNet also moves Jarvis forward.

> **Disagreement (2026-09-24 handoff PART 8 vs the human's 2026-09-25 direction):** the handoff says "Do not chase a StarNet clone... Add a station view to Jarvis instead." The human now wants both StarNet and Jarvis completed and merged. The newer statement is the human's own decision. The handoff's advice is kept as the record of what was tried.
>
> Not yet defined:
> - what "merge" means concretely: StarNet using Jarvis as its model gateway, StarNet's code moved into the jarvis-x repo, or the Station view absorbing StarNet;
> - which repo "this repo" refers to.
>
> Left for the human to confirm.
>
> **Resolved (2026-09-25):** asked to choose, the human said "A then C, go ahead". A means StarNet uses Jarvis as its model gateway ([[jarvis-x-starnet-gateway]]). C means building the [[jarvis-x-station-view]], with StarNet's roster idea (Raqib plus role templates) moved into Jarvis. Both were built on 2026-09-26 and are awaiting merge (`raw/2026-09-26-starnet-gateway-and-station-build.md`).

Implication (interpretation): the smallest step that serves both is the handoff's own Priority 2, routing StarNet through Jarvis's [[jarvis-x-openai-compatible-api]]. That gives StarNet Jarvis's working providers, and would sidestep Bug A if that bug is on the Groq path. Every StarNet run then also exercises Jarvis.

## Running StarNet itself on the Chromebook (2026-09-26)

**The human's ruling** (verbatim, `raw/2026-09-26-ahmed-ruling-3-starnet-itself-on-chromeos.md`):

> "I wanted to clone the whole system of Starnet as Jarvis exactly how it is to be able run on chrome os, mainly same exact interface as Starnet or be able to run Starnet itself on chrome os or clone there system as it is"

**What was done:** StarNet itself runs, unmodified, in web mode, with Jarvis as its model provider through [[jarvis-x-starnet-gateway]]. One script does it: `scripts/starnet.sh` in jarvis-x PR #37. Source: `raw/2026-09-26-starnet-on-chromeos-install-findings.md`.

- **Why run it rather than clone it.** StarNet's `npm start` is `node sidecar/index.js`, which serves the whole product (UI and engine) on :8787. Its public installers are Windows and macOS only, but web mode is plain Node and needs `node >= 18`. Running the upstream code keeps its updates. A fork would drift.
- **Install fixes found by installing it on Debian:**
  - skip `onnxruntime-node`'s CUDA download (`ONNXRUNTIME_NODE_INSTALL=skip`);
  - prune a 343 MB CUDA library plus Mac/Windows binaries (packages go from 1210 MB to 592 MB);
  - `node-pty` compiles from source, so it needs `build-essential` and `python3`;
  - a fresh clone skips history and `website/`, `docs/`, `output/` and `qa/`, for about 2.8 GB in total. An existing `~/starnet` is reused untouched.
- **Verified in a cloud container, with a stand-in model:**
  - StarNet's full UI rendered;
  - its custom-provider probe reported Jarvis reachable and verified;
  - a chat run and an 87-tool task run finished `done` at $0;
  - Jarvis's kill switch surfaced inside StarNet.
- **Not verified on the Chromebook.**
- **Safety.** StarNet's first-run screen offers ASK FOR APPROVAL (the default) or FULL POWER. The handoff's "no YOLO agents" rule means choosing ASK FOR APPROVAL. The launcher only advises this; it never sets approval.
- **Bug A and Bug C.** The launcher removes the provider keys from StarNet's environment, so StarNet's own Groq path (Bug A) is never used. It passes `CUSTOM_OPENAI_BASE_URL` so the backend knows Jarvis. In StarNet's UI the address must still be typed with `http://` (Bug C, cause 2).

> **Disagreement (2026-09-24 handoff PART 8 vs the human's 2026-09-26 ruling):** the handoff says "Do not chase a StarNet clone... Add a station view to Jarvis instead." The human now explicitly wants StarNet's exact interface on ChromeOS, and accepts either running StarNet itself or a clone. The build follows the human's ruling by running StarNet itself, and the handoff's advice stays as the record. The earlier Station tab ([[jarvis-x-station-view]]) is now optional, and whether to keep it is the human's call.

## Verdict (PART 8)

> Do not chase a StarNet clone. Jarvis already has 80% of StarNet's useful features. Add a station view to Jarvis instead.

PART 7 (Priority 3) puts it this way:

> StarNet is the ambition; a station tab in Jarvis is achievable.

The planned replacement is the [[jarvis-x-station-view]]: a "Station" tab in Jarvis's React frontend with a roster at `config/agents.yaml`. Interpretation (not stated in the handoff): the multi-agent roster idea echoes the July 2026 [[the-council]] plans; the handoff itself doesn't connect StarNet or the station view to the Council. Full source summary: [[source-jarvis-x-starnet-handoff]]. For how StarNet and the station view compare with the plans' multi-agent design, see [[jarvis-x-plan-vs-reality]].
