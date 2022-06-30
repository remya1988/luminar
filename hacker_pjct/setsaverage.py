def average(array):
    # your code goes here
    arr = set(array)

    avg = sum(arr)/len(arr)
    return float(avg)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input(" ").split()))
    # result = average(arr)
    # print(result)
    print(average(arr))