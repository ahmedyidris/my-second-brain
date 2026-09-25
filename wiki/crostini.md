---
title: Crostini
tags: [environment, linux, chromebook, networking, jarvis-x, entity]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x-hardware]], [[ipv6-dns-truncation-crostini]], [[jarvis-x-runtime]], [[groq]], [[openrouter]], [[gemini]], [[starnet]], [[ollama]], [[jarvis-x]], [[jarvis-x-voice-engine]], [[constitutional-autonomy]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[aider]]
last_updated: 2026-09-24
---

# Crostini

The Linux environment that [[jarvis-x]] and [[starnet]] run in, as of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]). The handoff describes it as "ASUS Chromebook, Crostini (Debian 13 trixie)". The handoff records three problems here: Crostini resolves IPv6 first, and the IPv6 path truncates POST bodies to Cloudflare-fronted APIs; Node's c-ares resolver path ignores the workarounds; and RAM and disk are limited. For the hardware, see [[jarvis-x-hardware]]. For what runs on it, see [[jarvis-x-runtime]].

## Environment facts (as of the 2026-09-24 handoff)

| Item | Value |
|------|-------|
| Hardware | ASUS Chromebook |
| Linux environment | Crostini (Debian 13 trixie) |
| RAM | 14GB total, ~9-10GB free after Chrome |
| CPU | 11th Gen i5, no GPU |
| Disk | 72GB total, ~11GB free (after cleanup) |
| Python | 3.11 in `~/venv-ai` (uv-managed) |
| Node | 20.x (system), 22.x (bundled for Tauri) |

> **Disagreement (2026-09-24 handoff vs DeepSeek Jarvis X Master Plan):** the earlier plans put Jarvis on a Lenovo Y50-70 running Pop!_OS 24.04 LTS. The handoff has it on this Chromebook under Crostini. The details are on [[jarvis-x-hardware]]. Left for the human to resolve.

## IPv6 truncation with Cloudflare-fronted APIs (fix 5)

This gotcha also has its own page, [[ipv6-dns-truncation-crostini]].

In the handoff's words: "Crostini resolves to IPv6 first. For Cloudflare-fronted APIs (Groq, OpenRouter), the IPv6 path truncates POST bodies."

The two providers named are [[groq]] and [[openrouter]]. The handoff says nothing about whether the [[gemini]] endpoint is affected. The handoff's [[aider]] launch also targets Groq (`groq/openai/gpt-oss-120b`); it doesn't report whether Aider was affected.

### Fix — system-level

```bash
sudo tee -a /etc/gai.conf > /dev/null << 'EOF'
precedence ::ffff:0:0/96  100
EOF
```

### Fix — Node processes (does NOT cover c-ares resolver)

```bash
export NODE_OPTIONS="--dns-result-order=ipv4first"
```

The same setting appears in three other places in the handoff:

| Where | How |
|-------|-----|
| Jarvis systemd drop-in (fix 6) | `Environment="NODE_OPTIONS=--dns-result-order=ipv4first"` in `/etc/systemd/system/jarvis-supervisord.service.d/env.conf` (see [[jarvis-x-runtime]]) |
| StarNet web-mode launch | `NODE_OPTIONS="--dns-result-order=ipv4first" \` prefix on `nohup node sidecar/index.js` (see [[starnet]]) |
| StarNet Priority 1 debug run | same prefix on the foreground `node sidecar/index.js` |

### Caveat — Node's c-ares resolver ignores both fixes

The fix 5 note says: "Node's https.get uses c-ares and ignores both of these. It still times out on nodejs.org, api.groq.com, etc. curl works because it uses glibc's resolver."

Gotcha 5 says: "Node's https ignores NODE_OPTIONS=--dns-result-order=ipv4first when it uses c-ares. curl works because it uses glibc. If a Node script fails with a network error but curl works, that's why."

The two statements differ slightly. The fix 5 note says Node's `https.get` ignores "both of these" (the `gai.conf` change and `NODE_OPTIONS`). Gotcha 5 says it conditionally ("when it uses c-ares") and mentions only `NODE_OPTIONS`. The handoff doesn't say which Node code paths use c-ares.

Implication: a passing curl test on this machine does not prove that a Node client will reach the same endpoint. The Jarvis test commands and the Gemini key check (gotcha 9, on [[gemini]]) both use curl.

### Link to StarNet Bug A (hypothesis only)

Bug A (StarNet Groq runs kill the sidecar) is "Not fixed. Not diagnosed." The handoff says the cause is "Likely one of" three candidates. The first is about this environment: "Streaming HTTP to Cloudflare-fronted endpoints fails silently on Crostini". It is a **hypothesis**, not a finding. The other two candidates are an uncaught async error and a provider-adapter field dereference. See [[starnet]].

The handoff's Priority 2 is to route StarNet through Jarvis, "which handles fallbacks and never dies on truncation". That is the handoff's own claim. It doesn't show how Jarvis avoids truncation.

## RAM and disk pressure

| Resource | Figure (as of the 2026-09-24 handoff) |
|----------|---------------------------------------|
| RAM | 14GB total, ~9-10GB free after Chrome |
| Disk | 72GB total, ~11GB free (after cleanup) |

Gotcha 7: "Chrome tabs eat 10GB of your 14GB. Before any heavy build, close them. free -h should show 6GB+ available."

```bash
free -h
```

Gotcha 8: "The Tauri build is 30-60 min and needs 8GB disk + 6GB RAM. It's rebuildable but not useful for daily work on this hardware."

> **Note — tension inside the handoff:** PART 5 gives "~9-10GB free after Chrome", and gotcha 7 says "Chrome tabs eat 10GB of your 14GB". Taken literally, those don't add up: 10GB used by Chrome would leave about 4GB. One reading is that "after Chrome" means after closing Chrome tabs, but the handoff doesn't say. Left for the human to resolve.

Implication (arithmetic on the handoff's figures):

- With ~11GB of disk free, a Tauri build (8GB disk) would use most of what is left.
- The ~5GB chatterbox checkpoint needed to fix the degraded tts-worker (Bug D, see [[jarvis-x-voice-engine]]) would use nearly half of it.
- The Ollama models present add up to about 13.5GB (see [[ollama]]).

## Machine rule

From PART 8: "Do not run YOLO-mode agents on this machine. The venv and StarNet workspace have both been destroyed by that pattern." Compare with the plan's approval model in [[constitutional-autonomy]].

## Related

[[jarvis-x-hardware]] | [[jarvis-x-runtime]] | [[groq]] | [[openrouter]] | [[gemini]] | [[starnet]] | [[ollama]] | [[aider]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
