from engin import engin

class car:
  def __init__(self,uip):
    self.age=90
    self.a=engin(uip)

    def car_details(self):
      return f"car details are : {self.age}"

obj = car(200)
print(obj.age , obj.a.name , obj.a.horsepower , obj.a.brand)
print(engin.brand)

print(obj.car_details)
print(obj.a.show_details())



