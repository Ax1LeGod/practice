from datetime import timedelta, datetime
a = timedelta(3)
b = datetime.utcnow()
c = a+b
print(a)
print(b)
print(c)