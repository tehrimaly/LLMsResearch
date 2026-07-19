# 03 — Strengths by Task: Reasoning, Coding, Summarization, Creativity

Benchmarks are noisy and vendor-reported numbers should be treated skeptically (everyone's own
benchmark chart puts their own model near the top). Treat the table below as a *starting hypothesis
to test yourself* with `code/prompt_battery.md`, not a verdict.

## Reasoning (math, logic, multi-step problems)

- **Grok 4.3** and **Gemini 3.1 Pro / Deep Think** are frequently cited as pure-reasoning leaders on
  benchmarks like GPQA Diamond and ARC-AGI-2.
- **Claude Opus**-tier models are consistently described as strong on thorough, cautious analysis —
  identifying subtle patterns and flagging their own uncertainty rather than overstating confidence.
- **DeepSeek**'s reasoning-tuned models (R1-lineage successors) punch well above their price point on
  quantitative/chain-of-thought reasoning.
- Takeaway: reasoning quality correlates with how much "thinking" budget a model is allowed to spend —
  most 2026 frontier models now expose an explicit reasoning-effort dial (none → max). A fair
  comparison means matching effort level, not just model name.

## Coding

- **DeepSeek V4 Pro** leads open-weight coding benchmarks (SWE-Bench Verified) at a small fraction of
  frontier closed-model pricing.
- **GPT-5.6 Sol** and **Claude Opus/Sonnet** lead on real-world agentic coding benchmarks
  (Terminal-Bench 2.x, long-horizon SWE tasks) — tasks that require using tools, running code, and
  iterating, not just producing a single correct function.
- **Qwen3-Coder-Next** and **Mistral Small 4 (Devstral-style)** are built specifically to be small and
  cheap enough to self-host as coding agents rather than to top a leaderboard.
- Takeaway: "best at coding" splits into two very different things — best at solving an isolated
  LeetCode-style problem, vs. best at multi-step agentic work (editing a real repo, running tests,
  fixing failures). Always specify which one you're testing.

## Summarization / long-document work

- Context window size matters less than *effective recall within that window*. Llama 4 Scout's
  10M-token window is the largest available, but independent testing shows recall degrades well
  before the advertised ceiling — it's best used for targeted retrieval in a huge document, not
  faithful end-to-end summarization of the whole thing.
- Gemini 3.1 Pro's 1M window with native multimodality makes it a strong pick for summarizing mixed
  content (a document with embedded images/charts, or a video transcript).
- For pure text summarization at moderate length, cost-efficient models (Gemini 3.1 Flash-Lite,
  DeepSeek V4 Flash) are usually "good enough" — this is a task where you rarely need the most
  expensive model.

## Creativity (writing, ideation, style)

- Consistently the hardest dimension to benchmark objectively — there's no equivalent of SWE-Bench for
  "is this a good short story."
- Anecdotally and in most public writing-quality comparisons, **Claude** and **GPT** flagship models
  are most often cited for prose quality and following nuanced style instructions; **Mistral Large**
  has been noted as punching above its price point on natural-sounding output.
- Practical test: give the same creative brief (see `code/prompt_battery.md`) to 3+ models and score
  blind — you'll likely find personal/domain preference matters more than any benchmark number here.

## A note on how to actually run this comparison fairly

1. Match reasoning-effort settings across models where the API exposes that dial.
2. Run each prompt 2-3 times per model — outputs are non-deterministic, and a single sample can
   mislead you.
3. Separate "one-shot correctness" tasks (coding a function, answering a factual question) from
   "open-ended quality" tasks (writing, summarizing) — they need different scoring rubrics.
4. Keep the *exact* prompt text identical across models, including system-prompt-equivalent
   instructions if the platform allows setting one — small wording differences change outputs more
   than people expect.
