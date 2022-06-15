# Word count
text = "hai hello hai i am remya and i am 33"
words = text.split(" ")
print(words)
word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1
print(word_count)