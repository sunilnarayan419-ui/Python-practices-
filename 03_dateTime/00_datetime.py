import datetime
from datetime import timedelta, timezone
import pytz

# -------------------------------------------------
# Parsing a string into a timezone-aware datetime
# -------------------------------------------------

dt_str = "2026-01-15T08:27:18-0500"
dt = datetime.datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S%z")
print("Parsed datetime:", dt)
print("Timezone:", dt.tzinfo)

# -------------------------------------------------
# Constructing timezone-aware datetimes (manual)
# -------------------------------------------------

JST = timezone(timedelta(hours=9), name="JST")
dt = datetime.datetime(2026, 1, 1, 12, 0, 0, tzinfo=JST)

print("\nJST datetime:", dt)
print("Timezone name:", dt.tzname())

# -------------------------------------------------
# Using pytz for DST-aware timezones
# -------------------------------------------------

PT = pytz.timezone("US/Pacific")

dt_pst = PT.localize(datetime.datetime(2025, 1, 1, 12, 0, 0))
dt_pdt = PT.localize(datetime.datetime(2026, 11, 1, 0, 30, 0))

print("\nPST datetime:", dt_pst)
print("PDT datetime:", dt_pdt)

# Adding time across DST boundary
dt_new = dt_pdt + timedelta(hours=3)
print("After adding 3 hours (raw):", dt_new)

dt_corrected = PT.normalize(dt_new)
print("After normalize:", dt_corrected)

# -------------------------------------------------
# Computing time differences
# -------------------------------------------------

now = datetime.datetime.now()
then = datetime.datetime(2026, 5, 23)

delta = then - now
print("\nDays difference:", delta.days)
print("Seconds remainder:", delta.seconds)

# -------------------------------------------------
# N days after today
# -------------------------------------------------

def get_n_days_date(date_format="%d %B %Y", add_days=120):
    date_n_days_after = datetime.datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)

print("\n120 days after today:", get_n_days_date())

# -------------------------------------------------
# N days before today
# -------------------------------------------------

def get_n_days_before_date(date_format="%d %B %Y", days_before=120):
    date_n_days_ago = datetime.datetime.now() - timedelta(days=days_before)
    return date_n_days_ago.strftime(date_format)

print("120 days before today:", get_n_days_before_date())

# -------------------------------------------------
# Basic datetime objects
# -------------------------------------------------

# Date object
today = datetime.date.today()
new_year = datetime.date(2026, 1, 15)

print("\nToday:", today)
print("New year date:", new_year)

# Time object
night = datetime.time(23, 0, 0)
print("Night time:", night)

# Current datetime
now = datetime.datetime.now()
print("Current datetime:", now)

# Specific datetime
millennium_turn = datetime.datetime(2000, 1, 1, 0, 0, 0)
print("Millennium turn:", millennium_turn)
