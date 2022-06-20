results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]

#sort result based on win percentage
print(sorted(results,key=lambda x:x["win"],reverse=True))

#print district with minimum win %
print(min(results,key=lambda x:x["win"]))

#print district with maximum win %
print(max(results,key=lambda x:x["win"]))

#print district with A+
print(sorted(results,key=lambda x:x["A+"],reverse=True))

#print district with low count A+
print(min(results,key=lambda x:x["A+"]))

#print total number of student who got ful A+
aplus = [res ["A+"] for res in results] # return only values of A+
print(sum(aplus))



