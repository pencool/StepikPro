from datetime import date, timedelta, datetime

data = datetime.strptime(input(), '%d.%m.%Y').date()
print((data + timedelta(hours=-24)).strftime('%d.%m.%Y'),(data + timedelta(hours=24)).strftime('%d.%m.%Y'),  sep='\n')
