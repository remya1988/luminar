lst1 = [10,20,30,40,15,90,22]
lst2 = [11,10,21,30,41,15,19]
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
print(sorted(lst1))

p1 = 0
p2 = 0
while (p1 < len(lst1) and p2 < len(lst2)):
    if lst1[p1] == lst2[p2]:
        print("The common elemnt is",lst1[p1])
        p1 += 1
        p2 += 1
    elif lst1[p1] > lst2[p2]:
        p2 += 1
    elif lst1[p1] < lst2[p2]:
        p1 += 1
