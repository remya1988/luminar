lst1 = [1,2,3,2,4,5,6]
lst2 = [3,4,3,3,4,2,3,4,1,7]
lst3 = []
# first recursive no.... 1
for n1 in lst1:
    if n1 in lst2:
        print("The first recursive number is......",n1)
        break

#Most frequent no in list 2 ....>4
cnt = 0
for n1 in lst2:
    if lst2.count(n1) > cnt:
        cnt = lst2.count(n1)
        num = n1
    else:
         continue
print("\nMost frequent number is........",num)

dup = []
for i in range(0,len(lst2)):
    for j in range(i+1,len(lst2)):
        if lst2[i] == lst2[j]:
            dup.append(lst2[i])
print(dup)