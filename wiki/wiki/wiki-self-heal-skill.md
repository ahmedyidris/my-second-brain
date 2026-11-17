---
title: wiki-self-heal Skill
tags: [skill, meta, maintenance, llm-wiki]
sources:
  - raw/ai-second-brain-skills/wiki-self-heal/SKILL.md
related: [[llm-wiki-pattern]], [[llm-wiki-setup-skill]], [[second-brain]]
last_updated: 2026-07-27
---

# wiki-self-heal Skill

Autonomous audit + research loop for a Karpathy-style LLM wiki. Finds what's weak or missing, researches high-quality answers, writes them into the wiki, and commits to a dedicated branch for human review. Never auto-merges.

Installed at `~/.claude/skills/wiki-self-heal` → invoked as `/wiki-self-heal` in Claude Code.

## Two modes

- **Full mode** (default) — audit → research → apply → commit on a heal branch
- **Audit-only** — audit → report only; no wiki pages changed. Use first.

Trigger phrases: "lint my wiki", "self-heal", "find gaps", "dry run wiki-self-heal", "audit only"

## The loop (full mode)

1. Read `CLAUDE.md`, `wiki/index.md`, last 10 `wiki/log.md` entries
2. `git checkout -b wiki-heal/YYYY-MM-DD`
3. Audit for 6 gap types (see below) → write `wiki/audits/audit-<date>.md`
4. Audit-only early exit if dry-run mode
5. Pick top N=3 high-severity, researchable gaps
6. Research each with ≥2 independent sources; reject SEO spam
7. Create/update wiki pages, add bidirectional `[[wikilinks]]`, update index
8. Append one entry to `wiki/log.md`
9. `git add wiki/ && git commit -m "heal: N gaps addressed, S skipped"`
10. Report — stay on branch, do not merge

## 6 gap types audited

1. Contradictions between pages
2. Stale claims superseded by newer sources
3. Orphan pages (no inbound wikilinks)
4. Missing pages (concepts referenced ≥2 times without a page)
5. Missing cross-references
6. Data gaps (concepts lacking depth)

## Simplicity rule

Fewer new pages wins. Prefer updating existing pages over creating stubs. A run that adds zero pages but strengthens existing ones is a success.

## Scheduling

Recommended: weekly for active vaults. Run manually in audit-only mode at least once before automating. See `/schedule` skill for cloud-agent setup.

## Installation

```bash
git clone https://github.com/NulightJens/ai-second-brain-skills.git ~/ai-second-brain-skills
ln -s ~/ai-second-brain-skills/wiki-self-heal ~/.claude/skills/wiki-self-heal
```
