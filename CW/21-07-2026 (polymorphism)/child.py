from parent import p

class c(p):

  def abc(self):
    print("Child abc")

  def add(self,a,b,c):
    return a+b+c

  def add_parent(self,a,b):
    return super().add(a,b)