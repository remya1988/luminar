def solve(s):
    print(s)
    # for x in t:
    #     x.capitalize()
    #     print(x)
    s.title()
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()