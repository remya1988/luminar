from collections import OrderedDict
def merge_the_tools(string, k):
    l = len(string)
    for i in range(0,l,k):
        sub = "".join(OrderedDict.fromkeys(string[i:i+k]))
        print(sub)



if __name__ == '__main__':
    string= input("String ")
    k = int(input("Enter l "))
    merge_the_tools(string, k)