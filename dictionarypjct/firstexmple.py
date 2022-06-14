car = {"brand":"swift","fuel":{"dsl","petrol","electric"},"mk_year":2020,"price":"9L"}
print(car["brand"])
print(car["fuel"])
print(car["mk_year"])
print(car["price"])

car["transmission_type"] = "manual"
print("transmission_type" in car)
print(car)
