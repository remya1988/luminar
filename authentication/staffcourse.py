def admin_only(fn):
    def post(**kwargs):

        user = kwargs.get("user")
        if user.role=="admin":
            return fn(**kwargs)
        else:
            print("no access")
    return post

#@admin_only
class Employee(object):
    id : int
    name : str
    role : str
    def __init__(self,**kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.role = kwargs.get("role")
    def __str__(self):
        return self.name

@admin_only
class AddDepartment(object):
    dname : str
    def __init__(self,**kwargs):
        self.dname=kwargs.get("dname")
        self.user =kwargs.get("user")

    def __str__(self):
        return self.dname




user = Employee(id = 100,name = "remya",role="admin")
print(user)
crs = AddDepartment(dname="bca",user=user)
print("course : ",crs)