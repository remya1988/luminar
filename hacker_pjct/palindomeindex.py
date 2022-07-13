def is_palin(s):


    lst_rev=''.join(reversed(s))
    # lst=list(s)
    # print(lst)
    lst =[]
    if s==lst_rev :
        return -1
    f =0
    for i in range(len(s)):
        s1=s.replace(s[i],"",1)
        s1_rev=''.join(reversed(s1))
        if s1==s1_rev:
            return i
        else:
            f =1
    if f==1:
        return 0

n = int(input("Enter no "))

for i in range(n):
    s = input("Enter string")
    res = is_palin(s)
    print(res)


