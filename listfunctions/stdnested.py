if __name__ == '__main__':
    std = []
    std_sub =[]
    for _ in range(int(input(" "))):
        name = input(" ")
        score = float(input(" "))
        std_sub = [name,score]
        std.append(std_sub)
    x = 99999
    for i in range(len(std)):
        if x > float(std[i][1]):
            x = float(std[i][1]) # 37.2
    y = 999999
    for i in range(len(std)):
        if float(std[i][1]) > float(x) and y > float(std[i][1]):
            y = float(std[i][1]) # 37.21
    runner = []
    for i in range(len(std)):
        if float(std[i][1]) == float(y):
            runner.append(std[i][0])
    runner = sorted(runner)

    for i in range(len(runner)):
        print(runner[i])
# sorting based on age
