#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    print(a)
    cnt = 0
    un = []
    for i in range(len(a)):
        for j in range(0, len(a)):
            if a[i] == a[j]:
                cnt += 1
        if cnt == 1:
            un.append(a[i])
        cnt =0
    print(un)


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input(" ").split(" ")))

    lonelyinteger(a)

