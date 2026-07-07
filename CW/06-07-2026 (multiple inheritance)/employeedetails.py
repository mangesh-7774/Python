from companydetails import company
from personaldetail import person

class employee(company,person):
  def __init__(self,name,city,age,dept,role,cname,salary):
    person.__init__(self,name,city,age)
    company.__init__(self,dept,role,cname)
    self.salary=salary

  def display_details(self):
    self.display_company()
    self.display_personal_details()
    print("\n-------Emp details-----------")
    print(f"Salary : {self.salary}")
  
