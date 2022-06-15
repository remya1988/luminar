mobile = {
    "name" : "samsung",
    "display":"Amoled",
    "price": 45000,
    "type": "4G",
    "ram":"6GB",
    "memory":"128GB"
}
#mobile price update  price-1000 if price>45000 else price-500

mobile["price"] = mobile["price"]-1000 if mobile["price"]>45000 else mobile["price"]- 500
print("Price of mobile is ",mobile.get("price"))

