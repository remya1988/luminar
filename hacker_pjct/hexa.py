hex_dict={0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
oct_dict = { 0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',
             6:'6',7:'7',8:'10',9:'11',10:'12',11:'13',12:'14',13:'15',14:'16',15:'17',
             16:'20',17:'21'
}

def decToHexaDecimal(number):
    hex_dec = ''

    number_tmp = number
    while(number_tmp>0):
        remainder = number_tmp % 16
        hex_dec = hex_dict[remainder]+hex_dec
        number_tmp = number_tmp//16
    print("Hexa Dec : ",hex_dec)

    # Decimal to OCTAL
def decToOctal(number):
    oct_dec = ''
    number_tmp = number
    while(number_tmp > 0):
        remainder = number_tmp%8
        oct_dec = oct_dict[remainder]+oct_dec
        number_tmp = number_tmp//8
    print("Octal : ",oct_dec)

# Decimal to BINARY
def decToBinary(number):
    bin_no =[]
    num_tmp = number
    while(num_tmp > 0):
        remainder = num_tmp%2
        bin_no.append(remainder)
        num_tmp = num_tmp//2
    bin_no.reverse()
    #print(bin_no)
    for i in bin_no:
        print(i, end="")
if __name__== '__main__':
    n = int(input("Enter the decimal number : "))
    for i in range(1,n+1):
        decToHexaDecimal(i)
        decToOctal(i)
        decToBinary(i)
