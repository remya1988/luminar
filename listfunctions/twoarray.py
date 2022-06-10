lst1 = [
    [10,21],
    [30,40],
    [50,60],
    [55,12],
    [13,11]
]

# for num in lst1:
#     for i in num:
#         if i > 20:
#             print(i,end=" ")

print("\n",max(lst1))
print("The nested list is.........",lst1)
f_list = []
for num in lst1:
    for i in num:
        f_list.append(i)
print("Appended list is...........",f_list)

# or also use instaed of append in one [] bracket
fl_list = [num for s_list in lst1 for num in s_list]
print("\nNew list using sinle [] ",fl_list)

# Number greater than 20
num_gt = [num for num in fl_list if num>20]
print("No > 16 : ",num_gt)

# Print Odd nos
odd_no = [num for num in fl_list if num%2 != 0]
print("Odd no list : ",odd_no)

#Print even nos sum
sum1 = [num for num in fl_list if num%2 == 0]
print("Even No sum : ",sum(sum1))

# Print num+1 if num>25 else num-1
mno = [num+1 if num>25 else num-1 for num in fl_list]
print(mno)


