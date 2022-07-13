num1 = int(input("enter 1 no : "))
num2 = int(input("enter 2 no : "))
try:
    res = num1/num2
    print(res)
except Exception as e1:
    num2 =int(input("Enter 2 no : "))
    try:
        res=num1/num2
        print(res)
    except Exception as e:
        print(e)

except ValueError as e:
    print(e)
finally:
    print("new db")
    print("Line 1")
    print("Line 2")