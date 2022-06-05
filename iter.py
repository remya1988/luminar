
num = int(input("Enter a number : "))
sum = 0



j = 1
pattern = ""
while (j<=num):
    pattern = pattern + str(num)
    sum = sum + int(pattern)
    j += 1
    print(pattern," + ")
print(" = ", sum)


