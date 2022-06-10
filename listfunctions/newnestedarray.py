frameworks = [
    ["django","Python",4],
    ["flask","Python",3.5],
    ["angular","Javascript",4.5],
    ["express","Javascript",4]
]

fw_lst = [fw for fw in frameworks if fw[1]=="Python"]
print(fw_lst)

fw_lst1 = [fw for fw in frameworks if fw[2]>4]
print(fw_lst1)