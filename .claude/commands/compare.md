---
description: Compare multiple agents' perspectives on the same query
argument-hint: <agent1> <agent2> "query" | all "query"
---

# Multi-Agent Comparison

Compares multiple agents' analysis on the same query to identify consensus and disagreements.

## Usage
```
/compare <agent1> <agent2> "query"
/compare all "query"
```

## Available Agents
- `risk` - Risk Manager
- `technicals` - Technical Analyst
- `fundamentals` - Fundamental Analyst  
- `quant` - Quantitative Analyst
- `sentiment` - Sentiment Analyst
- `trader` - Trader

## Examples
```
/compare risk technicals "Should we trim our tech exposure?"
/compare all "Fed policy implications for our portfolio"
/compare sentiment fundamentals "NVDA earnings outlook"
```

## What it does
- Invokes multiple agents simultaneously with the same query
- Each agent provides their specialized perspective
- Provides framework for synthesizing different viewpoints
- Helps identify areas of agreement and disagreement
- Guides Portfolio Manager decision-making

Use this to get comprehensive analysis before major portfolio decisions.