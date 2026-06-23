def print1to10():
      i=1
      while i<=10:
            print(i)
            i=i+1

def table():
      num = int(input("Enter a Number to print table : "))
      i=1
      while i<=10:
            print(num*i)
            i=i+1

def prime_1_to_100():
    n = 2

    while n <= 100:
        i = 2
        is_prime = True

        while i < n:
            if n % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            print(n)

        n += 1

def palindrome():
    n = int(input("Enter a number to check its palinfrome or not :"))
    original = n
    reverse = 0

    while n>0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    
    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")


while(1):
      print("1 - 1 to 10 \n2 - table \n3 - 1 to 100 prime \n4 - palindrome")
      ch = int(input("Enter your choice"))

      if ch==1:
            print1to10()
      elif ch==2:
            table()
      elif ch==3:
            prime_1_to_100()
      elif ch==4:
            palindrome()
      else:
            print("Invalid")
      
      c=int(input("do you want to continue press 1 and to stop press 2"))

      if c!=1:
            break

print("----------Thank You-------------1")