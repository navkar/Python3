import calendar

# Formats a calendar in HTML
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2018,4,0,0)
print(st)

# Formats a calendar in HTML
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2018,7,1)
print(st)



print("-------- MONTHS") 
#Locale
for name in calendar.month_name:
    print(name)

print("-------- DAYS")

for day in calendar.day_name:
    print(day)

# calculate the first Friday of the month