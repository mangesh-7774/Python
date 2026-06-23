# manunal input

x={10,20}
print(x,type(x))

# user input

y=set()
y.add(10)
print(y,type(y))

s={10,20,30,40,10,20}

for item in s:
  print(item)

s.add(90)
print(s)

# s.remove(80) #if not fount key error
s.remove(30)

s.discard(80)
print(s)

print(s.pop()) #removes random element and returns it 
print(s)

s.clear()
print(s)


a={1,2}
b=a.copy()
print(b)


# update

a.update([10,20,40])
print(a)

# functions 

s2={10,44,23,22,21}
print(len(s2))
print(min(s2))
print(max(s2))
print(sum(s2))


# operations 

x1={1,2,3}
x2={3,4,5}

print()

print(x1)
print(x2)

# union - it prints all unique elements from both sets 
print(x1.union(x2))
print(x1|x2)


# intersection --> common data

print(x1.intersection(x2))
print(x1&x2)



# difference

print(x1.difference(x2))
print(x1-x2)


# symentic difference --> prints all , ignore common data

print(x1.symmetric_difference(x2))
print(x1^x2)

