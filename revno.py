num = int(input("Enter a number : "))
rev = ""
while (num != 0):
    l = num % 10
    rev += str(l)
    num = num // 10

print("Reverse is ",rev)
