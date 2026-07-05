class vehicle:
  def __init__(self,brand,fuel_type):
    self.brand=brand
    self.fuel_type=fuel_type
  
  def start(self):
    return "Vehicle started!"
  
  def stop(self):
    return "Vehicle stopped"