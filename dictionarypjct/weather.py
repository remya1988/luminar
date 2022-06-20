weather=[
    {"district": "tvm", "temp":30},
    {"district": "ktm","temp":28 },
    {"district": "apy","temp":27},
    {"district": "idk","temp":18 },
    {"district": "ekm","temp":34 },
    {"district": "pta","temp":21},
    {"district": "tsr","temp":24},
    {"district": "kzd","temp":29},
    {"district": "pkd","temp":34},
    {"district": "mpm","temp":31},
    {"district": "tvm", "temp": 31},
    {"district": "ktm", "temp": 29},
    {"district": "apy", "temp": 26},
    {"district": "idk", "temp": 20},
    {"district": "ekm", "temp": 30},
    {"district": "pta", "temp": 22},
    {"district": "tsr", "temp": 27},
    {"district": "kzd", "temp": 28},
    {"district": "pkd", "temp": 30},
    {"district": "mpm", "temp": 29},

]

out = {}
for data in weather:
    dist_name= data["district"]
    cur_temp = data["temp"]
    if dist_name in out:
        old_temp = out[dist_name]
        if cur_temp > old_temp:
            out[dist_name] = cur_temp
    else:
        out[dist_name]=cur_temp
print(out)



# lst = sorted(weather,key = lambda x:(x["district"]),reverse=True)
# new_dict = dict()
# #temp = dict()
# for i in range(0,len(weather)-1):
#
#     if i<= len(weather)-1:
#         #print(lst[i])
#         if (lst[i]["district"] == lst[i+1]["district"]):
#             dist = lst[i]["district"]
#             if lst[i]["temp"] > lst[i+1]["temp"]:
#                 temp = lst[i]["temp"]
#             else:
#                 temp = lst[i+1]["temp"]
#             new_dict[dist] = temp
# print(new_dict)
# print(sorted(new_dict.items(),key = lambda item:item[1],reverse=True))
print(sorted(out.items(),key = lambda item:item[1],reverse= True))
max1 = max(out.values())
min1 = min(out.values())
max_temp =[]
min_temp =[]
for x in out:
    if out[x] == max1:
        max_temp.append(x)
        continue
    elif out[x] == min1:
        min_temp.append(x)
        continue
print("Maximum temperature districts are : ",max_temp," : ",max1)
print("Minimum temperature districts are : ", min_temp," : ",min1)

#copy function
# dic1 = new_dict.copy()
# print(dic1)
# print(dict.fromkeys(new_dict))
# print(new_dict.get("mpm"))
# print(new_dict.items())
# print(new_dict.keys())
# print(new_dict.pop("tvm"))
# print(new_dict.update({"district":"tvm","temp": 46000}))
