# no return type , no argument

def greet():
  print("Hello everyone")
greet()


# no return type , with argument

def greetuser(ip):
  print(f"Hello {ip}")
# name = input("Enter your name : ")
greetuser("mangesh")


# return type with argument

def add(a,b):
  return a+b

sum=add(10,20)
print("Sum : ",sum)


# returnt type without argument

def get_no():
  return 10**2
# print("Square of 10 : ",get_no())
square = get_no()
print("Square of 10 : ",square)


