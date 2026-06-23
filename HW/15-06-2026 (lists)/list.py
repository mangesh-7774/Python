x=[101,57,6,98,32,0,57,98]

ip = int(input("Enter a key : "))
found=0

for item in x:
  if item==ip:
    found=1
    break

  
if found==1:
  print("Key found")
else:
  print("Key not found")