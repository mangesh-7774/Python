class Bank:
  bank_name = "SBI"
  ifsc_code = "SBI12323"

  def __init__(self,name,balance,mail):
    self.name=name
    self.balance=balance
    self.mail=mail
  

  def show_details(self):
    print(f"name: {self.name} \nbalance : {self.balance} \nmail : {self.mail} \nbank name : {self.bank_name} \nIFSC : {self.ifsc_code}")
   

  def deposit(self):
    add = int(input("How many money you want to deposit : "))

    self.balance+=add

    print(f"{add} deposited successfully..! \nYour current balance is {self.balance}")


  def withdraw(self):
    wtihd = int(input("Enter amount to withdraw : "))
    if wtihd <= self.balance and wtihd>0:
      self.balance-=wtihd
      print(f"{wtihd} withdraw successfully..! \nYour current balance is {self.balance}")
    else:
      print("Invalid amount")

    


   
    

c1 = Bank("Mangesh",1000,"mangesh@gmail.com")
# c1.show_details()
# c1.deposit()
# c1.withdraw()

c2 = Bank("Ram",2000,"ram@gmail.com")

if c1.balance > c2.balance:
  c1.show_details()
else:
  c2.show_details()
