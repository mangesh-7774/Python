# howe work 
student = [[101,"Ram",98],[102,"sita",88],[103,"ramu",78],[104,"gita",99]]

while True:
    
    print("sms\n1.add\n2.view\n3.update\n4.delete\n5.topper\n6.Exit")
    choice=int(input("enter the choice: "))
    match choice:
        case 1:
            ip=int(input("enter how many student do u want to add : "))
            for i in range(ip):
                student_id=int(input("enter the id:"))
                student_name=input("enter the name:")
                student_marks=float(input("enter the marks:"))

                student.append([student_id,student_name,student_marks])
                print(f"student {i+1} added !")
        case 2:
            for s in student:
                print(f"ID:{s[0]} Name:{s[1]} Marks:{s[2]}")
        case 3:
            update_id=int(input("enter student id : "))

            get = False
            
            for s in student:
                if s[0]== update_id:
                    s[1]=input("enter new name: ")
                    s[2]=float(input("enter new marks: "))
                    print(f"student {s[0]} details update")
                    get = True
                    break
            if get == False:
                print("student not found!")
        case 4:
            delete_id=int(input("enter the student id :"))

            match = False

            for s in student:
                if s[0]==delete_id:
                    student.remove(s)
                    print(f"student {s[0]} deleted!")
                    match = True
                    break
            if match==False:
                print("student not found !")
        case 5:
            pass
        case 6:
            print("thanks for using sms")
        case _ :
            print("invalid condition")