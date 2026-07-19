# 04 — Context Windows & Pricing Snapshot (verified July 2026)

Prices and windows shift constantly — this is a snapshot, not a permanent reference. Always check the
provider's own pricing page before quoting these in something formal (thesis, report, client doc).

| Model | Context window | Input $/M tokens | Output $/M tokens | Notes |
|---|---|---|---|---|
| GPT-5.6 Sol | ~1.05M | $5.00 | $30.00 | flagship reasoning/coding |
| GPT-5.6 Terra | ~1.05M | $2.50 | $15.00 | balanced |
| GPT-5.6 Luna | ~1.05M | $1.00 | $6.00 | cost-optimized |
| Claude Opus 4.8 | up to 1M | $5.00 | $25.00 | highest-capability Claude |
| Claude Sonnet 5 | up to 1M | $3.00 | $15.00 | balanced Claude |
| Gemini 3.1 Pro | 1M (2x price >200K) | $2.00 | $12.00 | flagship reasoning, multimodal |
| Gemini 3.5 Flash | 1M | $1.50 | $9.00 | agentic/coding-optimized |
| Gemini 3.1 Flash-Lite | 1M | $0.25 | $1.50 | budget tier |
| Llama 4 Scout | 10M (self-hosted or 3rd-party) | hardware/hosting cost only | — | largest open-weight window |
| DeepSeek V4 Pro | 1M | ~$0.435 | ~$0.87 | best open-weight coding value |
| DeepSeek V4 Flash | 1M | ~$0.14 | ~$0.28 | cheapest viable coding option in the market |
| Grok 4.3 | 128K | subscription-gated (SuperGrok Heavy, ~$300/mo for top tier) | — | smallest context window among current flagships |
| Qwen 3.5 / 3.7 Max | up to 1M (preview pricing varies) | varies | varies | 200+ languages supported |
| Mistral Large 3 | large (varies by deployment) | open weights, Apache 2.0 | — | EU/compliance-friendly |

## Reading this table correctly

- **"Context window" ≠ "effective context."** Every model's ability to actually *use* information
  degrades to some degree as you approach the advertised limit. Treat the number as a ceiling, not a
  guarantee.
- **Long-context surcharges are common.** Several providers (notably Google) charge roughly double the
  input rate once you pass ~200K tokens in a single request — factor this in before assuming "1M
  tokens" is a flat-rate deal.
- **Open-weight "pricing" is really a hosting decision.** DeepSeek/Llama/Qwen prices above are for
  *hosted* API access from the model's own provider or a cloud partner. If you self-host, your real
  cost is GPU/hardware time, which can be far cheaper at high volume and far more expensive at low
  volume (idle GPU cost) than a pay-per-token API.
- **Caching changes the math substantially.** Most providers offer a cheaper rate for repeated/cached
  context (e.g., a long system prompt reused across many calls). If you're building anything with a
  fixed long instruction set, this is usually worth implementing.
