

def test1():
    import datetime as dt

    now = dt.date.today()
    print(now)
    print(now.day)
    
    today = dt.date.today()

    three_last_days = [f"{today-dt.timedelta(days=i)}" for i in range(1,4,1)]
    print(three_last_days)

    yesterday = today - dt.timedelta(days=1)
    befyes = today - dt.timedelta(days=2)
    yes_2 = today - dt.timedelta(days=3)
    print(today, yesterday, befyes,yes_2)
test1()
