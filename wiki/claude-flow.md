---
title: Claude Flow
tags: [tool, agent-architecture, orchestration, naming-collision]
sources:
  - https://github.com/ruvnet/ruflo (accessed 2026-08-02)
  - https://github.com/kodflow/claude-flow (accessed 2026-08-02)
  - https://www.npmjs.com/package/claude-flow (accessed 2026-08-02)
  - https://pasqualepillitteri.it/en/news/774/claude-flow-ruflo-multi-agent-orchestration-guide (accessed 2026-08-02)
related: [[ruflo]], [[agent-secure-comms]], [[the-council]]
last_updated: 2026-08-02
---

# Claude Flow

**"Claude Flow" is the original name of the project now called [[ruflo]].** Per ruvnet/ruflo's own README: *"Claude Flow is now Ruflo — named by rUv, who loves Rust, flow states, and building things that feel inevitable."* The `@claude-flow/` npm/plugin namespace is kept for backward compatibility, including the federation plugin:

```bash
npx claude-flow@latest plugins install @claude-flow/plugin-agent-federation
```

This is the same install path documented on [[ruflo]]'s page as "Federation via claude-flow" — not a separate compatible project as originally recorded, but the predecessor name for the same lineage.

## Naming collision — read before trusting any "claude-flow" repo

The name is not exclusively owned by the ruvnet/ruflo lineage. `kodflow/claude-flow` on GitHub describes itself as a **separate fork**, "forked from Ruflo (ruvnet/ruflo)... evolved from that codebase," at version `v2.0.0 Alpha`, installed via `npx claude-flow@alpha init --force`, with its own feature set (87 MCP tools, "Hive-Mind" queen-led coordination, SQLite memory with 12 tables). There are at least two other similarly-named repos in search results (`erfwn81/ruflow`, `barkain/claude-code-workflow-orchestration`) — this is an actively forked/rebranded ecosystem, not a single canonical project.

**Practical implication:** if researching or installing "claude-flow," confirm which repo/npm version is in play — the ruvnet/ruflo lineage (federation plugin, mTLS + ed25519, PII-stripping, zero-trust agent-to-agent) and the kodflow fork (Hive-Mind, 87 MCP tools) are not guaranteed to be feature-compatible despite sharing a name.

## Federation plugin (ruvnet/ruflo lineage)

`@claude-flow/plugin-agent-federation` lets agents across different machines discover each other, verify identity via mTLS + ed25519, and collaborate — described in the README as `federation init`, `federation join`, and agents "start talking." This is the mechanism enabling [[agent-secure-comms]]'s protocol across machine boundaries, and the same plugin [[ruflo]] documents installing via `/plugin install ruflo-federation@ruflo`.
