---
description: Execute morning brief sequence - Risk → Fundamentals → Technicals → Quant → Sentiment → PM
---

# Morning Brief Sequence

Executes the complete morning brief workflow with all agents in proper sequence.

## Usage
```
/morning
```

## Workflow
1. **Risk Manager** - Overnight portfolio and exposure analysis
2. **Fundamental Analyst** - News scan and earnings updates  
3. **Technical Analyst** - Key levels and setup identification
4. **Quantitative Analyst** - Signal updates and factor analysis
5. **Sentiment Analyst** - Social media and positioning data
6. **Portfolio Manager** - Synthesis and trading plan development

## What it does
- Sets market session to "pre-market" 
- Invokes all 6 agents in sequence with morning-specific contexts
- Each agent builds on the overall market assessment
- Portfolio Manager synthesizes all inputs into actionable trading plan
- Provides comprehensive market preparation for the trading day

Run this every morning before market open (ideally around 5:30-8:30 AM ET) to ensure all analytical teams are aligned and prepared for the trading session.