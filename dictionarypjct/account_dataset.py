accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]
# print details of account no 1002
ac_dtls = [ac for ac in accounts if ac["acno"] == 1002]
print(ac_dtls)

#print savings type account details
saving_acno = [ac["acno"] for ac in accounts if ac["ac_type"] == "savings"]
print(saving_acno)

#sort accounts based on balance desc
accounts.sort(reverse=True,key=lambda x:x["balance"])
print(accounts)

#print all phone pay transactions
for ac in accounts:
    # if ac["transactions"][2] =="phone-pay":
    #     print(ac,end="\n")
    #print(end="\n")
    for i in range(0,len(ac)-1):
        if ac["transactions"][i]["method"]=="phone-pay":
            print(ac["transactions"][i])

#print all transactions where transaction amount>500
print("*"*100)
for ac in accounts:
    for i in range(0,len(ac)-1):
        if ac["transactions"][i]["amount"]>500:
            print(ac["transactions"][i])

#print credit gransactions of 1002
print("*"*100)
s = 0
for ac in accounts:
    for i in range(0,len(ac)-1):
        if ac["transactions"][i]["to"] ==1002:
            print(ac["transactions"][i])
            s = s+ac["transactions"][i]["amount"]
print("Total amount transacted to accoynt 1002 : ",s)

