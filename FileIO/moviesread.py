movopen = open("movies.txt")

movlst = []
mov_2022 = []
mov_dict = {}
movdict=''
for mo in movopen:
    mov = mo.rstrip("\n").split(",")
    movlst.append(mov)

# Print movies released in 2022
mov_2022 = [mo for mo in movlst if mo[1] == '2022']
print(len(mov_2022), mov_2022)

# Number malayalam movies
mov_mal = [mo for mo in movlst if mo[3] == 'malayalam']
print(len(mov_mal), mov_mal)

# Theater released movies
mov_theatre = [mo for mo in movlst if mo[4] == 'theater']
print(len(mov_theatre), mov_theatre)

# List of movies whose rating > 5
mov_rating = [mo for mo in movlst if mo[2] == '5']
print(len(mov_rating), mov_rating)

# {2022:,4,2021:6,2020:2}
mod = [mo for mo in movlst]
for mo in mod:
    year = mo[1]
    if year in mov_dict:
        mov_dict[year]+=1
    else:
        mov_dict[year] =1
print(mov_dict)
out = max(mov_dict.items(),key=lambda item:item[1])
print(out)