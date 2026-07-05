import datetime

y=0
m=0
d=0
ram_dob=0
sita_dob=0

for i in range(2):
  y = int(input("Enter year : "))
  m = int(input("Enter month : "))
  d = int(input("Enter day"))
  if(i==0):
     ram_dob = datetime.date(y,m,d)
  else:
    sita_dob = datetime.date(y,m,d)


if(ram_dob>sita_dob):
  print("Ram is older")
else:
  print("Sita is older")

  