#!/usr/bin/env python3
"""
Market calendar and holiday management for trading schedule
"""

from datetime import datetime, date
from typing import Set

class MarketCalendar:
    def __init__(self):
        # US Market holidays (approximate - update yearly)
        self.holidays_2024 = {
            date(2024, 1, 1),   # New Year's Day
            date(2024, 1, 15),  # Martin Luther King Jr. Day
            date(2024, 2, 19),  # Presidents Day
            date(2024, 3, 29),  # Good Friday
            date(2024, 5, 27),  # Memorial Day
            date(2024, 6, 19),  # Juneteenth
            date(2024, 7, 4),   # Independence Day
            date(2024, 9, 2),   # Labor Day
            date(2024, 11, 28), # Thanksgiving
            date(2024, 12, 25), # Christmas Day
        }
        
        self.holidays_2025 = {
            date(2025, 1, 1),   # New Year's Day
            date(2025, 1, 20),  # Martin Luther King Jr. Day
            date(2025, 2, 17),  # Presidents Day
            date(2025, 4, 18),  # Good Friday
            date(2025, 5, 26),  # Memorial Day
            date(2025, 6, 19),  # Juneteenth
            date(2025, 7, 4),   # Independence Day
            date(2025, 9, 1),   # Labor Day
            date(2025, 11, 27), # Thanksgiving
            date(2025, 12, 25), # Christmas Day
        }
    
    def get_holidays_for_year(self, year: int) -> Set[date]:
        """Get holidays for a specific year"""
        if year == 2024:
            return self.holidays_2024
        elif year == 2025:
            return self.holidays_2025
        else:
            # Default to no holidays for other years
            return set()
    
    def is_market_day(self, check_date: date = None) -> bool:
        """Check if given date is a market day (weekday, not holiday)"""
        if check_date is None:
            check_date = date.today()
        
        # Check if it's a weekend
        if check_date.weekday() >= 5:  # Saturday=5, Sunday=6
            return False
        
        # Check if it's a holiday
        holidays = self.get_holidays_for_year(check_date.year)
        if check_date in holidays:
            return False
        
        return True
    
    def next_market_day(self, start_date: date = None) -> date:
        """Find the next market day from given date"""
        if start_date is None:
            start_date = date.today()
        
        check_date = start_date
        while not self.is_market_day(check_date):
            check_date = date.fromordinal(check_date.toordinal() + 1)
        
        return check_date
    
    def days_until_next_market_day(self) -> int:
        """Number of days until next market day"""
        today = date.today()
        next_market = self.next_market_day(today)
        
        if self.is_market_day(today):
            return 0
        else:
            return (next_market - today).days
    
    def get_market_status(self) -> dict:
        """Get current market status information"""
        today = date.today()
        now = datetime.now()
        
        return {
            "date": today.isoformat(),
            "is_market_day": self.is_market_day(today),
            "is_weekend": today.weekday() >= 5,
            "is_holiday": today in self.get_holidays_for_year(today.year),
            "next_market_day": self.next_market_day(today).isoformat(),
            "days_until_market": self.days_until_next_market_day(),
            "current_time": now.strftime("%H:%M ET"),
            "market_session": self.get_current_session(now)
        }
    
    def get_current_session(self, current_time: datetime = None) -> str:
        """Determine current market session"""
        if current_time is None:
            current_time = datetime.now()
        
        hour = current_time.hour
        minute = current_time.minute
        time_minutes = hour * 60 + minute
        
        # Market times in ET (minutes since midnight)
        pre_market_start = 5 * 60 + 30    # 5:30 AM
        market_open = 9 * 60 + 30         # 9:30 AM  
        market_close = 16 * 60            # 4:00 PM
        post_market_end = 18 * 60         # 6:00 PM
        
        if time_minutes < pre_market_start:
            return "overnight"
        elif time_minutes < market_open:
            return "pre-market"
        elif time_minutes < market_close:
            return "market-hours"
        elif time_minutes < post_market_end:
            return "post-market"
        else:
            return "after-hours"

# Test function
def main():
    calendar = MarketCalendar()
    status = calendar.get_market_status()
    
    print("📅 Market Calendar Status")
    print("=" * 30)
    for key, value in status.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()