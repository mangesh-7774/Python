class Car:
  brand = "TATA"
  def __init__(self,name,model,wheels,price,quantity):
    self.name=name
    self.model=model
    self.wheels=wheels
    self.price=price
    self.quantity=quantity

total=0 
car1=Car("Punch",2020,4,1400000,5)
car2=Car("XUV",2024,4,1300000,10)
car3=Car("ABC",2018,4,1200000,7)

l = [car1,car2,car3]

for i in l:
  if(i.quantity>=5 and i.quantity<10):
    print(f"Car Brand : {i.brand} {i.name} {i.model} {i.wheels} {i.price} {i.quantity}")
  total+=i.price*i.quantity

print("Total price of all cars : ",total)

print("------------------------------------------------------------------------------------")


for i in l:
  if(i.quantity>=5 and i.quantity<10):
    print(i.name, i.quantity)

