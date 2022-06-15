pattern ="CADBCDBBCDCD"

#print first recursive character
char_cout ={}
rec_char =[]


#print second recursive character
for char in pattern:
    if char in char_cout:
        rec_char.append(char)
    else:
        char_cout[char] = 1
print(rec_char)

print("First : ",rec_char[0])
print("Second : ",rec_char[1])
ch_cnt = {}
for ch in rec_char:
    if ch in ch_cnt:
        ch_cnt[ch] += 1
    else:
        ch_cnt[ch] =1
print(ch_cnt)
print("Most recursive character is : ",max(ch_cnt))


