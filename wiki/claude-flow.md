---
title: Claude Flow
tags: [entity, agent-framework, plugins, federation]
sources:
  - raw/2026-07-27-ruflo-federation-plugin.md
related: [[ruflo]], [[agent-secure-comms]]
last_updated: 2026-09-25
---

# Claude Flow

A separate project that is compatible with [[ruflo]]. The source describes it as "a separate but compatible project" that "shares the plugin-agent-federation package". It offers a second install path for the federation plugin behind [[agent-secure-comms]].

## Install path for the federation plugin

```bash
npx claude-flow@latest plugins install @claude-flow/plugin-agent-federation
```

The same package also installs through Ruflo's own plugin marketplace (`ruvnet/ruflo`):

```
/plugin install ruflo-federation@ruflo
```

## What the vault doesn't know yet

The source says nothing about Claude Flow beyond this install path: not its maintainers, features, or relationship to Ruflo beyond sharing the package. This page stays a stub until a source covers it. Research candidate.

## Related

[[ruflo]] | [[agent-secure-comms]]
