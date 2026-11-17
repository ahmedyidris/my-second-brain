---
permalink: second-brain/raw/2026-07-27-ruflo-federation-plugin
title: 2026-07-27-ruflo-federation-plugin
type: note
---

# Ruflo Federation Plugin

Enables agent-to-agent federation (the [[agent-secure-comms]] transport layer).

## Install via Ruflo plugin system
```
/plugin install ruflo-federation@ruflo
```

## Install via claude-flow CLI
```bash
npx claude-flow@latest plugins install @claude-flow/plugin-agent-federation
```

Two install paths:
1. Ruflo plugin marketplace (ruvnet/ruflo)
2. claude-flow — a separate but compatible project; shares the plugin-agent-federation package