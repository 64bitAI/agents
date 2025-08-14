#!/usr/bin/env python3
"""
Log management and archiving for hedge fund trading system
Handles log rotation, archiving, and cleanup
"""

import os
import shutil
import gzip
import glob
from datetime import datetime, timedelta
from pathlib import Path

class LogManager:
    def __init__(self):
        self.claude_dir = Path(".claude")
        self.logs_dir = self.claude_dir / "logs"
        self.archive_dir = self.claude_dir / "logs" / "archive"
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        
        # Log retention settings
        self.max_log_size_mb = 10           # Rotate when log exceeds 10MB
        self.keep_daily_logs_days = 30      # Keep daily logs for 30 days
        self.keep_archived_logs_days = 365  # Keep archived logs for 1 year
        self.compress_after_days = 7        # Compress logs older than 7 days
        
    def get_log_files(self):
        """Get all current log files"""
        return list(self.logs_dir.glob("*.log"))
    
    def get_file_size_mb(self, file_path):
        """Get file size in MB"""
        try:
            return file_path.stat().st_size / (1024 * 1024)
        except (OSError, FileNotFoundError):
            return 0
    
    def get_file_age_days(self, file_path):
        """Get file age in days"""
        try:
            mtime = file_path.stat().st_mtime
            return (datetime.now().timestamp() - mtime) / 86400
        except (OSError, FileNotFoundError):
            return 0
    
    def rotate_log(self, log_file):
        """Rotate a single log file"""
        if not log_file.exists():
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = log_file.stem  # filename without .log extension
        
        # Create rotated filename
        rotated_name = f"{base_name}_{timestamp}.log"
        rotated_path = self.archive_dir / rotated_name
        
        # Move log to archive
        shutil.move(str(log_file), str(rotated_path))
        
        # Create new empty log file
        log_file.touch()
        
        print(f"✅ Rotated {log_file.name} -> {rotated_name}")
        return rotated_path
    
    def compress_old_logs(self):
        """Compress logs older than threshold"""
        archived_logs = list(self.archive_dir.glob("*.log"))
        compressed_count = 0
        
        for log_file in archived_logs:
            age_days = self.get_file_age_days(log_file)
            
            if age_days > self.compress_after_days:
                compressed_path = log_file.with_suffix(".log.gz")
                
                # Compress the file
                with open(log_file, 'rb') as f_in:
                    with gzip.open(compressed_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                
                # Remove original
                log_file.unlink()
                compressed_count += 1
                print(f"🗜️  Compressed {log_file.name}")
        
        return compressed_count
    
    def cleanup_old_logs(self):
        """Remove logs older than retention period"""
        removed_count = 0
        
        # Remove old archived logs
        for pattern in ["*.log", "*.log.gz"]:
            for log_file in self.archive_dir.glob(pattern):
                age_days = self.get_file_age_days(log_file)
                
                if age_days > self.keep_archived_logs_days:
                    log_file.unlink()
                    removed_count += 1
                    print(f"🗑️  Removed old log: {log_file.name}")
        
        return removed_count
    
    def rotate_large_logs(self):
        """Rotate logs that exceed size threshold"""
        rotated_count = 0
        
        for log_file in self.get_log_files():
            size_mb = self.get_file_size_mb(log_file)
            
            if size_mb > self.max_log_size_mb:
                self.rotate_log(log_file)
                rotated_count += 1
        
        return rotated_count
    
    def daily_maintenance(self):
        """Run daily log maintenance tasks"""
        print("🧹 Running daily log maintenance...")
        
        # Rotate large logs
        rotated = self.rotate_large_logs()
        print(f"   Rotated {rotated} large logs")
        
        # Compress old logs  
        compressed = self.compress_old_logs()
        print(f"   Compressed {compressed} old logs")
        
        # Clean up very old logs
        removed = self.cleanup_old_logs()
        print(f"   Removed {removed} expired logs")
        
        # Show current status
        self.show_log_status()
    
    def show_log_status(self):
        """Display current log status"""
        print("\n📊 Log Status Summary")
        print("=" * 30)
        
        # Current logs
        current_logs = self.get_log_files()
        total_size_mb = sum(self.get_file_size_mb(f) for f in current_logs)
        
        print(f"Current logs: {len(current_logs)} files ({total_size_mb:.1f} MB)")
        
        if current_logs:
            print("\nActive log files:")
            for log_file in sorted(current_logs):
                size_mb = self.get_file_size_mb(log_file)
                age_days = self.get_file_age_days(log_file)
                print(f"  {log_file.name}: {size_mb:.1f} MB ({age_days:.1f} days old)")
        
        # Archived logs
        archived_logs = list(self.archive_dir.glob("*.log"))
        compressed_logs = list(self.archive_dir.glob("*.log.gz"))
        
        print(f"\nArchived logs: {len(archived_logs)} files")
        print(f"Compressed logs: {len(compressed_logs)} files")
        
        if archived_logs or compressed_logs:
            total_archived_size = 0
            total_archived_size += sum(self.get_file_size_mb(f) for f in archived_logs)
            total_archived_size += sum(self.get_file_size_mb(f) for f in compressed_logs)
            print(f"Total archived size: {total_archived_size:.1f} MB")
    
    def search_logs(self, pattern, days_back=7):
        """Search logs for a pattern"""
        print(f"🔍 Searching logs for: '{pattern}' (last {days_back} days)")
        print("=" * 50)
        
        cutoff_date = datetime.now() - timedelta(days=days_back)
        cutoff_timestamp = cutoff_date.timestamp()
        
        matches_found = 0
        
        # Search current logs
        for log_file in self.get_log_files():
            if log_file.stat().st_mtime > cutoff_timestamp:
                try:
                    with open(log_file, 'r') as f:
                        for line_num, line in enumerate(f, 1):
                            if pattern.lower() in line.lower():
                                print(f"{log_file.name}:{line_num}: {line.strip()}")
                                matches_found += 1
                except (OSError, UnicodeDecodeError):
                    continue
        
        # Search archived logs
        for log_file in self.archive_dir.glob("*.log"):
            if log_file.stat().st_mtime > cutoff_timestamp:
                try:
                    with open(log_file, 'r') as f:
                        for line_num, line in enumerate(f, 1):
                            if pattern.lower() in line.lower():
                                print(f"archive/{log_file.name}:{line_num}: {line.strip()}")
                                matches_found += 1
                except (OSError, UnicodeDecodeError):
                    continue
        
        # Search compressed logs (basic - doesn't decompress)
        compressed_count = len(list(self.archive_dir.glob("*.log.gz")))
        if compressed_count > 0:
            print(f"\nNote: {compressed_count} compressed logs not searched")
            print("Use 'zgrep' to search compressed logs manually")
        
        print(f"\nFound {matches_found} matches")
    
    def export_logs(self, days_back=30, output_file=None):
        """Export logs for external analysis"""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"hedge_fund_logs_export_{timestamp}.txt"
        
        cutoff_date = datetime.now() - timedelta(days=days_back)
        cutoff_timestamp = cutoff_date.timestamp()
        
        print(f"📤 Exporting logs from last {days_back} days to {output_file}")
        
        with open(output_file, 'w') as out_file:
            out_file.write(f"# Hedge Fund Trading Logs Export\n")
            out_file.write(f"# Generated: {datetime.now().isoformat()}\n")
            out_file.write(f"# Period: Last {days_back} days\n\n")
            
            # Export current logs
            for log_file in sorted(self.get_log_files()):
                if log_file.stat().st_mtime > cutoff_timestamp:
                    out_file.write(f"\n=== {log_file.name} ===\n")
                    try:
                        with open(log_file, 'r') as f:
                            out_file.write(f.read())
                    except (OSError, UnicodeDecodeError):
                        out_file.write("[Error reading file]\n")
            
            # Export archived logs
            for log_file in sorted(self.archive_dir.glob("*.log")):
                if log_file.stat().st_mtime > cutoff_timestamp:
                    out_file.write(f"\n=== archive/{log_file.name} ===\n")
                    try:
                        with open(log_file, 'r') as f:
                            out_file.write(f.read())
                    except (OSError, UnicodeDecodeError):
                        out_file.write("[Error reading file]\n")
        
        print(f"✅ Export completed: {output_file}")
        return output_file

def main():
    """CLI interface for log management"""
    import sys
    
    manager = LogManager()
    
    if len(sys.argv) < 2:
        print("Log Management Commands:")
        print("  python log_manager.py status      # Show current log status")
        print("  python log_manager.py rotate      # Rotate large logs")  
        print("  python log_manager.py cleanup     # Run daily maintenance")
        print("  python log_manager.py search <pattern>  # Search recent logs")
        print("  python log_manager.py export [days]     # Export logs")
        return
    
    command = sys.argv[1].lower()
    
    if command == "status":
        manager.show_log_status()
    
    elif command == "rotate":
        rotated = manager.rotate_large_logs()
        print(f"Rotated {rotated} logs")
    
    elif command == "cleanup":
        manager.daily_maintenance()
    
    elif command == "search":
        if len(sys.argv) < 3:
            print("Usage: python log_manager.py search <pattern> [days_back]")
            return
        pattern = sys.argv[2]
        days_back = int(sys.argv[3]) if len(sys.argv) > 3 else 7
        manager.search_logs(pattern, days_back)
    
    elif command == "export":
        days_back = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        manager.export_logs(days_back)
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()