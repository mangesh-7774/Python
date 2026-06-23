str = "       Hello  "
print("Length of string before removing whitespaces : ",len(str))
str2=""

for ch in str:
  if ch != " ":
    str2+=ch
print("Length of string After removing whitespaces",len(str2))

