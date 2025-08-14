# Cross-Platform Scheduling Guide

## Overview

The Hedge Fund Agent System includes sophisticated cross-platform scheduling to automate trading workflows throughout the market day. This works on macOS, Linux (cron), Windows (Task Scheduler), and includes manual options for any system.

## Trading Schedule (Eastern Time)

| Time  | Event | Action |
|-------|-------|--------|
| 05:30 | Pre-Market | Full morning brief sequence (`/morning`) |
| 09:30 | Market Open | Status check and alerts (`/statusline && /alerts`) |
| 12:00 | Midday Check | Risk and portfolio update |
| 16:00 | Market Close | Position management and close actions |
| 16:30 | Post-Market | Complete EOD review (`/eod`) |
| 18:00 | Overnight | Final review and session cleanup |

## Quick Setup

### 1. Check Current Status
```bash
/schedule status
```
This shows your platform, market day status, and current schedule.

### 2. Install Automation
```bash
/schedule install
```
This creates platform-appropriate scheduled tasks.

### 3. Manual Testing
```bash
# Test individual schedules
python .claude/scheduler/manual_runner.py pre_market
python .claude/scheduler/manual_runner.py post_market
```

## Platform-Specific Installation

### macOS & Linux (Cron)

1. **Install**: Run `/schedule install`
2. **Activate**: `crontab .claude/scheduler/hedge_fund_cron.txt`
3. **Verify**: `crontab -l`
4. **Logs**: Check `.claude/logs/` for execution logs

**Manual cron management:**
```bash
# Edit cron jobs
crontab -e

# View current jobs  
crontab -l

# Remove all jobs
crontab -r

# Install from file
crontab .claude/scheduler/hedge_fund_cron.txt
```

### Windows (Task Scheduler)

1. **Install**: Run `/schedule install`
2. **Activate**: Run `.claude/scheduler/install_tasks.bat` as Administrator
3. **Verify**: Check Task Scheduler or run `schtasks /query /fo table`

**Manual task management:**
```powershell
# View tasks
schtasks /query /fo table

# Run task manually  
schtasks /run /tn "HedgeFund_pre_market"

# Delete task
schtasks /delete /tn "HedgeFund_pre_market" /f

# Create from XML
schtasks /create /xml "task.xml" /tn "TaskName"
```

### WSL (Windows Subsystem for Linux)

WSL uses Linux cron but needs special handling:

1. Install cron: `sudo apt install cron`
2. Start cron service: `sudo service cron start`
3. Follow Linux instructions above
4. **Note**: WSL may not run when Windows sleeps

### Cross-Platform Manual Runner

For any system or testing purposes:

```bash
# List available schedules
python .claude/scheduler/manual_runner.py

# Run specific schedule
python .claude/scheduler/manual_runner.py pre_market
python .claude/scheduler/manual_runner.py market_close
python .claude/scheduler/manual_runner.py post_market
```

## Market Calendar Integration

The system includes US market holiday awareness:

```python
# Check if today is a market day
from .claude.scheduler.market_calendar import MarketCalendar
calendar = MarketCalendar()
print(calendar.is_market_day())  # True/False
```

**Holidays included:**
- New Year's Day
- Martin Luther King Jr. Day  
- Presidents Day
- Good Friday
- Memorial Day
- Juneteenth
- Independence Day
- Labor Day
- Thanksgiving
- Christmas Day

## Customization

### Modify Schedule Times

Edit `.claude/scheduler/scheduler.py`:

```python
self.schedules = {
    "pre_market": "05:00",      # Earlier start
    "market_open": "09:15",     # 15 min before open
    "midday_check": "13:00",    # 1 PM instead of noon
    # ... etc
}
```

Then run `/schedule install` to regenerate.

### Add Custom Schedules

Add new entries to both `schedules` and `commands` dictionaries:

```python
self.schedules = {
    # ... existing schedules
    "lunch_break": "12:30",
    "power_hour": "15:00"
}

self.commands = {
    # ... existing commands
    "lunch_break": "claude code --directory '{}' --message '/portfolio \"lunch update\"'",
    "power_hour": "claude code --directory '{}' --message '/alerts && /technicals \"power hour setups\"'"
}
```

