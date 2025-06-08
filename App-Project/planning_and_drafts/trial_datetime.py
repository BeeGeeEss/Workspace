#Python date and time library
import datetime
#Python Timezone library
import pytz


aest_tz = pytz.timezone('Australia/Sydney')

# Example:  Current time in UTC
utc_now = datetime.datetime.utcnow()

# Convert to AEST
aest_now = utc_now.replace(tzinfo=pytz.utc).astimezone(aest_tz)

print(f"Current time in AEST: {aest_now}")