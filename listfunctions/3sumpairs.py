# Home work 3 sum pairs

lst_no = [4, 3, 5, 6, 2, 1, 8]
lst_no.sort()
sum_to_find = int(input("Enter the sum to find pais : "))
for i in range(len(lst_no)):
    n1 = lst_no[i]
    rem = sum_to_find - n1
    for j in range(i+1,len(lst_no)):
            for k in range(j+1,len(lst_no)):
                    if lst_no[j] + lst_no[k] == rem:
                        print("(",lst_no[i],",", lst_no[j],",", lst_no[k],")")



