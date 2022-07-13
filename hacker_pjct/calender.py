from collections import namedtuple
n = int(input("Enter total stud : "))
class_col = namedtuple('class_col',['ID',"MARKS","NAME","CLASS"])
for i in range(0,n):
    xy[i] = class_col()