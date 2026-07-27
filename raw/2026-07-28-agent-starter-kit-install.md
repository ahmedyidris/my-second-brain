# Agent Starter Kit — Install Commands

## Source
`~/my-second-brain/.claude/skills/agent-starter-kit/install.sh`

## Usage variants

```bash
bash install.sh                 # Claude Code — installs everything
bash install.sh --agent cursor  # Cursor — installs the Tier 1 skills
bash install.sh --agent codex   # Codex  — installs the Tier 1 skills
bash install.sh --agent '*'     # every detected agent
bash install.sh --skills-only   # skip the Claude-Code-only plugins/MCPs
```

## What gets installed

### Tier 1 — Skills (all agents)
- find-skills
- agent-browser
- karpathy-guidelines
- ui-ux-pro-max
- caveman
- arabic-design

### Tier 2 — Claude Code plugins/MCPs only
- frontend-design
- code-review
- claude-md-management
- playwright
- github
- superpowers

## Install path
Skills land in `~/.claude/skills/` (global) or `.claude/skills/` (project-scoped).
Plugins register in `~/.claude/plugins/`.
