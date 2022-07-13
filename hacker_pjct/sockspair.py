#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ars):

    lst = {}
    for i in range(0,n):
        if ars[i] in lst:
            lst[ars[i]]+=1
        else:
            lst[ars[i]]=1
    #print(lst)
    it = [it for it in lst.values()]
    #print(it)
    cnt = 0
    for i in range(0,len(it)):
        #print(it[i])
        if it[i]>=2:

            #print(it[i],end = " ")
            res = it[i]//2
            cnt+=res
            # else:
            #     res1 = it[i]/2
            #     cnt+=res1
    print(cnt)




if __name__ == '__main__':


    n = int(input(" ").strip())

    ar = list(map(int, input(" ").rstrip().split()))

    sockMerchant(n, ar)


