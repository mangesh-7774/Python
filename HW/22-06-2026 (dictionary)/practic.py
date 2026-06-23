student = {
  "name":"Mangesh",
  "age":22
}

# for key , value in student.items():
#   print(key,":",value)

# student2 = student.copy()
# student2.setdefault("Address",0)

# print(student2)

# keys = ["name","age","address"]

# student = dict.fromkeys(keys,"N/A")
# print(student)


if "age" in student:
  print("Hay")

else:
  print("Nay")


print(len(student))


dictionary = {
  x:x*2 for x in range(6)
  }

print(dictionary)