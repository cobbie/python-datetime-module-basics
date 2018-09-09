import datetime
import random
# Given an array of datetimes, filter them based on time intervals
# (5 min, 10 min, 15 min, 60 min, 12 hours, 24 hours, 1 week, 1 month, 1 year).


# sample dates
d1 = datetime.datetime(2018, 9, 10)
d2 = datetime.datetime(2018, 8, 3)
d3 = datetime.datetime(2018, 2, 2)
d4 = datetime.datetime(2018, 8, 3)
d5 = datetime.datetime(2018, 1, 2)
d6 = datetime.datetime(2018, 4, 5)
d7 = datetime.datetime(2018, 6, 6)
d8 = datetime.datetime(2018, 9, 7)
tday = datetime.datetime.today()

arr_dates = [d1, d2, d3, d4, d5, d6, d7, d8, tday]
print(arr_dates)


import random
from datetime import datetime, timedelta

min_year = 1900
max_year = datetime.now().year

start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year+1
end = start + timedelta(days=365 * years)

for i in range(10):
    random_date = start + (end - start) * random.random()
    print(random_date)
