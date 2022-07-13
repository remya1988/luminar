import json
import random
try:
    with open("users.json",encoding="utf-8") as f:
        data = json.load(f)
        all_users = list(map(lambda user:user["id"],data))
        print(all_users)
        cur_following = [user["followers"]for user in data if user["username"]=="akhil"][0]
        print(cur_following)
        to_follow_users = set(all_users)-set(cur_following)
        print(to_follow_users)
        to_follow_users.remove(1)
        print(to_follow_users)
        x = random.choice(list(to_follow_users))
        cur_following.append(x)
        print(cur_following)
except Exception as e:
    print(e)