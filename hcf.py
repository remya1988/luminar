num1 = int(input("Enter 1 no : "))
num2 = int(input("Enter 2 no : "))
num3 = int(input("Enter 3 no : "))
hcf = 1
l = min(num1,num2,num3)
# if num1 > num2:
#     l = num2
# else :
#     l = num1
for i in range(2, (l+1)):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        hcf = i
        i += 1
print("Hcf of ", num1, num2, "and ", num3, "is ", hcf)

