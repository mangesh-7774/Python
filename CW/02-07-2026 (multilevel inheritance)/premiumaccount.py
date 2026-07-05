from savingaccount import SavingAccount

class PremiumAccount(SavingAccount):

  def __init__(self,account_number,account_holder,balance,intrest_rate):
    super().__init__(account_number,account_holder,balance,intrest_rate)
    self.benifit = 500

  def calculate_benifit(self):
    if self.balance > 5000:
      print(f"Congratulations..!, You won the Rs.{self.benifit}")

      choice = input("Do you want to add this reward to your bank (press 'y' - if yes , otherwise 'n') : ")

      if choice.lower() == 'y':
        self.balance += self.benifit
        print("Congrats your reward successfully added to your ban account...!")
      elif choice.lower() == 'n':
        print("You can add reward to bank account next time..!")
      else:
        print("Invalid Choice")
    else:
      print("Maintain a mininum balance Rs.5000 to get benefits")
      print(f"Your current balance : {self.balance}")

  def show_summary(self):
     print("\n------ Summary ------")
     print("Account Number :", self.account_number)
     print("Account Holder :", self.account_holder)
     print("Balance        :", self.balance)
     print("Interest Rate  :", self.intrest_rate, "%")
     print("Benefits       :", self.benifit)
   

account = PremiumAccount(7774874737,"Mangesh",4500,5)


# account.deposit(2000)
# account.withdraw(300)

# print()

# print(account.calculate_intrest())
# account.apply_intrest()
# print(account.check_balance())

# print()
# account.calculate_benifit()
# print(account.check_balance())

# account.show_summary()



while True:
  print("\nChoose your role : \n1.Customer \n2.Admin \n3.Exit\n")
  choice = int(input("Enter your choice : "))

  match choice:
       case 1:
           print("\n-------------- Customer Section -----------------")
           print("\n1.Deposit \n2.Withdraw \n3.See Balance \n4.Exit\n")
           ip = int(input("Enter your choice : "))

           match ip:
                case 1:
                    amount = int(input("Enter amount to Deposit : "))
                    account.deposit(amount)
                case 2:
                    amount = int(input("Enter amount to Withdraw : "))
                    account.withdraw(amount)
                case 3:
                    account.check_balance()
                case 4:
                    print("\nExit customer section...!")
                case _ :
                    print("Invalid choice please try again..!")   
       case 2:
           print("\n-------------- Admin Section -----------------")
           print("\n1.Deposit \n2.Withdraw \n3.See Balance \n4.Calculate intrest \n5.Apply Intrest \n6.Calculate benifit \n7.Show summary \n8.Exit\n")
           ip = int(input("Enter your choice : "))

           match ip:
                case 1:
                    amount = int(input("Enter amount to Deposit : "))
                    account.deposit(amount)
                case 2:
                    amount = int(input("Enter amount to Withdraw : "))
                    account.withdraw(amount)
                case 3:
                    print(account.check_balance())
                case 4:
                    print(account.calculate_intrest())
                case 5:
                    account.apply_intrest()
                case 6:
                    account.calculate_benifit()
                case 7:
                    account.show_summary()
                case 8:
                    print("Exit from Admin Section")
                case _ :
                    print("Invalid choice , please try with valid one")      
       case 3:
           print("Exit")
           break
       case _ :
           print("Invalid Choice, please try with valid one...!") 


          


