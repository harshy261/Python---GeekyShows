# DATE & TIME MODULES

from time import time, ctime, localtime

epoch = time()
print(epoch)

et = ctime(epoch)
print(et)

print(ctime())


stobj = localtime()
print(stobj)
print("Year ",stobj.tm_year)
print("Month ",stobj.tm_mon)
print("Day ",stobj.tm_mday)
print("Hour ",stobj.tm_hour)
print("Min ",stobj.tm_min)
print("Sec ",stobj.tm_sec)
print()
print(stobj.tm_hour, end=":")
print(stobj.tm_min, end=":")
print(stobj.tm_sec)










from datetime import datetime


dt1 = datetime(year=2019, month=6, day=30)
dt2 = datetime(year=2019, month=6, day=30, hour=15, minute=34)
dt3 = datetime(2017, 4, 28)
dt4 = datetime(2016, 3, 27, 14, 30)

print(dt1)
print(dt1.year)
print(dt1.month)
print(dt2)
print(dt3)
print(dt4)
print()

ct = datetime.now()
print(ct)
print(ct.year)
print(ct.month)
print(ct.day)
print(ct.hour)










from datetime import date

d1 = date(2019, 6, 30)
print(d1.year)
print(d1.month)
print(d1.day)

cd = date.today()
print(cd)







from datetime import time

t = time(hour=15, minute=34, second=12)
print(t.hour)
print(t.minute)







from datetime import timedelta

td = timedelta(days=10)
d = date.today()

print(d+td)
print(d-td)







from datetime import date

d1 = date(2019, 6, 30)
d2 = date(2018, 6, 30)
print(d1==d2)
print(d1>d2)
print(d1<d2)
print(d1!=d2)





from datetime import datetime

dt = datetime.today()
print(dt)
print()

newd1 = dt.strftime("%B, %d, %Y")
print(newd1)
print(type(newd1))
print()

newd2 = dt.strftime("%d/%b/%Y")
print(newd2)
print()

newd3 = dt.strftime("%d-%m-%Y")
print(newd3)
print()

newt1 = dt.strftime("%H:%M:%S")
print(newt1)
print()
