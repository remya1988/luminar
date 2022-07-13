import json
with open("blogs.json",encoding="utf-8")as f:
    data = json.load(f)
print( data)

#number of post by user id=1
po=[post for post in data if post["userId"]==1]
print(len(po))

# total number of likes for post id 6
po =[len(post["liked_by"]) for post in data if post["postId"]==6]
print(po)

#number of post liked by user 2
po = len([post for post in data if 2 in post["liked_by"]])
print(po)
