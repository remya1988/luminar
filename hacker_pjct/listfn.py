if __name__ == '__main__':
    N = int(input(" "))
    # Lists in Python - Hacker Rank Solution START
    Output = []
    for i in range(0,N):
        ip1 = input(" ").split(" ");
        ip = list(ip1)
        if ip[0] == "print":
            print(Output)
        elif ip[0] == "insert":
            Output.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            Output.remove(int(ip[1]))
        elif ip[0] == "pop":
            Output.pop()
        elif ip[0] == "append":
            Output.append(int(ip[1]))
        elif ip[0] == "sort":
            Output.sort()
        else:
            Output.reverse()