from math import *
n = int(input())

max_length = len(str(bin(n)))-2

for i in range(1, n+1):
    d = str(i).rjust(max_length)
    o = str(oct(i))[2:].rjust(max_length)
    h = str(hex(i))[2:].upper().rjust(max_length)
    b = bin(i)[2:].lstrip('0').rjust(max_length)
    print('{} {} {} {}'.format(d,o,h,b))