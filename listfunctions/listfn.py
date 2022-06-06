exp = [1000, 2000, 3000, 4000, "rem", "agn"]

for i in exp:
    print(i)
print("*"*30)
for i in range(0, len(exp)):
    print(exp[i])

exp.append("tan")
print(exp)