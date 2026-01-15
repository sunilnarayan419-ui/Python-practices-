# Subtracting months from a date accurately 

import calendar
from datetime import date

def monthdelta(dt, delta):
    # Calculate new month and year
    month = (dt.month + delta - 1) % 12 + 1
    year = dt.year + (dt.month + delta - 1) // 12

    # Clamp day to last day of target month
    day = min(dt.day, calendar.monthrange(year, month)[1])

    return dt.replace(year=year, month=month, day=day)

# Example usage
next_month = monthdelta(date.today(), 1)
print("Next month:", next_month)
