total = 0
grade='F'

for i in range(1,6):
  if i==1:
    marks = int(input("Enter marks for Python : "))
  elif i==2:
    marks = int(input("Enter marks for Java : "))
  elif i==3:
    marks = int(input("Enter marks for C : "))
  elif i==4:
    marks = int(input("Enter marks for C++ : "))
  elif i==5:
    marks = int(input("Enter marks for JavaScript : "))

  total +=marks

percentage = total/5

if percentage>90:
  grade='A'
elif percentage>80:
  grade='B'
elif percentage>70:
  grade='C'
elif percentage>60:
  grade='D'
else :
  grade='F'

print("------------------------------RESULT----------------------------")
print("Total : ",total)
print("Percentage : ",percentage,"%")
print("Grade : ",grade)