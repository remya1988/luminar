

num1 = int(input("Enter 1 no : "))
num2 = int(input("Enter 2 no : "))
num3 = int(input("Enter 3 no : "))

if (num1>num2) and (num1>num3) :
    if num2>num3 :
        print("Second Largest number is ",num2)
    else :
        print("Second Largest number is ", num3)
elif (num2>num1) and (num2>num3) :
    if num1>num3 :
        print("Second Largest number is ", num1)
    else :
        print("Second Largest number is ", num3)
   # print("Largest number is ", num2)
elif(num3>num1) and (num3>num2) :
    if num1>num2 :
        print("Second Largest number is ", num1)
    else :
        print("Second Largest number is ", num2)