### Environment-Specific Commands

Modify commands for different environments:

```python
# Development environment
"pre_market": "claude code --directory '{}' --message '/morning --mock'",

# Production environment  
"pre_market": "claude code --directory '{}' --message '/morning --live'",
```

## Logging and Monitoring

### Log Locations

**Unix/macOS**: `.claude/logs/[schedule_name].log`
**Windows**: Task Scheduler event logs + `.claude/logs/`

### Log Analysis
```bash
# View recent pre-market logs
tail -f .claude/logs/pre_market.log

# Check for errors
grep -i error .claude/logs/*.log

# Monitor all logs
tail -f .claude/logs/*.log
```

### Failed Execution Handling

Scheduled tasks may fail due to:
- Claude Code not in PATH
- Working directory issues
- Network connectivity
- System sleep/hibernation

**Solutions:**
1. Use absolute paths in scripts
2. Add retry logic to critical tasks
3. Set up monitoring/alerting
4. Use manual runner as backup

## Troubleshooting

### Common Issues

**1. "Command not found" errors**
- Ensure Claude Code is in system PATH
- Use full path to claude binary in scripts

**2. Wrong working directory**
- Scripts automatically `cd` to correct directory
- Verify paths in generated scripts

**3. Tasks not running**
- Check if system was asleep during scheduled time
- Verify cron service is running (Linux)
- Check Task Scheduler service (Windows)

**4. Permission errors**
- Make scripts executable: `chmod +x script.sh`
- Run Task Scheduler as Administrator (Windows)

### Debug Mode

Test schedules manually:
```bash
# Test a specific script directly
.claude/scheduler/scripts/pre_market.sh

# Run with debug output
bash -x .claude/scheduler/scripts/pre_market.sh

# Test the underlying command
claude code --directory "$PWD" --message '/morning'
```

## Advanced Configuration

### Time Zone Handling

All times are in Eastern Time (ET). To adjust for other time zones, modify the schedule times in `scheduler.py` or run your system in ET timezone.

### High-Frequency Schedules

For more frequent updates (every 15 minutes during market hours):

```python
# Add to schedules
"frequent_update": "*/15 9-16 * * 1-5"  # Every 15 min, 9 AM - 4 PM, weekdays
```

### Conditional Execution

Scripts include market day checking. Add additional conditions:

```bash
# Only run on high volatility days
if [ $(python -c "import yfinance; print(yfinance.Ticker('VIX').history(period='1d')['Close'].iloc[-1])") -gt 20 ]; then
    claude code --directory "$PWD" --message '/risk "high volatility protocols"'
fi
```

### Integration with External Systems

Connect to market data feeds, Bloomberg Terminal, etc.:

```python
# Add MCP server connections
"pre_market": "claude code --directory '{}' --message '/morning --mcp bloomberg'"
```

## Production Deployment

### Server Environment

For always-on servers:
1. Use system service accounts
2. Configure proper logging rotation  
3. Set up monitoring/alerting
4. Use process managers (systemd, supervisor)
5. Implement failure recovery

### Docker Deployment

```dockerfile
FROM python:3.11-slim
RUN apt-get update && apt-get install -y cron
COPY .claude/scheduler/hedge_fund_cron.txt /etc/cron.d/hedge-fund
RUN chmod 0644 /etc/cron.d/hedge-fund
RUN crontab /etc/cron.d/hedge-fund
CMD ["cron", "-f"]
```

### Cloud Scheduling

**AWS**: Use EventBridge (CloudWatch Events)  
**Azure**: Use Logic Apps or Azure Functions  
**GCP**: Use Cloud Scheduler  

These provide more reliability than cron for cloud deployments.

## Security Considerations

- Scripts run with user permissions
- Logs may contain sensitive trading data
- Consider encrypted logging for production
- Use service accounts with minimal permissions
- Audit scheduled task execution regularly

The scheduling system provides enterprise-grade automation for hedge fund operations while remaining simple to install and maintain across all major platforms.