numbers = [-1,0,2,3,-1,20,9,-9,-8,0,7,-7,5,-5,-4,-2,-6]
countp = 0
countn = 0
zer = 0

for num in numbers:
    if num > 0:
        countp += 1
    elif num < 0:
        countn += 1
    else:
        zer += 1
print("positive numbers are ",countp)
print("Negative numbers are ",countn)
print("Zero numbers are ",zer)

