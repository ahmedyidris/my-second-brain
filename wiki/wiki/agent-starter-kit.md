---
title: Agent Starter Kit
tags: [skills, plugins, tooling, setup]
sources:
  - raw/2026-07-28-agent-starter-kit-install.md
related: [[llm-wiki-setup-skill]], [[wiki-self-heal-skill]], [[composio]], [[the-council]]
last_updated: 2026-07-28
---

# Agent Starter Kit

A one-command skill + plugin installer for Claude Code (and other agents). Installs 6 Tier 1 skills and 6 Tier 2 Claude Code plugins in a single pass.

## Install

```bash
# Get the skill
npx -y skills add JamalMohafil/claude-skills --skill agent-starter-kit --agent claude-code

# Run the installer
bash ~/.claude/skills/agent-starter-kit/install.sh
```

## Usage variants

```bash
bash install.sh                 # Claude Code — installs everything
bash install.sh --agent cursor  # Cursor — Tier 1 skills only
bash install.sh --agent codex   # Codex  — Tier 1 skills only
bash install.sh --agent '*'     # every detected agent
bash install.sh --skills-only   # skip Claude-Code-only plugins/MCPs
```

## Tier 1 — Skills (all agents)

| Skill | Purpose |
|-------|---------|
| `find-skills` | Discover and install new skills |
| `agent-browser` | Browser automation |
| `karpathy-guidelines` | Karpathy coding philosophy |
| `ui-ux-pro-max` | Advanced UI/UX design |
| `caveman` | Simplified explanations |
| `arabic-design` | Arabic-first design patterns |

## Tier 2 — Claude Code plugins/MCPs

| Plugin | Purpose |
|--------|---------|
| `frontend-design` | Frontend design tools |
| `code-review` | Automated code review |
| `claude-md-management` | CLAUDE.md lifecycle management |
| `playwright` | E2E browser testing |
| `github` | GitHub integration |
| `superpowers` | Extended agent capabilities |

## Install paths

- Skills → `~/.claude/skills/` (global) or `.claude/skills/` (project-scoped)
- Plugins → registered in `~/.claude/plugins/` and `~/.claude/settings.json`
