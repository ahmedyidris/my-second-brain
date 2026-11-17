---
title: StarNet
tags: [starnet, ai-os, multi-agent, entity]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x]], [[jarvis-x-app]], [[ollama]], [[ipv6-dns-truncation-crostini]]
last_updated: 2026-09-24
---

# StarNet

A separate multi-agent chat platform, developed in parallel with [[jarvis-x]]. Repo: `androoAGI/starnet`, local working copy at `~/starnet`, local branch `feat/harness-backend`, working commit `658dc7ce9` (agentId sanitization) as of 2026-09-24.

Runs as a web app: `node sidecar/index.js` → `http://127.0.0.1:8787`. A Tauri desktop shell was built successfully once but was deleted — slow, no benefit over the web UI on this hardware. See [[jarvis-x-app]] guardrail against building Tauri for daily use, which applies equally here.

## Working configuration (2026-09-24)

- Only **Ollama** works as a provider end-to-end.
- Working agent: **Raqib (Overseer)**.
- Working model: `qwen2.5:7b` via [[ollama]] — slow, ~10 tok/s on this hardware.
- Working provider file: `sidecar/providers/openai-compatible.js`.
- Groq and Gemini keys verify as **valid** but every run either returns HTTP 400 or kills the sidecar outright (see Bug A below). Do not select Groq in the UI until that bug is fixed.

## Message sanitization fix (landed, commit 658dc7ce9)

StarNet attaches internal fields (`agentId` and others) to outgoing chat messages. Strict OpenAI-schema validators reject requests carrying those extra fields with HTTP 400.

Fix — filter each message object down to the OpenAI schema before sending, in `sidecar/providers/openai-compatible.js`:

```javascript
req.messages.map(m => {
  const o = {};
  for (const k of ['role','content','tool_calls','tool_call_id','name','function_call']) {
    if (k in m) o[k] = m[k];
  }
  return o;
})
```

## Provider env vars — correct names

The registry reads plain names, **not** an `SKYNET_` prefix:

- `GROQ_API_KEY`
- `GEMINI_API_KEY`
- `OPENROUTER_API_KEY`
- `CUSTOM_OPENAI_BASE_URL`
- `CUSTOM_OPENAI_KEY`

The `SKYNET_<PROVIDER>_API_KEY` pattern seen in `secrets.js` is for Discord/Telegram bot tokens, not provider keys. This was a source of confusion during setup.

## Open bugs (as of 2026-09-24)

**Bug A — Groq runs kill the sidecar.** After picking Groq and sending a message, the sidecar process dies with no error in `/tmp/starnet.log` (log ends normally after "connectors up"). Not diagnosed. Suspected causes: streaming HTTP to Cloudflare-fronted endpoints failing silently on Crostini (see [[ipv6-dns-truncation-crostini]]), an uncaught async error killing Node without logging, or the provider adapter dereferencing a field that doesn't exist for non-Ollama providers. A `stream: false` patch was tried and made things worse (broke Ollama too) — it was reverted. **Priority 1 open item.**

**Bug C — custom provider verification rejects localhost.** Adding `http://127.0.0.1:8000/v1` (the [[jarvis-x-app]] OpenAI-compatible adapter) as a custom provider in the StarNet UI fails verification even with a valid key. `CUSTOM_OPENAI_BASE_URL` env var support exists correctly in the registry, but UI-side verification blocks it. Not fully investigated — the env-var path at launch may bypass UI verification if StarNet reads it at boot. **Priority 2 open item**: routing all StarNet traffic through Jarvis X would let it inherit Jarvis's provider fallbacks and never die on truncation.

## Operational gotcha — workspace lock

StarNet's workspace lock is fragile. After any ungraceful exit, the sidecar refuses to start with `WORKSPACE_BUSY`:

```bash
cat ~/.local/share/StarNet/workspaces/.starnet-workspace-owner.json
# note the PID, kill it if it's dead
pkill -f "node sidecar/index.js"
rm ~/.local/share/StarNet/workspaces/.starnet-workspace-owner.json
```

## Launch command (web mode)

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

Open `http://127.0.0.1:8787`, set Raqib's model to Ollama → `qwen2.5:7b`. Do not pick Groq (Bug A).

## Strategic note

Explicit direction as of 2026-09-24: **do not chase a full StarNet clone inside Jarvis X.** [[jarvis-x]] already has ~80% of StarNet's useful features. The preferred path is a lighter "Station" tab added to Jarvis X's existing React frontend (roster file, four endpoints, simple grid UI, one background worker per agent) rather than continuing to build out StarNet as a second, parallel system. See [[jarvis-x-app]] for the Station-tab plan.
