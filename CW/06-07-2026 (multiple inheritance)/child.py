from parent1 import p1
from parent2 import p2

class child(p1,p2):
  def __init__(self,p1name,p2name,c_name):
    p1.__init__(self,p1name)
    p2.__init__(self,p2name)
    self.c_name=c_name

obj = child("Ram","Sita","AKash")
print(obj.c_name)
print(obj.p1name)
print(obj.p2name)
