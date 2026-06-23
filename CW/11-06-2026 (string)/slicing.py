# x="India is my country"

# print(x[6:8])

# print(x[12:17])

# print(x[7:10])

# print(x[16:])

# print(x[10:5:-1])

# print(x[::-1])





# palindrome string---------------------------------------------------------------------------------


# ip = input("Enter a string : ")

# if ip==ip[::-1]:
#   print("Palindrome")
# else :
#   print("Not palindrome")




# find count of digit and charecters in given string------------------------------------------------


# x="abc1234"
# ct_digit=0
# ct_char=0

# for ch in x:
  # if ch>='0' and ch<='9':
  #   ct_digit+=1
  # elif ch>='a' and ch<='z' or ch>='A' and ch<='Z':
  #   ct_char+=1

  # if ch.isdigit():
  #   ct_digit+=1
  # elif ch.isalpha():
  #   ct_char+=1


# print("Count of digit is :",ct_char)
# print("Count of charecter is :",ct_digit)

# print(f"Count of digit is : {ct_digit} \nCount of charecter is : {ct_char}")





# swap case-----------------------------------------------------------------------------------------

# str="sWapCaSe"

# str2=""


# for ch in str:
#    if ord(ch)>=65 and ord(ch)<=90:
#     str2+=(chr(ord(ch)+32))
#    else:
#     str2+= ch
   
# print(str2)


# unique char stor in new string using not in------------------------------------------------------


# str="programming"
# unique=""

# for ch in str:
#   if ch not in unique:
#     unique+=ch

# print(unique)

# count a word-------------------------------------------------------------------------------------

# x="i love python programming"
# count=1

# for ch in x:
#   if " " in ch:
#     count+=1
# print(count) 

x="i love python programming"
count=0

for ch in x:
  if " " in ch:
    count+=1

count+=1
print(count) 