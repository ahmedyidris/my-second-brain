# LLM Wiki Skills — Installation

Clone the skills repo and symlink the two skills into Claude Code's skills directory:

```bash
git clone https://github.com/NulightJens/ai-second-brain-skills.git ~/ai-second-brain-skills
ln -s ~/ai-second-brain-skills/llm-wiki-setup  ~/.claude/skills/llm-wiki-setup
ln -s ~/ai-second-brain-skills/wiki-self-heal  ~/.claude/skills/wiki-self-heal
```

After this, both skills are available as /llm-wiki-setup and /wiki-self-heal in Claude Code.
