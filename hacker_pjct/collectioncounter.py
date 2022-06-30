import collections
No_shoe = int(input())
shoe = collections.Counter(map(int, input().split()))
print(shoe)
No_cust =int(input())
total_price = 0
for i in range(0,No_cust):
   size,price=map(int,input().split(" "))
   if shoe[size]:
       total_price+=price
       shoe[size]-=1
print(total_price)