import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.ceil(44.23))
print(math.floor(44.23))
print(math.pow(2,3))
print(math.pi)

print()
calcu=2*math.pi*2
print(calcu)

import random as r

print(r.randint(1000,9999))
print(r.random())
print(r.randrange(1,20))

#generates even number only
print(r.randrange(2,10,2))


# choose random option from list
x=["red","black","blue","orange"]
print(r.choice(x))
print()
print(r.choices(x,k=2))


# shuffle the list elements 

print(x)
r.shuffle(x)
print(x)


import datetime

# print(datetime.datetime.now())
d=datetime.datetime.now()
print(d.time())
print(d.day)
print(d.month)
print(d.year)

today_date=datetime.date.today()
print(today_date)

# after 5 days

after_5day=today_date+datetime.timedelta(days=5)
print(after_5day)


dob = datetime.date(2004,4,8)
cur_date = datetime.date.today()

print(cur_date-dob)
print(cur_date.year-dob.year)
