stud={}


print()
print("-------------------------------------Student Management-----------------------------------")
print()



while True:
  print("Enter your choice to perform operation : \n1.Add students \n2.View marks \n3.See topper-lower")

  choice = int(input("Enter choice here : "))
  
  match choice : 
     case 1:
         ip= int(input("How many students you want to add : "))
         print()
         
         for i in range(0,ip):
           rollnumber = int(input("Enter student roll number : "))
           name = input("Enter name : ")
           age = int(input("Enter age : "))
           sub = input("enter subjects seperated by space (e.g. math science english) : ").split(" ")
           marks = tuple(input("enter marks of subjects seperated by space (e.g. 90 70 85) : ").split(" "))
           print()
           
           stud[rollnumber]={
           "name":name,
           "age":age,
           "sub":sub,
           "marks":marks
           }
     case 2:
         print()
         total=0
         percentage=0
         ip = int(input("1.view all subject marks \n2.marks with percentage \nEnter your choice here : "))
         match ip :
            case 1:
                id = int(input("Enter student id to see his all subject marks : "))  
                for key in stud.keys():
                 if key==id:
                   for j in range(len(stud[key]["marks"])):
                     print(f"{stud[key]["sub"][j]} : {stud[key]["marks"][j]}")
        
            case 2:
                id = int(input("Enter student id to see his percentage with marks : "))  
                for key in stud.keys():
                 if key==id:
                   for j in range(len(stud[key]["marks"])):
                     
                     total = total + ({stud[key]["marks"][j]})
                     percentage = (total/300)*100
                     
                   print("Percentage : ", percentage)
                print(total)

# incomplete--------------------------------------------------------------------------------- 
          



  
        


# for key in stud.keys():
#   print(stud[key])


