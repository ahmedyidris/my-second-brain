# LLM Wiki — Self-Heal Trigger Prompt

"Run wiki-self-heal on this vault"

Triggers the autonomous audit + research loop from the wiki-self-heal skill:
1. Reads CLAUDE.md, wiki/index.md, last 10 log entries
2. Creates a dedicated heal branch (wiki-heal/YYYY-MM-DD)
3. Audits for 6 gap types: contradictions, stale claims, orphans, missing pages, missing cross-refs, data gaps
4. Researches and fills top-N high-severity gaps (default N=3)
5. Commits changes to the heal branch — never auto-merges to main
6. Reports what was created, updated, skipped

For audit-only (no changes): "Run wiki-self-heal audit-only" or "dry run wiki-self-heal"
For scheduling: see wiki-self-heal skill scheduling references
