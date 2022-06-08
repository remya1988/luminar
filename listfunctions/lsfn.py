lst = [1, 2, 3, 4, 5, 6, 7, 8, 2, 9, 3, 4, 0]

# To reverse a specefic list
lst.sort(reverse=True)
print(lst)

# to remove a specefic element from first position
lst.remove(2)
print(lst)

# To insert an item in an index position
lst.insert(4,100)
print(lst)

# To count the number of times a no occur in the list
print(lst.count(3))