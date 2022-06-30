class Course:
    c_id: int
    c_name: str
    status: bool

    def post(self, **kwargs):
        self.c_id = kwargs.get("id")
        self.c_name = kwargs.get("cname")
        self.status = kwargs.get("status")

    def __str__(self):
        return self.c_name


class Batch:
    c_name: Course
    b_code: str
    b_name: str

    def post(self, **kwargs):
        self.b_code = kwargs.get("bcode")
        self.b_name = kwargs.get("bname")
        self.c_name = kwargs.get("cname")


    def __str__(self):
        return self.b_code


class Student:
    stud_batch : Batch
    stud_name:str
    stud_phone:str
    stud_gender:str
    def post(self, **kwargs):
        self.stud_name = kwargs.get("sname")
        self.stud_phone = kwargs.get("phone")
        self.stud_gender = kwargs.get("gender")
        self.stud_batch = kwargs.get("bname")

    def __str__(self):
        return self.stud_name


# def print_stud(**kwargs):
#     us1 = kwargs.get("user")
#     print(us1.c_name)
course1 = Course()
course2 = Course()
course3 = Course()
course1.post(id=1, cname="MEARN", status=True)
course2.post(id=2, cname="Django", status=True)
course3.post(id=3, cname="BigData", status=True)
print("Courses : ",course1, course2, course3)

djb1 = Batch()
djb2 = Batch()
djb1.post(bcode="djmay2022", bname="May First", cname=course1)
djb2.post(bcode="BDmay2_k22", bname="Jun First", cname=course3)
print("Batches : ",djb1, djb2)

stud1 = Student()
stud2 = Student()
stud3 = Student()
stud1.post(sname="Remya", phone="980947668", gender="Female", bname=djb1)
stud2.post(sname="Rahul", phone="980947668", gender="Male", bname=djb1)
stud3.post(sname="Jyothis", phone="980947668", gender="Male", bname=djb2)
print("Students : ",stud1,stud2,stud3)
print("Course of ", stud1,"is : ",stud1.stud_batch.c_name)
print("Course of ", stud2,"is : ",stud2.stud_batch.c_name)
print("Course of ", stud3,"is : ",stud3.stud_batch.c_name)
