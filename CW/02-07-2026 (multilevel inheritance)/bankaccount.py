class BankAccount:
  def __init__(self,account_number,account_holder,balance):
    self.account_number=account_number
    self.account_holder=account_holder
    self.balance=balance
  
  def deposit(self,amount):
    if amount > 0:
       self.balance += amount
       print(f"Deposited Rs. {amount} \nCurrent Avl.Balance is {self.balance}")
    else:
      print("Invalid Amount")
  
  def withdraw(self,amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"Withdraw Rs. {amount} \nCurrent Avl.Balance is {self.balance}")
    else:
      print("Insufficient Balance..!")

  def check_balance(self):
    return f"Available Balance is {self.balance}"

    


   
    
    