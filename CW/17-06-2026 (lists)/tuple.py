# x=(10,20,30)
# print(type(x))
# print(x[2])

# for i in x:
#   print(i)

#   x=("red","pink","black")

#   print("red" in x)

#   x=(10,20)
#   y=(10,20)

#   print(x is y) #true

#   z=x
#   print(x is z) #true



#-------------------------------------------------------------------------------------------------

# x=(10,20,30)
# a,b,c=x
# print(a) #10
# print(b) #20
# print(c) #30
# print(a,b,c) #10 20 30


# x=(10,20,30)


# print(len(x)) #3
# print(x.count(20)) #1
# print(x.index(30)) #2
# print(x[1:]) #(20,30)
# print(x[1:2]) #(20,)


# Nested tuple

# x=((10,20),(30,40))
# for i in x:
#   for j in i:
#     print(j)


# x=((10,20),30,(40,50),"hi")

# for i in x:
#   if type(i)==tuple:
#     for j in i:
#       print(j)
#     continue
#   print(i)

  


# mixture of lists and tuples--------------------------------------------------------------------

# x=(90,  "hi",   ("red",[10,20]),   [100,200])

# for i in x:
#   if type(i)==tuple or type(i)==list:
#     for j in i: 
#       if type(j)==list:
#         for k in j:
#           print(k)     
#       continue
#   continue
#   print(i)

# above example is wrong -> check again



# conversion list to tuple and tuple to list 

x=(10,20)
print(x,type(x))
y=list(x)
print(y,type(y))

y.append(90)
print(y,type(y))

x=tuple(y)
print(x,type(x))








