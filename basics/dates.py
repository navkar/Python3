from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print("today is : " + str(now))
print("after 1 yr: " + str(now + timedelta(days=365)))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago: " + s)

# April Fools day
today = date.today()
afd = date(today.year, 4, 1)

if (afd < today):
    print("April fools day was %d days ago" % (today-afd).days)
    afd = afd.replace(year = today.year+1)

time_to_afd = afd - today

print("Next one is after ", time_to_afd.days, " days")




