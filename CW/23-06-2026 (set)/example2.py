s1={12,35,8,25,5}
s2={25,6,35,15,8}

all_elements = s1|s2
print("elements divisible by 5 : ")
for item in all_elements:
  if item%5==0:
    print(item)



evensum=0

for item in all_elements:
  if item%2==0:
    evensum += item

print("Sum of even elements : ",evensum)


common_elements = s1&s2
csum=sum(common_elements)
square=csum**2
print("Cube : ",square**3)
  

# nonrepeating elements multiplication

nonrepeting = s1^s2
print(nonrepeting)
mult=1

for item in nonrepeting:
  mult*=item

print("Multiplication : ",mult)
