# Log Management Guide

## Overview

The hedge fund trading system includes comprehensive log management with automatic rotation, archiving, compression, and cleanup. All trading activities are logged with timestamps for audit trails and performance analysis.

## Log Locations

### Active Logs
- **Location**: `.claude/logs/`
- **Format**: `{schedule_name}.log` (e.g., `pre_market.log`, `post_market.log`)
- **Content**: Real-time trading system outputs, agent responses, errors

### Archived Logs  
- **Location**: `.claude/logs/archive/`
- **Format**: `{schedule_name}_{timestamp}.log` (e.g., `pre_market_20240115_053001.log`)
- **Compressed**: Files older than 7 days are gzip compressed (`.log.gz`)

## Log Management Commands

### View Current Status
```bash
/logs status                # Show log sizes, counts, disk usage
/logs view                  # List available logs
/logs view pre_market       # Tail specific log (live updates)
```

### Search and Analysis
```bash
/logs search error          # Find errors in recent logs
/logs search NVDA 14        # Search for NVDA mentions in last 14 days
/logs export 30             # Export last 30 days to single file
```

### Maintenance
```bash
/logs cleanup               # Run full maintenance (rotate, compress, clean)
/logs archive               # Manually rotate large logs
```

## Automatic Log Management

### Schedule
The system runs automatic log maintenance daily at **2:00 AM ET**:
- Rotates logs exceeding 10MB
- Compresses logs older than 7 days  
- Removes archived logs older than 365 days
- Updates log status metrics

### Retention Policy
- **Active logs**: Keep current until rotation needed
- **Daily archives**: 30 days uncompressed
- **Compressed archives**: 365 days (1 year)
- **Size threshold**: Rotate when log exceeds 10MB

### Log Rotation Triggers
1. **Size-based**: Automatically when log > 10MB
2. **Time-based**: Daily maintenance at 2:00 AM
3. **Manual**: Via `/logs archive` command

## Log File Structure

### Trading Schedule Logs
```
pre_market.log      # 05:30 ET - Morning brief outputs
market_open.log     # 09:30 ET - Market open status  
midday_check.log    # 12:00 ET - Midday risk/P&L updates
market_close.log    # 16:00 ET - Market close actions
post_market.log     # 16:30 ET - EOD review outputs
overnight.log       # 18:00 ET - Overnight preparation
log_maintenance.log # 02:00 ET - Log system maintenance
```

### Agent-Specific Logs
Individual agents may create their own logs:
```
risk_analysis.log       # Risk manager detailed outputs
technical_alerts.log    # Technical analysis alerts
fundamental_events.log  # Fundamental analysis events
portfolio_decisions.log # Portfolio manager decisions
```

## Log Content Examples

### Pre-Market Log
```
2024-01-15 05:30:01 - Starting pre-market analysis
2024-01-15 05:30:02 - Portfolio NAV: $50.2M (+0.4% overnight)
2024-01-15 05:30:05 - Risk VaR: $2.1M (4.2% NAV)
2024-01-15 05:30:07 - Technical setups: 3 identified
2024-01-15 05:30:10 - News scan: NVDA earnings preview
2024-01-15 05:30:15 - Morning brief completed
```

### Error Log Example
```
2024-01-15 09:30:15 - ERROR: Market data feed timeout
2024-01-15 09:30:16 - RETRY: Attempting reconnection
2024-01-15 09:30:18 - SUCCESS: Market data restored
2024-01-15 09:30:20 - INFO: Alert sent to risk manager
```

## Advanced Log Analysis

### Search Patterns
```bash
# Find all errors
/logs search "ERROR\|FAIL"

# Find specific trading activity  
/logs search "NVDA.*buy\|NVDA.*sell"

# Find risk alerts
/logs search "VaR\|breach\|limit"

# Find performance data
/logs search "P&L\|performance\|return"
```

### Export for Analysis
```bash
# Export recent logs
/logs export 7              # Last 7 days

# Export to specific file
/logs export 30 monthly_review.txt

# For external tools (Excel, Python, etc.)
/logs export 90 quarterly_analysis.csv
```

### Manual Log Operations

#### Direct File Access
```bash
# View recent entries
tail -n 50 .claude/logs/pre_market.log

# Monitor live updates
tail -f .claude/logs/pre_market.log

# Search specific patterns
grep -i "error\|alert" .claude/logs/*.log
```

#### Compressed Log Access
```bash
# View compressed logs
zcat .claude/logs/archive/pre_market_20240101_053000.log.gz

# Search compressed logs
zgrep -i "NVDA" .claude/logs/archive/*.log.gz
```

## Performance Monitoring

### Log Metrics Dashboard
The system tracks:
- **Log Generation Rate**: Entries per minute during active periods
- **Error Rate**: Error frequency and types
- **Agent Activity**: Which agents are most/least active
- **Storage Usage**: Current and projected disk usage

### Alerts and Notifications
Automatic alerts for:
- High error rates (>5 errors in 10 minutes)
- Log disk usage >1GB
- Missing scheduled log entries
- Log rotation failures

## Integration with Trading System

### Agent Logging Standards
All agents follow structured logging:
```python
# Standard log entry format
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"{timestamp} - {level} - {agent} - {message}"

# Examples
"2024-01-15 05:30:05 - INFO - risk - VaR calculation: $2.1M"  
"2024-01-15 09:30:15 - ALERT - technicals - SPX breakout detected"
"2024-01-15 16:30:01 - SUCCESS - portfolio - EOD review completed"
```

### Audit Trail Requirements
For compliance and performance review:
- All trading decisions logged with rationale
- Agent interactions and chain sequences recorded
- P&L attribution events tracked
- Risk limit checks and breaches documented

## Troubleshooting

### Common Issues

**1. Logs not generating**
- Check if scheduled tasks are running
- Verify Claude Code is accessible from cron/Task Scheduler
- Check permissions on `.claude/logs/` directory

**2. Log rotation not working**
- Verify log maintenance schedule installed
- Check disk space availability
- Ensure Python accessible from scheduled tasks

**3. Search not finding results**
- Check if logs exist for specified time period
- Verify search pattern syntax (case-sensitive)
- Consider searching compressed archives

**4. Large disk usage**
- Run `/logs cleanup` to remove old archives
- Adjust retention policy in `log_manager.py`
- Consider moving archives to external storage

### Recovery Procedures

**Lost logs**: Check `.claude/logs/archive/` for backups

**Corrupted logs**: 
```bash
# Verify log integrity
file .claude/logs/*.log

# Repair if needed (remove corrupted entries)
grep -v "^$" pre_market.log > pre_market_clean.log
```

**Performance issues**:
```bash
# Rotate all logs immediately
/logs archive

# Clean up aggressively  
python3 .claude/scheduler/log_manager.py cleanup

# Check disk usage
du -sh .claude/logs/
```

## Production Recommendations

### High-Volume Trading
- Reduce log retention to 30 days for archives
- Increase rotation frequency (5MB threshold)
- Use external log aggregation (ELK stack, Splunk)
- Implement real-time log streaming

### Compliance Requirements
- Enable log integrity checking (checksums)
- Implement tamper-evident logging
- Ensure logs are backed up offsite
- Maintain detailed audit trails

### Performance Optimization
- Use asynchronous logging for high-frequency events
- Implement log buffering during market hours
- Consider log compression during market hours
- Monitor log I/O impact on trading performance

The log management system provides comprehensive visibility into hedge fund operations while maintaining performance and compliance requirements.