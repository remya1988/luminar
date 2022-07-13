def getTotlX(arr,brr):
    print(arr," : b : ",brr)
    f =[]
    for i in range(len(arr)):
        for j in range(len(brr)):
            if brr[j]%arr[i]==0:
                f[j]=1
            else:
                f[j]=0
    print(f)


first_multiple_input = input("Enter limits of 2 array : ").rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input("Enter a array : ").rstrip().split()))

brr = list(map(int, input("Enter b array : ").rstrip().split()))


total = getTotlX(arr, brr)
