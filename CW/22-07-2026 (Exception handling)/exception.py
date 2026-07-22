# print("Start")
# try:
#   print(10/0)
# except ZeroDivisionError:
#   print("Don't divide by zero")

# print("Program end")

# -------------------------------------------------------------------------------------------------

# print("Start")
# try:
#   ip = int(input("Enter a number : "))
#   print(ip)
# except ValueError as e:
#   print(e)

# print("Program end")

# --------------------------------------------------------------------------------------------------

# print("Start")
# try:
#   x=[10,20,30]
#   print(x[5])
# except IndexError:
#   print("Please enter valid index")

# print("Program end")



# multiple custom errors ---------------------------------------------------------------------

# print("Start")
# try:
#   num1 = int(input("Enter a number one : "))
#   num2 = int(input("Enter number two : "))

#   division = num1/num2
#   print(division)

# except ZeroDivisionError:
#   print("You cannot divide a number by zero")
# except ValueError as e:
#   print(e)

# print("Program end")



# handle multiple errors with predefined error message -------------------------------------------


# print("start")
# try:
#   x=[10,20,30]
#   print(x[1])
#   print(10/0)
# except Exception as e:
#   print(e)
# print("end program")


# handleing multiple errors with custom message -------------------------------------------------

# print("Start")
# try:
#   ip = int(input("Enter a number : "))
#   print(10/ip)
# except (ZeroDivisionError , ValueError):
#   print("something went wrong")

# print("End program")



# finaly - always executes --------------------------------------------------------------------

# print("Start")
# try:
#   ip = int(input("Enter a number : "))
#   print(10/ip)
# except (ZeroDivisionError , ValueError):
#   print("something went wrong")
# finally:
#   print("I'm always executes")

# print("End program")



# Custom error handling --------------------------------------------------------------------

class AgeError(Exception):
  pass

print("Start")
try:
  age = int(input("Enter your age : "))
  if age>18:
    print("Eligible")
  else:
    raise AgeError("Age shoud be greater than 18")
except Exception as e:
  print(e)
       
print("Successfully executed")




  


