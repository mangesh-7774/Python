from employeedetails import employee
from personaldetail import person
from companydetails import company

emp = employee("MAngehs","Nanded",22,"IT","PY-Deveoper","TCS",22000)
emp.display_details()

emp.show()


# if we want to call the both methods of different class
person.show(emp)
company.show(emp)