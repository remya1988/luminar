from functools import reduce
import itertools
numbers=[3,30,34,5,9,8,7]

# str_num = [str(n) for n in numbers]
# max_no = reduce(lambda n1,n2: (n1+n2) if (n1+n2)>(n2+n1) else (n2+n1),str_num)
# print(max_no)
res = []
# for per in itertools.permutations(str(num) for num in numbers):
#     res.append(''.join(per))
# print(max(res))
ch =''
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        # print(str(numbers[i]))
        if str(numbers[i])> str(numbers[j]):
            ch =str(numbers[i])+str(numbers[j])
        else:
            ch = str(numbers[j])+str(numbers[i])
print(ch)
