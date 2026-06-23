# stud={
#    "rollno":101,
#    "name":"ram",
#    "age":30,
#    "sub":["math","eng","java"],
#    "marks":(90,89,67)
# }


# print(stud.keys())
# print(stud.values())
# print(stud.items())

# print()


# for key in stud:
#   print(key)


# for value in stud.values():
#   print(value)



# for k,v in stud.items():
#   print(k,v)

# for k,v in stud.items():
#   if k==stud["sub"]:
#     print(k)
#   print(k,v)


# for i in range(len(stud["sub"])):
#   print(f"{stud["sub"][i]} : {stud["marks"][i]}")


# output  -> math : 90
#            eng : 89
#            java : 67



# using zip()

# for sv , mv in zip(stud["sub"],stud["marks"]):
#   print(sv,mv)



stud={
  101:{
    "name":"ram",
    "age":22,
    "sub":["math","eng","java"],
    "marks":(90,89,67)
  },
  102:{
    "name":"sita",
    "age":20,
    "sub":["math","eng","java"],
    "marks":(92,69,67)
  },
  103:{
    "name":"shyam",
    "age":18,
    "sub":["math","eng","java"],
    "marks":(90,90,57)
  }
}

# print(stud)
# print(stud[101]["sub"])
# print(stud[102]["marks"][2])


# for key in stud:
#   for v in stud[key]["marks"]:
#     print(v, end=" ")
#   print()

for key in stud:
  print("student Id: ",key)
  for k,v in stud[key].items():
    print(k," : ",v)
  print("-----------")
