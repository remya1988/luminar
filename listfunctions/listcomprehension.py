if __name__ == '__main__':
    x = int(input(" x "))
    y = int(input(" y "))
    z = int(input(" Z "))
    n = int(input(" N "))
    lst1 = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if (i+j+k) != n:
                     colist = [i,j,k]
                     lst1.append(colist)
    print(lst1)