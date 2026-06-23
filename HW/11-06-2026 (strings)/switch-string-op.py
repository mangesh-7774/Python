str = input("Enter a string : ")

print("your sring is :",str)

print()



ch = int(input("Press the number which you want to perform : \n1 - reverse string \n2 - check palindrome \n3 - convert string \n4 - count words \n5 - sort string \nEnter yur choice here : "))

match ch:
       case 1:
           rev = str[::-1]
           print("\nReversed String : ",rev)
       case 2:
           rev = str[::-1]
           if str==rev:
            print("\npalindrome string")
           else:
            print("\nNot a palindrome")
       case 3:
           ip=int(input("\nSelect your choice to convert : \n1 - To Upper Case \n2 - To Lower Case \n3 - Swap Case \nSelect choice here :"))
           match ip:
                  case 1:
                     upper = str.upper()
                     print("\nUpper :",upper)
                  case 2:
                     lower = str.lower()
                     print("\nLower :",lower)
                  case 3:
                     swapped = str.swapcase()
                     print("\nSwapped :",swapped)
                  case _:
                     print("\nInvalid selection please try with valid one")
       case 4:
           word=0
           for ch in str:
               if " " in ch:
                word+=1
           word+=1
           print("\nWords in String :",word)

       case 5:
           sortedstr = " ".join(sorted(str))
           print("\nSorted string : ",sortedstr) 
       case _:
           print("\nInvalid choice please try with valid one")
           

    
