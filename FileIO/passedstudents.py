total = open("students.txt",'r')
fail = open("failed.txt",'r')
passed = open("passed.txt",'w')

tot= set(st.rstrip("\n") for st in total)
fal =set(st.rstrip("\n") for st in fail)
pas = tot.difference(fal)
for ps in pas:
    ps +="\n"
    passed.write(ps)
name= "ani"
passed=open("passed.txt","a")
passed.write(name)