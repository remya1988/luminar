lst1 = [10, 11, 12, 13, 14, 11]
lst2 = [11, 12, 16, 177, 11]
lst3 = []

for n1 in lst1:
    if n1 in lst2:# or we cn use
        lst3.append(n1)

print("The common numbers in 2 list are....",set(lst3))


#print most frequent element and first recursive element
