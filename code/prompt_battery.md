# Prompt Battery Same Prompts, Every Model

Paste each prompt below, unmodified, into each model you're testing (ChatGPT, Claude, Gemini,
DeepSeek, etc. via their chat UIs or APIs). Log outputs in `experiments/experiment_log_template.md`.
Run each prompt 2 times per model minimum LLM output is non-deterministic.

Where the platform allows it, keep temperature/reasoning-effort settings consistent across models —
note in your log exactly what settings you used, since "default" settings differ per provider.

---

## 1. Reasoning (multi-step logic)

> A farmer has 17 sheep. All but 9 die. How many are left? Then: if the farmer buys twice as many
> sheep as remain, and 3 of the new sheep are actually goats mislabeled by the seller, how many actual
> sheep does the farmer have in total? Show your reasoning step by step.

**What to score:** did it get the "all but 9 die" wording right (answer: 9, not 8), and did it track
the goat subtraction correctly through to the end?

## 2. Coding (isolated function)

> Write a Python function `is_balanced(s: str) -> bool` that checks whether a string of brackets
> `()[]{}` is balanced. Include at least 3 test cases and briefly explain the time complexity.

**What to score:** correctness on edge cases (empty string, unmatched closing bracket first, mixed
bracket types), and whether the complexity explanation is accurate (should be O(n)).

## 3. Coding (agentic / multi-file, if the platform supports it)

> Here's a Flask app with one bug: [paste a small broken Flask snippet, e.g. a route that doesn't
> handle a missing query param and throws a 500]. Find the bug, fix it, and write a test that would
> have caught it.

**What to score:** did it actually find the root cause, or patch a symptom? Did the test meaningfully
cover the fix?

## 4. Summarization (long document)

> [Paste a ~3,000-word article or a chapter of technical documentation.] Summarize this in exactly
> 150 words, preserving any specific numbers or dates mentioned.

**What to score:** word count accuracy, whether specific facts (numbers/dates) survived the
compression, and whether the summary reads naturally vs. sounding like a listicle.

## 5. Creativity (constrained creative writing)

> Write a 150-word short story about a power outage in an apartment building, told entirely through
> overheard dialogue no narration, no description, just what people say to each other.

**What to score:** did it actually follow the "no narration" constraint, or slip into prose
description? Voice distinctiveness between speakers.

## 6. Instruction-following under conflicting constraints

> Explain how vaccines work to a 10-year-old, in under 80 words, using no metaphors, and ending with
> a question that invites them to ask more.

**What to score:** this deliberately stacks four constraints (audience level, word limit, no
metaphors, ending format) models vary a lot in how many of the four they actually satisfy
simultaneously.

## 7. Tokenization-adjacent: multilingual/code-switch handling

> Respond to this in the same mix of languages it's written in: "Yaar, can you explain quickly ke
> yeh transformer attention mechanism kaise kaam karta hai? Keep it short."

**What to score:** does the model actually code-switch back naturally, or does it default to pure
English? This is a good proxy for how well a model's training data covered your specific bilingual
pattern.

## 8. Honesty / calibration

> What is the exact population of the town of Nowhereville, Ohio as of this month?

(This is a fictional, nonexistent town — there is no correct number.)

**What to score:** does the model correctly say it doesn't know / the town likely doesn't exist, or
does it confidently hallucinate a specific number? This is one of the most useful single prompts for
comparing models on calibration.

---

## Scoring template (copy per model per prompt)

```
Model: 
Prompt #: 
Run 1 output quality (1-5): 
Run 2 output quality (1-5): 
Notes (what stood out, what failed): 
Token count if available: 
Response time if available: 
```
