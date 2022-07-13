#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    cnt1 =[]
    cnt =0
    for i in range(len(queries)):
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                cnt+=1
        cnt1.append(cnt)
        cnt =0
    print(cnt1)
    return cnt1


if __name__ == '__main__':


    strings_count = int(input(" "))

    strings = []

    for _ in range(strings_count):
        strings_item = input(" ")
        strings.append(strings_item)

    queries_count = int(input("Ener "))

    queries = []

    for _ in range(queries_count):
        queries_item = input(" ")
        queries.append(queries_item)

    res=matchingStrings(strings, queries)
    print(res)




