from mathsoperations.add import *
n = int(input("Enter a number : "))
s = 0
while(n>0):
    n1 = n%10
    s = s + cub(n1)
    n = n//10

print("sum is ",s)