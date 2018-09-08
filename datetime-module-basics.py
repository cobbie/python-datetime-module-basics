import datetime
# understand naive and aware datetimes

# naive
d = datetime.date(2018, 9, 9)
tday = datetime.date.today()
print('basic stuff:')
print(tday.year)
print(tday.weekday())
print(tday.isoweekday())

# weekday : Monday 0 Sunday 6
# isoweekday : Monday 1 Sunday 7

# performing operations on time and dates: timedelta
print('understanding timedelta:')
tdelta = datetime.timedelta(days=7)
print(tday - tdelta)

# take note:
# date2 = date1 + timedelta
# timedelta = date1 + date2

print('timedelta operations:')
bday = datetime.date(2018, 7, 10)

till_bday = bday - tday
till_christmas = datetime.date(2018, 12, 25) - datetime.date.today()
print(till_bday.days)
print('days til christmas: {}, seconds til christmas: {}'.format(
    till_christmas.days, till_christmas.total_seconds()))

# datetime.time
print('datetime.time:')
print(datetime.time(9, 30, 45, 100000).hour)

# datetime.datetime
print('\ndatetime.datetime')
dt = datetime.datetime.today()
print(dt.time())

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
