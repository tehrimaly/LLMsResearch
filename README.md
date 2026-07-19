# LLM Research Deep Dive on Major Language Models (2026)

Independent research project comparing today's major LLM families: architecture, tokenization,
context windows, task-specific strengths, and hands-on usage. Built as part of an ML engineering
internship — the goal isn't a shallow spec-sheet comparison, it's understanding *why* these models
behave differently and *how* to prove it experimentally.

## Repo structure

```
llm-research/
├── README.md                          ← you are here
├── research/
│   ├── 01_model_landscape.md          ← every major model family: who makes it, architecture, scale, license
│   ├── 02_tokenization_deep_dive.md   ← BPE vs SentencePiece vs tiktoken, vocab sizes, why token counts differ
│   ├── 03_strengths_by_task.md        ← reasoning / coding / summarization / creativity, model-by-model
│   └── 04_context_windows_and_pricing.md
├── code/
│   ├── tokenizer_comparison.py        ← run the same text through multiple real tokenizers, compare counts
│   └── prompt_battery.md              ← a fixed set of prompts to test every model on the same tasks
└── experiments/
    └── experiment_log_template.md     ← template for recording your own model outputs + scores
```

## How to use this repo

1. Read `research/01_model_landscape.md` first for the big picture.
2. Run `code/tokenizer_comparison.py` locally (needs internet + `pip install tiktoken transformers`) to see
   real token counts for the same sentence across model families.
3. Use `code/prompt_battery.md` as your test set — paste the same prompts into ChatGPT, Claude, Gemini,
   DeepSeek, etc., and log what you find in `experiments/experiment_log_template.md`.
4. Everything is markdown-first so it renders cleanly on GitHub with no extra tooling.

## Why this matters (the actual research angle)

Benchmark leaderboards tell you *what* score a model got. They don't tell you:
- why the same 20-word sentence costs 35% more tokens on one model than another (tokenizer design)
- why a model that wins on reasoning benchmarks can still write worse prose (different training objectives)
- why "context window" on a spec sheet isn't the same as *usable* context in practice (recall degrades
  long before the limit)

This repo tries to build intuition for those questions, not just repeat vendor marketing pages.

## Status

Research current as of **July 2026**. Model landscape moves fast check the "last verified" date at the
top of each file before citing numbers from here in anything formal.
