import functools
import json
import random

with open("songs.json", encoding='utf-8') as f:
    data = json.load(f)
    # print(data)
# high_rate_song = [song for song in data if song["album"]=="album1"]
album1 = list(filter(lambda song: song["album"] == "album1", data))
print(len(album1))

# hihest rating song
# hig_rate = list(map(lambda song:song["rating"],data))
# hig = max(hig_rate)
# high_rate_song = [s["name"] for s in data if s["rating"]==hig]

high_rate_song = functools.reduce(lambda s1, s2: s1 if s1["rating"] > s2["rating"] else s2, data)
print(high_rate_song)

# total number of albums
tot_albums = set([song["album"] for song in data])
print(len(tot_albums))

# which album contain most songs
most_songs = {}
for msong in data:
    x = msong["album"]
    if x in most_songs:
        most_songs[x] += 1
    else:
        most_songs[x] = 1
print(most_songs)
print("*******")
print(max(most_songs.items(),key=lambda x:x[1]))
print("*******")
#sad song
sad_song=[s for s in data if s["mode"]=="sad"]
print(random.sample(sad_song,2))