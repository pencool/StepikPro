from datetime import datetime

week = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}
start = datetime(year=1, month=1, day=1).toordinal()
end = datetime(year=9999, month=12, day=31).toordinal()
for i in range(start, end + 1):
    if datetime.fromordinal(i).day == 13:
        week[datetime.fromordinal(i).weekday()] += 1
print(*[v for k, v in week.items()], sep='\n')

