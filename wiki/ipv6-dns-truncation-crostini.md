---
title: IPv6 DNS Truncation on Crostini
tags: [jarvis-x, starnet, infrastructure, gotcha, networking]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x-hardware]], [[jarvis-x]], [[starnet]], [[crostini]], [[groq]], [[openrouter]], [[jarvis-x-runtime]], [[source-jarvis-x-starnet-handoff]]
last_updated: 2026-09-24
---

# IPv6 DNS Truncation on Crostini

Environment-level networking bug affecting both [[jarvis-x]] and [[starnet]] on Crostini (Debian 13 trixie, ChromeOS Linux container). For the environment as a whole (RAM, disk, the other gotchas), see [[crostini]].

## Symptom

Crostini resolves hostnames to IPv6 first. For Cloudflare-fronted APIs ([[groq]], [[openrouter]]), the IPv6 path truncates POST request bodies. The handoff lists this as one of three likely causes of [[starnet]] Bug A (the sidecar dies silently on Groq calls). None of the three is confirmed.

## System-level fix

```bash
sudo tee -a /etc/gai.conf > /dev/null << 'EOF'
precedence ::ffff:0:0/96  100
EOF
```

This forces IPv4 preference at the glibc resolver level.

## Node-specific fix (partial)

```bash
export NODE_OPTIONS="--dns-result-order=ipv4first"
```

This covers Node's `dns` module resolution order, but **does not** cover Node's `https` module when it uses the bundled c-ares resolver — c-ares ignores `NODE_OPTIONS=--dns-result-order=ipv4first` entirely.

## The trap

If a Node script fails with a network error (timeout, truncation) but `curl` to the same host succeeds, this is why: `curl` uses glibc's resolver (respects `/etc/gai.conf`), while Node's `https.get` uses c-ares (does not). Debugging by "well curl works so the network is fine" is a dead end here — test with Node directly, not curl, when diagnosing Node network failures on this host.

## Where this bites

- `api.groq.com`, `nodejs.org`, and other Cloudflare-fronted hosts have been observed timing out from Node despite `curl` working.
- Applied as a systemd `EnvironmentFile` + `Environment=NODE_OPTIONS=...` override for the `jarvis-supervisord.service` unit (see [[jarvis-x]] and [[jarvis-x-runtime]]), since systemd units don't inherit shell exports.
- Suspected root cause of [[starnet]]'s unresolved Bug A (Groq kills the sidecar). Not yet confirmed — the `/etc/gai.conf` and `NODE_OPTIONS` fixes were applied for Jarvis X's own services, but StarNet's sidecar was still observed dying on Groq calls as of 2026-09-24, which is consistent with the c-ares gap above (Node's `https` still bypasses both fixes).
