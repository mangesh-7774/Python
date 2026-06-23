num1 = int(input("Emter first number : "))
num2 = int(input("Emter second number : "))

hcf=1
for i in range(1,min(num1,num2)+1):
  if(num1%i==0 and num2%i==0):
    hcf=i

lcm = max(num1, num2)
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += 1

print("HCF : ",hcf)
print("LCM : ",lcm)