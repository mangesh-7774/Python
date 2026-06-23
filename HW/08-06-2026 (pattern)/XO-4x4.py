for i in range(4):
  for j in range(4):
    if (i==0 or i==3) and (j==0 or j==3):
      print("O", end=" ")
    elif i == 0 or i == 3 or j == 0 or j == 3:
      print("X", end=" ")
    else:
      print(" ", end=" ")
  print()


