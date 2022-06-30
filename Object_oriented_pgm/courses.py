# course details cname cid cfee
class Course:
    c_id:int
    c_name:str
    c_fee:int
    def __init__(self,**kwargs):
        self.c_id=kwargs.get("c_id")
        self.c_name=kwargs.get("c_name")
        self.c_fee=kwargs.get("c_fee")
        self.print_details()
    def print_details(self):
        print("Course name : ",self.c_name,"\n Course Id : ",self.c_id,"\n Course Fee : ",self.c_fee)

c = Course(c_name ="Bsc",c_id=1,c_fee=30000)