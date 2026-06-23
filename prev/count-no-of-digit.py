# num = 1234
# sum=0
# while num>0:
#   rem = num%10
#   sum = sum+rem
#   num = num//10
# print(sum)

# count nummber of digits 

# num=242832
# count=0

# while num>0:
#     num = num//10
#     count+=1

# print(count)
    


# palindrome number 

# num = int(input("Enter a number"))
# rev=0
# originalnum = num
# while num>0:
#   rem = num%10
#   rev = rev*10+rem
#   num = num//10
# if(rev==originalnum):
#   print("Palindrome")
# else:
#   print("Not Palindrome")

# Armstrong number

# num = int(input("Enter a number"))

# temp = num

# sum =0
# count = 0

# while temp>0:
#     count+=1
#     temp = temp//10

# temp = num

# while temp>0:
#     rem = temp%5`10`
#     sum = sum+rem**count
#     temp = temp//10

# if num==sum:
#     print("Armstrong")
# else: 
#     print("Not armstrong")


# happy number 

# num = int(input("Enter a number : "))

# while num!=0 and num!=4:
#   sum=0
#   while num>0:
#     rem=num%10
#     sum+=rem*rem
#     num//=10
#   num=sum

# if(num==1):
#   print("Happy")
# else:
#   print("Sad")



# Buzz number

# num = int(input("Enter a number : "))

# if num%7==0 or num%10==7:
#   print("Buzz")
# else:
#   print("Not buzz")


# star pattern 

n = int(input("Enter a number : "))

for i in range(1,n+1):
    print("*"*n)
print()


# n= int(input("Enter a number"))

# for i in range(1,n+1):
#   for j in range(n):
#     print(i,end=" ")
#   print("")



# num = 1

# for i in range(3):
#     for j in range(3):
#         print(num, end=" ")
#         num += 1
#     print()


