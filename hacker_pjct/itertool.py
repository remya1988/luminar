from itertools import product
#print(list(product([1,2,3],repeat = 2)))
A = input(" ").split(" ")
A = list(map(int,A))
B = input(" ").split(" ")
B = list(map(int,B))
print(A)
print(B)


print(list(product(A,B)))