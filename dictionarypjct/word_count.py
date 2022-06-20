# Word count
text = "hai hello hai hello i am remya and and i am i i 33 33 33"
words = text.split(" ")
print(words)
word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1
print(word_count)
#w_count = word_count.items() -> to convert dictionary into a set of tuple values
print(sorted(word_count.items(),key=lambda x:x[1],reverse=True))
print(max(word_count.items(),key=lambda item:item[1]))
print(min(word_count.items(),key=lambda item:item[1]))

