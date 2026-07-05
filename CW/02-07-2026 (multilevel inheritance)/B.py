from A import GP

class P(GP):
  xyz="Hiii"

  def __init__(self,name,age):
    self.age=age
    super().__init__(name)
