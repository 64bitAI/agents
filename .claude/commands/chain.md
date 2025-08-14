---
description: Chain agents together for multi-perspective analysis
argument-hint: <origin> <target> "query"
---

# Agent Chain Analysis

Chains two agents together, passing the output from the origin agent to the target agent for deeper analysis.

## Usage
```
/chain <origin> <target> "query"
```

## Available Agents
- `risk` - Risk Manager
- `technicals` - Technical Analyst  
- `fundamentals` - Fundamental Analyst
- `quant` - Quantitative Analyst
- `sentiment` - Sentiment Analyst
- `trader` - Trader
- `portfolio` - Portfolio Manager

## Examples
```
/chain risk technicals "NVDA position analysis"
/chain sentiment fundamentals "AAPL earnings reaction"
/chain technicals risk "breakout trade sizing"
```

## What it does
1. Invokes the origin agent with your query
2. Passes the origin agent's analysis to the target agent
3. Target agent provides combined insights and recommendations
4. Saves chain context for debugging and review

Perfect for getting multiple specialized perspectives on complex trading decisions.