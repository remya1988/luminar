account ={
        "acno":10000,
        "pname":"Rem",
        "type":"Savings",
        "date":"10-5.2020"
}
#print(account)
print("balance" in account)
account["balance"] = 40000
print(account)
account["balance"] += 10000
print(account)