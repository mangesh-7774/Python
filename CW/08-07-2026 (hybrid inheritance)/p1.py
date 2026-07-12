from gp import GP

class P1(GP):
  def __init__(self,age,**kwargs):
    print("I am P1 constructor")
    self.age = age
    print("Age : ",self.age)
    super().__init__(**kwargs)


