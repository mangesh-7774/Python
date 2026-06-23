sum=0
mul=1

num = 1124
temp = num
while num>0 : 
  rem = num%10
  sum += rem
  mul *= rem
  num = num//10

if(sum==mul):
  print("Spy")
else:
  print("Not spy")



