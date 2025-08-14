# Hedge Fund Agent System

A comprehensive Claude Code implementation simulating a boutique hedge fund trading desk with specialized AI agents.

## Overview

This system provides a realistic hedge fund simulation with seven specialized agents:

- **Portfolio Manager** (`/portfolio`) - Decision hub, strategy, P&L oversight
- **Risk Manager** (`/risk`) - Exposure monitoring, VaR, stress testing  
- **Trader** (`/trader`) - Order execution, market microstructure
- **Technical Analyst** (`/technicals`) - Chart patterns, levels, momentum
- **Fundamental Analyst** (`/fundamentals`) - Company research, valuations
- **Quantitative Analyst** (`/quant`) - Models, factors, attribution
- **Sentiment Analyst** (`/sentiment`) - Social media, news, alternative data

## Quick Start

```bash
# Morning workflow
/morning              # Run morning brief sequence
/alerts               # Check active alerts
/portfolio What's our game plan today?

# Agent interaction
/technicals           # Chat with technical analyst
/sentiment test       # Run sentiment tests
/chain risk portfolio "check our exposure"

# End of day
/eod                  # Run EOD review
/status               # Check all agent status
```

## Key Features

- **Structured Workflows**: Pre-market, intraday, and post-market sequences
- **Agent Chaining**: Connect agents for multi-perspective analysis
- **Development Tools**: Test suites, prompt editing, debugging
- **Cross-Platform Notifications**: Desktop alerts for important events
- **Realistic Simulation**: Based on real hedge fund operations

## Agent Capabilities

Each agent produces structured markdown reports and supports:
- Direct chat mode (`/agent`)
- Testing (`/agent test`)
- Debugging (`/agent debug`)
- Prompt editing (`/agent prompt`)
- MCP integration (`/agent mcp server`)

## Folder Structure

```
.claude/
├── agents/           # Agent definitions
├── commands/         # Slash commands  
├── hooks/            # Event automation
├── context/          # Shared state
├── reports/          # Agent outputs
├── alerts/           # Active alerts
└── tests/            # Test suites
```

## Documentation

- [Workflow Guide](docs/workflow-guide.md) - Daily operations
- [Agent Reference](docs/agent-reference.md) - Detailed capabilities  
- [Development Guide](docs/development.md) - Customization and testing

## Getting Started

1. Ensure you have Claude Code installed
2. Navigate to this directory in Claude Code
3. Run `/morning` to start your first trading day
4. Use `/help` or `/agent help` for specific guidance

Built for realistic hedge fund simulation and agent development.