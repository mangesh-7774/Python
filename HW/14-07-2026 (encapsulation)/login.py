import random as r
import time
from mail import send_email
from mail import send_success


class Login :
  def __init__(self):
    self.mobile = ""
    self.email = ""
    self.__otp = None
    self.sendTime = None
    self.attempts = 0
    self.recievedTime = None

  def get_mobile_no(self):
    while True :
      email = input("Enter yur email : ")
      self.email = email
      mobile = input("Enter 10 digit mobile number : ")
      if len(mobile)==10 and mobile.isdigit() :
        self.mobile = mobile
        return
      else :
        print("\nInvalid mobile number..!")
  
  def generate_otp(self) :
    self.__otp = r.randint(1000,9999)
    self.sendTime = time.time()
    send_email(self.email,self.__otp)

  def verify_otp(self) :
    while True :
      if self.attempts < 3 :
        user_otp = int(input("Reenter your OTP : "))
        self.recievedTime = time.time()
    
        expired = self.check_expired()
    
        if expired :
          print("OTP Expired..!")
          choice = int(input("Do you want to resend OTP ? \n1.Yes \n2.No \n"))
          if choice == 1 :
            self.generate_otp()
          else : 
            return

        elif self.__otp == user_otp:
          send_success(self.email)
          return
        else :
          print("Invalid OTP")
          self.attempts += 1
      else : 
        print("You reached maximum trial limit...! , please try after 24 hours.")
        return

  def check_expired(self) : 
    if self.recievedTime - self.sendTime > 30 :
      return True
    else :
      return False

  def login(self) :
    self.get_mobile_no()
    self.generate_otp()
    self.verify_otp()

obj = Login()
obj.login()
    
   


