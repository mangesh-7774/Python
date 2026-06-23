menu = ((1, "paneer", 400),(2, "chicken", 600),(3, "desert", 200),(4, "noodles", 150))
orders=[]
bill=0

while True:
    print()
    print("-----HOTEL MENU-------\n1.View menu\n2.Order\n3.Generate bill\n4.Exit")
    choice = int(input("Enter choice : "))

    match choice:
        case 1:
            print("Items are :")
            print("---------------------------------")
            print("ItemId    Name    Price")
            print("---------------------------------")
            for item in menu:
                print(f"   {item[0]}     {item[1]}   {item[2]}")

        case 2:
            print()
            for item in menu:
                print(f"   {item[0]}     {item[1]}   {item[2]}")
            id = int(input("Enter dish Id to place order : "))
            flag=0
            for item in menu:
                if item[0]==id:
                    flag=1
                    ord = (item[0],item[1],item[2])
                    orders.append(ord)
            
            if flag==0:
                print("Invalid item  id please try with valid")
                    
        case 3:
            for item in orders:
                
                bill+=item[2]
                cgst = bill*0.10
                sgst = bill*0.10
                finalBill = bill+cgst+sgst
                print()
                
            break

        case 4:
            break  

        case _:
            print("Invalid choice")

print("---------------")
print("Bill : ",bill)
print("CGST : ",cgst)
print("SGST : ",sgst)
print("---------------")
print("Final Bill : ",finalBill)

