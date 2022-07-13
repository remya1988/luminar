
import json

# Print total number of countries
with open("country.json",encoding="utf-8")as f:
    data = json.load(f)
print( len(data))

# Print languages of Ukraine
uk_language = [ln["languages"] for ln in data if ln["name"]=="Ukraine"]
language_name = [ln["name"] for ln in uk_language[0]]
print(language_name)

# Print currency of China
currency_china =[cur["currencies"] for cur in data if cur["name"].startswith("Palestine")]
print(currency_china)
curr = [curr["name"] for curr in currency_china[0]]
print(curr)
# for curr in currency_china:
#     for i in range(len(curr)):
#         print(curr[i]["name"])


# Print population of India
pop_ind = [po["population"] for po in data if po["name"]=="India"]
print(pop_ind)

# Print neighbouring countries of Australia
neighbour = [ne.get("borders") for ne in data if ne["name"]=="India"]
print(neighbour)
# cod =[]
# ln = len(neighbour[0])
# for i in range(0,ln):
#     #print(neighbour[0][i])
#     #dat = [con for con in neighbour[i]]
#     # print(dat)
#     nam = [nam["name"] for nam in data if nam["alpha3Code"]==neighbour[0][i]]
#     cod.append(nam[0])
# print(cod)
sharing_borders =[country.get("name") for country in data if country["alpha3Code"] in neighbour[0]]
print(sharing_borders)

# Most populated country
# pop_all=[pop["population"] for pop in data]
# pop_name = [pop["name"] for pop in data if pop["population"]==max(pop_all)]
# print(max(pop_all)," - ",pop_name[0])


pop_country = max(data,key=lambda d:d.get("population"))
print(pop_country["name"]," - ",pop_country["population"])