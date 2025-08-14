#!/usr/bin/env python3
"""
Manual schedule runner - runs trading schedule on demand
Usage: python manual_runner.py [schedule_name]
"""

import sys
import os
import subprocess
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scheduler import CrossPlatformScheduler

def run_schedule(schedule_name=None):
    scheduler = CrossPlatformScheduler()
    
    if not scheduler.is_market_day():
        print("⏰ Not a market day - skipping scheduled tasks")
        return
    
    if schedule_name:
        if schedule_name in scheduler.commands:
            command = scheduler.commands[schedule_name].format(scheduler.get_current_directory())
            print(f"🚀 Running {schedule_name}: {command}")
            subprocess.run(command, shell=True)
        else:
            print(f"❌ Unknown schedule: {schedule_name}")
            print(f"Available schedules: {list(scheduler.commands.keys())}")
    else:
        print("📅 Available schedules:")
        for name, time in scheduler.schedules.items():
            print(f"  {name}: {time} ET")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_schedule(sys.argv[1])
    else:
        run_schedule()
