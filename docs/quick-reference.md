# Quick Reference Guide

## Core Commands

### Trading Workflow
```bash
/morning           # Execute morning brief sequence (Risk → Fund → Tech → Quant → Sentiment → PM)
/eod               # End-of-day review and performance attribution
/alerts            # View all active alerts across agents
/status            # Detailed agent status dashboard
/statusline        # Rotating status line (use 'next' to rotate)
```

### Agent Interaction
```bash
/portfolio [msg]   # Chat with Portfolio Manager (primary interface)
/risk [subcommand] # Risk manager (exposure, VaR, stress tests)
/technicals        # Technical analyst (charts, levels, patterns)  
/fundamentals      # Fundamental analyst (valuations, earnings)
/quant             # Quantitative analyst (models, factors)
/sentiment         # Sentiment analyst (social, news, alt data)
/trader            # Trader (execution, fills, market structure)
```

### Advanced Analysis
```bash
/chain origin target "query"    # Chain agents for multi-perspective analysis
/compare agent1 agent2 "query"  # Compare different agent views
/compare all "query"            # Get all agent perspectives
```

## Agent Subcommands

Each agent supports subcommands:
```bash
/[agent]           # Enter chat mode
/[agent] test      # Run agent test suite
/[agent] debug     # Verbose debug mode
/[agent] prompt    # Edit agent system prompt
/[agent] status    # Show agent's latest report
/[agent] help      # Show agent-specific commands
```

## Status Line Integration

The `/statusline` command generates rotating status updates:
1. Portfolio basics (NAV, P&L, session)
2. Risk metrics (exposure, alerts, activity)  
3. Agent activity summary
4. Time-based context (pre-market, trading, post-market)

Use `/statusline next` to manually rotate or `/statusline all` to see all lines.

## File Organization

```
.claude/
├── agents/          # Agent definitions with structured prompts
├── commands/        # Python-based slash commands
├── context/         # Shared state (portfolio, market conditions)
├── reports/         # Agent outputs organized by agent
├── alerts/          # Active alerts aggregation
├── hooks/           # Event automation and orchestration
└── temp/            # Chain context, status rotation state
```

## Example Workflows

### Morning Routine
```bash
/statusline          # Check overnight status
/morning             # Run full morning brief
/alerts              # Review any new alerts
/portfolio "What's the game plan today?"
```

### Intraday Analysis
```bash
/chain technicals risk "NVDA approaching resistance"
/compare all "Fed policy implications"
/portfolio "Should we hedge our tech exposure?"
```

### End of Day
```bash
/eod                 # Full EOD review
/status              # Check all agent status
/portfolio "How did we perform today?"
```

### Development Mode
```bash
/technicals prompt   # Edit technical agent
/technicals test     # Run test suite
/technicals debug "Analyze AAPL breakout"
```

## Key Features

- **Realistic Simulation**: $50M fund with institutional processes
- **Python-Based**: Robust commands with JSON/markdown parsing  
- **Cross-Platform**: Works on Mac, Windows, Linux
- **Structured Output**: All agents use consistent markdown format
- **Development Tools**: Testing, debugging, prompt engineering
- **Status Integration**: Rotating status line for Claude Code
- **Chain Analysis**: Multi-agent perspective synthesis

## Getting Started

1. Navigate to the agents directory in Claude Code
2. Run `/morning` for your first trading session
3. Use `/portfolio` to interact with the Portfolio Manager
4. Try `/statusline` to see the rotating status display
5. Experiment with `/chain` and `/compare` for analysis

The system simulates a realistic hedge fund environment while providing powerful tools for agent development and testing.