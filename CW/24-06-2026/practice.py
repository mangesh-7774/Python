# def cube(num):
#   return num**3

# num = int(input("Enter a number : "))
# print("Cube : ",cube(num))


# addition of two numbers----------------------------------------------

# def add(a,b):
#   return a+b

# num1 = int(input("Enter a number 1 : "))
# num2 = int(input("Enter a number 2 : "))

# print("Addition : ",add(num1,num2))


# addition of multiple numbers -----------------------------------------
#arbitaries 

# def add(*args):
#   print(sum(args))
#   print(type(args))

# add(1,4,3,54,54,7,678)





# print user info-------------------------------

def info(name,age,marks):
  return f"name: {name} \nage: {age} \nmarks: {marks}"

name = input("Enter name : ")
age = int(input("Enter age : "))
marks = input("Marks : ")

print(info(name,age,marks))

