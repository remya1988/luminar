num = [10,11,12,14,15,17,18,19]

n = 20
f = 0
for n1 in num:
    if n1 == n:
        print("Number", +n ,"is in array....")
        break
    else :
        f = 1
if f == 1:
    print("Number", +n ,"is not in array....")

