num = 9
sum = 0
sq = num*num

while sq>0:
  rem = sq%10
  sum += rem
  sq = sq//10

if(num==sum):
  print("Neon")
else:
  print("Not a neon")


