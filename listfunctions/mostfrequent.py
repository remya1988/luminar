lst1 = [1,2,3,2,4,5,6]
lst2 = [3,4,4,2,4,1,7]
lst3 = []
for n1 in lst1:
    if n1 in lst2:
        print("The first recursive number is ",n1)
        break
for n1 in lst1:
    if n1 in lst2:
        lst3.append(n1)
