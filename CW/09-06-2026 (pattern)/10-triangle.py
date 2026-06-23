n = 4

for i in range(1,n+1):
    for j in range(i):
        if(i%2==0):
          print("0", end=" ")
        else:
          print("1", end=" ")

    print()