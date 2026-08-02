---
title: PAL MCP
tags: [tool, mcp, multi-model, orchestration]
sources:
  - https://github.com/BeehiveInnovations/pal-mcp-server (accessed 2026-08-02)
  - https://glama.ai/mcp/servers/BeehiveInnovations/pal-mcp-server (accessed 2026-08-02)
  - https://www.decisioncrafters.com/pal-mcp-server-revolutionary-multi-model-ai-development/ (accessed 2026-08-02)
related: [[the-council]], [[agent-secure-comms]], [[ruflo]]
last_updated: 2026-08-02
---

# PAL MCP

**PAL = Provider Abstraction Layer.** A Model Context Protocol server that lets Claude Code, Gemini CLI, Codex CLI, Qwen Code CLI, Cursor, and VS Code extensions work as one across multiple model providers — Gemini, OpenAI (GPT-5 series, O3), Azure OpenAI, X.AI Grok, OpenRouter, DIAL, and local Ollama models. Requires Python 3.10+, Git, and the `uv` package manager.

## Install

```bash
git clone https://github.com/BeehiveInnovations/pal-mcp-server.git
cd pal-mcp-server
./run-server.sh
```

The script handles environment setup, configuration, API key loading, and auto-configuration for Claude Desktop, Claude Code, Gemini CLI, and Codex CLI. (`uvx` is available as a clone-free alternative.)

## The `clink` tool

`clink` ("CLI + Link") is PAL's mechanism for turning a single CLI session into a multi-agent orchestrator:

- **CLI subagents** — launch isolated CLI instances from within the current session (e.g. Claude Code spawning a Codex subagent, which can itself spawn a Gemini CLI subagent).
- **Context isolation** — subagent investigations run without contaminating the primary workspace's context.
- **Role specialization** — subagents can be spawned with specialized system prompts (planner, code reviewer, etc.), e.g. *"clink with codex codereviewer to audit auth module for security issues."*
- **Seamless continuity** — subagent responses feed back with full conversation context preserved; sub-CLIs participate as first-class members, not one-shot tool calls.

## Role in this vault's ecosystem

PAL MCP is the "Team Connector" member of [[the-council]], sitting between the Claude Orchestrator and the other CLI-based council members (Codex CLI, Gemini CLI) — see `the-council.md`'s integration architecture diagram. Because `clink` lets one CLI spawn and hand off to another with full context, the identity-verification and injection-blocking guarantees in [[agent-secure-comms]] are directly relevant here: a compromised subagent spawned via `clink` could otherwise inject instructions back into the orchestrator.
