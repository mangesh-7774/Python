class demo:
  def __init__(self,name,id,age):
    self.name=name
    self.id=id
    self.age=age

  def modify(self,new_name):
    ex_name = self.name
    new_name = input("Ener new name : ")
    self.name = new_name
    print(f"Existing name : {ex_name} , Updated name : {self.name}")


obj1 = demo("ram",101,21)
print(obj1.name , obj1.id, obj1.age)

obj1.modify("Ramu")
print(obj1.name , obj1.id, obj1.age)

