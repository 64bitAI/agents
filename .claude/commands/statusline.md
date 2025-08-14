---
description: Rotating status line for Claude Code status bar integration
argument-hint: [next|all]
---

# Status Line Integration

Provides rotating status updates for Claude Code's status line feature.

## Usage
```
/statusline          # Show current status rotation
/statusline next     # Manually advance to next status  
/statusline all      # Show all available status lines
```

## Status Rotations
1. **Portfolio Basics**: NAV, P&L, current market session
2. **Risk Metrics**: Exposure levels, active alerts, risk activity
3. **Agent Activity**: Summary of agent status and recent activity  
4. **Time Context**: Market session timing and next scheduled events

## What it does
- Integrates with Claude Code's status line for persistent visibility
- Rotates through different status perspectives automatically
- Shows key metrics at a glance without full dashboard
- Updates based on current market session and activity

Perfect for keeping key fund metrics visible in your Claude Code interface while working on other tasks.