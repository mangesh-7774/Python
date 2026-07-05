result = int(input("Enter a number : "))

while True:
  op = input("Enter a operator : ")

  if op=="=":
    print("Result : ",result)
    break

  num = int(input("Enter next number : "))
  
  if op=="+":
    result+=num
  elif op=="-":
    result-=num
  elif op=="*":
    result*=num
  elif op=="/":
    result/=num
  elif op=="%":
    result%=num
  else :
    print("Invalid choice")



   