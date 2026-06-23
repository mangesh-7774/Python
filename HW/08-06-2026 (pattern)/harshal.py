num = 132
sum = 0
temp = num

while num>0:
  rem = num%10
  sum += rem
  num = num//10

if(temp%sum==0):
  print("Harshal")
else:
  print("Not a Harshal")