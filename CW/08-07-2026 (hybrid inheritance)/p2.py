from gp import GP

class P2(GP):
  def __init__(self,marks,**kwargs):
    print("I am P2 constructor")
    self.marks = marks
    print("Marks : ",self.marks)
    # GP.__init__(self)
    super().__init__(**kwargs)