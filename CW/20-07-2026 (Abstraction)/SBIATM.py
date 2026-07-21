from ATM import ATM

class SBIATM(ATM):
  def withdraw(self,amount):
    if amount>0:
      self.bal -= amount
      print(f"Amount is {amount} debited")

obj = SBIATM(1000)
print(obj.getbal())
obj.withdraw(300)
print(obj.getbal())