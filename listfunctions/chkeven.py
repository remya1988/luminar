numbers = [3, 4, 10, 15, 22, 19]

for num in numbers:
    if num % 2 == 0:
        print(num)
    else:
        continue

newno = [11, 12, 13, 14, 15, 16, 17, 18]

for new in newno:
    if new > 15:
        print(new+1)
    elif new < 15:
        print(new-1)
    elif new == 15:
        print("15")
count = 0
for rn in newno:
    if rn >= 14 and rn <= 18:
        print(rn,end=" ")
        count += 1
print("\n",count)