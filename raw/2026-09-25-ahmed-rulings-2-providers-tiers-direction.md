# Ahmed's rulings (2): free vs paid, providers, tier names, direction
# Date: 2026-09-25
# Author: Ahmed Yidris (chat reply in the Claude Code session that ingested the 2026-09-24 handoff)

---

## Context: the eight open questions this reply answers

1. gpt-oss (OpenAI's open-weight model, free on Groq): slot 1 (free open-source) or slot 4 (OpenAI)?
2. Gemma (Google's open models): slot 1, slot 2 or both?
3. Kimi: where does it sit in the paid slot, and does a free route (OpenRouter `:free`) move it up?
4. Tier names: the plan's `long` vs the as-built `quality` / `frontier`?
5. Does the Lenovo upgrade roadmap still apply?
6. Which adapter does "do not re-enable stream: false" refer to?
7. Does $0/month still bind?
8. Keep `gemini-3.6-flash`, or move to Flash-Lite, which reportedly has higher free limits?

## Reply (verbatim)

> 1. If it’s free make it count as free but if it’s name is open AI you can leave it’s name as it is , it depends on what’s official name of model and also if free 100% should be in free tier. 2 if it fits both let it be in both. 3.Kimi is Kimi it have multiple models , if it’s paid put it as standalone paid model, if it have a free tier yes add in free tiers and also how it should be accessible, for example all models that are free and accessible through a provider should be done through and under that provider even if it could be done through another one, it will also be there. 4. Tier names should be as they are, copy Starnet way, it should be either by provider using api or local, 5.which Lenovo ignore it for now .6 I don’t know I was actually trying to set up Starnet and merge with Jarvis, then I was thinking of building Jarvis using Starnet but it didn’t work with me then I thought it could be built as part of Jarvis, now I want to complete both and merge in this repo in a meaning that I want to continue working on Jarvis when I setup Starnet but I want to know what are you doing right now and what did you understand I want to do from the beginning 7. Still zero but leave it as an option.8. Yes we need more tokens.

## Rulings as stated (no interpretation added)

1. **Free counts as free.** A model that is 100% free goes in the free tier, even if its official name contains "OpenAI" (e.g. gpt-oss). Keep each model's official name.
2. **Fits both → list in both** (e.g. Gemma in the local/open slot and the Google slot).
3. **Kimi:**
   - Kimi has multiple models. A paid Kimi model is listed as a standalone paid model.
   - A Kimi model with a free tier is also listed in the free tiers, with how to access it.
   - General rule: a free model accessible through a provider is listed under that provider. If several providers serve it, it appears under each of them.
4. **Tier names stay as they are.** Follow StarNet's way: a model is chosen either by provider (through its API) or local.
5. **Lenovo:** ignore it for now.
6. **stream:false:** unknown. **Direction:**
   - History: the human was trying to set up StarNet and merge it with Jarvis. Then they considered building Jarvis using StarNet, which didn't work. Then they thought StarNet could be built as part of Jarvis.
   - Now: "complete both and merge in this repo", meaning they want to keep working on Jarvis while setting up StarNet.
   - The human asked what the assistant is doing now, and what it understood the human wanted from the beginning.
7. **Budget:** still $0, with paid options left available.
8. **Tokens:** "Yes we need more tokens." This answers question 8.
