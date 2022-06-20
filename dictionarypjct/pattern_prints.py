pattern = "CADBDCBBCAC"

# print first recursive character
char_cout = {}
rec_char = []

# print second recursive character
for char in pattern:
    if char in char_cout:
        char_cout[char] += 1
        rec_char.append(char)
    else:
        char_cout[char] = 1
print(rec_char)

print("First : ", rec_char[0])
print("Second : ", rec_char[1])

print(char_cout)
max_no = []
for ch in char_cout:
    max_no.append(char_cout[ch])
print("Most recursive element is : ",max(max_no))

