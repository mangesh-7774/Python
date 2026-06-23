str="hElLO"

# print(ord(str[0]))

for ch in str:
   if ord(ch)>=97:
    print(chr(ord(ch)-32))
   else:
    print(chr(ord(ch)+32))