def factorial(n):
  factorial=1
  for i in range(1,n+1):
     factorial= factorial*i
  return factorial

num = int(input("Enter a number : "))
originalNumber = num
sumOfFactorials = 0

while(num>0):
  digit = num % 10
  sumOfFactorials = sumOfFactorials+factorial(digit)
  num = num//10
  
if(originalNumber==sumOfFactorials):
  print("It is strong number")
else:
  print("Not a strong number")