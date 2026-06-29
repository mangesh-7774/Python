# class demo:
#   def __init__(self):
#     print("Default constructor called")

# obj=demo()

# class demo:
#   inst_name="Linkcode"

# print(demo.inst_name)

# obj = demo()
# print(obj.inst_name)


# class demo:
#   #instance variable
#   def __init__(self):
#     self.name="Ram"
#     self.age=22

# obj = demo()
# print(obj.name)
# print(obj.age)


class mobile:
  def __init__(self,name,brand,color,price):
    self.name=name
    self.brand=brand
    self.color=color
    self.price=price

iphone15 = mobile("iphone15","Apple","Black",10000)
print(f"{iphone15.name} , {iphone15.brand} , {iphone15.color} , {iphone15.price}")

iphone16 = mobile("iphone16","Apple","White",15000)
print(f"{iphone16.name} , {iphone16.brand} , {iphone16.color} , {iphone16.price}")


l = [iphone15,iphone16]
# print(l)
for i in l:
  print(i.name)