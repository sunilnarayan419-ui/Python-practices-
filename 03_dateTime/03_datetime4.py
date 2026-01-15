# Converting timestamp to datetime 

import time
from datetime import datetime, timezone

seconds_since_epoch = time.time()

utc_date = datetime.fromtimestamp(seconds_since_epoch, tz=timezone.utc)

print(utc_date)
