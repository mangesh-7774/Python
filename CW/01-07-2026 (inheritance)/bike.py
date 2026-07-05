from vehicle import vehicle

class bike(vehicle):
  def __init__(self,color,price,brand,fuel_type):
    self.color=color
    self.price=price
    super().__init__(brand,fuel_type)

  def ride(self):
    return "bike rides do fast"
  
  def custom_start(self):
    print(super().start())
    return "HRUMHHHHH"

b1 = bike("Black",1000000,"Hero","Petrol")
# print(b1.color)
# print(b1.price)
# print(b1.brand)
# print(b1.fuel_type)

print(b1.custom_start())

