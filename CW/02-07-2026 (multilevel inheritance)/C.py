from B import P

class C(P):
  pqr = "Byeee"

  def __init__(self,name,age,marks):
    self.marks=marks
    super().__init__(name,age)

obj = C("Mangesh", 22 , 66)
print(obj.pqr, obj.xyz, obj.abc)
print()
print(obj.name)
print(obj.age)
print(obj.marks)