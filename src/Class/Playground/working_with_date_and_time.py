import calendar
from datetime import datetime, timedelta, date, time

print(calendar.calendar(2022))

now = datetime.now()
print(f"{now: %A, %B %d %Y}")
print(now.strftime('%A, %B %d %Y'))

dd = datetime.datetime(year=2022, month=2, day=23, hour=10, minute=56)
print(dd)

ddd = datetime.strptime("2022/10/10 10:30", "Y/%m/%d% %H:%M")
print(ddd)

x = ddd + timedelta(days=10)
print(ddd.day)
print(x.day)
