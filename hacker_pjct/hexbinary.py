# conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
#                     5: '5', 6: '6', 7: '7',
#                     8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
#                     13: 'D', 14: 'E', 15: 'F'}


# def decimalToHexadecimal(decimal):
#     hexadecimal = ''
#     while (decimal > 0):
#         remainder = decimal % 16
#         hexadecimal = conversion_table[remainder] + hexadecimal
#         decimal = decimal // 16
#     print(hexadecimal)
def decimalToHexadecimal(number):
    for num in range(1,n+1):
        dec_no= int(num)
        octal = oct(num)
        hexal = hex(num)
        bin_no = bin(num)
        print(str(dec_no).rjust(5,' '),octal[2:].rjust(5),hexal[2:].rjust(5),bin_no[2:].rjust(5))

if __name__ == '__main__':
    n = int(input())
    decimalToHexadecimal(n)