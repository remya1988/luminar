from Blog.models import users,posts
#print(users)

def authenticate(**kwargs):
    username =kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"]==username and user["password"]==password]
    return user
#print(authenticate(username="akhil",password= "Password@123"))
session ={}
def sigin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("Invalid user")
    return wrapper

class LoginView:
  def login(self,**kwargs):
      username =kwargs.get("username")
      password = kwargs.get("password")
      user = authenticate(username=username,password=password)
      if user:
          session["user"] = user[0] #to avoid storing as list of dictionary... only store dictionary
      #print(session)
class PostListView:

    @sigin_required
    def get(self,**kwargs):
        return posts

    @sigin_required
    def post(self,**kwargs):
        post = kwargs.get("data")
        id=session["user"]["id"]
        # id = session["id"]
        post["userId"]=id
        posts.append(post)

class MyPostView:
    @sigin_required
    def get(self,**kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = authenticate(username=username, password=password)
        if user:
            #session["user"] = user[0]
            id = session["user"]["id"]
            pos = [pos for pos in posts if pos["userId"]==id]
            print(pos)
        else:
            print("No authenticated user")
lg_in = LoginView()
lg_in.login(username="akhil",password= "Password@123")
post_view =PostListView()
# print(post_view.get())
my_post={
    "title":"Nu new post","content":"new one","liked_by":[]
}
post_view.post(data=my_post)
my_list = MyPostView()
my_list.get(username="akhil",password= "Password@123")

