if __name__ == '__main__':
    n = int(input(" "))
    integer_list =  input(" ")
    tup = tuple(map(int, integer_list.split(' ')))
    print(tup)
    print(hash(tup))