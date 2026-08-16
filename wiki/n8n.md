---
title: n8n
tags: [tool, automation, workflow, integrations]
sources:
  - https://github.com/n8n-io/n8n (accessed 2026-08-16)
  - https://www.digitalocean.com/community/conceptual-articles/n8n-workflow-automation-guide (accessed 2026-08-16)
related: [[jarvis-x-income-roadmap]], [[source-jarvis-x-v2-ascension-plan]], [[composio]]
last_updated: 2026-08-16
---

# n8n

A fair-code workflow automation platform with native AI capabilities — visual canvas for building workflows, with JavaScript/Python/npm-package escape hatches for custom logic. Named twice in this vault ([[jarvis-x-income-roadmap]]'s "Background" row, [[source-jarvis-x-v2-ascension-plan]]'s v1→v2 changes table) with zero elaboration until this pass.

## What it is

- 1500+ pre-built integrations (per the project's own GitHub README, Aug 2026) connecting apps, APIs, and databases without hand-writing each client.
- 9,000+ community workflow templates to start from instead of building from scratch.
- Multi-step AI agent workflows: chains tool use and logic across steps, with first-class support for OpenAI, Anthropic, Google, and open-source models as workflow nodes.
- Role-based access, audit trails, and enterprise security features available on paid tiers.

## License & deployment

"Fair-code" — Sustainable Use License for the self-hosted core (source-available, free to self-host and extend, restrictions mainly around reselling n8n itself as a competing service), with a separate Enterprise License unlocking additional features. Not OSI-approved open source, but free and inspectable.

Two deployment paths:
- **Self-hosted** — full control, run on your own infrastructure (Docker or `npx n8n` for a quick local start; requires Node.js).
- **n8n.cloud** — hosted/managed option.

## Role in this vault

Named in [[jarvis-x-income-roadmap]] as a "Background" skill-building track (ongoing, low-hours) toward the Bilingual AI Operations Specialist path — building visible automation demos strengthens the freelance/consulting pitch described there. [[source-jarvis-x-v2-ascension-plan]] lists "Outlier + n8n gigs" as the v1 income model, superseded in v2 by [[jarvis-x-content-engine]] as income stream #3 (n8n skill-building continues as a background thread, not replaced).

Complementary to [[composio]]: n8n gives you a visual workflow canvas with its own integration nodes; Composio gives an MCP-native tool-connector surface for agents (like [[jarvis-x]]'s [[the-council]]) to call external services directly. A Jarvis X build could reasonably use n8n for scheduled/visual automations and Composio for agent-initiated tool calls — the vault doesn't currently specify which handles what, which is worth resolving if both get built out.
