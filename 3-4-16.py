from datetime import datetime, timedelta

clock = datetime.strptime(input(), '%H:%M:%S')
answer = clock + timedelta(seconds=int(input()))
print(answer.time())
