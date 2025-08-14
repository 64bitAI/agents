---
description: Log management and analysis tools
argument-hint: [status|view|search|export|cleanup|archive]
---

# Log Management System

Comprehensive logging and analysis tools for trading system monitoring.

## Usage
```
/logs <command> [options]
```

## Commands
- `status` - Show log sizes, counts, disk usage
- `view [log_name]` - List or tail specific logs
- `search <pattern> [days]` - Search logs for patterns
- `export <days> [filename]` - Export logs for analysis
- `cleanup` - Run maintenance (rotate, compress, clean)
- `archive` - Manually rotate large logs

## Log Categories
- **Trading Schedules**: pre_market, market_open, midday_check, market_close, post_market, overnight
- **Agent Reports**: risk_analysis, technical_alerts, fundamental_events, portfolio_decisions  
- **System Logs**: log_maintenance, error tracking, performance monitoring

## Features
- **Automatic Rotation**: Logs > 10MB rotated automatically
- **Compression**: Files older than 7 days compressed with gzip
- **Retention**: 365 days total retention (30 days uncompressed)
- **Search**: Full-text search across all logs with time filtering
- **Export**: Aggregated exports for external analysis

## Examples
```
/logs view pre_market        # Monitor morning brief logs
/logs search "NVDA" 14      # Find NVDA mentions in last 14 days  
/logs export 30 monthly.txt # Export last 30 days for review
```

Essential for audit trails, performance analysis, and system troubleshooting.