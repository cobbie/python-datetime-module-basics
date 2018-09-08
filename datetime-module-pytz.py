import datetime
import pytz

dt = datetime.datetime(2018, 9, 9, 3, 53, 30, tzinfo=pytz.UTC)

print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
