from person import Person

class Developer(Person):
  def __init__(self,name,id,skills,age):
    super().__init__(name,id,skills)
    self.age=age

  def calculate_bonus(self):
    salary = int(input("Enter your saary : "))
    bonous_amount = salary * 0.15
    super().bonus()
    print(bonous_amount)
    print(f'Your salary in this month is {salary + bonous_amount}')

  def development(self):
    print("I am writing code")


# dev = Developer("Mangesh",101,"Python",22)
# print(dev.name)
# print(dev.skills)
# print(dev.age)
# dev.bonus()
# dev.calculate_bonus()
# dev.development()