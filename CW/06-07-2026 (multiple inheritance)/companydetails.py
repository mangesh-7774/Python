class company:
  def __init__(self,dept,role,cname):
    self.dept=dept
    self.role=role
    self.cname=cname

  def display_company(self):
    print("\n----------Componey details-------")
    print(f"Department : {self.dept} , Role : {self.role} , Company : {self.cname}")

  def show(self):
    print("Hello i am from compeny")