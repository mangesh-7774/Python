from bankaccount import BankAccount

class SavingAccount(BankAccount):
  def __init__(self,account_number,account_holder,balance,intrest_rate):
    super().__init__(account_number,account_holder,balance)
    self.intrest_rate=intrest_rate

  def calculate_intrest(self):
    return (self.balance * self.intrest_rate) / 100

  def apply_intrest(self):
    intrest = self.calculate_intrest()
    self.balance += intrest
    print(f"Intrest of Rs.{intrest:.2f} applied")

