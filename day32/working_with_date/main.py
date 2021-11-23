import datetime as dt

def time_now():
    return dt.datetime.now()

def waths_day(num):
    if num == 0:
        return "Sunday"
    elif num == 1:
        return "Monday"
    elif num == 2:
        return "Thursday"
    elif num == 3:
        return "Wensday"
    elif num == 4:
        return "Thuesday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    else:
        return "Wrong input"

now = time_now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minutes = now.minute
seconds = now.second
microsecond = now.microsecond
tzinfo = now.tzinfo
if tzinfo is None:
    tzinfo = "Naive system(objects)"
weekday = now.weekday()
print(f"""
Now = {now},
year = {year}, month = {month}, day = {day},

hour = {hour}, seconds = {seconds}, minute = {minutes}, microsecond = {microsecond},

weekday = {waths_day(weekday)},

Zone infomation = {tzinfo}
""")

#-- playing whit datetime
birth_year = 2000
birth_month = 1
birth_day = 7
birth_hour = 4
#we can especify more

#creating an date_of_birth now
date_of_birth = dt.datetime(year=birth_year,month=birth_month,day=birth_day)
print(date_of_birth)