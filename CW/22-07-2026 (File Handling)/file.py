# file = open("myfile.txt",'x')
# print(f"{file} created")

try:
  file = open("CW/22-07-2026 (File Handling)/demo.txt",'x')
  print(f"{file} created")
except Exception as e:
  print(e)


# mode -> 'w'

with open("CW/22-07-2026 (File Handling)/demo.txt","w") as f:
  f.write("How R U?")  #write() overrides -> first deletes existing data and then write
  print("Data inserted")

# mode -> 'r'

with open("CW/22-07-2026 (File Handling)/demo.txt","r") as f:
  # sentence = f.read()  
  # print(sentence)
  print(f.read())


# mode -> 'a'

with open("CW/22-07-2026 (File Handling)/demo.txt","a") as f:
  f.write("\nData added")
  print("New data added")




