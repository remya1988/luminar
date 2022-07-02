from Blog.models import users, posts


def authenticate(**kwargs):
    username = kwargs.get("username")
    password = kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user


session = {}


def sigin_required(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            print("Invalid user")

    return wrapper


class LoginView:
    def login(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = authenticate(username=username, password=password)
        if user:
            session["user"] = user[0]  # to avoid storing as list of dictionary... only store dictionary
        # print(session)


class PostListView:

    @sigin_required
    def get(self, **kwargs):
        return posts

    @sigin_required
    def post(self, **kwargs):
        post = kwargs.get("data")
        id = session["user"]["id"]
        post["userId"] = id
        posts.append(post)


class MyPostView:
    @sigin_required
    def get(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = authenticate(username=username, password=password)
        if user:
            id = session["user"]["id"]
            pos = [pos for pos in posts if pos["userId"] == id]
            print(pos)
        else:
            print("No authenticated user")


class AddLike:
    @sigin_required
    def post(self, *args, **kwargs):
        pid = kwargs.get("postid")
        post = [post for post in posts if post["postId"] == pid]
        if post:
            post = post[0]
            userid = session["user"]["id"]
            post["liked_by"].append(userid)
            print("like Added : ", post)
        else:
            print("No post to list")


lg_in = LoginView()
lg_in.login(username="akhil", password="Password@123")
post_view = PostListView()
# print(post_view.get())
my_post = {
    "postId": 9, "title": "Nu new post", "content": "new one", "liked_by": []
}
post_view.post(data=my_post)
my_list = MyPostView()
my_list.get(username="akhil", password="Password@123")

addlike = AddLike()
addlike.post(postid=9)

