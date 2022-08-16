from datetime import datetime

sec = datetime.strptime(input(), '%H:%M:%S')
secon = sec.hour*3600 + sec.minute*60 + sec.second
print(secon)