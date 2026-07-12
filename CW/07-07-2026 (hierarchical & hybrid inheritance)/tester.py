from person import Person

class Tester(Person):
  def __init__(self,name,id,skills,age):
    super().__init__(name,id,skills)
    self.age=age

  def calculate_bonus(self):
    salary = int(input("Enter your saary : "))
    bonous_amount = salary * 0.20
    super().bonus()
    print(bonous_amount)
    print(f'Your salary in this month is {salary + bonous_amount}')
 
  def testing(self):
    print("I am Testing Application")

# t = Tester("Mangesh",101,"Python",22)
# print(t.name)
# print(t.skills)
# print(t.age)
# t.bonus()
# t.calculate_bonus()
# t.testing()