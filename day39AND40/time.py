import datetime

i=4

today = datetime.date.today()
date = f"{today.strftime('%Y/%m/%d')}"
day_del = (today- datetime.timedelta(days=i)).strftime("%d/%m/%Y")
six_months_later = (today + datetime.timedelta(days=(30*6))).strftime("%d/%m/%Y")

print(f"date: {date}")
print(f"date result: {day_del}")
print(f"Six months later: {six_months_later}")
