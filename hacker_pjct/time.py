def timeConversion(s):
    # Write your code here
    h,m,se=map(str,s.split(":"))
    h1=int(h)
    tfour=h
    if s[-2:] == "PM":
        if h1<12:
            tfour = str(h1+12)
    else:
        if h1==12:
            tfour = "00"
    res = tfour+":"+m+":"+se
    print(res[:-2])

if __name__ == '__main__':


    s = input()

    result = timeConversion(s)

