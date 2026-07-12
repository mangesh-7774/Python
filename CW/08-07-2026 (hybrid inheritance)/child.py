from p1 import P1
from p2 import P2

class Child(P1,P2):
  def __init__(self,city,**kwargs):
    print("I am child constructor")
    self.city = city
    print("City : ",self.city)
    # P1.__init__(self)
    # P2.__init__(self)
    super().__init__(**kwargs)

ch = Child(city="Nanded",age=22,marks=97,name="Mangesh Patil")

print(Child.mro())
