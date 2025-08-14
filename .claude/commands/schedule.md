---
description: Manage cross-platform trading schedule automation
argument-hint: [install|status|uninstall|manual]
---

# Trading Schedule Management

Manages automated trading workflows across different operating systems.

## Usage
```
/schedule [command]
```

## Commands
- `install` - Set up automated scheduling (cron/Task Scheduler)
- `status` - Show current schedule status and installed tasks
- `uninstall` - Remove automated scheduling
- `manual` - Create manual runner for testing

## Trading Schedule (Eastern Time)
- **05:30** - Pre-market analysis (`/morning`)
- **09:30** - Market open status check
- **12:00** - Midday risk and P&L update  
- **16:00** - Market close position management
- **16:30** - End-of-day review (`/eod`)
- **18:00** - Overnight preparation and cleanup
- **02:00** - Daily log maintenance and archiving

## Platform Support
- **macOS/Linux**: Uses cron jobs for scheduling
- **Windows**: Uses Task Scheduler for automation
- **Manual**: Python runner for any system or testing

## What it does
- Creates platform-appropriate scheduled tasks
- Automates trading workflow execution
- Handles market day detection (weekdays only)
- Provides logging and error handling
- Enables "lights-out" trading desk operation

Essential for maintaining consistent daily workflows and ensuring no trading sessions are missed.