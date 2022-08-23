import calendar
from datetime import datetime

def get_days_in_month(year, month):
    answer = []
    month = list(calendar.month_name).index(month)
    all_dates = calendar.monthcalendar(year, month)
    for i in all_dates:
        if i != 0:
            answer.append(datetime(year=year, month=month, day=int(i)).date())
    print(answer)

get_days_in_month(2021, 'December')