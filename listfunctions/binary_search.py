lst1 = [12,3,1,44,11,9,17,9,22]
n = 44
lst1.sort()
print(lst1)
end = len(lst1)
start = 0
while start <= end:
    mid = (start + end)//2
    if lst1[mid] == n:
        print("Number is in ",mid,"position")
        start = mid + 1

    elif lst1[mid] > n:
        end = mid - 1
    else:
        start = mid + 1
