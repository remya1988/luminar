age = int(input("Enter age : "))
if(age<18):
    raise Exception ("not eligible ")
else:print("Eligible")