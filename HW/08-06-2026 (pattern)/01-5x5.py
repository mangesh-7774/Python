for i in range(5):
  for j in range(5):
    if i==0 or i==4 or j==0 or j==4:
      print("0", end=" ")
    elif i==2 and j==2:
      print("0", end=" ")
    else:
      print("1", end=" ")
  print()