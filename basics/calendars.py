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

# calculate the first Saturday of the month
for m in range(1,13):
    cal = calendar.monthcalendar(2018, m)
    week1 = cal[0]
    week2 = cal[1]

    # 0 is for previous month
    if (week1[calendar.SATURDAY] != 0):
        meetday = week1[calendar.SATURDAY]
    else:
        meetday = week2[calendar.SATURDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))


