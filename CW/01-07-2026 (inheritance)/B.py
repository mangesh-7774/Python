from A import A

class B(A):
  def abc(self):
    print("hello abc")

  def __init__(self):
    print("def con in B class")

obj = B()
print(B.mro())
# mro() --> method resolution order
