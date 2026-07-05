from car import car

class engin:
  brand = "XYZ"
  def __init__(self,uip):
    self.name = "V8"
    self.hp=uip  

  def show_engin(self):
    return f"engin details are : {self.brand} \n{self.name} \n{self.hp}"


