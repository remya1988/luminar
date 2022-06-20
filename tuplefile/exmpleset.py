lst = [10,11,12,13,14,15,16]
st = set(lst)
print(lst)
print(st)
print(dir(set))
st1 = {10,11,13,14}
# st1 = {33}
st2 = {1,2,13,4,5}
st1.add(90)
print(st1)
union_set = st1.union(st2)
print("Combines set : ",union_set)
inter_set = st1.intersection(st2)
print("Common elemnet : ",inter_set)
diff = st1.difference(st2) # remove elements in set1 that also in set2.. in this 13 in set 2 is deleted and print remaining in set1
print(diff)
st3 = {300,200,100}
st1.update(st3)

print("Updated set1 : ",st3)

students = ["ram","raj","ravi","agn","jyo","tanvi"]
passed_stdnt = ["tanvi","raj","agn"]
std_all = set(students)
pass_std = set(passed_stdnt)
failed_std= std_all.difference(pass_std)
f = std_all - pass_std
print("Failed : ",f)
print("Failed students are : ",failed_std)
print(len(failed_std))