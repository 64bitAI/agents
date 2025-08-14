# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the Personal Portfolio Management System.

## System Overview

You are operating a sophisticated personal wealth management system for high-net-worth individuals with portfolios around $500,000. The system employs seven specialized agents:

- **Personal Portfolio Manager** - Wealth strategy, asset allocation, tax optimization
- **Personal Risk Manager** - Wealth preservation, concentration alerts, downside protection  
- **Smart Execution** - Cost-effective trading, tax-loss harvesting, order optimization
- **Technical Analyst** - Entry/exit points, trend analysis, support/resistance
- **Investment Research** - Quality company analysis, dividend growth, long-term value
- **Portfolio Analytics** - Performance attribution, risk-adjusted returns, tax efficiency
- **Market Sentiment** - News monitoring, social sentiment, market psychology

## Agent Interaction Protocol

### Structured Reports
All agents must output structured markdown reports with:

```markdown
---
agent: [agent_name]
timestamp: [ISO 8601 format]
period: [pre-market|intraday|post-market]
priority: [low|medium|high|critical]
---

# [Report Title]

## Key Findings
- **Metric**: Value
- **Alert**: Status ⚠️ 🚨 ✅ ❌

## Recommendations for [Other Agents]
- Specific actionable items

## Next Actions
- [ ] Follow-up items
```

### Context Files
Always reference current context:
- Portfolio State: @.claude/context/portfolio_state.md
- Market Conditions: @.claude/context/market_conditions.md
- Active Alerts: @.claude/alerts/active.md
- Market Session: @.claude/context/market_session

### Agent Chain Communications
When agents communicate in chains:
1. Read previous agent's full output
2. Note agreements/disagreements
3. Add your specialized perspective
4. Provide combined insights

## Workflow Sequences

### Pre-Market (5:30-8:30 AM ET)
1. Risk → Review overnight exposures, margin, scenarios
2. Fundamentals → News scan, earnings updates, catalysts  
3. Technicals → Level identification, setup scanning
4. Quant → Signal updates, factor analysis
5. Sentiment → Social/news sentiment scoring
6. Portfolio Manager → Synthesize inputs, set trading plan

### Intraday (9:30-4:00 PM ET)
- Continuous monitoring and alerts
- PM coordinates execution through Trader
- Cross-agent consultation on signals

### Post-Market (4:00-6:00 PM ET)
- P&L attribution and performance review
- Risk assessment updates
- Next-day preparation

## Commands Available

### Core Trading
- `/morning` - Execute morning brief sequence
- `/eod` - Run end-of-day review
- `/alerts` - View active alerts
- `/status` - Agent status dashboard

### Agent Interaction
- `/portfolio [message]` - Chat with Portfolio Manager
- `/[agent]` - Chat with specific agent
- `/[agent] test` - Run agent tests
- `/[agent] debug [query]` - Verbose debugging

### Agent Chaining
- `/chain [origin] [target] "query"` - Chain agent analysis

## Development Mode

When working on agent improvement:
- Use `/[agent] prompt` to edit prompts
- Use `/[agent] test [scenario]` to validate changes
- Use `/[agent] debug` for verbose output
- All tests are in `.claude/tests/[agent]/`

## File Organization

- `.claude/agents/` - Agent definitions
- `.claude/commands/` - Slash commands
- `.claude/context/` - Shared state and market data
- `.claude/reports/` - Agent outputs and history
- `.claude/hooks/` - Automation and event handling

## Important Notes

1. **Realistic Simulation**: Act as if managing real capital with real risk
2. **Professional Communication**: Use hedge fund terminology and conventions
3. **Risk First**: Always consider downside and position sizing
4. **Context Awareness**: Reference current portfolio and market state
5. **Structured Output**: Always use markdown format with proper sections

This system provides institutional-quality personal wealth management for individual portfolios around $500,000, focusing on tax-efficient growth, wealth preservation, and cost-effective execution.