from developer import Developer
from tester import Tester
from common_feature import cm

# d = Developer("ram",101,"python",90)
# t = Tester("sita",102,"selenium",88)

# d.development()
# t.testing()

choice = int(input("\n1.Develpoer \n2.Tester \n3.Analyst \n4.Exit \nEnter your choce : "))

if choice==1:
  obj = Developer("Ram",101,"Python",22)
elif choice==2:
  obj = Tester("Sita",102,"Java",20)
else :
  print("Invalid chice..!")


if obj :
  cm(obj)
else : 
  print("No object created..!")