import datetime
now = datetime.datetime.now()

print(now)

t = datetime.time(6, 56, 34)
print(t.hour)

t2= datetime.datetime.today()
print(t2.ctime())

t3 = datetime.date(2000, 5, 30)
t4 = datetime.date(1959, 6, 4)

a=t3-t4

print(a)