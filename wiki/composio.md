---
title: Composio
tags: [tool-connector, integrations, council, mcp]
sources:
  - raw/2026-07-27-composio-setup.md
related: [[the-council]], [[jarvis-x]], [[ruflo]], [[agent-secure-comms]]
last_updated: 2026-07-27
---

# Composio

A tool connector platform with 1000+ app integrations. Member of [[the-council]] as the "Tool Connector" role — bridges Jarvis X agents to external services without custom API wiring per integration.

## Installation

```bash
curl -fsSL https://composio.dev/install | bash
```

Installs the binary to `~/.composio/composio`. PATH update requires a shell restart (or use the full path in the current session).

```bash
~/.composio/composio --version  # verify
```

## Login

```bash
composio login
# or before shell restart:
~/.composio/composio login
```

Opens a browser to `composio.dev`. Authenticate there; the CLI confirms once done.

## MCP endpoint

Previously configured in the DeepSeek master plan via web UI: Customize → Connectors → Add Custom Connector, URL: `https://connect.composio.dev/mcp`. This exposes Composio as an MCP server — any MCP-compatible agent (including Claude Code) can call Composio tools through this endpoint.

## Role in Jarvis X

Composio provides the integration surface that would otherwise require hand-rolling each API client. In [[the-council]], it sits between the agents and external services (email, calendars, databases, SaaS tools). Combined with [[ruflo]]'s plugin system and [[agent-secure-comms]], agents can call external tools with secret-stripping and identity verification applied before the call leaves the system.
