import random as r
import time

class login:
  def __init__(self):
    self.mob = ""
    self.__otp = None
    self.__attempts=0

  def check_attempt(self):
    if self.__attempts < 3 :
      self.check_login()

  def check_login(self):
    self.mob = input("Enter mobile number : ")
    if len(self.mob)==10 and self.mob.isdigit() :
     self.__otp = r.randint(1000,9999)
     print(f"Your otp is : {self.__otp}")
     self.sendtime = time.time()
     self.userOtp = int(input("Reenter OTP : "))
     self.currenttime = time.time()
 
     if self.currenttime - self.sendtime > 30:
       print("OTP expired...!")
       choice = int(input("Do you want to resend OTP if yes press 1 otherwise 2 : "))
       if choice == 1:
        self.resendOtp()
       
       return
 
     if self.__otp == self.userOtp :
       print("welcome user..!")
       return
     else: 
       print("OTP not matched")
       self.__attempts += 1
       print(3-self.__attempts ,"attempts remaining")
       if self.__attempts == 3 :
         print("Attempts reached , please try after some tyme..!")
         return
       self.check_attempt()
    else:
      print("please give 10 digit nub no ")
  
  def resendOtp(self):
    self.check_login()

obj = login()
obj.check_login()