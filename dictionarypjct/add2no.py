#
def add(*num):
     return sum(num)
# def max_num(*args):
#     return max(args)
#
#
# print(add(10,2))
# print(add(10,11,12,14))
# print(max_num(10,80,90,88))
def print_no(*args):
    print(args)

def print_details(**kwargs):
    print(kwargs)

def print_sum(**kwarg):
    print("Sum of nos ",kwarg,"is :",sum([v for k,v in kwarg.items()]))

print_details(name="Remya",place ="Kollam",age=25)
print_no(10,20,30,40,50,60,70,80,90)
print_sum(n1=10,n2=20,n3=30)
