class person:
  def __init__(self,name,city,age):
    self.name=name
    self.city=city
    self.age=age

  def display_personal_details(self):
    print("\n----------Personal details-----------")
    print(f"Name : {self.name} , City : {self.city} , Age : {self.age}")

  def show(self):
    print("Hello i am from Person")