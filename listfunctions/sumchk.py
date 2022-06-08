lst = [2,3,4,5,6,77]
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i] + lst[j] ==8:
#             print(lst[i],lst[j])
lst.sort()
elm = 8
low = 0
upp = len(lst)-1
while(low < upp):
    cur_sum = lst[low]+lst[upp]
    if cur_sum == elm:
        print(lst[low],lst[upp])
        low += 1
        # upp -= 1
    elif cur_sum > elm:
        upp -= 1
    elif cur_sum < elm:
        low += 1

