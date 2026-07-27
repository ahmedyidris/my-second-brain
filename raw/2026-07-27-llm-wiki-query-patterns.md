# LLM Wiki — Example Query Patterns

Three core prompts that show the wiki in action:

1. "Where do my sources agree and disagree about <topic>?"
   → Contradiction/synthesis query. The LLM reads all pages tagged to the topic, surfaces agreements and conflicts, cites the specific wiki pages and their source frontmatter.

2. "What are the gaps in my wiki right now?"
   → Lint/audit query. Triggers the lint workflow: scans for orphan pages, missing cross-references, concepts referenced ≥2 times without their own page, stale claims, data gaps. Returns a severity-ranked list with proposed fixes.

3. "Write a comparison page for X vs Y and file it back into the wiki."
   → Query + file-back-as-analysis. The LLM synthesizes the comparison from existing pages, writes it as a new analysis page (e.g. wiki/x-vs-y-comparison.md), adds it to wiki/index.md under Analyses, and links it bidirectionally from both X and Y pages. Good answers don't disappear into chat history — they compound.
