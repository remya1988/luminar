lst = [10,11,14,7,8,9,21,55,22,34]
oddlst = []
evenlst = []
lst.insert(2,80)
lst.insert(3,45)

cnt = lst.count(22)
print(cnt)
for num in lst:
    if num % 2 == 0:
        evenlst.append(num)
    else:
        oddlst.append(num)
print("Even number list....")
evenlst.sort()
print(evenlst)
print("Odd number list.....")
oddlst.sort()
print(oddlst)