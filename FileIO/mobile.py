mobs = open("mobiles.txt")
mob =[]
for mo in mobs:
    mobiles=mo.rstrip("\n").split(",")
    mob.append(mobiles)
costly_mob = max(mob,key = lambda mob:mob[2])
print(costly_mob)
for item in mob:
    if item[1] =="samsung":
        print(item)
