class Person:
    name: str
    age: int
    gender: str

    def person_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.print_details()

    def print_details(self):
        print(self.name, self.age, self.gender)

class Bottle:
    materieal :str
    price:int
    color:str
    capacity:int
    def __init__(self,**kwargs):
        self.materieal=kwargs.get("material")
        self.price=kwargs.get("price")
        self.color=kwargs.get("color")
        self.capacity=kwargs.get("capacity")
    def print_details(self):
        print(self.materieal,self.price)

b = Bottle(material="plastic",price=200,capacity=100,color="red") # calling constructor

b.print_details()
p = Person()
p.person_details("rem", 15, "Female")
