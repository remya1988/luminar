from itertools import permutations
s,n = input().split()
k = int(n)
prod = list(permutations(s,k))
prod = sorted(prod,reverse=False)
for i in prod:
    print(*i,sep='')

