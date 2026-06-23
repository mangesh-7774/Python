str = "hello evryone"

evencount=0
oddcount=0
vowelcount=0

for i in range(0,len(str),1):
  if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
    print("vowel : ",str[i])
    vowelcount += 1
  if i%2==0:
    evencount += 1
  else:
    oddcount += 1

print("even count : ",evencount)
print("odd count : ",oddcount)
print("vowel count : ",vowelcount)
