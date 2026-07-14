class xyz:
  x=20
  __a=90
  
  def getA(self):
    return self.__a
  
  def abc(self):
    print("Public method")
  
  def __show(self):
    return "Private mentod"
  
  def call_show(self):
    return self.__show()

  

print(xyz.x)

obj = xyz()

print(obj.getA())
print(obj.call_show())
