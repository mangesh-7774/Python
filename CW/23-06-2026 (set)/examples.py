py_stud={"ram","sita","komal","ramu"}
jv_stud={"ram","pavan","gita"}
fd_stud={"gita","komal","payal","ram"}


# total count of each
print(len(py_stud))
print(len(jv_stud))
print(len(fd_stud))

# length of all students 
all_stud = py_stud | jv_stud | fd_stud
print("All students : ",len(all_stud))

# names of students who are attending java & python

print("Java and python students : ",jv_stud | py_stud)

# who are attending java , python & frontend 

print("java , python and frontend : ",jv_stud & py_stud & fd_stud)

# only java student

print("Only python student : ",jv_stud)

# only python student

print("Only java : ",py_stud)

# names of students who are not attendin java

print("student who are not attending java : ",(py_stud & fd_stud)-jv_stud)

# count of student who attending 3 batches at a time 

print("Count of student who attends 3 batches at a time : ",len(py_stud & jv_stud & fd_stud))

# name of student who attend only 1 batch at a time 

for stud in all_stud:
  count = 0
  if stud in py_stud:
    count+=1
  if stud in jv_stud:
    count+=1
  if stud in fd_stud:
    count+=1
  if count==1:
    print(stud)