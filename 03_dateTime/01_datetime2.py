# Switching between time zones

from datetime import datetime
from dateutil import tz

# -------------------------------------------------
# Define timezones
# -------------------------------------------------

utc = tz.tzutc()
local = tz.tzlocal()
india = tz.gettz("Asia/Kolkata")

# -------------------------------------------------
# Get current UTC time (timezone-aware)
# -------------------------------------------------

utc_now = datetime.now(tz=utc)
print("UTC time:", utc_now)

# -------------------------------------------------
# Convert UTC → Local timezone
# -------------------------------------------------

local_now = utc_now.astimezone(local)
print("Local time:", local_now)

# -------------------------------------------------
# Convert UTC → India timezone
# -------------------------------------------------

india_time = utc_now.astimezone(india)
print("India time:", india_time)

