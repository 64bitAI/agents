---
description: Show detailed status dashboard for all agents
---

# Agent Status Dashboard

Displays comprehensive status information for all agents and system health.

## Usage
```
/status
```

## What it shows
- **Market Session**: Current trading session (pre-market, intraday, post-market)
- **Portfolio Summary**: NAV, P&L, key metrics
- **Agent Status**: Last update times, priorities, alert counts for each agent
- **Development Status**: Available test suites per agent
- **Available Commands**: Quick reference for system commands

## Agent Status Information
For each of the 7 agents (Portfolio, Risk, Trader, Technicals, Fundamentals, Quant, Sentiment):
- Last report timestamp
- Current priority level
- Market session context
- Number of active alerts
- Activity status

## Development Information  
- Test suite availability for each agent
- System health indicators
- Available debugging and testing commands

Use this to quickly assess system health and agent activity levels throughout the trading day.