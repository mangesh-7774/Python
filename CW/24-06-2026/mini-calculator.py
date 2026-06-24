def addition():
  a = int(input("Enter number 1 : "))
  b = int(input("Enter number 2 : "))
  print("Addition : ",a+b)

def substraction():
  a = int(input("Enter number 1 : "))
  b = int(input("Enter number 2 : "))
  print("Substraction : ",a-b)

def multiplication():
  a = int(input("Enter number 1 : "))
  b = int(input("Enter number 2 : "))
  print("Multiplication : ",a*b)

def division():
  a = int(input("Enter number 1 : "))
  b = int(input("Enter number 2 : "))
  print("Division : ",a//b)

def reminder():
  a = int(input("Enter number 1 : "))
  b = int(input("Enter number 2 : "))
  print("Reminder : ",a%b)

print("\n1.Addition \n2.Substraction \n3.Multiplication \n4.Division \n5.Reminder")
choice = int(input("\nEnter your choice : "))



match choice:
     case 1:
         addition()
     case 2:
         substraction()
     case 3:
         multiplication()
     case 4: 
         division()
     case 5:
         reminder()
     case _:
        print("Invalid choice..!")