str="hello"
len=0
rev=""
for i in str:
  len += 1

for i in range(len-1,-1,-1):
  # print(str[i], end=" ")
  rev+=str[i]
  

print(rev)