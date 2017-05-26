import calendar
import datetime

for year in range(1006,2000,10):
    day = datetime.date(year,1,27)
    if(calendar.isleap(year) and day.weekday()==1 ):
        print(year)