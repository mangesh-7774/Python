# x=[10,20,30]
# print(x)
# print(x[1])
# x[1] = 200
# print(x[1])





# print all elements in list 
 
# for item in x:
#   print(item)

# adding elementts in list

# x.append(40)
# print(x)

# x=[]
# print(x)

# for i in range(6):
#   ip  = input(f"Enter {i+1} element : ")
#   x.append(ip)

# print(x)




# extend method of list 

# x=[1,2]
# print(x)
# x.extend([3,4])
# print(x)


# insert method

# x=[11,13]
# print(x)
# x.insert(1,12)
# print(x)

# remove() and pop()

# x=[11,13,14,15]
# x.remove(13)
# print(x)
# x.pop(2)
# print(x)


# clear()  

# x.clear()
# print(x)

# count()

# x=[10,20,40,23,10]
# print(x.count(10))

# print(x.index(23))
# x.sort()
# print(x)
# y=x.copy()
# print(y)

# functions 
# print(len(x))
# print(max(x))
# print(min(x))

# x=[10,20,45,30]
# sum=0

# for i in x:
#   sum+=i

# print(sum)


#  find count without function 

# count=0

# for i in x:
#   count+=1

# print(count)

# min= x[0]

# for i in x:
#   if i<min:
#     min=i
# print(min)


# student = [1,"ram",2,"sita",3,"pooja"]

# for i in range(len(student)):
#   if i%2!=0:
#     print(student[i])


student = [1,"ram",45,2,"sita",78,3,"pooja",90]
          
# for i in range(len(student)):
#   if i%3==0:
#     print(student[i])
#   elif i==2 or i%2!=0:
#     print(student[i])
#   else:
#     print(student[i])

for i in range(len(student)):
  if i%3==0:
    print(student[i])
    print(student[i+1])
    print(student[i+2])
    print("====")

 
 




