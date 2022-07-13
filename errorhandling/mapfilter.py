lst = [2,4,6,8]
sq = list(map(lambda n:n**2,lst))
print(sq)

num_out = list(map(lambda n:n-1 if n>5 else n+1,lst))
print(num_out)