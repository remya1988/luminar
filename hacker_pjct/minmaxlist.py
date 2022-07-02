import math
import os
import random
import re
import sys



def miniMaxSum(arr):
    lst = []

    for i in range(0,len(arr)-3):
        sum_no = 0
        for j in range(i,i+4):
            sum_no = sum_no+arr[j]
        lst.append(sum_no)
    print(lst)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)