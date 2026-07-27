---
title: Agent-to-Agent Secure Communication
tags: [security, agent-architecture, protocol, trust]
sources:
  - raw/2026-07-27-agent-secure-comms.md
related: [[ruflo]], [[the-council]], [[constitutional-autonomy]], [[jarvis-x]], [[claude-flow]]
last_updated: 2026-07-27
---

# Agent-to-Agent Secure Communication

A protocol for agents communicating with other agents safely. Five layers on the send path, three on the receive path, plus a meta-layer for reputation.

## The protocol

```
Your Agent --> [ Remove secrets ] --> [ Sign message ] --> [ Encrypted channel ]
                 Emails, SSNs,        Proves it came       No one reads it
                 keys stripped         from you              in transit
                                                                |
                                                                v
Their Agent <-- [ Block attacks ] <-- [ Check identity ] <------+
                 Stops prompt          Rejects forgeries
                 injection

                          Audit trail on both sides.
                  Trust builds over time. Bad behavior = instant downgrade.
```

## Send path (your agent)

| Step | What it does | Why it matters |
|------|-------------|----------------|
| Remove secrets | Strip emails, SSNs, API keys before send | Prevents accidental credential leakage to untrusted agents |
| Sign message | Cryptographic proof of origin | Receiving agent can verify the message is genuinely from you |
| Encrypted channel | Payload unreadable in transit | No eavesdropping on the wire |

## Receive path (their agent)

| Step | What it does | Why it matters |
|------|-------------|----------------|
| Check identity | Verify sender signature | Rejects forgeries — no impersonation |
| Block attacks | Filter prompt injection attempts | Malicious agents can't hijack the receiver's behaviour via crafted payloads |

## Trust layer

- **Audit trail** — both sides log every message independently
- **Reputation** — trust score accumulates over time through observed behaviour
- **Downgrade** — bad behaviour (injection attempts, forged messages, secret leakage) triggers immediate trust downgrade

## Enabling layer: ruflo-federation

The `ruflo-federation` plugin implements this protocol in [[ruflo]]:

```
/plugin install ruflo-federation@ruflo
# or via claude-flow:
npx claude-flow@latest plugins install @claude-flow/plugin-agent-federation
```

## Relationship to Ruflo and Jarvis X

In [[ruflo]]'s architecture, this protocol governs how the Swarm agents communicate with external agents or services. In [[jarvis-x]], [[constitutional-autonomy]] handles the governance side (what agents may do), while this protocol handles the transport side (how agents communicate safely). The audit trail requirement mirrors the append-only audit log in [[constitutional-autonomy]].

The [[the-council]] members (Claude, Codex, Gemini, etc.) communicating via PAL MCP would benefit from this pattern — identity verification prevents a compromised sub-agent from injecting malicious instructions into the orchestrator.
