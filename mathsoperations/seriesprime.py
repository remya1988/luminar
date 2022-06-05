def prime_no(num):
    flag = 0
    for i in range(2,num):
        if (num % i == 0):
            flag = 1
            break
    return flag

def find_prime(low,high):
    for i in range(low,high):
        bol = prime_no(i)
        if bol == 0:
            print(i,end = " ")
        else :
            continue

low = int(input("Enter the low range : "))
high = int(input("Enter the high range : "))
find_prime(low,high)


