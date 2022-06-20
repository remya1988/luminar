# Enter your code here. Read input from STDIN. Print output to STDOUT
# Eng_n =int(input("Enter total no of student subscribes ENGLISH :"))
# eng = input("Enter roll numbers : ")
# eng_s = set(eng.split(" "))
# Fre_n =int(input("Enter total no of student subscribes FRENCH :"))
# fre = input("Enter roll no : ")
# fre_s = set(fre.split(" "))
# print(len(eng_s.difference(fre_s)))
# Enter your code here. Read input from STDIN. Print output to STDOUT
nA = int(input(" "))
A = input(" ")
nN = int(input(" "))
As= set(A.split(" "))


for i in range(0,nN):
    op_Name_setno =input(" ")
    op_set = set(op_Name_setno.split(" "))

    op_numbers = input(" ")
    op_number_set = set(op_numbers.split(" "))
    if "intersection_update" in op_set:
        As.intersection_update(op_number_set)
       # print("Inter : ",As)
    elif "update" in op_set:
        As.update(op_number_set)
       # print("Update : ",As)
    elif "symmetric_difference_update" in op_set:
        As.symmetric_difference_update(op_number_set)
       # print("Symmetric : ",As)
    elif "difference_update" in op_set:
        As.difference_update(op_number_set)
        #print("Difference : ",As)

sum1 =0
for x in As:
    sum1 += int(x)
print(sum1)





