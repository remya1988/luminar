import math
import os
import random
import re
import sys

def solve(s):
    t = s.split(" ")
    for x in t:
        s = s.replace(x,x.capitalize())
    print(s)

if __name__ == '__main__':


    s = input()

    result = solve(s)

