class Staff(object):
    id : int
    name : str
    role : str
    def __init__(self,*arg,**kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.role = kwargs.get("role")
    def __str__(self):
        return self.name

class AddCourse():
    cname : str
    def addcourse(self,**kwarg):
        self.cname=kwarg.get("cname")
        self.user =kwarg.get("user")
        return self.cname
    # def __str__(self):
    #     return self.cname
user = Staff(id = 100,name = "remya",role="admin")
crs = AddCourse()
crses = crs.addcourse(cname="bca",user=user)
print("course : ",crses)