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
print("*"*100)
saving_acno = [ac["acno"] for ac in accounts if ac["ac_type"] == "savings"]
print(saving_acno)

#sort accounts based on balance desc
print("*"*100)
accounts.sort(reverse=True,key=lambda x:x["balance"])
print(accounts)

#print all phone pay transactions
print("*"*100)
all_trans = [ac["transactions"] for ac in accounts ]
ph_pay_trans = [trans for flists  in all_trans for trans in flists if trans["method"] == "phone-pay"]
print(ph_pay_trans)

# for ac in accounts:
#     for i in range(0,len(ac)-1):
#
#         if ac["transactions"][i]["method"]=="phone-pay":
#             print(ac["transactions"][i])

#print all transactions where transaction amount>500
print("*"*100)
amnt_gt_500 =[trans for flists in all_trans for trans in flists if trans["amount"]>500 ]
print(amnt_gt_500)
# for ac in accounts:
#     for i in range(0,len(ac)-1):
#         if ac["transactions"][i]["amount"]>500:
#             print(ac["transactions"][i])

#print credit gransactions of 1002
print("*"*100)
s = 0
trans_of_1002 = [trans for flists in all_trans for trans in flists if trans["to"] == 1002 ]
print(trans_of_1002)
for i in range(0,len(trans_of_1002)):
    s = s+trans_of_1002[i]["amount"]
# for ac in accounts:
    # for i in range(0,len(ac)-1):
    #     if ac["transactions"][i]["to"] ==1002:
    #         print(ac["transactions"][i])
    #         s = s+ac["transactions"][i]["amount"]
print("Total amount transacted to accoynt 1002 : ",s)

#aggregate methods
flist = [flist for flist in all_trans]
print(flist)
flist = [trans for flist in all_trans for trans in flist]
agg = {}

for t in flist:
    pay_method = t["method"]
    pay_amount = t["amount"]
    if pay_method in agg:
        agg[pay_method] += pay_amount
    else:
        agg[pay_method] = pay_amount
print(agg)
print(max(agg.items(),key = lambda x:x[1]))