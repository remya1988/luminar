f = open("abc.txt", 'w')
#lstfile=[line.rstrip("\n") for line in f]
# for line in f:
#     lstfile.append(line)
#     print(line)
company = "luminar"
lst =["rem","raj","dev","jyo","agn","tanv"]
for name in lst:
    name+="\n"
    f.write(name)
    # f.write("\n")