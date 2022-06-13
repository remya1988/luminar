mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 80],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]

# uSing loops iin one line without using multiple line is called list comprehension

# No of mobiles
print("Total no of Mobiles : ", len(mobiles))

# Total No of out of stock Mobiles
out_of_stck = [item for item in mobiles if item[-1] == 0]
print("\nTotal no of items out of stock : ", len(out_of_stck))
print(out_of_stck)

# Total stock
total_stock = [item[-1] for item in mobiles]
print("\nTotal stock is : ", sum(total_stock))

# Mobiles in range of 20k to 30k
rage_2030 = [item for item in mobiles if item[4] in range(20000, 30000)]
print("\nItem with in the range of 20k to 30k : ", rage_2030)

# Print all 5g Mobiles
fiveG = [item[1] for item in mobiles if item[2] == "5g"]
print("\n5G mobiles are : ", fiveG)

# Print samsung mobiles
samsung_mob = [item[1] for item in mobiles if item[5] == "samsung"]
print("\nSamsung mobiles are : ", samsung_mob)

# Print costly Mobiles
costly_price = max([item[4] for item in mobiles])
costly_mob = [item for item in mobiles if item[4] == costly_price]
print("\nCostly mobile is : ", costly_mob)

# pRint mobile having maximum stock
avl_max_pro = max(mobiles, key=lambda m: m[-1])
print("\nmobile having maximum stock :", avl_max_pro)

# Print low cost mobiles
low_cost_mob = min(mobiles, key=lambda m: m[4])
print("\nLow Cost mobiles are : ", low_cost_mob)
# low_mob = [item[1] for item in mobiles if item[4] <= 25000]
# print("\nLow Cost mobiles are : ",low_mob)

# Print mobiles having stock>10
stock_gt_10 = [item[1] for item in mobiles if item[-1] > 10]
print("\nMobiles having stock greTer than 10 : ", stock_gt_10)

# Count of mobiles having display Amoled
display_amld = [item[1] for item in mobiles if item[3] == "AMOLED"]
print("\nMobiles having display amoled : ", display_amld)

# Sort mobiles based on price
price = [item[4] for item in mobiles]
price.sort()
print("\nItems sorted : ", price)

# Sort mobiles based on available stock order by desc
stock_sort = [item[6] for item in mobiles]
stock_sort.sort(reverse=True)
print("\nItems order by stock : ", stock_sort)

# Is there any mobile available at Rs 10000 ?

f = [True if item[4] == 10000 else False for item in mobiles]
print(f)
if True in f:
    print("\nThere is one item having price 10000")
else:
    print("\nNo item having price 10000")
# for item in mobiles:
#     if item[4] == 10000:
#         print("\nThere is one item ", item[1], " having price 10000")
#         f = 1
#         break
# if f == 0:
#     print("\nNo mobiles having rate 10000")

# List all mobiles having same price
mob_same_price = [item for item in mobiles]
