import itertools
import functools
import operator
from itertools import combinations
master = 'abbcceddfafggtn'
ch_word = "cat"
mw={}
f = 1
for ch in master:
    if ch in mw:
        mw[ch]+=1
    else:
        mw[ch]=1
print(mw)
for ch in ch_word:


        if ch in mw:
            cur_ch_count = mw.get(ch)
            if cur_ch_count > 0:
                mw[ch]-=1
            elif cur_ch_count ==0:
                f=0
                break
        else:
             # print("Word cannot be formed")
            f =0
            break
if f==0:
    print("Word not formed")
else:
    print("word can form")
# lst = []
# f = 1
# ch =""
# list_combinations = list()
# nums = list(master)
# print(nums)
# for n in range(len(nums) + 1):
#     list_combinations += list(combinations(nums, n))
# for i in range(1,len(list_combinations)):
#
#     tup1 = list_combinations[i]
#     str = functools.reduce(operator.add, (tup1))
#     lst.append(str)
#
#
# for wrd in lst:
#      if ch_word == wrd:
#         f =0
#         break
# if f==0:
#     print("word exist")
# else:
#     print("word not exist")

# for num in ch_word:
#     if num in nums:
#         ch+=num
# print(ch)
#
# # for i in range(0,len(master)):
# #     for j in range(0,len(ch_word)):
# #         if master[i] in ch_word[j]:
# #             ch = ch+master[i]
# # print(ch)
# if ch == ch_word:
#     print("Th word is in master word")
# else:
#     print("The word is not in master word")
